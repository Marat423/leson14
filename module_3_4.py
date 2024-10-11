def single_root_words(root_word, *other_words): # Создаем функцию
    same_words = [] # Создаем список
    root_word_lower = root_word.lower() # Переводим слово в нижний регистр
    for word in other_words: # Перебираем слова
        word_lower = word.lower() # Переводим слова в нижний регистр
        if root_word_lower in word_lower or word_lower in root_word_lower: # Проверяем слово содержится ли оно в переменной
            same_words.append(word) # Добавляем в список
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

