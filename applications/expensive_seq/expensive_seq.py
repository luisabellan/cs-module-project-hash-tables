# Your code here


expensive_seq_cache = {}

def expensive_seq(x,y,z):
    input = (x,y,z)
    if input in expensive_seq_cache:
        return expensive_seq_cache[(input)]
   
    if x <= 0:
        value = y + z
    elif x >  0:
        value = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    expensive_seq_cache[input] = value
    return value




if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
