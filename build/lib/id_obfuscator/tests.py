"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import sys
from django.test import TestCase
from utils import obfuscate, deobfuscate

class SimpleTest(TestCase):
    
    def test_correctly_hashes(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        seen_hashes = set()
        collisions = 0
        max_num = 1000000
        for k in range(0, max_num):
            o = obfuscate(k)
            d = deobfuscate(o)
            if d in seen_hashes:
                collisions += 1
            seen_hashes.add(d)
            self.assertEquals(k, d, "Incorrect hash: %s -> %s -> %s " % (k, o, d))
        self.assertEqual(collisions, 0, "There were %d collisions between 0 and %d" % (collisions, max_num))
        
        for k in range(0, 4294967295, 1048576):
            o = obfuscate(k)
            d = deobfuscate(o)
            self.assertEquals(k, d, "Incorrect hash: %s -> %s -> %s " % (k, o, d))
    
    def test_bad_inputs(self):
        self.assertRaises(ValueError, obfuscate, -1)
        self.assertRaises(ValueError, obfuscate, "noninteger")
        self.assertRaises(ValueError, deobfuscate, "!@#$%^")
        self.assertRaises(ValueError, deobfuscate, "Zd..4")
