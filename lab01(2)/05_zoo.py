def run_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
    
    zoo.insert(1,'bear')
    print(zoo)
    
    
    birds = ['rooster', 'ostrich', 'lark', ]
    
    zoo += birds
    print(zoo)
    
    zoo.remove('elephant')
    print(zoo)
    
    lion_cell = zoo.index('lion') + 1
    lark_cell = zoo.index('lark') + 1
    
    
    print(f"Лев сидит в клетке №{lion_cell}")
    print(f"Жаворонок сидит в клетке №{lark_cell}")
    
    return zoo
