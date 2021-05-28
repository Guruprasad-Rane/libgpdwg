=================
Reading .dwg file
=================
.. note::
	Current version |version| can read only release 2000 .dwg files.

.. module:: gpdwg
.. function:: read(dwgFilePath)

   returns :class:`gpdwgData` object

Example::

   import gpdwg
   DwgFileData=gpdwg.read("path/to/file.dwg")
   print(repr(DwgFileData))

Output::

   gpdwgObject Type
      some text here