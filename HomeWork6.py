def all_variants(text):
    # Внешний цикл: перебираем все возможные длины подпоследовательностей от 1 до длины строки
    for length in range(1, len(text) + 1):

        # Внутренний цикл: для каждой длины генерируем все возможные подпоследовательности
        for start in range(len(text) - length + 1):
            # Возвращаем подстроку, начиная с индекса start и длиной length
            yield text[start:start + length]


# Создаем генератор all_variants для строки "abc"
a = all_variants("abc")

# Выводим все подпоследовательности
for i in a:
    print(i)
