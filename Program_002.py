#print("hello world from pycharm")

text = input().split()
length = [len(x) for x in text]
maximum = max(length)
text_index = length.index(maximum)
print(text[text_index])
try:
  print(10/0)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")