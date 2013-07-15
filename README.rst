=====================
qgis-apicompat-plugin
=====================

`QGIS <http://www.qgis.org/>`_ API compatibility wrapper loaded as plugin.

Loading this compatibility wrapper enables QGIS 1.8 to run plugins written with QGIS 2.0 API.

This page summarizes the changes needed in migrating QGIS python plugins from the 1.8 API to the 2.0 API.
The version 2.0 API has many breaking changes which plugins need to account for.

With the following conventions your plugin will also run with QGIS 1.8.

For information about the API changes see:

- http://hub.qgis.org/wiki/quantum-gis/Python_plugin_API_changes_from_18_to_20
- http://nathanw.net/2013/06/13/new-qgis-20-api/


Include apicompat
=================

Include the latest apicompat.py in your plugin main directory::

  wget https://github.com/pka/qgis-apicompat-plugin/raw/master/apicompat/apicompat.py

And in your plugin main file add::

  import apicompat

This adds global compatibility functions and checks wheter the plugin is loaded in QGIS 1.8.


SIP API upgrade
===============

The SIP API manages the mapping between python and C++/Qt objects. This has been upgraded to version 2.
The most significant impact of this is that there is a much tighter mapping between Qt data types and python data types - QVariant and QString are removed. 
Also the "old style" signal and slot format is no longer available.


Replacing QVariant
__________________

The "QVariant" type doesn't exist anymore so any methods returning "QVariant" will be auto converted to Python types.
You no longer need to convert the return type using the "toXXXX" methods.  

Replacement rules:

====================  ====================
 API V1                API V2
====================  ====================
qvar.toString()        pystring(qvar)
qvar.toList()          pylist(qvar)
qvar.toInt()           pyint(qvar)
qvar.toFloat()         pyfloat(qvar)
qvar.toStringList()    pystringlist(qvar)
qvar.toByteArray()     pybytearray(qvar)
qvar.toPyObject()      pyobject(qvar)
====================  ====================

Replacement rules for assignments::

  QVariant(..)
  QString(..)

Note that the autoconversion to a Python type is based on the type of the QVariant, which may not be the same as the type returned by a toXXX conversion.
Note also that some of the toXXX functions return a tuple of (type, valid) to specify whether the conversion is successful.

For example:

Before::

    value,ok = variantValue.toDouble()
    if not ok:
        handleError()

After::

    # Best option to ensure value has the same type as in original code
    value = pyfloat(variantValue)
 
    # To handle conversion errors
    try: 
        value=pyfloat(variantValue)
    except:
        handleError()


QSettings return type
_____________________

The type of QSettings return values is specified in the QSettings.value() call. More info: http://pyqt.sourceforge.net/Docs/PyQt4/pyqt_qsettings.html.

Before::

      settings.value(“/yourboolsetting”, True).toBool()
      settings.value(“/yourintsetting”, 10).toInt()[0]
      settings.value(“/yourintsetting”).toByteArray()

After::

      settings.value(“/yourboolsetting”, True, type=bool)
      settings.value(“/yourintsetting”, 10, type=int)
      settings.value(“/yourintsetting”, QByteArray(), type=QByteArray)


Replace QString methods
_______________________

"QString" no longer exists in the new QGIS API.  Any methods that return a "QString" will be converted into a native Python "unicode".  All QString methods need to be replaced with equivalent native string methods.

Before::

  yourstring.right(4)
  files.join(",")
  if yourstring.length() > 4:
  if yourstring.isEmpty()
  
After::

  unicode(yourstring)[4:]
  ",".join(files)
  if len(unicode(yourstring)) > 4
  if not unicode(yourstring)


Replace QStringList with list
_____________________________

Before::

  mystrings = QStringList()

After:

  mystrings = []


Remove QVariant calls
_____________________

The "QVariant" also doesn't exist as an instantiated type anymore - any methods returning "QVariant" will be auto converted to Python types.  However "QVariant" can still be used to access it's enum values e.g. "QVariant.Int" can set be used.

Before::

  myvalue = QVariant(10)
  myvalue = QVariant("Hello World")

After::

  myvalue = 10
  myvalue = "Hello World"

Note that Null QVariant values (ie values for which QVariant.IsNull() returns True) are not mapped to the python None value as you might expect.
Instead they return a QPyNullVariant value.  This preserves the type information of the null object.


Replace QList methods with python list function
_______________________________________________

Before::

  if files.isEmpty()
  files.count()

After::

  if not files
  len(files)


Replace signals with new style signals and connections
______________________________________________________

*Emitting* before::

  self.emit(SIGNAL("valuesChanged(const QStringList &)"), self.getArguments())

After::

  class Test():
    valuesChanged = QtCore.pyqtSignal(list)

    def yourmethod():
      self.valuesChanged.emit(self.getArguments)

**Connecting** before::

  QObject.connect(self.iface,SIGNAL('projectRead ()'),self.readSettings) 

After::

  self.iface.projectRead.connect(self.readSettings)


Vector layer API changes
========================

QgsFeatureRequest replaces select()
___________________________________

In QGIS 1.8 features are selected from a vector layer by using QgsVectorLayer.select() and then loop over provider.nextFeature().  In QGIS 2.0 the selection is defined by a QgsFeatureRequest object and features are retrieved using a python iterator created by QgsVectorLayer.getFeatures(QgsFeatureRequest). The QgsFeatureRequest object is only required to add selection criteria to the request - otherwise it can be omitted and all features will be returned.

Before::

    layer.select()
    f=QgsFeature()
    while layer.nextFeature(f):
       ....

After::

    for f in layer.getFeatures():
       ...

To add criteria to the selection you need to explicitly define a QgsFeatureRequest, for example::

     request=QgsFeatureRequest()
     request.setFilterRect(areaOfInterest)

     for f in layer.getFeatures(request):
         ...

Other criteria and be set using setSubsetOfFields and setFlags___::

     request.setSubsetOfFields([0,2])                  # Only return selected fields
     request.setSubsetOfFields(['name','id'],layer.fields())  # More user friendly version
     request.setFlags( QgsFeatureRequest.NoGeometry )  # Don't return geometry objects


Getting/setting QgsFeature attributes simplified
________________________________________________

Feature attributes can be get and set by index, for example

Before::

    index = layer.fieldNameIndex(fieldname)
    layer.select()
    f = QgsFeature()
    while layer.nextFeature(inFeat):
        fieldvalue=f.attributeMap()[index].toString())

After::

    for f in layer.getFeatures():
        fieldvalue=f[fieldname]

Feature attributes can also be set by index, for example::

    fields=layer.fields()
    f = QgsFeature(fields)
    f['name']='Bruce'
    f['id']=42

**NOTE**: Do not use f=QgsFeature(layer.fields()) - this will kill QGIS.  The QgsFieldList returned by layer.fields() must have at least the same lifetime as the QgsFeature.



Plugin repository and metadata changes
======================================

The plugin should include a metadata.txt file to upload to the repository. For example::

  name=My Plugin
  description=Does useful stuff
  category=Plugins
  version=1.0
  experimental=False
  qgisMinimumVersion=1.8
  qgisMaximumVersion=2.99
  author=My name
  email=myemail@somewhere.com
  icon=./plugin.png

Note: The default maximum version that is floor(qgisMinimumVersion) + 0.99.
Plugin __init__.py file should contain only the classFactory() method, all other information is in metadata.txt. ALL other members should be deleted from __init__.py .


Copyright and License
=====================

Copyright (c) 2013 Pirmin Kalberer, Sourcepole AG

qgis-apicompat-plugin is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
