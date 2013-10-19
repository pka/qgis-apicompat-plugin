# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ApiCompatTest
                                 A QGIS plugin
 Test suite for apicompat
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "apicompattest"


def description():
    return "Test suite for apicompat"


def version():
    return "0.2.0"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def qgisMaximumVersion():
    return "2.99"

def author():
    return "Pirmin Kalberer, Sourcepole"

def email():
    return "pka@sourcepole.ch"

def classFactory(iface):
    # load ApiCompatTest class from file ApiCompatTest
    from apicompattest import ApiCompatTest
    return ApiCompatTest(iface)
