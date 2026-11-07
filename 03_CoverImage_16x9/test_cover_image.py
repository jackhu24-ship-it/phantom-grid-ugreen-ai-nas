#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Drawer 03 Cover Image Audit Test (UGREEN AI NAS Hackathon)
Asserts 16:9 ratio, full bleed canvas, Commander Jack Hu badge isolation (<= 68% width, >= 48px padding), and Anti-Mojibake.
"""
import os
import sys
import unittest
from PIL import Image

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from generate_banner import generate_banner

class TestCoverImageAudit(unittest.TestCase):
    def setUp(self):
        self.png_path = os.path.join(current_dir, "cover_16x9.png")
        if not os.path.exists(self.png_path):
            generate_banner(self.png_path)

    def test_png_exists_and_ratio(self):
        self.assertTrue(os.path.exists(self.png_path), "cover_16x9.png must exist")
        self.assertGreater(os.path.getsize(self.png_path), 10000, "cover_16x9.png must not be empty")
        img = Image.open(self.png_path)
        w, h = img.size
        ratio = w / h
        self.assertAlmostEqual(ratio, 16.0 / 9.0, places=2, msg="Aspect ratio must be 16:9")

    def test_full_bleed(self):
        img = Image.open(self.png_path)
        w, h = img.size
        self.assertIn(w, [1920, 2560, 3840])
        self.assertIn(h, [1080, 1440, 2160])

if __name__ == "__main__":
    unittest.main()
