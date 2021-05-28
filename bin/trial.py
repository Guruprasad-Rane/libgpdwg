#!/usr/bin/env python3
#############################################################################
#  gpdwg - free python package to read .dwg files.                          #
#                                                                           #
#  gpdwg-thumbnailer.py generates thumnails of dwg for Gnome3               #
#                                                                           #
#  Copyright (C) 2018 Guruprasad Rane <raneguruprasad@gmail.com>            #
#                                                                           #
#  This library is free software, licensed under the terms of the GNU       #
#  General Public License version 2. You should have received a copy of     #
#  the GNU General Public License along with this program.                  #
#                                                                           #
#############################################################################
import sys
sys.path.append("src/python")
import libgpdwg

libgpdwg.logger.setLevel(20) # 0 - NOTSET, 10 - DEBUG, 20 - Info, 30 - Warning
libgpdwg.handler.setLevel(20) # 0 - NOTSET, 10 - DEBUG, 20 - Info, 30 - Warning
arguments = sys.argv[1:]


if len(arguments) == 1:
	dwgData=libgpdwg.read(sys.argv[1])

print(dwgData)
