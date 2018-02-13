from unittest import TestCase
from unittest.mock import patch, Mock

import requests
import sys

import fixer


class test_fixer(TestCase):
    @patch('fixer.setup', return_value = {'base':'USD','date':'2018-02-13','rates':{'AUD':1.2742,'BGN':1.5858,'BRL':3.2954,'CAD':1.2604}})
    def test_get_data(self, api_data):
        data = fixer.setup()
        self.assertEqual({'base':'USD','date':'2018-02-13','rates':{'AUD':1.2742,'BGN':1.5858,'BRL':3.2954,'CAD':1.2604}}, data)

    @patch('fixer.get_cad', return_value = 1.2604)
    def test_get_cad(self, api_data):
        data = fixer.setup()
        cad = fixer.get_cad(data)
        self.assertEqual(1.2604, cad)

    @patch('fixer.setup', side_effect=Exception)
    def test_setup_error_connecting(self, api_patch):
        with self.assertRaises(Exception):
            fixer.setup()
