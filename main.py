# module_3_4

def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Приводим корень к нижнему регистру для сравнения без учета регистра
    root_word_lower = root_word.lower()

    # Перебираем каждое слово из переданных аргументов
    for word in other_words:
        # Приводим текущее слово к нижнему регистру для сравнения без учета регистра
        word_lower = word.lower()

        # Проверяем наличие корня в текущем слове или текущего слова в корне
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words


# Вызываем функцию и выводим результат
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
