from camelcase import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):
        self.assertEqual('helloHelloWorld', camelcase('hello HELLO world'))

    def test_remove_spaces(self):
        self.assertEqual('noMoreSpaces', camelcase('    no    more    spaces   '))

    def test_remove_special_characters(self):
        self.assertEqual('noSpecialCharacters', camelcase('@$@$no @#special c#$#haract%^ers'))

    def test_keep_numbers(self):
        self.assertEqual('1234Th353Ar3Numb3r5', camelcase('1234 Th353 Ar3 Numb3r5'))
