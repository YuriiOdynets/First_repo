# Іменовані кортежі. Оголосивши шаблон - його можна повторно використовувати для організації схожих записів. У цьому прикладі 
# попередньо оголосивши шаблон і заповни
import collections
Person=collections.namedtuple('Person',['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

Yurii = Person('Yurii', 'Odynets', 32, 'Lviv', '52-131')
Kate = Person('Kate', 'Sikora', 27, 'Harkiv', '52-131')

print(Yurii.age)
print(Kate.birth_place)