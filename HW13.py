# 1. Write a decorator that ensures a function is only called by users with a specific role. Each function should have a user_type with a string type in kwargs. Example:

def is_admin(func):
    def wrapper(*args, **kwargs):
        if 'admin' not in args or 'admin' not in kwargs:
            raise ValueError('Permission denied')
        else:
            func(*args, **kwargs)
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation
    print('receipt')

show_customer_receipt(user_type='user')

show_customer_receipt(user_type='admin')

#2. Write a decorator that wraps a function in a try-except block and prints an error if any type of error has happened.
#  Example:

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError:
            print(f'Found an error during execution of your function: KeyError no such key')
    return wrapper        


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})


some_function_with_risky_operation({'key': 'bar'})

