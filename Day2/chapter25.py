def breakWords(stuff):
    """Break up words"""
    words = stuff.split(' ')
    return words

def sortWords(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after pop"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after pop"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = breakWords(sentence)
    return sortWords(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence"""
    words = breakWords(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# ====================================================================
# Python 3.8.2 (default, Apr  8 2021, 23:19:18) 
# [Clang 12.0.5 (clang-1205.0.22.9)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import chapter25
# >>> sentence = "All good things come to those who wait."
# >>> words = chapter25.breakWords(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> sorted_words = chapter25.sortWords(words)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> chapter25.print_first_word(words)
# All
# >>> chapter25.print_last_word(words)
# wait.
# >>> words
# ['good', 'things', 'come', 'to', 'those', 'who']
# >>> chapter25.print_last_word(sorted_words)
# who
# >>> chapter25.print_first_word(sorted_words)
# All
# >>> sorted_words
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = chapter25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> chapter25.print_first_and_last(sentence)
# All
# wait.
# >>> chapter25.print_first_and_last_sorted(sentence)
# All
# who