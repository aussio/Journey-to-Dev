import unittest
from nose_parameterized import parameterized

# Code under test:
from sticker import sticker_machine


class TestSticker(unittest.TestCase):
    
    @parameterized.expand([
        ('wpengine', 1),
        ('win', 1),
        ('pig', 1),
        ])
    def test_result_found_within_one_sticker(self, input_word, expected_num_of_stickers, sticker_word='wpengine'):
        self.assertEqual(sticker_machine(input_word, sticker_word=sticker_word), expected_num_of_stickers)


    @parameterized.expand([
        ('nope', -1),
        ('wpengineb', -1),
        ])
    def test_failure(self, input_word, expected_num_of_stickers, sticker_word='wpengine'):
        self.assertEqual(sticker_machine(input_word, sticker_word=sticker_word), expected_num_of_stickers)


    @parameterized.expand([
        ('weeeee', 3),
        ('winning', 2),
        ('ggggggg', 7),
        ])
    def test_failure(self, input_word, expected_num_of_stickers, sticker_word='wpengine'):
        self.assertEqual(sticker_machine(input_word, sticker_word=sticker_word), expected_num_of_stickers)
