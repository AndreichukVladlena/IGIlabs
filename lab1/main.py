from utilities import hello_world
from utilities import operation
from utilities import save_even_numbers
hello_world()
print("6 * 7 = ")
print(operation(6, 7, "mult"))
print ("even numbers from list")
even_num = save_even_numbers()
for element in even_num:
    print(element)