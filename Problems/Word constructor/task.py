text_1 = str(input())
text_2 = str(input())
text_1 = list(text_1)
text_2 = list(text_2)
text_f = ""
for a, b in zip(text_1, text_2):
    text_f += a+b
print(text_f)
