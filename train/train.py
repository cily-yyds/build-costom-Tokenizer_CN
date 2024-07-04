"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
from minbpe import RegexTokenizer

# open some text and train a vocab of 512 tokens
text = open("../dataset.txt", "r", encoding="utf-8").read()

# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()
# construct the Tokenizer object and kick off verbose training
tokenizer = RegexTokenizer()
tokenizer.train(text, 5000, verbose=True)
# writes two files in the models directory: name.model, and name.vocab
prefix = os.path.join("models", 'regex5k')
tokenizer.save(prefix)
tokenizer.load('regex5k.model')
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")