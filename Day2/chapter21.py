def add(x, y):
    print(f"ADD: {x} + {y}")
    return x + y

def subtract(x, y):
    print(f"SUBTRACT: {x} - {y}")
    return x - y

def multiply(x, y):
    print(f"MULTIPLY: {x} * {y}")
    return x * y

def divide(x, y):
    print(f"DIVIDE: {x} / {y}")
    return x / y


print("Let's do some math with just functions!!!!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# x puzzle 
print("Here is x puzzle.")

what = add(age, divide(height, multiply(weight, subtract(iq, 2))))

print("That becomes: ", what, "Can you do it by hand or not?")