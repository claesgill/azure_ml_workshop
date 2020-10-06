import argparse
import string
from tqdm import tqdm
import torch
import torch.nn as nn
from torch.autograd import Variable
from azureml.core import Workspace, Dataset, Run, Model

# local
from helpers import read_file, save
from char_rnn import CharRNN, train, char_tensor, random_training_set
from generate import generate

# Get experiment run context and workspace details
run = Run.get_context()
ws = run.experiment.workspace

# Reading and un-unicode-encoding data
all_characters = string.printable
n_characters = len(all_characters) # 100

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument('--dataset',       type=str,   default='shakespeare.txt')
argparser.add_argument('--model',         type=str,   default='gru')
argparser.add_argument('--n_epochs',      type=int,   default=2000)
argparser.add_argument('--print_every',   type=int,   default=100)
argparser.add_argument('--hidden_size',   type=int,   default=100)
argparser.add_argument('--n_layers',      type=int,   default=2)
argparser.add_argument('--learning_rate', type=float, default=0.01)
argparser.add_argument('--chunk_len',     type=int,   default=200)
argparser.add_argument('--batch_size',    type=int,   default=100)
argparser.add_argument('--shuffle',       action='store_true')
argparser.add_argument('--cuda',          action='store_true')
args = argparser.parse_args()

# Downloads dataset from azure
dataset = Dataset.get_by_name(ws, name=args.dataset)
file_path = dataset.download(target_path='.', overwrite=True)
file, file_len = read_file(file_path[0])

# Initialize models and start training
decoder = CharRNN(
    n_characters,
    args.hidden_size,
    n_characters,
    model=args.model,
    n_layers=args.n_layers,
)

decoder_optimizer = torch.optim.Adam(decoder.parameters(), lr=args.learning_rate)
criterion = nn.CrossEntropyLoss()

print("Training for {} epochs...".format(args.n_epochs))
loss_avg = 0
for epoch in tqdm(range(1, args.n_epochs + 1)):
    inp, target = random_training_set(args.chunk_len, args.batch_size, file, file_len, False)
    loss = train(decoder=decoder, 
                 criterion=criterion, 
                 decoder_optimizer=decoder_optimizer,
                 inp=inp, 
                 target=target, 
                 cuda=False, 
                 batch_size=args.batch_size, 
                 chunk_len=args.chunk_len)
    loss_avg += loss
    
    if epoch % 100 == 0:
        prediction = generate(decoder=decoder, 
                              prime_str='Wh', 
                              predict_len=100, 
                              temperature=0.8, 
                              cuda=args.cuda)
        print("\n" + prediction)

save_filename = "outputs/char_rnn_model.pt"
# save(decoder.state_dict(), save_filename)
save(decoder, save_filename)

# TODO: Use the Model class and the register method to upload the model to Azure ML
# Register the model
model = Model.register(workspace=ws,
                       model_name="char_rnn_model",
                       model_path="outputs/")

# Complete the run
run.complete()