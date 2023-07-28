#creating and opening a new file hello.py
#Command: $ touch hello.py
#Command: $ goopen hello.py
#creating a function that greets a person by name

def hello(name:'str'):
    return print(f"Hello {name}!")


#creating and opening a new file with a different name to import the function
#Command: $ touch main.py
#Command: $ goopen main.py
#importing the function, printing the name

from hello import hello

hello('Margarita')
