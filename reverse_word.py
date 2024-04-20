input_str = "sky is blue"
words = input_str.split(" ")
words = list(reversed(words))
output_str = " ".join(words)
print(output_str)