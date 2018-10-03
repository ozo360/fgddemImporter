########################################################################
# fgddemImporter - A QGIS plugin
# Copyright (C) 2012 Akagri Minoru
# email : akaginch@yahoo.co.jp
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
########################################################################

from qgis.PyQt.QtCore import *
import os, locale

def name():
    return "fgddemImporter"

def description():
    return "Import fgddem xml/zip files."

def category():
  return "Raster"

def version():
    return "Version 0.0.2"

def icon():
    return "icon.png"

def qgisMinimumVersion():
    return "1.0"

def authorName():
    return "Minoru Akagi"

def classFactory(iface):
    # import fgddemImporter
    from .fgddemImporter import fgddemImporter

    # return fgddemImporter.fgddemImporter(iface)
    return fgddemImporter(iface)

