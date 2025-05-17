
def count_unique_char(user_input):
    '''
    The function counts the number of unique characters in a string and prints True
    to the console if the count exceeds 10;
    otherwise, it prints False.
    '''
    return len(set(user_input.lower())) > 10


def list_only_with_string (input_list):
    '''
    The function creates a new list containing only the string elements from the input list
    '''
    lst_with_string = [x for x in input_list if isinstance(x,str)]
    return lst_with_string


def sum_even_numbers(list_with_numbers):
    '''
    The function calculates the sum of all EVEN numbers in a list
    '''
    list_with_even_num = [i for i in list_with_numbers if isinstance(i,int) and i % 2 == 0]
    return sum(list_with_even_num)


def is_anagram(word1, word2):
    '''
    Checks whether two words are anagrams of each other.
    Returns True if the sorted characters of both words match; otherwise, returns False.
    '''
    word1_without_spaces = word1.replace(' ', '')
    word2_without_spaces = word2.replace(' ', '')
    return sorted(word1_without_spaces.lower()) == sorted(word2_without_spaces.lower())


def longest_word(list_of_words):
    '''
    The function takes a list of words and returns the longest word in the list
    '''
    max_len = max(len(word.replace(' ', '')) for word in list_of_words)
    return [word for word in list_of_words if len(word.replace(' ', '')) == max_len]