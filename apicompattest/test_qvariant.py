import unittest
from PyQt4.QtCore import *
from qgis.core import *

class TestQvariant(unittest.TestCase):

    def setUp(self):
        self.settings = QSettings()

    def test_int(self):
        self.settings.setValue("testint", 58)
        if sipv1():
            value,ok = self.settings.value("testint", 1024).toInt()
            self.assertEqual(value, 58)
        #SIP V1+V2
        value = self.settings.value("testint", 1024, type=int)
        self.assertEqual(type(value), int)
        self.assertEqual(value, 58)
