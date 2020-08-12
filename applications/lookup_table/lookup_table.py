# Your code here
import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def create_table():
    # keys will be arrays holding x and y, where x
    table = {}

    for x in range(2, 14):
        for y in range(3, 6):
            table[x, y] = ((math.factorial(math.pow(x, y))) //
                        (x + y)) % 982451653 

    return table

table = create_table()

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
  
   
    return table.get((x,y))
   
    



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
    
    
