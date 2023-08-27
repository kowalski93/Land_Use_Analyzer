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
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Alexandros Voukenas'
__date__ = '2023-08-09'
__copyright__ = '(C) 2023 by Alexandros Voukenas'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LandUseAnalyzer class from file LandUseAnalyzer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .land_use_analyzer import LandUseAnalyzerPlugin
    return LandUseAnalyzerPlugin(iface)
