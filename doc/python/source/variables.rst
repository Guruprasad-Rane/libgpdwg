===============
gpdwg variables
===============
.. module:: gpdwg

.. class:: gpdwgData.gpdwgVariables

   DWG header vaiables are stored in *gpdwgVariables* class. Each variable can be accessed or modified using following attributes.


   =====================================  ===========  ====================================================
   Variables                              Type         Version
   =====================================  ===========  ====================================================
   SIZE_IN_BITS                           int          Available in DWG version 2007 only.
   REQUIREDVERSIONS                       int          Available in DWG version 2013 and above only.
   UNKNOWN_01                             float        Available in all DWG versions.
   UNKNOWN_02                             float        Available in all DWG versions.
   UNKNOWN_03                             float        Available in all DWG versions.
   UNKNOWN_04                             float        Available in all DWG versions.
   UNKNOWN_05                             str          Available in all DWG versions.
   UNKNOWN_06                             str          Available in all DWG versions.
   UNKNOWN_07                             str          Available in all DWG versions.
   UNKNOWN_08                             str          Available in all DWG versions.
   UNKNOWN_09                             float        Available in all DWG versions.
   UNKNOWN_10                             float        Available in all DWG versions.
   UNKNOWN_11                             float        Available in DWG version 13 and 14 only.
   CURRENT_VIEWPORT_HANDLE                bit.handle   Available in DWG version 13, 14 and 2000 only.
   DIMASO                                 int          Available in all DWG versions.
   DIMSHO                                 int          Available in all DWG versions.
   DIMSAV                                 int          Available in DWG version 13 and 14 only.
   PLINEGEN                               int          Available in all DWG versions.
   ORTHOMODE                              int          Available in all DWG versions.
   REGENMODE                              int          Available in all DWG versions.
   FILLMODE                               int          Available in all DWG versions.
   QTEXTMODE                              int          Available in all DWG versions.
   PSLTSCALE                              int          Available in all DWG versions.
   LIMCHECK                               int          Available in all DWG versions.
   BLIPMODE                               int          Available in DWG version 13 and 14 only.
   UNDOCUMENTED                           int          Available in DWG version 2004 and above only.
   USRTIMER                               int          Available in all DWG versions.
   SKPOLY                                 int          Available in all DWG versions.
   ANGDIR                                 int          Available in all DWG versions.
   SPLFRAME                               int          Available in all DWG versions.
   ATTREQ                                 int          Available in DWG version 13 and 14 only.
   ATTDIA                                 int          Available in DWG version 13 and 14 only.
   MIRRTEXT                               int          Available in all DWG versions.
   WORLDVIEW                              int          Available in all DWG versions.
   WIREFRAME                              int          Available in DWG version 13 and 14 only.
   TILEMODE                               int          Available in all DWG versions.
   PLIMCHECK                              int          Available in all DWG versions.
   VISRETAIN                              int          Available in all DWG versions.
   DELOBJ                                 int          Available in DWG version 13 and 14 only.
   DISPSILH                               int          Available in all DWG versions.
   PELLIPSE                               int          Available in all DWG versions.
   PROXYGRAPHICS                          float        Available in all DWG versions.
   DRAGMODE                               float        Available in DWG version 13 and 14 only.
   TREEDEPTH                              float        Available in all DWG versions.
   LUNITS                                 float        Available in all DWG versions.
   LUPREC                                 float        Available in all DWG versions.
   AUNITS                                 float        Available in all DWG versions.
   AUPREC                                 float        Available in all DWG versions.
   OSMODE                                 float        Available in DWG version 13 and 14 only.
   ATTMODE                                float        Available in all DWG versions.
   COORDS                                 float        Available in DWG version 13 and 14 only.
   PDMODE                                 float        Available in all DWG versions.
   PICKSTYLE                              float        Available in DWG version 13 and 14 only.
   UNKNOWN_12                             float        Available in DWG version 2004 and above only.
   UNKNOWN_13                             float        Available in DWG version 2004 and above only.
   UNKNOWN_14                             float        Available in DWG version 2004 and above only.
   USERI1                                 float        Available in all DWG versions.
   USERI2                                 float        Available in all DWG versions.
   USERI3                                 float        Available in all DWG versions.
   USERI4                                 float        Available in all DWG versions.
   USERI5                                 float        Available in all DWG versions.
   SPLINESEGS                             float        Available in all DWG versions.
   SURFU                                  float        Available in all DWG versions.
   SURFV                                  float        Available in all DWG versions.
   SURFTYPE                               float        Available in all DWG versions.
   SURFTAB1                               float        Available in all DWG versions.
   SURFTAB2                               float        Available in all DWG versions.
   SPLINETYPE                             float        Available in all DWG versions.
   SHADEDGE                               float        Available in all DWG versions.
   SHADEDIF                               float        Available in all DWG versions.
   UNITMODE                               float        Available in all DWG versions.
   MAXACTVP                               float        Available in all DWG versions.
   ISOLINES                               float        Available in all DWG versions.
   CMLJUST                                float        Available in all DWG versions.
   TEXTQLTY                               float        Available in all DWG versions.
   LTSCALE                                float        Available in all DWG versions.
   TEXTSIZE                               float        Available in all DWG versions.
   TRACEWID                               float        Available in all DWG versions.
   SKETCHINC                              float        Available in all DWG versions.
   FILLETRAD                              float        Available in all DWG versions.
   THICKNESS                              float        Available in all DWG versions.
   ANGBASE                                float        Available in all DWG versions.
   PDSIZE                                 float        Available in all DWG versions.
   PLINEWID                               float        Available in all DWG versions.
   USERR1                                 float        Available in all DWG versions.
   USERR2                                 float        Available in all DWG versions.
   USERR3                                 float        Available in all DWG versions.
   USERR4                                 float        Available in all DWG versions.
   USERR5                                 float        Available in all DWG versions.
   CHAMFERA                               float        Available in all DWG versions.
   CHAMFERB                               float        Available in all DWG versions.
   CHAMFERC                               float        Available in all DWG versions.
   CHAMFERD                               float        Available in all DWG versions.
   FACETRES                               float        Available in all DWG versions.
   CMLSCALE                               float        Available in all DWG versions.
   CELTSCALE                              float        Available in all DWG versions.
   MENUNAME                               str          Available in DWG version 13, 14, 2000 and 2004 only.
   TDCREATE_JD                            float        Available in all DWG versions.
   TDCREATE_MS                            float        Available in all DWG versions.
   TDUPDATE_JD                            float        Available in all DWG versions.
   TDUPDATE_MS                            float        Available in all DWG versions.
   UNKNOWN_15                             float        Available in DWG version 2004 and above only.
   UNKNOWN_16                             float        Available in DWG version 2004 and above only.
   UNKNOWN_17                             float        Available in DWG version 2004 and above only.
   TDINDWG_JD                             float        Available in all DWG versions.
   TDINDWG_MS                             float        Available in all DWG versions.
   TDUSRTIMER_JD                          float        Available in all DWG versions.
   TDUSRTIMER_MS                          float        Available in all DWG versions.
   CECOLOR                                bit.color    Available in all DWG versions.
   HANDSEED                               bit.handle   Available in all DWG versions.
   CLAYER                                 bit.handle   Available in all DWG versions.
   TEXTSTYLE                              bit.handle   Available in all DWG versions.
   CELTYPE                                bit.handle   Available in all DWG versions.
   CMATERIAL                              bit.handle   Available in DWG version 2007 and above only.
   DIMSTYLE                               bit.handle   Available in all DWG versions.
   CMLSTYLE                               bit.handle   Available in all DWG versions.
   PSVPSCALE                              float        Available in DWG version 2000 and above only.
   INSBASE_PS                             bit.point3D  Available in all DWG versions.
   EXTMIN_PS                              bit.point3D  Available in all DWG versions.
   EXTMAX_PS                              bit.point3D  Available in all DWG versions.
   LIMMIN_PS                              bit.point2D  Available in all DWG versions.
   LIMMAX_PS                              bit.point2D  Available in all DWG versions.
   ELEVATION_PS                           float        Available in all DWG versions.
   UCSORG_PS                              bit.point3D  Available in all DWG versions.
   UCSXDIR_PS                             bit.point3D  Available in all DWG versions.
   UCSYDIR_PS                             bit.point3D  Available in all DWG versions.
   UCSNAME_PS                             bit.handle   Available in all DWG versions.
   PUCSORTHOREF                           bit.handle   Available in DWG version 2000 and above only.
   PUCSORTHOVIEW                          float        Available in DWG version 2000 and above only.
   PUCSBASE                               bit.handle   Available in DWG version 2000 and above only.
   PUCSORGTOP                             bit.point3D  Available in DWG version 2000 and above only.
   PUCSORGBOTTOM                          bit.point3D  Available in DWG version 2000 and above only.
   PUCSORGLEFT                            bit.point3D  Available in DWG version 2000 and above only.
   PUCSORGRIGHT                           bit.point3D  Available in DWG version 2000 and above only.
   PUCSORGFRONT                           bit.point3D  Available in DWG version 2000 and above only.
   PUCSORGBACK                            bit.point3D  Available in DWG version 2000 and above only.
   INSBASE_MS                             bit.point3D  Available in all DWG versions.
   EXTMIN_MS                              bit.point3D  Available in all DWG versions.
   EXTMAX_MS                              bit.point3D  Available in all DWG versions.
   LIMMIN_MS                              bit.point2D  Available in all DWG versions.
   LIMMAX_MS                              bit.point2D  Available in all DWG versions.
   ELEVATION_MS                           float        Available in all DWG versions.
   UCSORG_MS                              bit.point3D  Available in all DWG versions.
   UCSXDIR_MS                             bit.point3D  Available in all DWG versions.
   UCSYDIR_MS                             bit.point3D  Available in all DWG versions.
   UCSNAME_MS                             bit.handle   Available in all DWG versions.
   UCSORTHOREF                            bit.handle   Available in DWG version 2000 and above only.
   UCSORTHOVIEW                           float        Available in DWG version 2000 and above only.
   UCSBASE                                bit.handle   Available in DWG version 2000 and above only.
   UCSORGTOP                              bit.point3D  Available in DWG version 2000 and above only.
   UCSORGBOTTOM                           bit.point3D  Available in DWG version 2000 and above only.
   UCSORGLEFT                             bit.point3D  Available in DWG version 2000 and above only.
   UCSORGRIGHT                            bit.point3D  Available in DWG version 2000 and above only.
   UCSORGFRONT                            bit.point3D  Available in DWG version 2000 and above only.
   UCSORGBACK                             bit.point3D  Available in DWG version 2000 and above only.
   DIMPOST                                str          Available in DWG version 2000 and above only.
   DIMAPOST                               str          Available in DWG version 2000 and above only.
   DIMTOL                                 int          Available in DWG version 13 and 14 only.
   DIMLIM                                 int          Available in DWG version 13 and 14 only.
   DIMTIH                                 int          Available in DWG version 13 and 14 only.
   DIMTOH                                 int          Available in DWG version 13 and 14 only.
   DIMSE1                                 int          Available in DWG version 13 and 14 only.
   DIMSE2                                 int          Available in DWG version 13 and 14 only.
   DIMALT                                 int          Available in DWG version 13 and 14 only.
   DIMTOFL                                int          Available in DWG version 13 and 14 only.
   DIMSAH                                 int          Available in DWG version 13 and 14 only.
   DIMTIX                                 int          Available in DWG version 13 and 14 only.
   DIMSOXD                                int          Available in DWG version 13 and 14 only.
   DIMALTD                                int          Available in DWG version 13 and 14 only.
   DIMZIN                                 int          Available in DWG version 13 and 14 only.
   DIMSD1                                 int          Available in DWG version 13 and 14 only.
   DIMSD2                                 int          Available in DWG version 13 and 14 only.
   DIMTOLJ                                int          Available in DWG version 13 and 14 only.
   DIMJUST                                int          Available in DWG version 13 and 14 only.
   DIMFIT                                 int          Available in DWG version 13 and 14 only.
   DIMUPT                                 int          Available in DWG version 13 and 14 only.
   DIMTZIN                                int          Available in DWG version 13 and 14 only.
   DIMALTZ                                int          Available in DWG version 13 and 14 only.
   DIMALTTZ                               int          Available in DWG version 13 and 14 only.
   DIMTAD                                 int          Available in DWG version 13 and 14 only.
   DIMUNIT                                float        Available in DWG version 13 and 14 only.
   DIMAUNIT                               float        Available in DWG version 13 and 14 only.
   DIMDEC                                 float        Available in DWG version 13 and 14 only.
   DIMTDEC                                float        Available in DWG version 13 and 14 only.
   DIMALTU                                float        Available in DWG version 13 and 14 only.
   DIMALTTD                               float        Available in DWG version 13 and 14 only.
   DIMTXSTY                               bit.handle   Available in DWG version 13 and 14 only.
   DIMSCALE                               float        Available in all DWG versions.
   DIMASZ                                 float        Available in all DWG versions.
   DIMEXO                                 float        Available in all DWG versions.
   DIMDLI                                 float        Available in all DWG versions.
   DIMEXE                                 float        Available in all DWG versions.
   DIMRND                                 float        Available in all DWG versions.
   DIMDLE                                 float        Available in all DWG versions.
   DIMTP                                  float        Available in all DWG versions.
   DIMTM                                  float        Available in all DWG versions.
   DIMFXL                                 float        Available in DWG version 2007 and above only.
   DIMJOGANG                              float        Available in DWG version 2007 and above only.
   DIMTFILL                               float        Available in DWG version 2007 and above only.
   DIMTFILLCLR                            bit.color    Available in DWG version 2007 and above only.
   DIMTOL                                 int          Available in DWG version 2000 and above only.
   DIMLIM                                 int          Available in DWG version 2000 and above only.
   DIMTIH                                 int          Available in DWG version 2000 and above only.
   DIMTOH                                 int          Available in DWG version 2000 and above only.
   DIMSE1                                 int          Available in DWG version 2000 and above only.
   DIMSE2                                 int          Available in DWG version 2000 and above only.
   DIMTAD                                 float        Available in DWG version 2000 and above only.
   DIMZIN                                 float        Available in DWG version 2000 and above only.
   DIMAZIN                                float        Available in DWG version 2000 and above only.
   DIMARCSYM                              float        Available in DWG version 2007 and above only.
   DIMTXT                                 float        Available in all DWG versions.
   DIMCEN                                 float        Available in all DWG versions.
   DIMTSZ                                 float        Available in all DWG versions.
   DIMALTF                                float        Available in all DWG versions.
   DIMLFAC                                float        Available in all DWG versions.
   DIMTVP                                 float        Available in all DWG versions.
   DIMTFAC                                float        Available in all DWG versions.
   DIMGAP                                 float        Available in all DWG versions.
   DIMPOST                                str          Available in DWG version 13 and 14 only.
   DIMAPOST                               str          Available in DWG version 13 and 14 only.
   DIMBLK                                 str          Available in DWG version 13 and 14 only.
   DIMBLK1                                str          Available in DWG version 13 and 14 only.
   DIMBLK2                                str          Available in DWG version 13 and 14 only.
   DIMALTRND                              float        Available in DWG version 2000 and above only.
   DIMALT                                 int          Available in DWG version 2000 and above only.
   DIMALTD                                float        Available in DWG version 2000 and above only.
   DIMTOFL                                int          Available in DWG version 2000 and above only.
   DIMSAH                                 int          Available in DWG version 2000 and above only.
   DIMTIX                                 int          Available in DWG version 2000 and above only.
   DIMSOXD                                int          Available in DWG version 2000 and above only.
   DIMCLRD                                bit.color    Available in all DWG versions.
   DIMCLRE                                bit.color    Available in all DWG versions.
   DIMCLRT                                bit.color    Available in all DWG versions.
   DIMADEC                                float        Available in DWG version 2000 and above only.
   DIMDEC                                 float        Available in DWG version 2000 and above only.
   DIMTDEC                                float        Available in DWG version 2000 and above only.
   DIMALTU                                float        Available in DWG version 2000 and above only.
   DIMALTTD                               float        Available in DWG version 2000 and above only.
   DIMAUNIT                               float        Available in DWG version 2000 and above only.
   DIMFRAC                                float        Available in DWG version 2000 and above only.
   DIMLUNIT                               float        Available in DWG version 2000 and above only.
   DIMDSEP                                float        Available in DWG version 2000 and above only.
   DIMTMOVE                               float        Available in DWG version 2000 and above only.
   DIMJUST                                float        Available in DWG version 2000 and above only.
   DIMSD1                                 int          Available in DWG version 2000 and above only.
   DIMSD2                                 int          Available in DWG version 2000 and above only.
   DIMTOLJ                                float        Available in DWG version 2000 and above only.
   DIMTZIN                                float        Available in DWG version 2000 and above only.
   DIMALTZ                                float        Available in DWG version 2000 and above only.
   DIMALTTZ                               float        Available in DWG version 2000 and above only.
   DIMUPT                                 int          Available in DWG version 2000 and above only.
   DIMATFIT                               float        Available in DWG version 2000 and above only.
   DIMFXLON                               int          Available in DWG version 2007 and above only.
   DIMTXTDIRECTION                        int          Available in DWG version 2010 and above only.
   DIMALTMZF                              float        Available in DWG version 2010 and above only.
   DIMALTMZS                              str          Available in DWG version 2010 and above only.
   DIMMZF                                 float        Available in DWG version 2010 and above only.
   DIMMZS                                 str          Available in DWG version 2010 and above only.
   DIMTXSTY                               bit.handle   Available in DWG version 2000 and above only.
   DIMLDRBLK                              bit.handle   Available in DWG version 2000 and above only.
   DIMBLK                                 bit.handle   Available in DWG version 2000 and above only.
   DIMBLK1                                bit.handle   Available in DWG version 2000 and above only.
   DIMBLK2                                bit.handle   Available in DWG version 2000 and above only.
   DIMLTYPE                               bit.handle   Available in DWG version 2007 and above only.
   DIMLTEX1                               bit.handle   Available in DWG version 2007 and above only.
   DIMLTEX2                               bit.handle   Available in DWG version 2007 and above only.
   DIMLWD                                 float        Available in DWG version 2000 and above only.
   DIMLWE                                 float        Available in DWG version 2000 and above only.
   BLOCK_CONTROL_OBJECT                   bit.handle   Available in all DWG versions.
   LAYER_CONTROL_OBJECT                   bit.handle   Available in all DWG versions.
   STYLE_CONTROL_OBJECT                   bit.handle   Available in all DWG versions.
   LINETYPE_CONTROL_OBJECT                bit.handle   Available in all DWG versions.
   VIEW_CONTROL_OBJECT                    bit.handle   Available in all DWG versions.
   UCS_CONTROL_OBJECT                     bit.handle   Available in all DWG versions.
   VPORT_CONTROL_OBJECT                   bit.handle   Available in all DWG versions.
   APPID_CONTROL_OBJECT                   bit.handle   Available in all DWG versions.
   DIMSTYLE_CONTROL_OBJECT                bit.handle   Available in all DWG versions.
   VIEWPORT_ENTITY_HEADER_CONTROL_OBJECT  bit.handle   Available in DWG version 13, 14 and 2000 only.
   DICTIONARY_ACAD_GROUP                  bit.handle   Available in all DWG versions.
   DICTIONARY_ACAD_MLINESTYLE             bit.handle   Available in all DWG versions.
   DICTIONARY_NAMED_OBJECTS               bit.handle   Available in all DWG versions.
   TSTACKALIGN                            float        Available in DWG version 2000 and above only.
   TSTACKSIZE                             float        Available in DWG version 2000 and above only.
   HYPERLINKBASE                          str          Available in DWG version 2000 and above only.
   STYLESHEET                             str          Available in DWG version 2000 and above only.
   DICTIONARY_LAYOUTS                     bit.handle   Available in DWG version 2000 and above only.
   DICTIONARY_PLOTSETTINGS                bit.handle   Available in DWG version 2000 and above only.
   DICTIONARY_PLOTSTYLES                  bit.handle   Available in DWG version 2000 and above only.
   DICTIONARY_MATERIALS                   bit.handle   Available in DWG version 2004 and above only.
   DICTIONARY_COLORS                      bit.handle   Available in DWG version 2004 and above only.
   DICTIONARY_VISUALSTYLE                 bit.handle   Available in DWG version 2007 and above only.
   UNKNOWN_18                             bit.handle   Available in DWG version 2013 and above only.
   FLAGS                                  float        Available in DWG version 2000 and above only.
   INSUNITS                               float        Available in DWG version 2000 and above only.
   CEPSNTYPE                              float        Available in DWG version 2000 and above only.
   CPSNID                                 bit.handle   Available in DWG version 2000 and above only.
   FINGERPRINTGUID                        str          Available in DWG version 2000 and above only.
   VERSIONGUID                            str          Available in DWG version 2000 and above only.
   SORTENTS                               int          Available in DWG version 2004 and above only.
   INDEXCTL                               int          Available in DWG version 2004 and above only.
   HIDETEXT                               int          Available in DWG version 2004 and above only.
   XCLIPFRAME                             int          Available in DWG version 2004 and above only.
   DIMASSOC                               int          Available in DWG version 2004 and above only.
   HALOGAP                                int          Available in DWG version 2004 and above only.
   OBSCUREDCOLOR                          float        Available in DWG version 2004 and above only.
   INTERSECTIONCOLOR                      float        Available in DWG version 2004 and above only.
   OBSCUREDLTYPE                          int          Available in DWG version 2004 and above only.
   INTERSECTIONDISPLAY                    int          Available in DWG version 2004 and above only.
   PROJECTNAME                            str          Available in DWG version 2004 and above only.
   BLOCK_RECORD_PS                        bit.handle   Available in all DWG versions.
   BLOCK_RECORD_MS                        bit.handle   Available in all DWG versions.
   LTYPE_BYLAYER                          bit.handle   Available in all DWG versions.
   LTYPE_BYBLOCK                          bit.handle   Available in all DWG versions.
   LTYPE_CONTINUOUS                       bit.handle   Available in all DWG versions.
   CAMERADISPLAY                          int          Available in DWG version 2007 and above only.
   UNKNOWN_19                             float        Available in DWG version 2007 and above only.
   UNKNOWN_20                             float        Available in DWG version 2007 and above only.
   UNKNOWN_21                             float        Available in DWG version 2007 and above only.
   STEPSPERSEC                            float        Available in DWG version 2007 and above only.
   STEPSIZE                               float        Available in DWG version 2007 and above only.
   DWFPREC_3D                             float        Available in DWG version 2007 and above only.
   LENSLENGTH                             float        Available in DWG version 2007 and above only.
   CAMERAHEIGHT                           float        Available in DWG version 2007 and above only.
   SOLIDHIST                              int          Available in DWG version 2007 and above only.
   SHOWHIST                               int          Available in DWG version 2007 and above only.
   PSOLWIDTH                              float        Available in DWG version 2007 and above only.
   PSOLHEIGHT                             float        Available in DWG version 2007 and above only.
   LOFTANG1                               float        Available in DWG version 2007 and above only.
   LOFTANG2                               float        Available in DWG version 2007 and above only.
   LOFTMAG1                               float        Available in DWG version 2007 and above only.
   LOFTMAG2                               float        Available in DWG version 2007 and above only.
   LOFTPARAM                              float        Available in DWG version 2007 and above only.
   LOFTNORMALS                            int          Available in DWG version 2007 and above only.
   LATITUDE                               float        Available in DWG version 2007 and above only.
   LONGITUDE                              float        Available in DWG version 2007 and above only.
   NORTHDIRECTION                         float        Available in DWG version 2007 and above only.
   TIMEZONE                               float        Available in DWG version 2007 and above only.
   LIGHTGLYPHDISPLAY                      int          Available in DWG version 2007 and above only.
   TILEMODELIGHTSYNCH                     int          Available in DWG version 2007 and above only.
   DWFFRAME                               int          Available in DWG version 2007 and above only.
   DGNFRAME                               int          Available in DWG version 2007 and above only.
   UNKNOWN_22                             int          Available in DWG version 2007 and above only.
   INTERFERECOLOR                         bit.color    Available in DWG version 2007 and above only.
   INTERFEREOBJVS                         bit.handle   Available in DWG version 2007 and above only.
   INTERFEREVPVS                          bit.handle   Available in DWG version 2007 and above only.
   DRAGVS                                 bit.handle   Available in DWG version 2007 and above only.
   CSHADOW                                int          Available in DWG version 2007 and above only.
   UNKNOWN_23                             float        Available in DWG version 2007 and above only.
   UNKNOWN_24                             float        Available in DWG version 14 and above only.
   UNKNOWN_25                             float        Available in DWG version 14 and above only.
   UNKNOWN_26                             float        Available in DWG version 14 and above only.
   UNKNOWN_27                             float        Available in DWG version 14 and above only.
   CELWEIGHT                              int          Available in all DWG versions.
   ENDCAPS                                int          Available in all DWG versions.
   JOINSTYLE                              int          Available in all DWG versions.
   LWDISPLAY                              int          Available in all DWG versions.
   XEDIT                                  int          Available in all DWG versions.
   EXTNAMES                               int          Available in all DWG versions.
   PSTYLEMODE                             int          Available in all DWG versions.
   OLESTARTUP                             int          Available in all DWG versions.
   =====================================  ===========  ====================================================

   .. note::
      UNKNOWN variables are those which are yet to be reverse engineered.