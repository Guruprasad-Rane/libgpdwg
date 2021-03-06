libgpdwg
========

A python package to read [.dwg](https://en.wikipedia.org/wiki/.dwg) files.

It follows dwg file specifications from [Open Design Specification for .dwg files version 5.4.1](https://www.opendesign.com/files/guestdownloads/OpenDesign_Specification_for_.dwg_files.pdf) prepared by Open Design Alliance.

Aim
---
Main aim of the project is to understand the file structure of dwg files.

Methodology
-----------
Part of the code of the library is static while the rest of the code is dynamically generated by ```code generator/python/code-generator.py```. Static code is written in files named ``` part1.py ``` , ``` part2.py ``` , etc in ```code generator/python``` folder. Where as dynamic code is generated from the csv file in ```csv spec``` folder. By running ``` ./code\ generator/python/code-generator.py ``` a fresh code is created in src/python .

Usage
-----
Refer ```bin/trial.py``` for basic usage. This will read a dwg file and dump the data. Example of [dump file](https://raw.githubusercontent.com/Guruprasad-Rane/libgpdwg/main/test1_dump.txt) created.


References
----------
Following open source projects were referred while working on gpdwg.
* [libdwg](http://libdwg.sourceforge.net/en/index.html) developed by Felipe Castro
* [libredwg](http://www.gnu.org/software/libredwg/) 
