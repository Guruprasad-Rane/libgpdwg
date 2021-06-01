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

#include "variables.h"
#include "bit.h"
#include "logger.h"
#include "libgpdwg.h"
#include <stdio.h>
#include <inttypes.h>
#include <string.h>
int read_variables(Bit_Data *dat, Gpdwg_Data *gpdwg)
{
	BITCODES_ALL read_data;
	if (dat->version == 2007)
	{
		read_data=readwithlog(RL,dat,"SIZE_IN_BITS");//gpdwg->variable.size_in_bits=read_data.bitcode_rl;
	}
	if (dat->version >= 2013)
	{
		read_data=readwithlog(BLL,dat,"REQUIREDVERSIONS");//gpdwg->variable.requiredversions=read_data.bitcode_bll;
	}
	read_data=readwithlog(BD,dat,"UNKNOWN_01");//gpdwg->variable.unknown_01=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"UNKNOWN_02");//gpdwg->variable.unknown_02=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"UNKNOWN_03");//gpdwg->variable.unknown_03=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"UNKNOWN_04");//gpdwg->variable.unknown_04=read_data.bitcode_bd;
	read_data=readwithlog(TV,dat,"UNKNOWN_05");//gpdwg->variable.unknown_05=read_data.bitcode_tv;
	read_data=readwithlog(TV,dat,"UNKNOWN_06");//gpdwg->variable.unknown_06=read_data.bitcode_tv;
	read_data=readwithlog(TV,dat,"UNKNOWN_07");//gpdwg->variable.unknown_07=read_data.bitcode_tv;
	read_data=readwithlog(TV,dat,"UNKNOWN_08");//gpdwg->variable.unknown_08=read_data.bitcode_tv;
	read_data=readwithlog(BL,dat,"UNKNOWN_09");//gpdwg->variable.unknown_09=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"UNKNOWN_10");//gpdwg->variable.unknown_10=read_data.bitcode_bl;
	if (dat->version <= 14)
	{
		read_data=readwithlog(BS,dat,"UNKNOWN_11");//gpdwg->variable.unknown_11=read_data.bitcode_bs;
	}
	if (dat->version <= 2000)
	{
		read_data=readwithlog(H,dat,"CURRENT_VIEWPORT_HANDLE");//gpdwg->variable.current_viewport_handle=read_data.bitcode_h;
	}
	read_data=readwithlog(B,dat,"DIMASO");//gpdwg->variable.dimaso=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"DIMSHO");//gpdwg->variable.dimsho=read_data.bitcode_b;
	if (dat->version <= 14)
	{
		read_data=readwithlog(B,dat,"DIMSAV");//gpdwg->variable.dimsav=read_data.bitcode_b;
	}
	read_data=readwithlog(B,dat,"PLINEGEN");//gpdwg->variable.plinegen=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"ORTHOMODE");//gpdwg->variable.orthomode=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"REGENMODE");//gpdwg->variable.regenmode=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"FILLMODE");//gpdwg->variable.fillmode=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"QTEXTMODE");//gpdwg->variable.qtextmode=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"PSLTSCALE");//gpdwg->variable.psltscale=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"LIMCHECK");//gpdwg->variable.limcheck=read_data.bitcode_b;
	if (dat->version <= 14)
	{
		read_data=readwithlog(B,dat,"BLIPMODE");//gpdwg->variable.blipmode=read_data.bitcode_b;
	}
	if (dat->version >= 2004)
	{
		read_data=readwithlog(B,dat,"UNDOCUMENTED");//gpdwg->variable.undocumented=read_data.bitcode_b;
	}
	read_data=readwithlog(B,dat,"USRTIMER");//gpdwg->variable.usrtimer=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"SKPOLY");//gpdwg->variable.skpoly=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"ANGDIR");//gpdwg->variable.angdir=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"SPLFRAME");//gpdwg->variable.splframe=read_data.bitcode_b;
	if (dat->version <= 14)
	{
		read_data=readwithlog(B,dat,"ATTREQ");//gpdwg->variable.attreq=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"ATTDIA");//gpdwg->variable.attdia=read_data.bitcode_b;
	}
	read_data=readwithlog(B,dat,"MIRRTEXT");//gpdwg->variable.mirrtext=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"WORLDVIEW");//gpdwg->variable.worldview=read_data.bitcode_b;
	if (dat->version <= 14)
	{
		read_data=readwithlog(B,dat,"WIREFRAME");//gpdwg->variable.wireframe=read_data.bitcode_b;
	}
	read_data=readwithlog(B,dat,"TILEMODE");//gpdwg->variable.tilemode=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"PLIMCHECK");//gpdwg->variable.plimcheck=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"VISRETAIN");//gpdwg->variable.visretain=read_data.bitcode_b;
	if (dat->version <= 14)
	{
		read_data=readwithlog(B,dat,"DELOBJ");//gpdwg->variable.delobj=read_data.bitcode_b;
	}
	read_data=readwithlog(B,dat,"DISPSILH");//gpdwg->variable.dispsilh=read_data.bitcode_b;
	read_data=readwithlog(B,dat,"PELLIPSE");//gpdwg->variable.pellipse=read_data.bitcode_b;
	read_data=readwithlog(BS,dat,"PROXYGRAPHICS");//gpdwg->variable.proxygraphics=read_data.bitcode_bs;
	if (dat->version <= 14)
	{
		read_data=readwithlog(BS,dat,"DRAGMODE");//gpdwg->variable.dragmode=read_data.bitcode_bs;
	}
	read_data=readwithlog(BS,dat,"TREEDEPTH");//gpdwg->variable.treedepth=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"LUNITS");//gpdwg->variable.lunits=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"LUPREC");//gpdwg->variable.luprec=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"AUNITS");//gpdwg->variable.aunits=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"AUPREC");//gpdwg->variable.auprec=read_data.bitcode_bs;
	if (dat->version <= 14)
	{
		read_data=readwithlog(BS,dat,"OSMODE");//gpdwg->variable.osmode=read_data.bitcode_bs;
	}
	read_data=readwithlog(BS,dat,"ATTMODE");//gpdwg->variable.attmode=read_data.bitcode_bs;
	if (dat->version <= 14)
	{
		read_data=readwithlog(BS,dat,"COORDS");//gpdwg->variable.coords=read_data.bitcode_bs;
	}
	read_data=readwithlog(BS,dat,"PDMODE");//gpdwg->variable.pdmode=read_data.bitcode_bs;
	if (dat->version <= 14)
	{
		read_data=readwithlog(BS,dat,"PICKSTYLE");//gpdwg->variable.pickstyle=read_data.bitcode_bs;
	}
	if (dat->version >= 2004)
	{
		read_data=readwithlog(BL,dat,"UNKNOWN_12");//gpdwg->variable.unknown_12=read_data.bitcode_bl;
		read_data=readwithlog(BL,dat,"UNKNOWN_13");//gpdwg->variable.unknown_13=read_data.bitcode_bl;
		read_data=readwithlog(BL,dat,"UNKNOWN_14");//gpdwg->variable.unknown_14=read_data.bitcode_bl;
	}
	read_data=readwithlog(BS,dat,"USERI1");//gpdwg->variable.useri1=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"USERI2");//gpdwg->variable.useri2=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"USERI3");//gpdwg->variable.useri3=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"USERI4");//gpdwg->variable.useri4=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"USERI5");//gpdwg->variable.useri5=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SPLINESEGS");//gpdwg->variable.splinesegs=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SURFU");//gpdwg->variable.surfu=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SURFV");//gpdwg->variable.surfv=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SURFTYPE");//gpdwg->variable.surftype=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SURFTAB1");//gpdwg->variable.surftab1=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SURFTAB2");//gpdwg->variable.surftab2=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SPLINETYPE");//gpdwg->variable.splinetype=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SHADEDGE");//gpdwg->variable.shadedge=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"SHADEDIF");//gpdwg->variable.shadedif=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"UNITMODE");//gpdwg->variable.unitmode=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"MAXACTVP");//gpdwg->variable.maxactvp=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"ISOLINES");//gpdwg->variable.isolines=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"CMLJUST");//gpdwg->variable.cmljust=read_data.bitcode_bs;
	read_data=readwithlog(BS,dat,"TEXTQLTY");//gpdwg->variable.textqlty=read_data.bitcode_bs;
	read_data=readwithlog(BD,dat,"LTSCALE");//gpdwg->variable.ltscale=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"TEXTSIZE");//gpdwg->variable.textsize=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"TRACEWID");//gpdwg->variable.tracewid=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"SKETCHINC");//gpdwg->variable.sketchinc=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"FILLETRAD");//gpdwg->variable.filletrad=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"THICKNESS");//gpdwg->variable.thickness=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"ANGBASE");//gpdwg->variable.angbase=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"PDSIZE");//gpdwg->variable.pdsize=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"PLINEWID");//gpdwg->variable.plinewid=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"USERR1");//gpdwg->variable.userr1=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"USERR2");//gpdwg->variable.userr2=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"USERR3");//gpdwg->variable.userr3=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"USERR4");//gpdwg->variable.userr4=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"USERR5");//gpdwg->variable.userr5=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"CHAMFERA");//gpdwg->variable.chamfera=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"CHAMFERB");//gpdwg->variable.chamferb=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"CHAMFERC");//gpdwg->variable.chamferc=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"CHAMFERD");//gpdwg->variable.chamferd=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"FACETRES");//gpdwg->variable.facetres=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"CMLSCALE");//gpdwg->variable.cmlscale=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"CELTSCALE");//gpdwg->variable.celtscale=read_data.bitcode_bd;
	if (dat->version <= 2004)
	{
		read_data=readwithlog(TV,dat,"MENUNAME");//gpdwg->variable.menuname=read_data.bitcode_tv;
	}
	read_data=readwithlog(BL,dat,"TDCREATE_JD");//gpdwg->variable.tdcreate_jd=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"TDCREATE_MS");//gpdwg->variable.tdcreate_ms=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"TDUPDATE_JD");//gpdwg->variable.tdupdate_jd=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"TDUPDATE_MS");//gpdwg->variable.tdupdate_ms=read_data.bitcode_bl;
	if (dat->version >= 2004)
	{
		read_data=readwithlog(BL,dat,"UNKNOWN_15");//gpdwg->variable.unknown_15=read_data.bitcode_bl;
		read_data=readwithlog(BL,dat,"UNKNOWN_16");//gpdwg->variable.unknown_16=read_data.bitcode_bl;
		read_data=readwithlog(BL,dat,"UNKNOWN_17");//gpdwg->variable.unknown_17=read_data.bitcode_bl;
	}
	read_data=readwithlog(BL,dat,"TDINDWG_JD");//gpdwg->variable.tdindwg_jd=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"TDINDWG_MS");//gpdwg->variable.tdindwg_ms=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"TDUSRTIMER_JD");//gpdwg->variable.tdusrtimer_jd=read_data.bitcode_bl;
	read_data=readwithlog(BL,dat,"TDUSRTIMER_MS");//gpdwg->variable.tdusrtimer_ms=read_data.bitcode_bl;
	read_data=readwithlog(CMC,dat,"CECOLOR");//gpdwg->variable.cecolor=read_data.bitcode_cmc;
	read_data=readwithlog(H,dat,"HANDSEED");//gpdwg->variable.handseed=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"CLAYER");//gpdwg->variable.clayer=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"TEXTSTYLE");//gpdwg->variable.textstyle=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"CELTYPE");//gpdwg->variable.celtype=read_data.bitcode_h;
	if (dat->version >= 2007)
	{
		read_data=readwithlog(H,dat,"CMATERIAL");//gpdwg->variable.cmaterial=read_data.bitcode_h;
	}
	read_data=readwithlog(H,dat,"DIMSTYLE");//gpdwg->variable.dimstyle=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"CMLSTYLE");//gpdwg->variable.cmlstyle=read_data.bitcode_h;
	if (dat->version >= 2000)
	{
		read_data=readwithlog(BD,dat,"PSVPSCALE");//gpdwg->variable.psvpscale=read_data.bitcode_bd;
	}
	read_data=readwithlog(BD3,dat,"INSBASE_PS");//gpdwg->variable.insbase_ps=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"EXTMIN_PS");//gpdwg->variable.extmin_ps=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"EXTMAX_PS");//gpdwg->variable.extmax_ps=read_data.bitcode_bd3;
	read_data=readwithlog(RD2,dat,"LIMMIN_PS");//gpdwg->variable.limmin_ps=read_data.bitcode_rd2;
	read_data=readwithlog(RD2,dat,"LIMMAX_PS");//gpdwg->variable.limmax_ps=read_data.bitcode_rd2;
	read_data=readwithlog(BD,dat,"ELEVATION_PS");//gpdwg->variable.elevation_ps=read_data.bitcode_bd;
	read_data=readwithlog(BD3,dat,"UCSORG_PS");//gpdwg->variable.ucsorg_ps=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"UCSXDIR_PS");//gpdwg->variable.ucsxdir_ps=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"UCSYDIR_PS");//gpdwg->variable.ucsydir_ps=read_data.bitcode_bd3;
	read_data=readwithlog(H,dat,"UCSNAME_PS");//gpdwg->variable.ucsname_ps=read_data.bitcode_h;
	if (dat->version >= 2000)
	{
		read_data=readwithlog(H,dat,"PUCSORTHOREF");//gpdwg->variable.pucsorthoref=read_data.bitcode_h;
		read_data=readwithlog(BS,dat,"PUCSORTHOVIEW");//gpdwg->variable.pucsorthoview=read_data.bitcode_bs;
		read_data=readwithlog(H,dat,"PUCSBASE");//gpdwg->variable.pucsbase=read_data.bitcode_h;
		read_data=readwithlog(BD3,dat,"PUCSORGTOP");//gpdwg->variable.pucsorgtop=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"PUCSORGBOTTOM");//gpdwg->variable.pucsorgbottom=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"PUCSORGLEFT");//gpdwg->variable.pucsorgleft=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"PUCSORGRIGHT");//gpdwg->variable.pucsorgright=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"PUCSORGFRONT");//gpdwg->variable.pucsorgfront=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"PUCSORGBACK");//gpdwg->variable.pucsorgback=read_data.bitcode_bd3;
	}
	read_data=readwithlog(BD3,dat,"INSBASE_MS");//gpdwg->variable.insbase_ms=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"EXTMIN_MS");//gpdwg->variable.extmin_ms=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"EXTMAX_MS");//gpdwg->variable.extmax_ms=read_data.bitcode_bd3;
	read_data=readwithlog(RD2,dat,"LIMMIN_MS");//gpdwg->variable.limmin_ms=read_data.bitcode_rd2;
	read_data=readwithlog(RD2,dat,"LIMMAX_MS");//gpdwg->variable.limmax_ms=read_data.bitcode_rd2;
	read_data=readwithlog(BD,dat,"ELEVATION_MS");//gpdwg->variable.elevation_ms=read_data.bitcode_bd;
	read_data=readwithlog(BD3,dat,"UCSORG_MS");//gpdwg->variable.ucsorg_ms=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"UCSXDIR_MS");//gpdwg->variable.ucsxdir_ms=read_data.bitcode_bd3;
	read_data=readwithlog(BD3,dat,"UCSYDIR_MS");//gpdwg->variable.ucsydir_ms=read_data.bitcode_bd3;
	read_data=readwithlog(H,dat,"UCSNAME_MS");//gpdwg->variable.ucsname_ms=read_data.bitcode_h;
	if (dat->version >= 2000)
	{
		read_data=readwithlog(H,dat,"UCSORTHOREF");//gpdwg->variable.ucsorthoref=read_data.bitcode_h;
		read_data=readwithlog(BS,dat,"UCSORTHOVIEW");//gpdwg->variable.ucsorthoview=read_data.bitcode_bs;
		read_data=readwithlog(H,dat,"UCSBASE");//gpdwg->variable.ucsbase=read_data.bitcode_h;
		read_data=readwithlog(BD3,dat,"UCSORGTOP");//gpdwg->variable.ucsorgtop=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"UCSORGBOTTOM");//gpdwg->variable.ucsorgbottom=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"UCSORGLEFT");//gpdwg->variable.ucsorgleft=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"UCSORGRIGHT");//gpdwg->variable.ucsorgright=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"UCSORGFRONT");//gpdwg->variable.ucsorgfront=read_data.bitcode_bd3;
		read_data=readwithlog(BD3,dat,"UCSORGBACK");//gpdwg->variable.ucsorgback=read_data.bitcode_bd3;
		read_data=readwithlog(TV,dat,"DIMPOST");//gpdwg->variable.dimpost=read_data.bitcode_tv;
		read_data=readwithlog(TV,dat,"DIMAPOST");//gpdwg->variable.dimapost=read_data.bitcode_tv;
	}
	if (dat->version <= 14)
	{
		read_data=readwithlog(B,dat,"DIMTOL");//gpdwg->variable.dimtol=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMLIM");//gpdwg->variable.dimlim=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTIH");//gpdwg->variable.dimtih=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTOH");//gpdwg->variable.dimtoh=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSE1");//gpdwg->variable.dimse1=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSE2");//gpdwg->variable.dimse2=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMALT");//gpdwg->variable.dimalt=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTOFL");//gpdwg->variable.dimtofl=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSAH");//gpdwg->variable.dimsah=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTIX");//gpdwg->variable.dimtix=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSOXD");//gpdwg->variable.dimsoxd=read_data.bitcode_b;
		read_data=readwithlog(RC,dat,"DIMALTD");//gpdwg->variable.dimaltd=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMZIN");//gpdwg->variable.dimzin=read_data.bitcode_rc;
		read_data=readwithlog(B,dat,"DIMSD1");//gpdwg->variable.dimsd1=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSD2");//gpdwg->variable.dimsd2=read_data.bitcode_b;
		read_data=readwithlog(RC,dat,"DIMTOLJ");//gpdwg->variable.dimtolj=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMJUST");//gpdwg->variable.dimjust=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMFIT");//gpdwg->variable.dimfit=read_data.bitcode_rc;
		read_data=readwithlog(B,dat,"DIMUPT");//gpdwg->variable.dimupt=read_data.bitcode_b;
		read_data=readwithlog(RC,dat,"DIMTZIN");//gpdwg->variable.dimtzin=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMALTZ");//gpdwg->variable.dimaltz=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMALTTZ");//gpdwg->variable.dimalttz=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMTAD");//gpdwg->variable.dimtad=read_data.bitcode_rc;
		read_data=readwithlog(BS,dat,"DIMUNIT");//gpdwg->variable.dimunit=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMAUNIT");//gpdwg->variable.dimaunit=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMDEC");//gpdwg->variable.dimdec=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMTDEC");//gpdwg->variable.dimtdec=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMALTU");//gpdwg->variable.dimaltu=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMALTTD");//gpdwg->variable.dimalttd=read_data.bitcode_bs;
		read_data=readwithlog(H,dat,"DIMTXSTY");//gpdwg->variable.dimtxsty=read_data.bitcode_h;
	}
	read_data=readwithlog(BD,dat,"DIMSCALE");//gpdwg->variable.dimscale=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMASZ");//gpdwg->variable.dimasz=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMEXO");//gpdwg->variable.dimexo=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMDLI");//gpdwg->variable.dimdli=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMEXE");//gpdwg->variable.dimexe=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMRND");//gpdwg->variable.dimrnd=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMDLE");//gpdwg->variable.dimdle=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMTP");//gpdwg->variable.dimtp=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMTM");//gpdwg->variable.dimtm=read_data.bitcode_bd;
	if (dat->version >= 2007)
	{
		read_data=readwithlog(BD,dat,"DIMFXL");//gpdwg->variable.dimfxl=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"DIMJOGANG");//gpdwg->variable.dimjogang=read_data.bitcode_bd;
		read_data=readwithlog(BS,dat,"DIMTFILL");//gpdwg->variable.dimtfill=read_data.bitcode_bs;
		read_data=readwithlog(CMC,dat,"DIMTFILLCLR");//gpdwg->variable.dimtfillclr=read_data.bitcode_cmc;
	}
	if (dat->version >= 2000)
	{
		read_data=readwithlog(B,dat,"DIMTOL");//gpdwg->variable.dimtol=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMLIM");//gpdwg->variable.dimlim=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTIH");//gpdwg->variable.dimtih=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTOH");//gpdwg->variable.dimtoh=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSE1");//gpdwg->variable.dimse1=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSE2");//gpdwg->variable.dimse2=read_data.bitcode_b;
		read_data=readwithlog(BS,dat,"DIMTAD");//gpdwg->variable.dimtad=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMZIN");//gpdwg->variable.dimzin=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMAZIN");//gpdwg->variable.dimazin=read_data.bitcode_bs;
	}
	if (dat->version >= 2007)
	{
		read_data=readwithlog(BS,dat,"DIMARCSYM");//gpdwg->variable.dimarcsym=read_data.bitcode_bs;
	}
	read_data=readwithlog(BD,dat,"DIMTXT");//gpdwg->variable.dimtxt=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMCEN");//gpdwg->variable.dimcen=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMTSZ");//gpdwg->variable.dimtsz=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMALTF");//gpdwg->variable.dimaltf=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMLFAC");//gpdwg->variable.dimlfac=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMTVP");//gpdwg->variable.dimtvp=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMTFAC");//gpdwg->variable.dimtfac=read_data.bitcode_bd;
	read_data=readwithlog(BD,dat,"DIMGAP");//gpdwg->variable.dimgap=read_data.bitcode_bd;
	if (dat->version <= 14)
	{
		read_data=readwithlog(T,dat,"DIMPOST");//gpdwg->variable.dimpost=read_data.bitcode_t;
		read_data=readwithlog(T,dat,"DIMAPOST");//gpdwg->variable.dimapost=read_data.bitcode_t;
		read_data=readwithlog(T,dat,"DIMBLK");//gpdwg->variable.dimblk=read_data.bitcode_t;
		read_data=readwithlog(T,dat,"DIMBLK1");//gpdwg->variable.dimblk1=read_data.bitcode_t;
		read_data=readwithlog(T,dat,"DIMBLK2");//gpdwg->variable.dimblk2=read_data.bitcode_t;
	}
	if (dat->version >= 2000)
	{
		read_data=readwithlog(BD,dat,"DIMALTRND");//gpdwg->variable.dimaltrnd=read_data.bitcode_bd;
		read_data=readwithlog(B,dat,"DIMALT");//gpdwg->variable.dimalt=read_data.bitcode_b;
		read_data=readwithlog(BS,dat,"DIMALTD");//gpdwg->variable.dimaltd=read_data.bitcode_bs;
		read_data=readwithlog(B,dat,"DIMTOFL");//gpdwg->variable.dimtofl=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSAH");//gpdwg->variable.dimsah=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMTIX");//gpdwg->variable.dimtix=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSOXD");//gpdwg->variable.dimsoxd=read_data.bitcode_b;
	}
	read_data=readwithlog(CMC,dat,"DIMCLRD");//gpdwg->variable.dimclrd=read_data.bitcode_cmc;
	read_data=readwithlog(CMC,dat,"DIMCLRE");//gpdwg->variable.dimclre=read_data.bitcode_cmc;
	read_data=readwithlog(CMC,dat,"DIMCLRT");//gpdwg->variable.dimclrt=read_data.bitcode_cmc;
	if (dat->version >= 2000)
	{
		read_data=readwithlog(BS,dat,"DIMADEC");//gpdwg->variable.dimadec=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMDEC");//gpdwg->variable.dimdec=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMTDEC");//gpdwg->variable.dimtdec=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMALTU");//gpdwg->variable.dimaltu=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMALTTD");//gpdwg->variable.dimalttd=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMAUNIT");//gpdwg->variable.dimaunit=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMFRAC");//gpdwg->variable.dimfrac=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMLUNIT");//gpdwg->variable.dimlunit=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMDSEP");//gpdwg->variable.dimdsep=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMTMOVE");//gpdwg->variable.dimtmove=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMJUST");//gpdwg->variable.dimjust=read_data.bitcode_bs;
		read_data=readwithlog(B,dat,"DIMSD1");//gpdwg->variable.dimsd1=read_data.bitcode_b;
		read_data=readwithlog(B,dat,"DIMSD2");//gpdwg->variable.dimsd2=read_data.bitcode_b;
		read_data=readwithlog(BS,dat,"DIMTOLJ");//gpdwg->variable.dimtolj=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMTZIN");//gpdwg->variable.dimtzin=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMALTZ");//gpdwg->variable.dimaltz=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMALTTZ");//gpdwg->variable.dimalttz=read_data.bitcode_bs;
		read_data=readwithlog(B,dat,"DIMUPT");//gpdwg->variable.dimupt=read_data.bitcode_b;
		read_data=readwithlog(BS,dat,"DIMATFIT");//gpdwg->variable.dimatfit=read_data.bitcode_bs;
	}
	if (dat->version >= 2007)
	{
		read_data=readwithlog(B,dat,"DIMFXLON");//gpdwg->variable.dimfxlon=read_data.bitcode_b;
	}
	if (dat->version >= 2010)
	{
		read_data=readwithlog(B,dat,"DIMTXTDIRECTION");//gpdwg->variable.dimtxtdirection=read_data.bitcode_b;
		read_data=readwithlog(BD,dat,"DIMALTMZF");//gpdwg->variable.dimaltmzf=read_data.bitcode_bd;
		read_data=readwithlog(T,dat,"DIMALTMZS");//gpdwg->variable.dimaltmzs=read_data.bitcode_t;
		read_data=readwithlog(BD,dat,"DIMMZF");//gpdwg->variable.dimmzf=read_data.bitcode_bd;
		read_data=readwithlog(T,dat,"DIMMZS");//gpdwg->variable.dimmzs=read_data.bitcode_t;
	}
	if (dat->version >= 2000)
	{
		read_data=readwithlog(H,dat,"DIMTXSTY");//gpdwg->variable.dimtxsty=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DIMLDRBLK");//gpdwg->variable.dimldrblk=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DIMBLK");//gpdwg->variable.dimblk=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DIMBLK1");//gpdwg->variable.dimblk1=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DIMBLK2");//gpdwg->variable.dimblk2=read_data.bitcode_h;
	}
	if (dat->version >= 2007)
	{
		read_data=readwithlog(H,dat,"DIMLTYPE");//gpdwg->variable.dimltype=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DIMLTEX1");//gpdwg->variable.dimltex1=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DIMLTEX2");//gpdwg->variable.dimltex2=read_data.bitcode_h;
	}
	if (dat->version >= 2000)
	{
		read_data=readwithlog(BS,dat,"DIMLWD");//gpdwg->variable.dimlwd=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"DIMLWE");//gpdwg->variable.dimlwe=read_data.bitcode_bs;
	}
	read_data=readwithlog(H,dat,"BLOCK_CONTROL_OBJECT");//gpdwg->variable.block_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"LAYER_CONTROL_OBJECT");//gpdwg->variable.layer_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"STYLE_CONTROL_OBJECT");//gpdwg->variable.style_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"LINETYPE_CONTROL_OBJECT");//gpdwg->variable.linetype_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"VIEW_CONTROL_OBJECT");//gpdwg->variable.view_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"UCS_CONTROL_OBJECT");//gpdwg->variable.ucs_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"VPORT_CONTROL_OBJECT");//gpdwg->variable.vport_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"APPID_CONTROL_OBJECT");//gpdwg->variable.appid_control_object=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"DIMSTYLE_CONTROL_OBJECT");//gpdwg->variable.dimstyle_control_object=read_data.bitcode_h;
	if (dat->version <= 2000)
	{
		read_data=readwithlog(H,dat,"VIEWPORT_ENTITY_HEADER_CONTROL_OBJECT");//gpdwg->variable.viewport_entity_header_control_object=read_data.bitcode_h;
	}
	read_data=readwithlog(H,dat,"DICTIONARY_ACAD_GROUP");//gpdwg->variable.dictionary_acad_group=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"DICTIONARY_ACAD_MLINESTYLE");//gpdwg->variable.dictionary_acad_mlinestyle=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"DICTIONARY_NAMED_OBJECTS");//gpdwg->variable.dictionary_named_objects=read_data.bitcode_h;
	if (dat->version >= 2000)
	{
		read_data=readwithlog(BS,dat,"TSTACKALIGN");//gpdwg->variable.tstackalign=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"TSTACKSIZE");//gpdwg->variable.tstacksize=read_data.bitcode_bs;
		read_data=readwithlog(TV,dat,"HYPERLINKBASE");//gpdwg->variable.hyperlinkbase=read_data.bitcode_tv;
		read_data=readwithlog(TV,dat,"STYLESHEET");//gpdwg->variable.stylesheet=read_data.bitcode_tv;
		read_data=readwithlog(H,dat,"DICTIONARY_LAYOUTS");//gpdwg->variable.dictionary_layouts=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DICTIONARY_PLOTSETTINGS");//gpdwg->variable.dictionary_plotsettings=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DICTIONARY_PLOTSTYLES");//gpdwg->variable.dictionary_plotstyles=read_data.bitcode_h;
	}
	if (dat->version >= 2004)
	{
		read_data=readwithlog(H,dat,"DICTIONARY_MATERIALS");//gpdwg->variable.dictionary_materials=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DICTIONARY_COLORS");//gpdwg->variable.dictionary_colors=read_data.bitcode_h;
	}
	if (dat->version >= 2007)
	{
		read_data=readwithlog(H,dat,"DICTIONARY_VISUALSTYLE");//gpdwg->variable.dictionary_visualstyle=read_data.bitcode_h;
	}
	if (dat->version >= 2013)
	{
		read_data=readwithlog(H,dat,"UNKNOWN_18");//gpdwg->variable.unknown_18=read_data.bitcode_h;
	}
	if (dat->version >= 2000)
	{
		read_data=readwithlog(BL,dat,"FLAGS");//gpdwg->variable.flags=read_data.bitcode_bl;
		read_data=readwithlog(BS,dat,"INSUNITS");//gpdwg->variable.insunits=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"CEPSNTYPE");//gpdwg->variable.cepsntype=read_data.bitcode_bs;
		if (gpdwg->variables.cepsntype  == 3)
			read_data=readwithlog(H,dat,"CPSNID");//gpdwg->variable.cpsnid=read_data.bitcode_h;
		read_data=readwithlog(TV,dat,"FINGERPRINTGUID");//gpdwg->variable.fingerprintguid=read_data.bitcode_tv;
		read_data=readwithlog(TV,dat,"VERSIONGUID");//gpdwg->variable.versionguid=read_data.bitcode_tv;
	}
	if (dat->version >= 2004)
	{
		read_data=readwithlog(RC,dat,"SORTENTS");//gpdwg->variable.sortents=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"INDEXCTL");//gpdwg->variable.indexctl=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"HIDETEXT");//gpdwg->variable.hidetext=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"XCLIPFRAME");//gpdwg->variable.xclipframe=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DIMASSOC");//gpdwg->variable.dimassoc=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"HALOGAP");//gpdwg->variable.halogap=read_data.bitcode_rc;
		read_data=readwithlog(BS,dat,"OBSCUREDCOLOR");//gpdwg->variable.obscuredcolor=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"INTERSECTIONCOLOR");//gpdwg->variable.intersectioncolor=read_data.bitcode_bs;
		read_data=readwithlog(RC,dat,"OBSCUREDLTYPE");//gpdwg->variable.obscuredltype=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"INTERSECTIONDISPLAY");//gpdwg->variable.intersectiondisplay=read_data.bitcode_rc;
		read_data=readwithlog(TV,dat,"PROJECTNAME");//gpdwg->variable.projectname=read_data.bitcode_tv;
	}
	read_data=readwithlog(H,dat,"BLOCK_RECORD_PS");//gpdwg->variable.block_record_ps=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"BLOCK_RECORD_MS");//gpdwg->variable.block_record_ms=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"LTYPE_BYLAYER");//gpdwg->variable.ltype_bylayer=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"LTYPE_BYBLOCK");//gpdwg->variable.ltype_byblock=read_data.bitcode_h;
	read_data=readwithlog(H,dat,"LTYPE_CONTINUOUS");//gpdwg->variable.ltype_continuous=read_data.bitcode_h;
	if (dat->version >= 2007)
	{
		read_data=readwithlog(B,dat,"CAMERADISPLAY");//gpdwg->variable.cameradisplay=read_data.bitcode_b;
		read_data=readwithlog(BL,dat,"UNKNOWN_19");//gpdwg->variable.unknown_19=read_data.bitcode_bl;
		read_data=readwithlog(BL,dat,"UNKNOWN_20");//gpdwg->variable.unknown_20=read_data.bitcode_bl;
		read_data=readwithlog(BD,dat,"UNKNOWN_21");//gpdwg->variable.unknown_21=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"STEPSPERSEC");//gpdwg->variable.stepspersec=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"STEPSIZE");//gpdwg->variable.stepsize=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"DWFPREC_3D");//gpdwg->variable.dwfprec_3d=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"LENSLENGTH");//gpdwg->variable.lenslength=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"CAMERAHEIGHT");//gpdwg->variable.cameraheight=read_data.bitcode_bd;
		read_data=readwithlog(RC,dat,"SOLIDHIST");//gpdwg->variable.solidhist=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"SHOWHIST");//gpdwg->variable.showhist=read_data.bitcode_rc;
		read_data=readwithlog(BD,dat,"PSOLWIDTH");//gpdwg->variable.psolwidth=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"PSOLHEIGHT");//gpdwg->variable.psolheight=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"LOFTANG1");//gpdwg->variable.loftang1=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"LOFTANG2");//gpdwg->variable.loftang2=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"LOFTMAG1");//gpdwg->variable.loftmag1=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"LOFTMAG2");//gpdwg->variable.loftmag2=read_data.bitcode_bd;
		read_data=readwithlog(BS,dat,"LOFTPARAM");//gpdwg->variable.loftparam=read_data.bitcode_bs;
		read_data=readwithlog(RC,dat,"LOFTNORMALS");//gpdwg->variable.loftnormals=read_data.bitcode_rc;
		read_data=readwithlog(BD,dat,"LATITUDE");//gpdwg->variable.latitude=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"LONGITUDE");//gpdwg->variable.longitude=read_data.bitcode_bd;
		read_data=readwithlog(BD,dat,"NORTHDIRECTION");//gpdwg->variable.northdirection=read_data.bitcode_bd;
		read_data=readwithlog(BL,dat,"TIMEZONE");//gpdwg->variable.timezone=read_data.bitcode_bl;
		read_data=readwithlog(RC,dat,"LIGHTGLYPHDISPLAY");//gpdwg->variable.lightglyphdisplay=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"TILEMODELIGHTSYNCH");//gpdwg->variable.tilemodelightsynch=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DWFFRAME");//gpdwg->variable.dwfframe=read_data.bitcode_rc;
		read_data=readwithlog(RC,dat,"DGNFRAME");//gpdwg->variable.dgnframe=read_data.bitcode_rc;
		read_data=readwithlog(B,dat,"UNKNOWN_22");//gpdwg->variable.unknown_22=read_data.bitcode_b;
		read_data=readwithlog(CMC,dat,"INTERFERECOLOR");//gpdwg->variable.interferecolor=read_data.bitcode_cmc;
		read_data=readwithlog(H,dat,"INTERFEREOBJVS");//gpdwg->variable.interfereobjvs=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"INTERFEREVPVS");//gpdwg->variable.interferevpvs=read_data.bitcode_h;
		read_data=readwithlog(H,dat,"DRAGVS");//gpdwg->variable.dragvs=read_data.bitcode_h;
		read_data=readwithlog(RC,dat,"CSHADOW");//gpdwg->variable.cshadow=read_data.bitcode_rc;
		read_data=readwithlog(BD,dat,"UNKNOWN_23");//gpdwg->variable.unknown_23=read_data.bitcode_bd;
	}
	if (dat->version >= 14)
	{
		read_data=readwithlog(BS,dat,"UNKNOWN_24");//gpdwg->variable.unknown_24=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"UNKNOWN_25");//gpdwg->variable.unknown_25=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"UNKNOWN_26");//gpdwg->variable.unknown_26=read_data.bitcode_bs;
		read_data=readwithlog(BS,dat,"UNKNOWN_27");//gpdwg->variable.unknown_27=read_data.bitcode_bs;
	}
	logger(LOG_DEBUG,dat->byte,dat->bit,"Generating Flag variables.");
	BITCODE_BL FlagsValue=gpdwg->variables.flags;
	gpdwg->variables.celweight= FlagsValue & 0X001F;
	gpdwg->variables.endcaps=( FlagsValue & 0X0060) >> 5;
	gpdwg->variables.joinstyle=( FlagsValue & 0X0180) >> 7;
	gpdwg->variables.lwdisplay= !(FlagsValue & 0X0200);
	gpdwg->variables.xedit= !(FlagsValue & 0X0400);
	gpdwg->variables.extnames=(FlagsValue & 0X0800) >> 11;
	gpdwg->variables.pstylemode=(FlagsValue & 0X2000) >> 13;
	gpdwg->variables.olestartup=(FlagsValue & 0X4000) >> 14;
}