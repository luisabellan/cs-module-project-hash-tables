import time

# naive solution: it took: 0.011001825332641602ms
def word_count(s):
    # Your code here
    words = s.split()
  

    counter = 0
    for i in range(len(words)):
        counter += 1
    
    print(words)
    #print(counter)

    return counter

   

  
    
#word_count('Hello, my cat. And my cat doesn\'t say "hello" back.')



if __name__ == "__main__":
    start = time.time()
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('a a\ra\na\ta \t\r\n'))
    end = time.time()
    print(f'it took: {end-start}ms')
