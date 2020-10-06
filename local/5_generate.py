import os
import argparse
import string
import torch
from azureml.core import Workspace, Model

from model.generate import generate
from model.char_rnn import CharRNN

ws = Workspace.from_config()

# Parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("--modelname",         type=str,   default="char_rnn_model")
argparser.add_argument("-p", "--prime_str",   type=str,   default="A")
argparser.add_argument("-l", "--predict_len", type=int,   default=100)
argparser.add_argument("-t", "--temperature", type=float, default=0.8)
argparser.add_argument("--cuda",              action="store_true")
args = argparser.parse_args()

all_characters = string.printable
n_characters = len(all_characters)

# TODO: Use the Model class to download your trained model
model = Model(workspace=ws, name=args.modelname) # , version=5
model = model.download(target_dir='.', exist_ok=True)

filename = "outputs/" + args.modelname + ".pt"
print(filename)
decoder_state = torch.load(filename)
char_rnn = CharRNN(n_characters,
                   100,
                   n_characters,
                   "gru",
                   2)
char_rnn.load_state_dict(decoder_state)

# predicted = generate(decoder, **vars(args))
predicted = generate(decoder=char_rnn,
                     prime_str=args.prime_str,
                     predict_len=args.predict_len,
                     temperature=args.temperature,
                     cuda=args.cuda)

print(predicted)
