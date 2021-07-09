with open('py-digits.txt','r') as reader:
    contents = reader.read()
# Relative
with open('relative_text_file/text.txt') as reader:
    desktop_content = reader.read()
    
# Line by Line
with open('py-digits.txt','r') as reader:
    print('Line by line')
    for line in reader:
        print(line.rstrip()) # remove right side whitespaces

# Store it in a list 
with open('py-digits.txt','r') as reader:
    lines = reader.readlines()
    
# Working with file contents    
pi_string = ''
for line in lines:
    pi_string += line.strip() # removing both sides withespaces

print('\nUsing strip')
print(pi_string)
        


    

