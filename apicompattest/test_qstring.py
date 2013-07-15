import unittest
from PyQt4.QtCore import *
from qgis.core import *

class TestQstring(unittest.TestCase):

    def test_qstring(self):

        value = QgsApplication.pluginPath()
        if sipv1():
            self.assertEqual(type(value), QString)
            self.assertEqual(value[-1], QString("s"))
        if not sipv1():
            self.assertEqual(type(value), unicode)
        self.assertEqual(value[-1], "s") #type cast in QString==
        #SIP V1+V2
        value = unicode(QgsApplication.pluginPath())
        self.assertEqual(value[-1], "s")
