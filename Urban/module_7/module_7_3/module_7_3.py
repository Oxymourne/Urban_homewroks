class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}

        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                lower_file = file.read().lower()
                for element in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    if element in lower_file:
                        lower_file = lower_file.replace(element, '')
                all_words[name] = lower_file.split()
        return all_words

    def find(self, word):
        find_result = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                find_result[key] = value.index(word.lower()) + 1
        return find_result

    def count(self, word):
        count_result = {}
        for key, value in self.get_all_words().items():
            count_result[key] = value.count(word.lower())
        return count_result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))