import unittest

from lesson_09.homework_09 import count_unique_char
from lesson_09.homework_09 import list_only_with_string
from lesson_09.homework_09 import sum_even_numbers
from lesson_09.homework_09 import is_anagram
from lesson_09.homework_09 import longest_word


class CountUniqueCharsTest(unittest.TestCase):

    def test_unique_chars_more_10(self):
        self.assertTrue(count_unique_char("abcdefjhilmfh"))

    def test_unique_chars_less_10(self):
        self.assertFalse(count_unique_char("abcdemvxzaazb"))

    def test_unique_chars_equal_10(self):
        self.assertFalse(count_unique_char("defghijklofgd"))

    def test_empty_field(self):
        self.assertFalse(count_unique_char(""))

    def test_upper_and_lower_letters(self):
        self.assertFalse(count_unique_char("DdGgUuOomMLl"))

    def test_special_char(self):
        self.assertTrue(count_unique_char("5^  ''#80-=?)"))


class ListWithStringTest(unittest.TestCase):

    def test_list_with_string(self):
        actual_result = list_only_with_string([1,'28989', 'Test', 0, '#454565fg', True, '  '])
        expected_result = ['28989', 'Test', '#454565fg', '  ']
        self.assertEqual(expected_result, actual_result)

    def test_list_without_string(self):
        actual_result = list_only_with_string([1, True, 2, False])
        expected_result = []
        self.assertEqual(expected_result, actual_result)

    def test_empty_list(self):
        actual_result = list_only_with_string([])
        expected_result = []
        self.assertEqual(expected_result, actual_result)


class SummarizeEvenNumbersTest(unittest.TestCase):

    def test_sum_with_even_numbers(self):
        actual_result = sum_even_numbers([21, 22, 10, 90, 9, 0])
        expected_result = 122
        self.assertEqual(expected_result, actual_result)

    def test_sum_only_odd_numbers(self):
        actual_result = sum_even_numbers([1, 9, 99, 13])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_sum_list_float_numbers(self):
        actual_result = sum_even_numbers([1.2, 2, 3.5, 0, 0.8, 12.1, 8.8, 8])
        expected_result = 10
        self.assertEqual(expected_result, actual_result)

    def test_sum_negative_numbers(self):
        actual_result = sum_even_numbers([-5, 0, -10, -3, -50, 50])
        expected_result = -10
        self.assertEqual(expected_result, actual_result)

    def test_sum_list_special_char(self):
        actual_result = sum_even_numbers([100, '22', '90', 21, '1oo', '  ', '@345'])
        expected_result = 100
        self.assertEqual(expected_result, actual_result)

    def test_empty_list(self):
        actual_result = sum_even_numbers([])
        expected_result = 0
        self.assertEqual(expected_result, actual_result)


class AnagramTest(unittest.TestCase):

    def test_words_are_anagram(self):
        self.assertTrue(is_anagram("fried", "fired"))

    def test_words_arent_anagram(self):
        self.assertFalse(is_anagram("random", "monday"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

    def test_string_with_symbols(self):
        self.assertTrue(is_anagram("@12?34/5", "5/43@21?"))

    def test_words_with_upper_letter(self):
        self.assertTrue(is_anagram("Heart", "Earth"))

    def test_with_spaces(self):
        self.assertTrue(is_anagram(" ra  ce", "         care"))



class LongestWordTest(unittest.TestCase):

    def test_one_longest_word(self):
        actual_result = longest_word(['test', 'principles', 'requirements'])
        expected_result = ['requirements']
        self.assertEqual(expected_result, actual_result)

    def test_words_with_similar_length(self):
        actual_result = longest_word(['bug', 'data', 'test'])
        expected_result = ['data', 'test']
        self.assertEqual(expected_result, actual_result)

    def test_empty_strings(self):
        actual_result = longest_word(['', '', ''])
        expected_result = ['', '', '']
        self.assertEqual(expected_result, actual_result)

    def test_with_numbers(self):
        actual_result = longest_word(['11', '990', '21', '27'])
        expected_result = ['990']
        self.assertEqual(expected_result, actual_result)

    def test_with_symbols(self):
        actual_result = longest_word(['  #&)-', '123ujk&', '=)*^%$'])
        expected_result = ['123ujk&']
        self.assertEqual(expected_result, actual_result)

    def test_words_only_spaces(self):
        actual_result = longest_word(['   ', ' ', '    '])
        expected_result = ['   ', ' ', '    ']
        self.assertEqual(expected_result, actual_result)



if __name__ == '__main__':
    unittest.main()


