import unittest
import FileService


class TestSentenceAmountMethod(unittest.TestCase):
    def test_sentences_counter(self):
        result = FileService.sentences_counter("Adfghjk. Efg... Mr. Rght?")
        self.assertEqual(result, [3, 1])

    def test_average_sent(self):
        result = FileService.average_sent("Anh! Mr. Bob. R67h??")
        self.assertEqual(result, 4)

    def test_average_word(self):
        result = FileService.average_word("Dr. 569876 ghjoi rk6l!!!")
        self.assertEqual(result, 4)

    def test_repeats(self):
        result = FileService.repeats("Dr. 569876 a a a ghjoi rk6l!!! Amk. Redf ghj 567. Mr. Grfhj gfjk7il!! GHG  a a a?? Amk. Redf ghj.", 3, 2)
        self.assertEqual(result, [(('a', 'a', 'a'), 2), (('amk', 'redf', 'ghj'), 2)])
