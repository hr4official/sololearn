file = open("/usercode/files/books.txt", "r")

#your code goes here
for line in file.readlines():
      print(f'{line[0]}{len(line.strip())}')
file.close()
