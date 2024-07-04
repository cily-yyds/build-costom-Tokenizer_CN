import os
import time
from minbpe import RegexTokenizer

text = open("../dataset.txt", "r", encoding="utf-8").read()
os.makedirs("models", exist_ok=True)
t0 = time.time()
tokenizer = RegexTokenizer()
tokenizer.train(text, 5000, verbose=True)
prefix = os.path.join("models", 'regex5k')
tokenizer.save(prefix)
tokenizer.load('regex5k.model')
t1 = time.time()
print(f"Training took {t1 - t0:.2f} seconds")