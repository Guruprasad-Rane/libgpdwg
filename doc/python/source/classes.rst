=============
gpdwg classes
=============
.. module:: gpdwg

.. class:: gpdwgClass

   DWG classes are stored as *gpdwgClass* object. Each class can have following attributes.


   ===================  =====  =============================================
   Attributes           Type   Version
   ===================  =====  =============================================
   CLASS_NUM            float  Available in all DWG versions.
   VERSION              float  Available in all DWG versions.
   APPNAME              str    Available in all DWG versions.
   CPLUSPLUSCLASSNAME   str    Available in all DWG versions.
   CLASSDXFNAME         str    Available in all DWG versions.
   WASAZOMBIE           int    Available in all DWG versions.
   ITEMCLASSID          float  Available in all DWG versions.
   PROXY_FLAGS          float  Available in DWG version 2004 and above only.
   NUM_OF_OBJECTS       float  Available in DWG version 2004 and above only.
   DWG_VERSION          float  Available in DWG version 2004 and above only.
   MAINTENANCE_VERSION  float  Available in DWG version 2004 and above only.
   UNKNOWN1             float  Available in DWG version 2004 and above only.
   UNKNOWN2             float  Available in DWG version 2004 and above only.
   ===================  =====  =============================================

   .. note::
         UNKNOWN attributes are those which are yet to be reverse engineered.