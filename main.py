fullName = input("Enter yout full name:")
age = int(input("Enter your Age: ")) #command int( before input, convert the data string to int
gender = chr(input("Enter your gender M, F, X :")) #command chr( before input, convert the data string to chr
height = float(input("Enter your height: ")) #command float( before input, convert the data string to float

print(type(fullName))  #command type shows the nature of the variable
print(type(age)) 

print(f""" Hi user {fullName}. How are you?, I'm Python.
      thanks por share your Age {age}, I didn't idea that you human gender are {gender}.
      """)
