/*****************************************************************************/
/*  libgpdwg - free c library to read .dwg files.                               */
/*                                                                           */
/*  Copyright (C) 2018-2021 Guruprasad Rane <raneguruprasad@gmail.com>       */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License version 3. You should have received a copy of     */
/*  the GNU General Public License along with this program.                  */
/*                                                                           */
/*****************************************************************************/
#ifndef LIBGPDWG_H
#define LIBGPDWG_H

#include <stdint.h>

#define LOG_NONE 0
#define LOG_ERROR 1
#define LOG_INFO 2
#define LOG_DEBUG 3

#define BITCODE_B uint8_t
#define FORMAT_B PRIu8
#define BITCODE_BB uint8_t
#define FORMAT_BB PRIu8
#define BITCODE_BD uint64_t
#define FORMAT_BD PRIu64
#define BITCODE_BL uint32_t
#define FORMAT_BL PRIu32
#define BITCODE_BLL uint64_t
#define FORMAT_BLL PRIu64
#define BITCODE_BS uint16_t
#define FORMAT_BS PRIu16
#define BITCODE_RC uint8_t
#define FORMAT_RC PRIu8
#define BITCODE_RD uint64_t
#define FORMAT_RD PRIu32
#define BITCODE_RL uint32_t
#define FORMAT_RL PRIu32
#define BITCODE_RS uint16_t
#define FORMAT_RS PRIu16
#define BITCODE_T uint8_t * 
#define FORMAT_T "%s"
#define BITCODE_TV uint8_t * 
#define FORMAT_TV "%s"




/*
#define BITCODE_DOUBLE double
#define BITCODE_RC uint8_t
#define FORMAT_RC PRIu8
#define BITCODE_MC int32_t
#define FORMAT_MC "%li"
#define BITCODE_MS uint32_t
#define FORMAT_MS "%lu"
#define BITCODE_B uint8_t
#define FORMAT_B "%d"
#define BITCODE_BB uint8_t
#define FORMAT_BB "%d"
#define BITCODE_BS uint16_t
#define FORMAT_BS "%d"
#define BITCODE_RS uint16_t
#define FORMAT_RS PRIu16
#define BITCODE_RL uint32_t
#define FORMAT_RL PRIu32
#define BITCODE_RD BITCODE_DOUBLE
#define FORMAT_RD "%g"
#define BITCODE_BL uint32_t
#define FORMAT_BL "%lu"
#define BITCODE_TV uint8_t *
#define FORMAT_TV "\"%s\""
#define BITCODE_BT BITCODE_DOUBLE
#define FORMAT_BT "%g"
#define BITCODE_DD BITCODE_DOUBLE
#define FORMAT_DD "%g"
#define BITCODE_BD BITCODE_DOUBLE
#define FORMAT_BD "%g"
#define BITCODE_BE BITCODE_3BD 
#define BITCODE_CMC Dwg_Color
#define BITCODE_H Dwg_Handle
#define BITCODE_4BITS BITCODE_RC
#define FORMAT_4BITS "%1x" 
#define BITCODE_T BITCODE_TV 
#define BITCODE_CRC uint16_t

*/

typedef enum bitcode_type
{
	RC,
	RL,
	RS,
	BL,
	BLL,
	BD,
	TV,
	BS,
	H,
	B,
	CMC,
	BD3,
	RD2,
	T,
	MC,
} BITCODE_TYPE;

typedef struct gpdwg_handle
{	
	BITCODE_RC code;
	BITCODE_RC size;
	BITCODE_RC value;
}GPDWG_HANDLE;

typedef struct gpdwg_point3D
{
	uint32_t x;
	uint32_t y;
	uint32_t z;
}GPDWG_POINT3D;

typedef struct gpdwg_point2D
{
	uint32_t x;
	uint32_t y;
}GPDWG_POINT2D;

typedef struct gpdwg_color
{
	BITCODE_BS index;
	char * name;
	char * book_name;
	uint8_t rgb;
	uint8_t byte;
}GPDWG_COLOR;

