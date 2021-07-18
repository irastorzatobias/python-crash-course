file = 'learning_python.txt'



# Reading the file

with open(file) as reader:
    content = reader.read()
    
#for i in range(3):
    #print(content,"\n")


# With a loop    
with open(file, 'r') as reader:
    for line in reader:
        print(line.strip())



# Working them outside the with block
with open(file, 'r') as reader:
    result = []
    for line in reader.readlines(): # List of lines
        result.append(line.strip())
        
print('\nWorking outside the with block')

for line in result:
   print(line.replace('Python','Java')) # Not modifying the real line.