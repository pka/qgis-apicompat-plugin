# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ApiCompat
                                 A QGIS plugin
 API compatibility layer
                              -------------------
        begin                : 2013-07-02
        copyright            : (C) 2013 by Pirmin Kalberer, Sourcepole
        email                : pka@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from qgis.core import *

import sip
import __builtin__

def sipv1():
    return sip.getapi("QVariant") == 1

__builtin__.sipv1 = sipv1

if sipv1():
    if __name__ == "apicompat.apicompat":
        #We are in the apicompat plugin
        import sipv1.compat
        import sipv1.vectorapi
    else:
        #Check if apicompat plugin is loaded
        if not hasattr(QgsVectorLayer, 'getFeatures'):
            from PyQt4.QtGui import QMessageBox
            QMessageBox.critical(None, "Load Error " + __name__, 'Please install the plugin "apicompat" first')
            #raise Exception('Please install the plugin "apicompat" first')
else:
    #Define backwards compatibility functions
    def strlist(strlist):
        return strlist
    __builtin__.strlist = strlist
