import unittest
from PyQt4.QtCore import *
from qgis.core import *

class TestQvariant(unittest.TestCase):

    def setUp(self):
        self.settings = QSettings()

    def test_settings_value(self):
        self.settings.setValue("testint", 58)
        if sipv1():
            value,ok = self.settings.value("testint", 1024).toInt()
            self.assertEqual(value, 58)
        #SIP V1+V2
        value = self.settings.value("testint", 1024, type=int)
        self.assertEqual(type(value), int)
        self.assertEqual(value, 58)

    def test_qvariant(self):
        self.settings.setValue("qvartest", "abc")
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pystring(qvar)), unicode)
        self.assertEqual(pystring(qvar), "abc")
        if sipv1():
            self.assertEqual(type(qvar.toString()), QString)

        self.settings.setValue("qvartest", [1,2])
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pylist(qvar)), list)
        self.assertEqual(pylist(qvar), [1,2])

        self.settings.setValue("qvartest", [1,2])
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pylist(qvar)), list)
        self.assertEqual(pylist(qvar), [1,2])

        self.settings.setValue("qvartest", 42)
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pyint(qvar)), int)
        self.assertEqual(pyint(qvar), 42)

        self.settings.setValue("qvartest", 3.14)
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pyfloat(qvar)), float)
        self.assertAlmostEqual(pyfloat(qvar), 3.14, 2)

        self.settings.setValue("qvartest", ["a", "b"])
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pystringlist(qvar)), list)
        self.assertEqual(type(pystringlist(qvar)[0]), unicode)
        self.assertEqual(pystringlist(qvar), ["a", "b"])

        #TODO: pybytearray
        #self.settings.setValue("qvartest", "abc")
        #qvar = self.settings.value("qvartest")
        #self.assertEqual(type(pybytearray(qvar)), unicode)
        #self.assertEqual(pybytearray(qvar), "abc")

        self.settings.setValue("qvartest", 3.14)
        qvar = self.settings.value("qvartest")
        self.assertEqual(type(pyobject(qvar)), float)
        self.assertAlmostEqual(pyobject(qvar), 3.14, 2)

    def test_helpers_without_conversion(self):
        self.assertEqual(pystring("abc"), "abc")
        self.assertEqual(pystring("abc"), u"abc")
        self.assertEqual(pystring(u"abc"), u"abc")

    def test_qvariant_exceptions(self):
        self.settings.setValue("qvartest", "xy")
        qvar = self.settings.value("qvartest")
        self.assertRaises(ValueError, pyfloat, qvar)
