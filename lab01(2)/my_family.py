my_family = ['Я','Мама','Папа','Брат 1','Брат 2']

my_family_height = [
    ['Я', 170],
    ['Мама', 156],
    ['Папа', 172],
    ['Брат 1', 166],
    ['Брат 2', 154]
]


for i in my_family_height:
    if i[0] == 'Папа':
        print(f'Рост отца - {i[1]} см')
        break

Allheight = 0
for j in my_family_height:
    Allheight += j[1]

def semia():
    print(f'Общий рост моей семьи - {Allheight} см')
    print(height_father())
