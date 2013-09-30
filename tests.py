# -*- coding: utf-8 -*-
import unittest

from birdback.xauth import compute_footprint, utf8


class ComputeFootprintTest(unittest.TestCase):
    def test_no_data(self):
        footprint = compute_footprint('GET', '/', {})
        self.assertEqual(footprint, 'GET&/&')

    def test_data(self):
        footprint = compute_footprint('GET', '/', dict(param_1='value 1',
            param_2='value 2'))
        self.assertEqual(footprint, 'GET&/&param_1=value+1&param_2=value+2')

    def test_data_unicode(self):
        footprint = compute_footprint('GET', '/', dict(param_1='value 1',
            param_2=u'éà&'))
        self.assertEqual(footprint,
            'GET&/&param_1=value+1&param_2=%C3%A9%C3%A0%26')

    def test_data_utf8(self):
        footprint = compute_footprint('GET', '/', dict(param_1='value 1',
            param_2='éà&'))
        self.assertEqual(footprint,
            'GET&/&param_1=value+1&param_2=%C3%A9%C3%A0%26')

    def test_query_string(self):
        footprint = compute_footprint('GET', '/?param=value', {})
        self.assertEqual(footprint, 'GET&/?param=value&')


class UTF8Test(unittest.TestCase):
    def test_unicode(self):
        self.assertEqual(type(utf8(u's & é à')), str)

    def test_utf8(self):
        self.assertEqual(type(utf8('s & é à')), str)


if __name__ == '__main__':
    unittest.main()
