garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)



def swetok():
    print("Цветы в саду:", garden_set)
    print("Цветы на лугу:", meadow_set)
    print(garden_set | meadow_set)
    print(garden_set & meadow_set)
    print(garden_set-meadow_set)
    print(meadow_set-garden_set)
