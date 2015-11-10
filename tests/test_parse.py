# -*- coding: utf-8 -*-
import unittest

from videoscene import core

class CoreTest(unittest.TestCase):

    def test_parse(self):
        release = "Southpaw.2015.720p.BluRay.x264.YIFY"
        parsed = core.parse(release)
        self.assertEqual(parsed['title'], 'Southpaw')
        self.assertEqual(parsed['year'], '2015')
        self.assertEqual(parsed['screenSize'], '720p')
        self.assertEqual(parsed['source'], 'BluRay')