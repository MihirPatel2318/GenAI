import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, I am Mihir Patel"

tokens = enc.encode(text)

print("Tokens:",tokens)

tokens = [13225, 11, 357, 939, 132414, 380, 122760]
decoded = enc.decode(tokens)

print("Decoded:",decoded)

