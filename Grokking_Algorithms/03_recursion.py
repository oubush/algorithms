# Recursion

def countdown(i):
    # base case
    if i <=0:
        return 0
    # recursive case
    else:
        print(i)
        return(countdown(i-1))

def greet2(name):
    print("how are you, ", name, "?")

def bye():
    print("ok bye!")

def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)
