import random

name_string=input("please enter names using coma, :")

names=name_string.split(",")

p=len(names)

p=p-1
r=random.randint(0,p)

print(f"{names[r]}, is going to pay today. ")


