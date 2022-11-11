import random
import os
from pystyleclean import *
attempts = 0
nums =0
os.system(f"title Number Bruter ^| Attempts:  {attempts}")
a = int(input("Enter number less than 10000 to be bruted: "))
if a<=10000:
 while True:
    attempts = attempts + 1
nums = nums+1
    if nums == a:
        print(Colorate.Horizontal(Colors.green_to_white, f"Number bruted after {attempts} attempts."))
        os.system(f"title Number Bruted")
        break
    else:
        os.system(f"title Number Bruter ^| Attempts : {attempts}")

else:
    print("Number needs to be less than 10000")