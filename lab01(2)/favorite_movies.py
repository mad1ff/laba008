my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

def movies():
    print(my_favorite_movies[0:10])
    print(my_favorite_movies[42:57])
    print(my_favorite_movies[12:25])
    print(my_favorite_movies[35:40])

import re

def task1():
    """Задача 1: последовательности длины 6 в {K,A,T,E,P}, начинающиеся на P и заканчивающиеся на K"""
    return 5 ** 4

def task2():
    """Задача 2: 216^6+216^4+36^6-6^14-24 в системе с основанием 6. Сколько различных цифр?"""
    val = 216**6 + 216**4 + 36**6 - 6**14 - 24
    digits = set()
    while val > 0:
        digits.add(val % 6)
        val //= 6
    return len(digits)

def task3():
    """Задача 3: числа до 10^9 по маске 12345??8, делящиеся на 23"""
    results = []
    for num in range(12345008, 12346000):
        if num % 23 == 0:
            results.append((num, num // 23))
    return results

if __name__ == "__main__":
    print("=" * 40)
    print("ВАРИАНТ 8")
    print("=" * 40)
    
    print(f"\nЗадача 1: {task1()}")
    print(f"\nЗадача 2: {task2()}")
    
    print("\nЗадача 3:")
    for num, div in task3():
        print(f"  {num} : {div}")
