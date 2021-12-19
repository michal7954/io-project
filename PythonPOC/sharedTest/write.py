import shared
shared.value = 'Hello'
def foo():
    print('Inner method use')

shared.method = foo