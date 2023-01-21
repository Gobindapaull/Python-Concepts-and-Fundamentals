print('hello world in the first line')

message = "Python For Crypto Bot           LAST"
new_message = message.replace('Python For', 'Python')
first = "first"
last = "last"
word = first + ' ' + last

print('{} {}'.format(first, last)) #or
print(f'{first} {last.upper()}') #or
print("word : " + word)

print(dir(message)) #all attributes and methods
print("message : " + message)
print("new message : " + new_message)
print(len(message)) #length of the string

print(message[1]) #second character
print(message[0]) #first character
print(message[-1])  #last character
print(message[0:4]) #range #4 excluded 0 included
print(message[6:9])

print(message.lower()) #all lowercase character
print(message.upper()) #all uppercase character

print(message.count('For')) #"For" word counting
print(message.find('Bot')) #find Bot index number
print(message.find('unknown')) # -1

#print(help(str))
#print(help(str.lower))
