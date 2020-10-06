import unidecode
import torch


def save(decoder, save_filename):
    torch.save(decoder, save_filename)
    print('Saved as {}'.format(save_filename))

def read_file(filename):
    file = unidecode.unidecode(open(filename).read())
    return file, len(file)
