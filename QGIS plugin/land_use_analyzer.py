# -*- coding: utf-8 -*-

"""
/***************************************************************************
 LandUseAnalyzer
                                 A QGIS plugin
 A plugin for Land Use spatial analysis tools
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-08-09
        copyright            : (C) 2023 by Alexandros Voukenas
        email                : avoukenas@gmail.com
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

__author__ = 'Alexandros Voukenas'
__date__ = '2023-08-09'
__copyright__ = '(C) 2023 by Alexandros Voukenas'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon

from qgis.core import QgsProcessingAlgorithm, QgsApplication
import processing

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .land_use_analyzer_provider import LandUseAnalyzerProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class LandUseAnalyzerPlugin(object):

    def __init__(self,iface):
        self.provider = None
        self.iface = iface
        
    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = LandUseAnalyzerProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()
        
        actionZonal = QAction(
            QIcon(os.path.join(os.path.join(cmd_folder,'landuseanalyzer', 'land_use_mix_logo.png'))),
            u"Zonal Analysis", self.iface.mainWindow())
            
        actionZonal.triggered.connect(self.runZonal)
        
        self.actions = [actionZonal]
        
        for action in self.actions:
            self.iface.addPluginToMenu(u"&Land Use Analyzer", action)
            self.iface.addToolBarIcon(action)

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
        for action in self.actions:
            self.iface.removePluginMenu(u"&Land Use Analyzer", action)
            self.iface.removeToolBarIcon(action)
            del action
        
    def runZonal(runZonal):
        processing.execAlgorithmDialog("Land Use Analyzer:zonal_analysis")