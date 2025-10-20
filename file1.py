with open ('filename.txt', 'r') as file:
    content = file.read()
    print (content)

with open('output.txt','a') as file:
    file.write("Hello world!\n")