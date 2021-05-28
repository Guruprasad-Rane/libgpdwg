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
import sys, PIL
sys.path.append("/home/guruprasad/librecad_dev/gpdwg_dev/gpdwg/src")
import libgpdwg

#libgpdwg.logger.setLevel(0)
#libgpdwg.handler.setLevel(0)
program_name = sys.argv[0]
arguments = sys.argv[1:]

if len(arguments) == 2:
	Preview=libgpdwg.getPreview(sys.argv[1])
	Preview.save(sys.argv[2],"PNG")

