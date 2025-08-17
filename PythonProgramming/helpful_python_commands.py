x = 1
weight_kg = 10.56
my_name = "David Smith"
price = 6
quit = True

# print() is used to print a value to the terminal, similar to $echo.
print(my_name)

# type() is used to find out what type of variable a variable is.
type(weight_kg)
type(price)
type(my_name)

'''
Variables should be be written in snake case in Python, 
i.e. my_name instead of myName (camel case in Java) or My_Name.
Also, variables should not start with numbers.
'''
# len() is used to figure out the length of a string or range.
length_of_my_name = len(my_name)
print(length_of_my_name)

# [] at the end of a variable can slice the part of the string specified in the [].
# will print the 3rd and 5th characters in "David Smith". Position in the array = position in string - 1.

sliced_name = my_name[2:5]
print(sliced_name)

# .find can find the position of a word in a string
sentence = "I need to find a word in this sentence."
position_in_sentence = sentence.find("need")
print(position_in_sentence)

# .split can be used to separate each word in a sentence by the value specified, even if it is just empty space. The words are split into an array.
split_sentence = sentence.split(" ")
print(split_sentence[3:])

#.join does the opposite of .split.
reformed_sentence = " ".join(split_sentence)
print(reformed_sentence, type(reformed_sentence))

# .replace can be used to replace a value in a variable with another value.
new_sentence = sentence.replace("need", "would like")
print(new_sentence)

'''
values can be inserted into strings to do different things
\t indents the remainder of the string
\n puts the remainder of the string on a new line
\n\r put the remainder of the string on a newline and indents it
'''

# The command below shows all the keywords by python.
help('keywords')

# help command can be used to get help on how to use other commands.
help(print)

# The input command allows user input and assigns it to a variable.
age = input("Please enter your age: ")
if int(age) <= 20:
    print("You are not allowed to drink alcohol!")
elif int(age) >= 21 and int(age) <= 50:
    print("Please drink responsibly.")
elif int(age) >=51:
    print("Collect your pension!")
else:
    print("Please enter a valid age")

# in lists, .append can add to a list. So can +
list = [1, 2, 3, 4]
list.append(5)
print(list)
new_list = list + [6, 7]
print(new_list)

# in lists del command can be used to delete a value in a specified position.
del list[-1]
print(list)

# .pop removes the last element in the list if a position is not specified
pop_list = new_list.pop()
print(pop_list)
print(new_list)

# To find out which virtual environments are on your computer:
conda info --envs

# To activate a virtual environment:
conda activate {virtual_environment_name}

# To find which python packages have been installed:
pip freeze