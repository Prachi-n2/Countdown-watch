# practice code
import time

# my_time = int(input("Enter the time in sececnds: "))

# for x in range(0, my_time):
# for x in range(my_time, 0, -1):
# for x in reversed(range(0, my_time)):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours =  int(x / 3600)
    # print(x)
    # print(f"00:00:{seconds}")
    # print(f"00:00:{seconds:02}")
    # print(f"00:{minutes:02}:{seconds:02}")
    # print(f"{hours:02}:{minutes:02}:{seconds:02}")
    # time.sleep(1)

# time.sleep(3)

# print("Times up")


# main code
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0 , -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times UP!")