import random as rd
import math as mt
from datetime import date as dt

motivation = ["You are smart", "You are beautiful", "It is not hard it is new","You are the best","You own your life"]

print(rd.randint(1,6))
print(rd.randint(1,6))
print(rd.choice(motivation))
print(f"Today's date: {dt.today()}")

area_circle =2*  mt.pi * 5
print(f"Area of a circle when the randius is 5: {round(area_circle,4)}")

