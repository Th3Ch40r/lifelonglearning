print("Encontrar parte do texto")

text = "X-DSPAM-Confidence:    0.8475"

textfinded=text.find(str(0.8475))
textsliced=text[textfinded:]
print(float(textsliced))