#define BITCODE_BD3 GPDWG_POINT3D
#define FORMAT_BD3 "d Pt(%d,%d)"
#define BITCODE_CMC GPDWG_COLOR
#define FORMAT_CMC Cl(%PRIu8,%PRIu16,%s,%PRIu16,%s)
#define BITCODE_H GPDWG_HANDLE
#define FORMAT_H "H(%i,%i,%i)"
#define BITCODE_RD2 GPDWG_POINT2D
#define FORMAT_RD2 Pt(%d,%d)

typedef enum dwg_sentinel
{
DWG_SENTINEL_HEADER_END,
DWG_SENTINEL_PICTURE_BEGIN,
DWG_SENTINEL_PICTURE_END,
DWG_SENTINEL_VARIABLE_BEGIN,
DWG_SENTINEL_VARIABLE_END,
DWG_SENTINEL_CLASS_BEGIN,
DWG_SENTINEL_CLASS_END,
DWG_SENTINEL_SECOND_HEADER_BEGIN,
DWG_SENTINEL_SECOND_HEADER_END
} DWG_SENTINAL;

typedef struct bit_data
{
	uint8_t *chain;
	uint32_t byte;
	uint32_t size;
	uint8_t bit;
	uint16_t version;
}Bit_Data;
typedef struct gpdwg_section
{
	uint8_t number;
	uint32_t address;
	uint32_t size;
	struct gpdwg_section* next;

}Gpdwg_Section;
typedef struct gpdwg_header
{
	uint8_t codepage;
	uint32_t sectionCount;
	struct gpdwg_section* section;
}Gpdwg_Header;


