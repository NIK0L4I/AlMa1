import unittest
import sys
import My_Float_Info as mfi


class TestAccuracy(unittest.TestCase):

    def testAccuracy(self):
        self.assertEqual(sys.float_info.max, mfi.My_Float_Info.getmax())