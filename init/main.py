# Link of the tutorial: https://www.youtube.com/watch?v=Ej_02ICOIgs
from phone import Phone
from keyboard import Keyboard

item1 = Phone("jshPhone", 1000, 3)
board = Keyboard("yamaha", 25, 4)

item1.apply_increment(0.2)

print(item1.price)