typedef struct variables
{
	BITCODE_BD angbase;
	BITCODE_B angdir;
	GPDWG_HANDLE appid_control_object;
	BITCODE_B attdia;
	BITCODE_BS attmode;
	BITCODE_B attreq;
	BITCODE_BS aunits;
	BITCODE_BS auprec;
	BITCODE_B blipmode;
	GPDWG_HANDLE block_control_object;
	GPDWG_HANDLE block_record_ms;
	GPDWG_HANDLE block_record_ps;
	BITCODE_B cameradisplay;
	BITCODE_BD cameraheight;
	GPDWG_COLOR cecolor;
	BITCODE_BD celtscale;
	GPDWG_HANDLE celtype;
	uint8_t celweight;
	BITCODE_BS cepsntype;
	BITCODE_BD chamfera;
	BITCODE_BD chamferb;
	BITCODE_BD chamferc;
	BITCODE_BD chamferd;
	GPDWG_HANDLE clayer;
	GPDWG_HANDLE cmaterial;
	BITCODE_BS cmljust;
	BITCODE_BD cmlscale;
	GPDWG_HANDLE cmlstyle;
	BITCODE_BS coords;
	GPDWG_HANDLE cpsnid;
	BITCODE_RC cshadow;
	GPDWG_HANDLE current_viewport_handle;
	BITCODE_B delobj;
	BITCODE_RC dgnframe;
	GPDWG_HANDLE dictionary_acad_group;
	GPDWG_HANDLE dictionary_acad_mlinestyle;
	GPDWG_HANDLE dictionary_colors;
	GPDWG_HANDLE dictionary_layouts;
	GPDWG_HANDLE dictionary_materials;
	GPDWG_HANDLE dictionary_named_objects;
	GPDWG_HANDLE dictionary_plotsettings;
	GPDWG_HANDLE dictionary_plotstyles;
	GPDWG_HANDLE dictionary_visualstyle;
	BITCODE_BS dimadec;
	BITCODE_B dimalt;
	BITCODE_BS dimaltd;
	BITCODE_BD dimaltf;
	BITCODE_BD dimaltmzf;
	BITCODE_T dimaltmzs;
	BITCODE_BD dimaltrnd;
	BITCODE_BS dimalttd;
	BITCODE_BS dimalttz;
	BITCODE_BS dimaltu;
	BITCODE_BS dimaltz;
	BITCODE_T dimapost;
	BITCODE_BS dimarcsym;
	BITCODE_B dimaso;
	BITCODE_RC dimassoc;
	BITCODE_BD dimasz;
	BITCODE_BS dimatfit;
	BITCODE_BS dimaunit;
	BITCODE_BS dimazin;
	GPDWG_HANDLE dimblk;
	GPDWG_HANDLE dimblk1;
	GPDWG_HANDLE dimblk2;
	BITCODE_BD dimcen;
	GPDWG_COLOR dimclrd;
	GPDWG_COLOR dimclre;
	GPDWG_COLOR dimclrt;
	BITCODE_BS dimdec;
	BITCODE_BD dimdle;
	BITCODE_BD dimdli;
	BITCODE_BS dimdsep;
	BITCODE_BD dimexe;
	BITCODE_BD dimexo;
	BITCODE_RC dimfit;
	BITCODE_BS dimfrac;
	BITCODE_BD dimfxl;
	BITCODE_B dimfxlon;
	BITCODE_BD dimgap;
	BITCODE_BD dimjogang;
	BITCODE_BS dimjust;
	GPDWG_HANDLE dimldrblk;
	BITCODE_BD dimlfac;
	BITCODE_B dimlim;
	GPDWG_HANDLE dimltex1;
	GPDWG_HANDLE dimltex2;
	GPDWG_HANDLE dimltype;
	BITCODE_BS dimlunit;
	BITCODE_BS dimlwd;
	BITCODE_BS dimlwe;
	BITCODE_BD dimmzf;
	BITCODE_T dimmzs;
	BITCODE_T dimpost;
	BITCODE_BD dimrnd;
	BITCODE_B dimsah;
	BITCODE_B dimsav;
	BITCODE_BD dimscale;
	BITCODE_B dimsd1;
	BITCODE_B dimsd2;
	BITCODE_B dimse1;
	BITCODE_B dimse2;
	BITCODE_B dimsho;
	BITCODE_B dimsoxd;
	GPDWG_HANDLE dimstyle;
	GPDWG_HANDLE dimstyle_control_object;
	BITCODE_BS dimtad;
	BITCODE_BS dimtdec;
	BITCODE_BD dimtfac;
	BITCODE_BS dimtfill;
	GPDWG_COLOR dimtfillclr;
	BITCODE_B dimtih;
	BITCODE_B dimtix;
	BITCODE_BD dimtm;
	BITCODE_BS dimtmove;
	BITCODE_B dimtofl;
	BITCODE_B dimtoh;
	BITCODE_B dimtol;
	BITCODE_BS dimtolj;
	BITCODE_BD dimtp;
	BITCODE_BD dimtsz;
	BITCODE_BD dimtvp;
	GPDWG_HANDLE dimtxsty;
	BITCODE_BD dimtxt;
	BITCODE_B dimtxtdirection;
	BITCODE_BS dimtzin;
	BITCODE_BS dimunit;
	BITCODE_B dimupt;
	BITCODE_BS dimzin;
	BITCODE_B dispsilh;
	BITCODE_BS dragmode;
	GPDWG_HANDLE dragvs;
	BITCODE_RC dwfframe;
	BITCODE_BD dwfprec_3d;
	BITCODE_BD elevation_ms;
	BITCODE_BD elevation_ps;
	uint8_t endcaps;
	GPDWG_POINT3D extmax_ms;
	GPDWG_POINT3D extmax_ps;
	GPDWG_POINT3D extmin_ms;
	GPDWG_POINT3D extmin_ps;
	uint8_t extnames;
	BITCODE_BD facetres;
	BITCODE_BD filletrad;
	BITCODE_B fillmode;
	BITCODE_TV fingerprintguid;
	BITCODE_BL flags;
	BITCODE_RC halogap;
	GPDWG_HANDLE handseed;
	BITCODE_RC hidetext;
	BITCODE_TV hyperlinkbase;
	BITCODE_RC indexctl;
	GPDWG_POINT3D insbase_ms;
	GPDWG_POINT3D insbase_ps;
	BITCODE_BS insunits;
	GPDWG_COLOR interferecolor;
	GPDWG_HANDLE interfereobjvs;
	GPDWG_HANDLE interferevpvs;
	BITCODE_BS intersectioncolor;
	BITCODE_RC intersectiondisplay;
	BITCODE_BS isolines;
	uint8_t joinstyle;
	BITCODE_BD latitude;
	GPDWG_HANDLE layer_control_object;
	BITCODE_BD lenslength;
	BITCODE_RC lightglyphdisplay;
	BITCODE_B limcheck;
	GPDWG_POINT2D limmax_ms;
	GPDWG_POINT2D limmax_ps;
	GPDWG_POINT2D limmin_ms;
	GPDWG_POINT2D limmin_ps;
	GPDWG_HANDLE linetype_control_object;
	BITCODE_BD loftang1;
	BITCODE_BD loftang2;
	BITCODE_BD loftmag1;
	BITCODE_BD loftmag2;
	BITCODE_RC loftnormals;
	BITCODE_BS loftparam;
	BITCODE_BD longitude;
	BITCODE_BD ltscale;
	GPDWG_HANDLE ltype_byblock;
	GPDWG_HANDLE ltype_bylayer;
	GPDWG_HANDLE ltype_continuous;
	BITCODE_BS lunits;
	BITCODE_BS luprec;
	uint8_t lwdisplay;
	BITCODE_BS maxactvp;
	BITCODE_TV menuname;
	BITCODE_B mirrtext;
	BITCODE_BD northdirection;
	BITCODE_BS obscuredcolor;
	BITCODE_RC obscuredltype;
	uint8_t olestartup;
	BITCODE_B orthomode;
	BITCODE_BS osmode;
	BITCODE_BS pdmode;
	BITCODE_BD pdsize;
	BITCODE_B pellipse;
	BITCODE_BS pickstyle;
	BITCODE_B plimcheck;
	BITCODE_B plinegen;
	BITCODE_BD plinewid;
	BITCODE_TV projectname;
	BITCODE_BS proxygraphics;
	BITCODE_B psltscale;
	BITCODE_BD psolheight;
	BITCODE_BD psolwidth;
	uint8_t pstylemode;
	BITCODE_BD psvpscale;
	GPDWG_HANDLE pucsbase;
	GPDWG_POINT3D pucsorgback;
	GPDWG_POINT3D pucsorgbottom;
	GPDWG_POINT3D pucsorgfront;
	GPDWG_POINT3D pucsorgleft;
	GPDWG_POINT3D pucsorgright;
	GPDWG_POINT3D pucsorgtop;
	GPDWG_HANDLE pucsorthoref;
	BITCODE_BS pucsorthoview;
	BITCODE_B qtextmode;
	BITCODE_B regenmode;
	BITCODE_BL requiredversions;
	BITCODE_BS shadedge;
	BITCODE_BS shadedif;
	BITCODE_RC showhist;
	BITCODE_RL size_in_bits;
	BITCODE_BD sketchinc;
	BITCODE_B skpoly;
	BITCODE_RC solidhist;
	BITCODE_RC sortents;
	BITCODE_B splframe;
	BITCODE_BS splinesegs;
	BITCODE_BS splinetype;
	BITCODE_BD stepsize;
	BITCODE_BD stepspersec;
	BITCODE_TV stylesheet;
	GPDWG_HANDLE style_control_object;
	BITCODE_BS surftab1;
	BITCODE_BS surftab2;
	BITCODE_BS surftype;
	BITCODE_BS surfu;
	BITCODE_BS surfv;
	BITCODE_BL tdcreate_jd;
	BITCODE_BL tdcreate_ms;
	BITCODE_BL tdindwg_jd;
	BITCODE_BL tdindwg_ms;
	BITCODE_BL tdupdate_jd;
	BITCODE_BL tdupdate_ms;
	BITCODE_BL tdusrtimer_jd;
	BITCODE_BL tdusrtimer_ms;
	BITCODE_BS textqlty;
	BITCODE_BD textsize;
	GPDWG_HANDLE textstyle;
	BITCODE_BD thickness;
	BITCODE_B tilemode;
	BITCODE_RC tilemodelightsynch;
	BITCODE_BL timezone;
	BITCODE_BD tracewid;
	BITCODE_BS treedepth;
	BITCODE_BS tstackalign;
	BITCODE_BS tstacksize;
	GPDWG_HANDLE ucsbase;
	GPDWG_HANDLE ucsname_ms;
	GPDWG_HANDLE ucsname_ps;
	GPDWG_POINT3D ucsorgback;
	GPDWG_POINT3D ucsorgbottom;
	GPDWG_POINT3D ucsorgfront;
	GPDWG_POINT3D ucsorgleft;
	GPDWG_POINT3D ucsorgright;
	GPDWG_POINT3D ucsorgtop;
	GPDWG_POINT3D ucsorg_ms;
	GPDWG_POINT3D ucsorg_ps;
	GPDWG_HANDLE ucsorthoref;
	BITCODE_BS ucsorthoview;
	GPDWG_POINT3D ucsxdir_ms;
	GPDWG_POINT3D ucsxdir_ps;
	GPDWG_POINT3D ucsydir_ms;
	GPDWG_POINT3D ucsydir_ps;
	GPDWG_HANDLE ucs_control_object;
	BITCODE_B undocumented;
	BITCODE_BS unitmode;
	BITCODE_BD unknown_01;
	BITCODE_BD unknown_02;
	BITCODE_BD unknown_03;
	BITCODE_BD unknown_04;
	BITCODE_TV unknown_05;
	BITCODE_TV unknown_06;
	BITCODE_TV unknown_07;
	BITCODE_TV unknown_08;
	BITCODE_BL unknown_09;
	BITCODE_BL unknown_10;
	BITCODE_BS unknown_11;
	BITCODE_BL unknown_12;
	BITCODE_BL unknown_13;
	BITCODE_BL unknown_14;
	BITCODE_BL unknown_15;
	BITCODE_BL unknown_16;
	BITCODE_BL unknown_17;
	GPDWG_HANDLE unknown_18;
	BITCODE_BL unknown_19;
	BITCODE_BL unknown_20;
	BITCODE_BD unknown_21;
	BITCODE_B unknown_22;
	BITCODE_BD unknown_23;
	BITCODE_BS unknown_24;
	BITCODE_BS unknown_25;
	BITCODE_BS unknown_26;
	BITCODE_BS unknown_27;
	BITCODE_BS useri1;
	BITCODE_BS useri2;
	BITCODE_BS useri3;
	BITCODE_BS useri4;
	BITCODE_BS useri5;
	BITCODE_BD userr1;
	BITCODE_BD userr2;
	BITCODE_BD userr3;
	BITCODE_BD userr4;
	BITCODE_BD userr5;
	BITCODE_B usrtimer;
	BITCODE_TV versionguid;
	GPDWG_HANDLE viewport_entity_header_control_object;
	GPDWG_HANDLE view_control_object;
	BITCODE_B visretain;
	GPDWG_HANDLE vport_control_object;
	BITCODE_B wireframe;
	BITCODE_B worldview;
	BITCODE_RC xclipframe;
	uint8_t xedit;
}VARIABLES;

