import unittest
from PyQt4.QtCore import *
from qgis.core import *

class TestVectorapi(unittest.TestCase):

    def test_added_method(self):
        layer = QgsVectorLayer()
        features = layer.getFeatures()
        self.assertEqual(hasattr(features, '__iter__'), True)
