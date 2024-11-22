import time
import random 
random_num=random.randint(0,100)
print(random_num)
start_time = time.perf_counter()

while True:
    try:
        num = int(input("enter a number in range limit:"))
        if num < random_num:
            print("the main number is bigger than yours")
            num = int(input("enter a number in range limit:"))
        elif num > random_num:
            print("the main number is smaller than yours,enter a number smaller than this")
            num = int(input("enter a number in range limit:"))
        else:
            print("u got it")
            break

    except ValueError:
        print("invalid input,pls enter an integer")

end_time = time.perf_counter()
elapsed_time = round(end_time - start_time)
print(f"Elapsed time: {elapsed_time} seconds")