typedef struct gpdwg_data
{
	Gpdwg_Header header;
	struct variables variables;
}Gpdwg_Data;

typedef union bitcodes_all
{
	BITCODE_B bitcode_b;
	BITCODE_BD bitcode_bd;
	BITCODE_BD3 bitcode_bd3;
	BITCODE_BL bitcode_bl;
	BITCODE_BLL bitcode_bll;
	BITCODE_BS bitcode_bs;
	BITCODE_CMC bitcode_cmc;
	BITCODE_H bitcode_h;
	BITCODE_RC bitcode_rc;
	BITCODE_RS bitcode_rs;
	BITCODE_RD2 bitcode_rd2;
	BITCODE_RL bitcode_rl;
	BITCODE_T bitcode_t;
	BITCODE_TV bitcode_tv;
}BITCODES_ALL;

/*
typedef union bitcodes_all
{
	BITCODE_RC bitcode_rc;
	BITCODE_MC bitcode_mc;
	BITCODE_MS bitcode_ms;
	BITCODE_B  bitcode_b;
	BITCODE_BB bitcode_bb;
	BITCODE_BS bitcode_bs;
	BITCODE_RS bitcode_rs;
	BITCODE_RL bitcode_rl;
	BITCODE_RD bitcode_rd;
	BITCODE_BL bitcode_bl;
	BITCODE_TV bitcode_tv;
	BITCODE_BT bitcode_bt;
	BITCODE_DD bitcode_dd;
	BITCODE_BD bitcode_bd;
	BITCODE_BE bitcode_be;
	BITCODE_H  bitcode_h;
	BITCODE_T  bitcode_t;
} BITCODES_ALL;
*/

int libgpdwg_loglevel;

void gpdwg_log_level(int level);
int gpdwg_read(char *filename, Gpdwg_Data  *gpdwg);


#endif