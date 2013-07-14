import unittest
from PyQt4.QtCore import *
from qgis.core import *
import sip

def sipv1():
    return sip.getapi("QVariant") == 1

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.settings = QSettings()

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

    def test_int(self):
        self.settings.setValue("testint", 58)
        if sipv1():
            value,ok = self.settings.value("testint", 1024).toInt()
            self.assertEqual(value, 58)
        #SIP V1+V2
        value = self.settings.value("testint", 1024, type=int)
        self.assertEqual(type(value), int)
        self.assertEqual(value, 58)

    def test_added_method(self):
        layer = QgsVectorLayer()
        features = layer.getFeatures()
        self.assertEqual(hasattr(features, '__iter__'), True)
