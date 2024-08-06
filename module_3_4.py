def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        if root_word.count(root_word) == word.count(root_word):
            same_words.append(word)
        if word.count(word) == root_word.count(word.lower()):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
