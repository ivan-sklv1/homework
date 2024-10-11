class WordsFinder:
    
    def __init__(self, *file_names):
        self.file_names = file_names
        
    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punctuations:
                        line = line.replace(symbol, '' if symbol != '-' else '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words
    
    def find(self, word):
        word = word.lower()
        find_words = {}
        for name, words in self.get_all_words().items():
            if word in words:
                find_words[name] = words.index(word) + 1
        return find_words
            
    def count(self, word):
        word = word.lower()
        count_words = {}
        for name, words in self.get_all_words().items():
            count_words[name] = words.count(word)
        return count_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
