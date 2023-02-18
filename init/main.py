# Link of the tutorial: https://www.youtube.com/watch?v=Ej_02ICOIgs
from item import Item
from phone import Phone

Item.instantiate_from_csv()
print(Item.all)

phone1 = Phone('jscOhone', 500, 5)
phone1.broken_phones = 1


