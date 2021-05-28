==========
gpdwgData 
==========
.. module:: gpdwg
.. toctree::
   :maxdepth: 2

   Variables <variables>
   Classes <classes>
   Objects <objects>

:mod:`gpdwg` reads the binary .dwg file using :func:`read` function and returns a :class:`gpdwgData` object.

.. class:: gpdwgData

   .. attribute:: version

      This `int` attribute provides the .dwg file version. Valid versions are |dwg_versions| .

      Example::

         import gpdwg
         DwgFileData=gpdwg.read("path/to/file.dwg")
         print(str(DwgFileData.version))

   .. attribute:: variable

      This attribute has to be of type :class:`gpdwgVariables` .

   .. attribute:: classes

      This attribute is a list of type :class:`gpdwgClass` .