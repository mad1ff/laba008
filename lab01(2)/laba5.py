"""
Лабораторная работа №5 - Вариант 8
Генераторы. Уровни Rare + Medium
"""

from functools import reduce


def generator_filter(sequence, func, n, threshold=0.5):
    """
    Генератор. Применяет func N раз к каждому элементу.
    Возвращает только значительно изменившиеся элементы.
    """
    for item in sequence:
        result = item
        for _ in range(n):
            result = func(result)
        
        # Проверка на значительное изменение
        if isinstance(item, (int, float)):
            if item == 0:
                if abs(result) > threshold:
                    yield result
            else:
                if abs(result - item) / abs(item) > threshold:
                    yield result
        elif isinstance(item, str):
            if item == "":
                if len(result) > 0:
                    yield result
            else:
                if abs(len(result) - len(item)) / len(item) > threshold:
                    yield result
        else:
            if result != item:
                yield result


# ============ RARE УРОВЕНЬ - ДЕМОНСТРАЦИЯ ============

print("=" * 60)
print("ЛАБОРАТОРНАЯ РАБОТА №5 - ВАРИАНТ 8")
print("=" * 60)

# Пример 1: Генератор + map
print("\n1. ГЕНЕРАТОР + MAP")
numbers = [1, 2, 3, 4, 5]
gen = generator_filter(numbers, lambda x: x * 2, n=3, threshold=0.5)
result_map = list(map(lambda x: f"Число: {x}", gen))
print(f"  Исходные числа: {numbers}")
print(f"  После 3 применений *2: {result_map}")

# Пример 2: Генератор + filter
print("\n2. ГЕНЕРАТОР + FILTER")
numbers = [1, 2, 3, 10, 20, 50]
gen = generator_filter(numbers, lambda x: x ** 2, n=2, threshold=0.3)
result_filter = list(filter(lambda x: x > 100, gen))
print(f"  Исходные числа: {numbers}")
print(f"  Квадраты >100 после 2 применений: {result_filter}")

# Пример 3: Генератор + reduce
print("\n3. ГЕНЕРАТОР + REDUCE")
numbers = [1, 2, 3, 4, 5]
gen = generator_filter(numbers, lambda x: x + 5, n=2, threshold=0.3)
result_list = list(gen)
if result_list:
    total = reduce(lambda a, b: a + b, result_list)
    print(f"  Исходные числа: {numbers}")
    print(f"  После 2 применений +5: {result_list}")
    print(f"  Сумма (reduce): {total}")
else:
    print("  Нет элементов, изменившихся значительно")

# Пример 4: Со строками
print("\n4. РАБОТА СО СТРОКАМИ")
words = ["a", "hi", "hello"]
gen = generator_filter(words, lambda s: s + s, n=2, threshold=0.5)
print(f"  Исходные слова: {words}")
for val in gen:
    print(f"  Результат: {val} (было изменено значительно)")

print("\n" + "=" * 60)
print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА (RARE УРОВЕНЬ)")
print("=" * 60)


# ============ MEDIUM УРОВЕНЬ - ТЕСТЫ ДЛЯ PYTEST ============

def test_basic_numbers():
    """Тест 1: Базовый тест с числами"""
    result = list(generator_filter([1, 2, 3], lambda x: x * 2, n=3, threshold=0.5))
    assert result == [8, 16, 24]


def test_no_significant_change():
    """Тест 2: Незначительные изменения не возвращаются"""
    result = list(generator_filter([100, 200], lambda x: x * 1.01, n=3, threshold=0.5))
    assert result == []


def test_strings():
    """Тест 3: Тест со строками"""
    result = list(generator_filter(["a", "bc"], lambda x: x + x, n=2, threshold=0.5))
    assert result == ["aaaa", "bcbcbcbc"]


def test_with_map():
    """Тест 4: Совместная работа с map"""
    gen = generator_filter([1, 2], lambda x: x * 3, n=2, threshold=0.5)
    result = list(map(lambda x: x + 1, gen))
    assert result == [10, 19]  # 1*3*3=9+1=10, 2*3*3=18+1=19


def test_with_filter():
    """Тест 5: Совместная работа с filter"""
    gen = generator_filter([1, 2, 3, 4], lambda x: x ** 2, n=2, threshold=0.5)
    result = list(filter(lambda x: x > 50, gen))
    assert result == [81, 256]  # 3^4=81, 4^4=256


def test_with_reduce():
    """Тест 6: Совместная работа с reduce"""
    gen = generator_filter([1, 2, 3], lambda x: x * 2, n=2, threshold=0.5)
    total = reduce(lambda a, b: a + b, list(gen))
    assert total == 4 + 8 + 12  # 1*2*2=4, 2*2*2=8, 3*2*2=12, сумма=24


def test_empty_sequence():
    """Тест 7: Пустая последовательность"""
    result = list(generator_filter([], lambda x: x, 5))
    assert result == []


def test_different_threshold():
    """Тест 8: Разные пороги"""
    result = list(generator_filter([10], lambda x: x * 1.1, n=5, threshold=0.6))
    # 10 → 16.1, изменение 61% > 60% → должно вернуться
    assert len(result) == 1


if __name__ == "__main__":
    print("\nДля запуска тестов выполните:")
    print("pytest laba5.py -v")
