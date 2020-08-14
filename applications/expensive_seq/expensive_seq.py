# Your code here


def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z
    if x > 0: 
        return expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)


def create_table():
    # keys will be arrays holding x and y, where x
    table = {}

    for x in range(2, 14):
        for y in range(3, 6):
            table[(x, y)] = ((math.factorial(math.pow(x, y))) //
                             (x + y)) % 982451653

    return table


table = create_table()

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
