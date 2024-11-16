



def maxOfThree(a,b,c):
    if a > b:
        if a > c:
            return a
        elif c > b:
            return c
    elif a < b:
        if b > c:
            return b
        else:
            return c
    else:
        return a

def factorial(num):
    if num < 0:
        raise ValueError("Can't use negative numbers in factorial!")
    z = 1
    for x in range(1, num + 1):
        z *= x
    return z

def readingCalculator(filename):
    # Initialize a list to store words
    words = []
    
    # Open the file and read its content
    with open(filename, 'r') as f:
        content = f.read()  # Read the entire content of the file
        words = content.split()  # Split content into words
    # Calculate the reading metric (number of words divided by 249)
    if len(words) == 0:
        return 0  # To avoid division by zero if the file is empty
    y = len(words) // 249
    return len(words), "words", str(y), "minute read"

# Call the function with the filename
result = readingCalculator('file.txt')
print(f"{result[0]} {result[1]}, a {result[2]} {result[3]}.") 