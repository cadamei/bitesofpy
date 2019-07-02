from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(*args):
        # Check the user exists
        if args[0] not in known_users:
            result = "please create an account"
        elif args[0] in known_users and args[0] not in loggedin_users:
            result = "please login"
        else:
            # Call the passed in function
            result = func(*args)
        return result
    # return decorated function
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f'welcome back {user}'



print(welcome('anonymous'))
print(welcome('julian'))
print(welcome('sue'))
