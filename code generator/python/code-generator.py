#!/usr/bin/env python3
import shutil, os, csv

'''
if os.path.isdir("src"):
	shutil.rmtree("src")
os.mkdir("src")
InitFIle=open('src/__init__.py','w')
InitFIle.close()
'''
from g_bit import generate_bit
from g_version import generate_version
from g_variables import generate_variable
from g_objects import generate_objects
from g_gpdwg import generate_gpdwg

#run_path("gpdwg/generate-gpdwg.py")
