#############################################################################
#  gpdwg - free python package to read .dwg files.                          #
#                                                                           #
#  Copyright (C) 2018 Guruprasad Rane <raneguruprasad@gmail.com>            #
#                                                                           #
#  This library is free software, licensed under the terms of the GNU       #
#  General Public License version 2. You should have received a copy of     #
#  the GNU General Public License along with this program.                  #
#                                                                           #
#############################################################################
import logging, mmap, os.path, bit

logger = logging.getLogger("gpdwg_logger")
logger.setLevel(0)
handler = logging.FileHandler('gpdwg-python.log')
handler.setLevel(0)
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

Versions={'AC1012':13, 'AC1014':14, 'AC1015':2000, 'AC1018':2004, 'AC1021':2007, 'AC1024':2010, 'AC1027':2013}

class dwg_extended_object(object):
	"""Class for Extended Object"""
	__slots__=['handle','xdatalength','xdata']
	def __setattr__(self,name,value):
		A_Types={'handle':bit.handle,'xdatalength':float,'xdata':dict}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\nExtended Object\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput

class dwg_non_entity(dwg_extended_object):
	"""Class for Non Entity"""
	__slots__=['num_reactors']
	def __setattr__(self,name,value):
		A_Types={'num_reactors':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\nNon Entity\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput

class dwg_entity_handles(dwg_extended_object):
	"""Class for Entity Handles"""
	__slots__=['subentry','reactors','xdicobjhandle','prvEntity','nxtEntity','layer','LineType','PlotStyle']
	def __setattr__(self,name,value):
		A_Types={'subentry':bit.handle,'reactors':dict,'xdicobjhandle':bit.handle,'prvEntity':bit.handle,'nxtEntity':bit.handle,'layer':bit.handle,'LineType':bit.handle,'PlotStyle':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\nEntity Handles\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput
		
class dwg_entity(dwg_entity_handles):
	"""Class for Entity"""
	__slots__=['Picture_Exist','Picture_Size','Entmode','NumReactors','NoLinks','EntColor','LineTypeScale','LineTypeFlag','PlotStyleFlag','Invisible','LineWeight']
	def __setattr__(self,name,value):
		A_Types={'Picture_Exist':bool, 'Picture_Size':int, 'Entmode':float, 'NumReactors':int, 'NoLinks':bool,'EntColor':bit.color, 'LineTypeScale':float,'LineTypeFlag':float,'PlotStyleFlag':float,'Invisible':float,'LineWeight':int}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\nEntity\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput

class dwg_dimension(dwg_entity):
	"""Class for Entity"""
	__slots__=['Extrusion','Text_Midpt','Elevation','Flags','User_Text','Text_Rot','Horiz_Dir','Ins_Scale_X','Ins_Scale_Y','Ins_Scale_Z','Ins_Rot','Attachment_Point','Linespacing_Style','Linespacing_Factor','Actual_Measurement','Pt12']
	def __setattr__(self,name,value):
		A_Types={'Extrusion':bit.point3D,'Text_Midpt':bit.point2D,'Elevation':float,'Flags':int,'User_Text':str,'Text_Rot':float,'Horiz_Dir':float,'Ins_Scale_X':float,'Ins_Scale_Y':float,'Ins_Scale_Z':float,'Ins_Rot':float,'Attachment_Point':float,'Linespacing_Style':float,'Linespacing_Factor':float,'Actual_Measurement':float,'Pt12':bit.point2D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\nDimension\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput

class hatch_path(object):
	"""Class fo hatch path"""
	__slots__=['path_flag','num_path_segments','path_segments','bulgespresent','closed','path_points','path_points_bulge','num_boundaryobj_handles']
	def __setattr__(self,name,value):
		A_Types={'path_flag':float,'num_path_segments':float,'path_segments':list,'bulgespresent':bool,'closed':bool,'path_points':list,'path_points_bulge':list,'num_boundaryobj_handles':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\n\t\t\tHatch path\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n\t\t\t'
		return TempOutput	

class hatch_path_line(object):
	"""Class fo hatch path line"""
	__slots__=['first_endpoint','second_endpoint']
	def __setattr__(self,name,value):
		A_Types={'first_endpoint':bit.point2D,'second_endpoint':bit.point2D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\n\t\t\tHatch path Line\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n\t\t\t'
		return TempOutput

class hatch_path_arc(object):
	"""Class fo hatch path arc"""
	__slots__=['center','radius','start_angle','end_angle','isccw']
	def __setattr__(self,name,value):
		A_Types={'center':bit.point2D,'radius':float,'start_angle':float,'end_angle':float,'isccw':bool}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\n\t\t\tHatch path Line\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n\t\t\t'
		return TempOutput

class hatch_path_elarc(object):
	"""Class fo hatch path elipse arc"""
	__slots__=['center','endpoint','maj_min_ratio','start_angle','end_angle','isccw']
	def __setattr__(self,name,value):
		A_Types={'center':bit.point2D,'endpoint':bit.point2D,'maj_min_ratio':float,'start_angle':float,'end_angle':float,'isccw':bool}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\n\t\t\tHatch path Line\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n\t\t\t'
		return TempOutput

class hatch_path_spline(object):
	"""Class fo hatch path spline"""
	__slots__=['degree','rational','periodic','knots','clt_points','clt_points_weight']
	def __setattr__(self,name,value):
		A_Types={'degree':float,'rational':bool,'periodic':bool,'knots':list,'clt_points':list,'clt_points_weight':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\n\t\t\tHatch path spline\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n\t\t\t'
		return TempOutput

class hatch_defination_lines(object):
	"""Class fo hatch path line"""
	__slots__=['angle','point','offset','dash_lengths']
	def __setattr__(self,name,value):
		A_Types={'angle':float,'point':bit.point2D,'offset':bit.point2D,'dash_lengths':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput='\n\t\t\tHatch defination Line\n'
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n\t\t\t'
		return TempOutput

class dwg_hatch(dwg_entity):
	"""Class for dwg_hatch"""
	__slots__=['gradient_fill_flag','reserved','gradient_angle','gradient_shift','single_color_grad','gradient_tint','num_gradient_colors','unknown_double','unknown_short','rgb_color','ignored_color_byte','gradient_name','z_coord','extrusion','name','solid_fill','associative','numpaths','hatch_paths','style','patterntype','angle','scale_or_spacing','double_hatch','num_defination_lines','pixelsize','seed_point','boundaryobj_handles','paths','defination_lines']
	def __setattr__(self,name,value):
		A_Types={'angle':float,'associative':int,'double_hatch':int,'extrusion':bit.point3D,'gradient_angle':float,'gradient_fill_flag':float,'gradient_name':int,'gradient_shift':float,'gradient_tint':float,'hatch_paths':list,'ignored_color_byte':list,'name':str,'num_defination_lines':float,'num_gradient_colors':float,'numpaths':float,'patterntype':float,'reserved':float,'rgb_color':list,'scale_or_spacing':float,'single_color_grad':float,'solid_fill':int,'style':float,'unknown_double':list,'unknown_short':list,'z_coord':float,'pixelsize':list,'seed_point':list,'boundaryobj_handles':list,'paths':list,'defination_lines':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class gpdwgVariables(object):
	"""Class for Variables"""
	__slots__=['CELWEIGHT','ENDCAPS','JOINSTYLE','LWDISPLAY','XEDIT','EXTNAMES','PSTYLEMODE','OLESTARTUP','SIZE_IN_BITS','REQUIREDVERSIONS','UNKNOWN_01','UNKNOWN_02','UNKNOWN_03','UNKNOWN_04','UNKNOWN_05','UNKNOWN_06','UNKNOWN_07','UNKNOWN_08','UNKNOWN_09','UNKNOWN_10','UNKNOWN_11','CURRENT_VIEWPORT_HANDLE','DIMASO','DIMSHO','DIMSAV','PLINEGEN','ORTHOMODE','REGENMODE','FILLMODE','QTEXTMODE','PSLTSCALE','LIMCHECK','BLIPMODE','UNDOCUMENTED','USRTIMER','SKPOLY','ANGDIR','SPLFRAME','ATTREQ','ATTDIA','MIRRTEXT','WORLDVIEW','WIREFRAME','TILEMODE','PLIMCHECK','VISRETAIN','DELOBJ','DISPSILH','PELLIPSE','PROXYGRAPHICS','DRAGMODE','TREEDEPTH','LUNITS','LUPREC','AUNITS','AUPREC','OSMODE','ATTMODE','COORDS','PDMODE','PICKSTYLE','UNKNOWN_12','UNKNOWN_13','UNKNOWN_14','USERI1','USERI2','USERI3','USERI4','USERI5','SPLINESEGS','SURFU','SURFV','SURFTYPE','SURFTAB1','SURFTAB2','SPLINETYPE','SHADEDGE','SHADEDIF','UNITMODE','MAXACTVP','ISOLINES','CMLJUST','TEXTQLTY','LTSCALE','TEXTSIZE','TRACEWID','SKETCHINC','FILLETRAD','THICKNESS','ANGBASE','PDSIZE','PLINEWID','USERR1','USERR2','USERR3','USERR4','USERR5','CHAMFERA','CHAMFERB','CHAMFERC','CHAMFERD','FACETRES','CMLSCALE','CELTSCALE','MENUNAME','TDCREATE_JD','TDCREATE_MS','TDUPDATE_JD','TDUPDATE_MS','UNKNOWN_15','UNKNOWN_16','UNKNOWN_17','TDINDWG_JD','TDINDWG_MS','TDUSRTIMER_JD','TDUSRTIMER_MS','CECOLOR','HANDSEED','CLAYER','TEXTSTYLE','CELTYPE','CMATERIAL','DIMSTYLE','CMLSTYLE','PSVPSCALE','INSBASE_PS','EXTMIN_PS','EXTMAX_PS','LIMMIN_PS','LIMMAX_PS','ELEVATION_PS','UCSORG_PS','UCSXDIR_PS','UCSYDIR_PS','UCSNAME_PS','PUCSORTHOREF','PUCSORTHOVIEW','PUCSBASE','PUCSORGTOP','PUCSORGBOTTOM','PUCSORGLEFT','PUCSORGRIGHT','PUCSORGFRONT','PUCSORGBACK','INSBASE_MS','EXTMIN_MS','EXTMAX_MS','LIMMIN_MS','LIMMAX_MS','ELEVATION_MS','UCSORG_MS','UCSXDIR_MS','UCSYDIR_MS','UCSNAME_MS','UCSORTHOREF','UCSORTHOVIEW','UCSBASE','UCSORGTOP','UCSORGBOTTOM','UCSORGLEFT','UCSORGRIGHT','UCSORGFRONT','UCSORGBACK','DIMPOST','DIMAPOST','DIMTOL','DIMLIM','DIMTIH','DIMTOH','DIMSE1','DIMSE2','DIMALT','DIMTOFL','DIMSAH','DIMTIX','DIMSOXD','DIMALTD','DIMZIN','DIMSD1','DIMSD2','DIMTOLJ','DIMJUST','DIMFIT','DIMUPT','DIMTZIN','DIMALTZ','DIMALTTZ','DIMTAD','DIMUNIT','DIMAUNIT','DIMDEC','DIMTDEC','DIMALTU','DIMALTTD','DIMTXSTY','DIMSCALE','DIMASZ','DIMEXO','DIMDLI','DIMEXE','DIMRND','DIMDLE','DIMTP','DIMTM','DIMFXL','DIMJOGANG','DIMTFILL','DIMTFILLCLR','DIMAZIN','DIMARCSYM','DIMTXT','DIMCEN','DIMTSZ','DIMALTF','DIMLFAC','DIMTVP','DIMTFAC','DIMGAP','DIMBLK','DIMBLK1','DIMBLK2','DIMALTRND','DIMCLRD','DIMCLRE','DIMCLRT','DIMADEC','DIMFRAC','DIMLUNIT','DIMDSEP','DIMTMOVE','DIMATFIT','DIMFXLON','DIMTXTDIRECTION','DIMALTMZF','DIMALTMZS','DIMMZF','DIMMZS','DIMLDRBLK','DIMLTYPE','DIMLTEX1','DIMLTEX2','DIMLWD','DIMLWE','BLOCK_CONTROL_OBJECT','LAYER_CONTROL_OBJECT','STYLE_CONTROL_OBJECT','LINETYPE_CONTROL_OBJECT','VIEW_CONTROL_OBJECT','UCS_CONTROL_OBJECT','VPORT_CONTROL_OBJECT','APPID_CONTROL_OBJECT','DIMSTYLE_CONTROL_OBJECT','VIEWPORT_ENTITY_HEADER_CONTROL_OBJECT','DICTIONARY_ACAD_GROUP','DICTIONARY_ACAD_MLINESTYLE','DICTIONARY_NAMED_OBJECTS','TSTACKALIGN','TSTACKSIZE','HYPERLINKBASE','STYLESHEET','DICTIONARY_LAYOUTS','DICTIONARY_PLOTSETTINGS','DICTIONARY_PLOTSTYLES','DICTIONARY_MATERIALS','DICTIONARY_COLORS','DICTIONARY_VISUALSTYLE','UNKNOWN_18','FLAGS','INSUNITS','CEPSNTYPE','CPSNID','FINGERPRINTGUID','VERSIONGUID','SORTENTS','INDEXCTL','HIDETEXT','XCLIPFRAME','DIMASSOC','HALOGAP','OBSCUREDCOLOR','INTERSECTIONCOLOR','OBSCUREDLTYPE','INTERSECTIONDISPLAY','PROJECTNAME','BLOCK_RECORD_PS','BLOCK_RECORD_MS','LTYPE_BYLAYER','LTYPE_BYBLOCK','LTYPE_CONTINUOUS','CAMERADISPLAY','UNKNOWN_19','UNKNOWN_20','UNKNOWN_21','STEPSPERSEC','STEPSIZE','DWFPREC_3D','LENSLENGTH','CAMERAHEIGHT','SOLIDHIST','SHOWHIST','PSOLWIDTH','PSOLHEIGHT','LOFTANG1','LOFTANG2','LOFTMAG1','LOFTMAG2','LOFTPARAM','LOFTNORMALS','LATITUDE','LONGITUDE','NORTHDIRECTION','TIMEZONE','LIGHTGLYPHDISPLAY','TILEMODELIGHTSYNCH','DWFFRAME','DGNFRAME','UNKNOWN_22','INTERFERECOLOR','INTERFEREOBJVS','INTERFEREVPVS','DRAGVS','CSHADOW','UNKNOWN_23','UNKNOWN_24','UNKNOWN_25','UNKNOWN_26','UNKNOWN_27']
	def __setattr__(self,name,value):
		A_Types={'ANGBASE':float,'ANGDIR':int,'APPID_CONTROL_OBJECT':bit.handle,'ATTDIA':int,'ATTMODE':float,'ATTREQ':int,'AUNITS':float,'AUPREC':float,'BLIPMODE':int,'BLOCK_CONTROL_OBJECT':bit.handle,'BLOCK_RECORD_MS':bit.handle,'BLOCK_RECORD_PS':bit.handle,'CAMERADISPLAY':int,'CAMERAHEIGHT':float,'CECOLOR':bit.color,'CELTSCALE':float,'CELTYPE':bit.handle,'CELWEIGHT':int,'CEPSNTYPE':float,'CHAMFERA':float,'CHAMFERB':float,'CHAMFERC':float,'CHAMFERD':float,'CLAYER':bit.handle,'CMATERIAL':bit.handle,'CMLJUST':float,'CMLSCALE':float,'CMLSTYLE':bit.handle,'COORDS':float,'CPSNID':bit.handle,'CSHADOW':int,'CURRENT_VIEWPORT_HANDLE':bit.handle,'DELOBJ':int,'DGNFRAME':int,'DICTIONARY_ACAD_GROUP':bit.handle,'DICTIONARY_ACAD_MLINESTYLE':bit.handle,'DICTIONARY_COLORS':bit.handle,'DICTIONARY_LAYOUTS':bit.handle,'DICTIONARY_MATERIALS':bit.handle,'DICTIONARY_NAMED_OBJECTS':bit.handle,'DICTIONARY_PLOTSETTINGS':bit.handle,'DICTIONARY_PLOTSTYLES':bit.handle,'DICTIONARY_VISUALSTYLE':bit.handle,'DIMADEC':float,'DIMALT':int,'DIMALTD':float,'DIMALTF':float,'DIMALTMZF':float,'DIMALTMZS':str,'DIMALTRND':float,'DIMALTTD':float,'DIMALTTZ':float,'DIMALTU':float,'DIMALTZ':float,'DIMAPOST':str,'DIMARCSYM':float,'DIMASO':int,'DIMASSOC':int,'DIMASZ':float,'DIMATFIT':float,'DIMAUNIT':float,'DIMAZIN':float,'DIMBLK':bit.handle,'DIMBLK1':bit.handle,'DIMBLK2':bit.handle,'DIMCEN':float,'DIMCLRD':bit.color,'DIMCLRE':bit.color,'DIMCLRT':bit.color,'DIMDEC':float,'DIMDLE':float,'DIMDLI':float,'DIMDSEP':float,'DIMEXE':float,'DIMEXO':float,'DIMFIT':int,'DIMFRAC':float,'DIMFXL':float,'DIMFXLON':int,'DIMGAP':float,'DIMJOGANG':float,'DIMJUST':float,'DIMLDRBLK':bit.handle,'DIMLFAC':float,'DIMLIM':int,'DIMLTEX1':bit.handle,'DIMLTEX2':bit.handle,'DIMLTYPE':bit.handle,'DIMLUNIT':float,'DIMLWD':float,'DIMLWE':float,'DIMMZF':float,'DIMMZS':str,'DIMPOST':str,'DIMRND':float,'DIMSAH':int,'DIMSAV':int,'DIMSCALE':float,'DIMSD1':int,'DIMSD2':int,'DIMSE1':int,'DIMSE2':int,'DIMSHO':int,'DIMSOXD':int,'DIMSTYLE':bit.handle,'DIMSTYLE_CONTROL_OBJECT':bit.handle,'DIMTAD':float,'DIMTDEC':float,'DIMTFAC':float,'DIMTFILL':float,'DIMTFILLCLR':bit.color,'DIMTIH':int,'DIMTIX':int,'DIMTM':float,'DIMTMOVE':float,'DIMTOFL':int,'DIMTOH':int,'DIMTOL':int,'DIMTOLJ':float,'DIMTP':float,'DIMTSZ':float,'DIMTVP':float,'DIMTXSTY':bit.handle,'DIMTXT':float,'DIMTXTDIRECTION':int,'DIMTZIN':float,'DIMUNIT':float,'DIMUPT':int,'DIMZIN':float,'DISPSILH':int,'DRAGMODE':float,'DRAGVS':bit.handle,'DWFFRAME':int,'DWFPREC_3D':float,'ELEVATION_MS':float,'ELEVATION_PS':float,'ENDCAPS':int,'EXTMAX_MS':bit.point3D,'EXTMAX_PS':bit.point3D,'EXTMIN_MS':bit.point3D,'EXTMIN_PS':bit.point3D,'EXTNAMES':int,'FACETRES':float,'FILLETRAD':float,'FILLMODE':int,'FINGERPRINTGUID':str,'FLAGS':float,'HALOGAP':int,'HANDSEED':bit.handle,'HIDETEXT':int,'HYPERLINKBASE':str,'INDEXCTL':int,'INSBASE_MS':bit.point3D,'INSBASE_PS':bit.point3D,'INSUNITS':float,'INTERFERECOLOR':bit.color,'INTERFEREOBJVS':bit.handle,'INTERFEREVPVS':bit.handle,'INTERSECTIONCOLOR':float,'INTERSECTIONDISPLAY':int,'ISOLINES':float,'JOINSTYLE':int,'LATITUDE':float,'LAYER_CONTROL_OBJECT':bit.handle,'LENSLENGTH':float,'LIGHTGLYPHDISPLAY':int,'LIMCHECK':int,'LIMMAX_MS':bit.point2D,'LIMMAX_PS':bit.point2D,'LIMMIN_MS':bit.point2D,'LIMMIN_PS':bit.point2D,'LINETYPE_CONTROL_OBJECT':bit.handle,'LOFTANG1':float,'LOFTANG2':float,'LOFTMAG1':float,'LOFTMAG2':float,'LOFTNORMALS':int,'LOFTPARAM':float,'LONGITUDE':float,'LTSCALE':float,'LTYPE_BYBLOCK':bit.handle,'LTYPE_BYLAYER':bit.handle,'LTYPE_CONTINUOUS':bit.handle,'LUNITS':float,'LUPREC':float,'LWDISPLAY':int,'MAXACTVP':float,'MENUNAME':str,'MIRRTEXT':int,'NORTHDIRECTION':float,'OBSCUREDCOLOR':float,'OBSCUREDLTYPE':int,'OLESTARTUP':int,'ORTHOMODE':int,'OSMODE':float,'PDMODE':float,'PDSIZE':float,'PELLIPSE':int,'PICKSTYLE':float,'PLIMCHECK':int,'PLINEGEN':int,'PLINEWID':float,'PROJECTNAME':str,'PROXYGRAPHICS':float,'PSLTSCALE':int,'PSOLHEIGHT':float,'PSOLWIDTH':float,'PSTYLEMODE':int,'PSVPSCALE':float,'PUCSBASE':bit.handle,'PUCSORGBACK':bit.point3D,'PUCSORGBOTTOM':bit.point3D,'PUCSORGFRONT':bit.point3D,'PUCSORGLEFT':bit.point3D,'PUCSORGRIGHT':bit.point3D,'PUCSORGTOP':bit.point3D,'PUCSORTHOREF':bit.handle,'PUCSORTHOVIEW':float,'QTEXTMODE':int,'REGENMODE':int,'REQUIREDVERSIONS':int,'SHADEDGE':float,'SHADEDIF':float,'SHOWHIST':int,'SIZE_IN_BITS':int,'SKETCHINC':float,'SKPOLY':int,'SOLIDHIST':int,'SORTENTS':int,'SPLFRAME':int,'SPLINESEGS':float,'SPLINETYPE':float,'STEPSIZE':float,'STEPSPERSEC':float,'STYLESHEET':str,'STYLE_CONTROL_OBJECT':bit.handle,'SURFTAB1':float,'SURFTAB2':float,'SURFTYPE':float,'SURFU':float,'SURFV':float,'TDCREATE_JD':float,'TDCREATE_MS':float,'TDINDWG_JD':float,'TDINDWG_MS':float,'TDUPDATE_JD':float,'TDUPDATE_MS':float,'TDUSRTIMER_JD':float,'TDUSRTIMER_MS':float,'TEXTQLTY':float,'TEXTSIZE':float,'TEXTSTYLE':bit.handle,'THICKNESS':float,'TILEMODE':int,'TILEMODELIGHTSYNCH':int,'TIMEZONE':float,'TRACEWID':float,'TREEDEPTH':float,'TSTACKALIGN':float,'TSTACKSIZE':float,'UCSBASE':bit.handle,'UCSNAME_MS':bit.handle,'UCSNAME_PS':bit.handle,'UCSORGBACK':bit.point3D,'UCSORGBOTTOM':bit.point3D,'UCSORGFRONT':bit.point3D,'UCSORGLEFT':bit.point3D,'UCSORGRIGHT':bit.point3D,'UCSORGTOP':bit.point3D,'UCSORG_MS':bit.point3D,'UCSORG_PS':bit.point3D,'UCSORTHOREF':bit.handle,'UCSORTHOVIEW':float,'UCSXDIR_MS':bit.point3D,'UCSXDIR_PS':bit.point3D,'UCSYDIR_MS':bit.point3D,'UCSYDIR_PS':bit.point3D,'UCS_CONTROL_OBJECT':bit.handle,'UNDOCUMENTED':int,'UNITMODE':float,'UNKNOWN_01':float,'UNKNOWN_02':float,'UNKNOWN_03':float,'UNKNOWN_04':float,'UNKNOWN_05':str,'UNKNOWN_06':str,'UNKNOWN_07':str,'UNKNOWN_08':str,'UNKNOWN_09':float,'UNKNOWN_10':float,'UNKNOWN_11':float,'UNKNOWN_12':float,'UNKNOWN_13':float,'UNKNOWN_14':float,'UNKNOWN_15':float,'UNKNOWN_16':float,'UNKNOWN_17':float,'UNKNOWN_18':bit.handle,'UNKNOWN_19':float,'UNKNOWN_20':float,'UNKNOWN_21':float,'UNKNOWN_22':int,'UNKNOWN_23':float,'UNKNOWN_24':float,'UNKNOWN_25':float,'UNKNOWN_26':float,'UNKNOWN_27':float,'USERI1':float,'USERI2':float,'USERI3':float,'USERI4':float,'USERI5':float,'USERR1':float,'USERR2':float,'USERR3':float,'USERR4':float,'USERR5':float,'USRTIMER':int,'VERSIONGUID':str,'VIEWPORT_ENTITY_HEADER_CONTROL_OBJECT':bit.handle,'VIEW_CONTROL_OBJECT':bit.handle,'VISRETAIN':int,'VPORT_CONTROL_OBJECT':bit.handle,'WIREFRAME':int,'WORLDVIEW':int,'XCLIPFRAME':int,'XEDIT':int}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		print('Variables')
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				print('\t'+str(i)+' : '+repr(getattr(self,i)))
		return ""



class dwg_text(dwg_entity):
	"""Class for dwg_text"""
	__slots__=['data_flags','elevation','insertion_point','alignment_point','extrusion','thickness','oblique_angle','rotation_angle','height','width_factor','text_value','generation','horizontal_align','vertical_align','style']
	def __setattr__(self,name,value):
		A_Types={'alignment_point':bit.point2D,'data_flags':int,'elevation':float,'extrusion':bit.point3D,'generation':float,'height':float,'horizontal_align':float,'insertion_point':bit.point2D,'oblique_angle':float,'rotation_angle':float,'style':bit.handle,'text_value':str,'thickness':float,'vertical_align':float,'width_factor':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_attrib(dwg_entity):
	"""Class for dwg_attrib"""
	__slots__=['data_flags','elevation','insertion_point','alignment_point','extrusion','thickness','oblique_angle','rotation_angle','height','width_factor','text_value','generation','horizontal_align','vertical_align','version','tag','field_length','flags','style']
	def __setattr__(self,name,value):
		A_Types={'alignment_point':bit.point2D,'data_flags':int,'elevation':float,'extrusion':bit.point3D,'field_length':float,'flags':int,'generation':float,'height':float,'horizontal_align':float,'insertion_point':bit.point2D,'oblique_angle':float,'rotation_angle':float,'style':bit.handle,'tag':str,'text_value':str,'thickness':float,'version':int,'vertical_align':float,'width_factor':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_attdef(dwg_entity):
	"""Class for dwg_attdef"""
	__slots__=['data_flags','elevation','insertion_point','alignment_point','extrusion','thickness','oblique_angle','rotation_angle','height','width_factor','text_value','generation','horizontal_align','vertical_align','version','tag','field_length','flags','prompt','style']
	def __setattr__(self,name,value):
		A_Types={'alignment_point':bit.point2D,'data_flags':int,'elevation':float,'extrusion':bit.point3D,'field_length':float,'flags':int,'generation':float,'height':float,'horizontal_align':float,'insertion_point':bit.point2D,'oblique_angle':float,'prompt':str,'rotation_angle':float,'style':bit.handle,'tag':str,'text_value':str,'thickness':float,'version':int,'vertical_align':float,'width_factor':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_block(dwg_entity):
	"""Class for dwg_block"""
	__slots__=['block_name']
	def __setattr__(self,name,value):
		A_Types={'block_name':str}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_endblk(dwg_entity):
	"""Class for dwg_endblk"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_seqend(dwg_entity):
	"""Class for dwg_seqend"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_insert(dwg_entity):
	"""Class for dwg_insert"""
	__slots__=['insertion_point','scale_x','scale_y','scale_z','scale_flag','scale','rotation','extrusion','attribute_flag','num_objects','block_header','attrib_first','attrib_last','attribs','seqend']
	def __setattr__(self,name,value):
		A_Types={'attrib_first':bit.handle,'attrib_last':bit.handle,'attribs':list,'attribute_flag':int,'block_header':bit.handle,'extrusion':bit.point3D,'insertion_point':bit.point3D,'num_objects':float,'rotation':float,'scale':bit.point3D,'scale_flag':int,'scale_x':float,'scale_y':float,'scale_z':float,'seqend':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_minsert(dwg_entity):
	"""Class for dwg_minsert"""
	__slots__=['ins_point','scale_x','scale_y','scale_z','scale_flags','scale','rotation','extrusion','attribute_flag','num_objects','num_cols','num_rows','col_spacing','row_spacing','block_header','attrib_first','attrib_last','attribs','seqend']
	def __setattr__(self,name,value):
		A_Types={'attrib_first':bit.handle,'attrib_last':bit.handle,'attribs':list,'attribute_flag':int,'block_header':bit.handle,'col_spacing':float,'extrusion':bit.point3D,'ins_point':bit.point3D,'num_cols':float,'num_objects':float,'num_rows':float,'rotation':float,'row_spacing':float,'scale':bit.point3D,'scale_flags':int,'scale_x':float,'scale_y':float,'scale_z':float,'seqend':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vertex_2d(dwg_entity):
	"""Class for dwg_vertex_2d"""
	__slots__=['flags','point','start_width','bulge','vertex_id','tangent_direction']
	def __setattr__(self,name,value):
		A_Types={'bulge':float,'flags':int,'point':bit.point3D,'start_width':float,'tangent_direction':float,'vertex_id':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vertex_3d(dwg_entity):
	"""Class for dwg_vertex_3d"""
	__slots__=['flags','point_10']
	def __setattr__(self,name,value):
		A_Types={'flags':int,'point_10':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vertex_mesh(dwg_entity):
	"""Class for dwg_vertex_mesh"""
	__slots__=['flags','point']
	def __setattr__(self,name,value):
		A_Types={'flags':int,'point':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vertex_pface(dwg_entity):
	"""Class for dwg_vertex_pface"""
	__slots__=['flags','point_10']
	def __setattr__(self,name,value):
		A_Types={'flags':int,'point_10':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vertex_pface_face(dwg_entity):
	"""Class for dwg_vertex_pface_face"""
	__slots__=['vertex_index_1','vertex_index_2','vertex_index_3','vertex_index_4']
	def __setattr__(self,name,value):
		A_Types={'vertex_index_1':float,'vertex_index_2':float,'vertex_index_3':float,'vertex_index_4':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_polyline_2d(dwg_entity):
	"""Class for dwg_polyline_2d"""
	__slots__=['flags','curve_type','start_width','end_width','thickness','elevation','extrusion','num_objects','vertex_first','vertex_last','vertex','seqend']
	def __setattr__(self,name,value):
		A_Types={'curve_type':float,'elevation':float,'end_width':float,'extrusion':bit.point3D,'flags':float,'num_objects':float,'seqend':bit.handle,'start_width':float,'thickness':float,'vertex':list,'vertex_first':bit.handle,'vertex_last':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_polyline_3d(dwg_entity):
	"""Class for dwg_polyline_3d"""
	__slots__=['spline_flags','closed_flags','num_objects','vertex_first','vertex_last','vertex','seqend']
	def __setattr__(self,name,value):
		A_Types={'closed_flags':int,'num_objects':float,'seqend':bit.handle,'spline_flags':int,'vertex':list,'vertex_first':bit.handle,'vertex_last':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_arc(dwg_entity):
	"""Class for dwg_arc"""
	__slots__=['center','radius','thickness','extrusion','angle_start','angle_end']
	def __setattr__(self,name,value):
		A_Types={'angle_end':float,'angle_start':float,'center':bit.point3D,'extrusion':bit.point3D,'radius':float,'thickness':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_circle(dwg_entity):
	"""Class for dwg_circle"""
	__slots__=['center','radius','thickness','extrusion']
	def __setattr__(self,name,value):
		A_Types={'center':bit.point3D,'extrusion':bit.point3D,'radius':float,'thickness':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_line(dwg_entity):
	"""Class for dwg_line"""
	__slots__=['start_point','end_point','z_flag','start_point_x','end_point_x','start_point_y','end_point_y','start_point_z','end_point_z','thickness','extrusion']
	def __setattr__(self,name,value):
		A_Types={'end_point':bit.point3D,'end_point_x':float,'end_point_y':float,'end_point_z':float,'extrusion':bit.point3D,'start_point':bit.point3D,'start_point_x':float,'start_point_y':float,'start_point_z':float,'thickness':float,'z_flag':int}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_ordinate(dwg_dimension):
	"""Class for dwg_dimension_ordinate"""
	__slots__=['point_10','point_13','point_14','flag_2','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimstyle':bit.handle,'flag_2':int,'point_10':bit.point3D,'point_13':bit.point3D,'point_14':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_linear(dwg_dimension):
	"""Class for dwg_dimension_linear"""
	__slots__=['point_13','point_14','point_10','extension_line_rotation','dimension_rotation','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimension_rotation':float,'dimstyle':bit.handle,'extension_line_rotation':float,'point_10':bit.point3D,'point_13':bit.point3D,'point_14':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_aligned(dwg_dimension):
	"""Class for dwg_dimension_aligned"""
	__slots__=['point_13','point_14','point_10','extension_line_rotation','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimstyle':bit.handle,'extension_line_rotation':float,'point_10':bit.point3D,'point_13':bit.point3D,'point_14':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_ang3pt(dwg_dimension):
	"""Class for dwg_dimension_ang3pt"""
	__slots__=['point_10','point_13','point_14','point_15','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimstyle':bit.handle,'point_10':bit.point3D,'point_13':bit.point3D,'point_14':bit.point3D,'point_15':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_ang2ln(dwg_dimension):
	"""Class for dwg_dimension_ang2ln"""
	__slots__=['point_16','point_13','point_14','point_15','point_10','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimstyle':bit.handle,'point_10':bit.point3D,'point_13':bit.point3D,'point_14':bit.point3D,'point_15':bit.point3D,'point_16':bit.point2D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_radius(dwg_dimension):
	"""Class for dwg_dimension_radius"""
	__slots__=['point_10','point_15','leader_length','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimstyle':bit.handle,'leader_length':float,'point_10':bit.point3D,'point_15':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimension_diameter(dwg_dimension):
	"""Class for dwg_dimension_diameter"""
	__slots__=['point_15','point_10','leader_length','dimstyle','anonymous_block']
	def __setattr__(self,name,value):
		A_Types={'anonymous_block':bit.handle,'dimstyle':bit.handle,'leader_length':float,'point_10':bit.point3D,'point_15':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_point(dwg_entity):
	"""Class for dwg_point"""
	__slots__=['point','thickness','extrusion','x_axis_angle']
	def __setattr__(self,name,value):
		A_Types={'extrusion':bit.point3D,'point':bit.point3D,'thickness':float,'x_axis_angle':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_3d_face(dwg_entity):
	"""Class for dwg_3d_face"""
	__slots__=['corner1','corner2','corner3','corner4','invisible','no_flag','z_flag','point1_x','point1_y','point1_z','point2','point3','point4']
	def __setattr__(self,name,value):
		A_Types={'corner1':bit.point3D,'corner2':bit.point3D,'corner3':bit.point3D,'corner4':bit.point3D,'invisible':float,'no_flag':int,'point1_x':float,'point1_y':float,'point1_z':float,'point2':bit.point3D,'point3':bit.point3D,'point4':bit.point3D,'z_flag':int}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_polyline_pface(dwg_entity):
	"""Class for dwg_polyline_pface"""
	__slots__=['num_vertices','num_faces','owned_object_count','first_vertex','last_vertex','vertex','seqend']
	def __setattr__(self,name,value):
		A_Types={'first_vertex':bit.handle,'last_vertex':bit.handle,'num_faces':float,'num_vertices':float,'owned_object_count':float,'seqend':bit.handle,'vertex':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_polyline_mesh(dwg_entity):
	"""Class for dwg_polyline_mesh"""
	__slots__=['flags','curve_type','m_vertex_count','n_vertex_count','m_density','n_density','owned_object_count','first_vertex','last_vertex','vertex','seqend']
	def __setattr__(self,name,value):
		A_Types={'curve_type':float,'first_vertex':bit.handle,'flags':float,'last_vertex':bit.handle,'m_density':float,'m_vertex_count':float,'n_density':float,'n_vertex_count':float,'owned_object_count':float,'seqend':bit.handle,'vertex':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_solid(dwg_entity):
	"""Class for dwg_solid"""
	__slots__=['thickness','elevation','corner1','corner2','corner3','corner4','extrusion']
	def __setattr__(self,name,value):
		A_Types={'corner1':bit.point2D,'corner2':bit.point2D,'corner3':bit.point2D,'corner4':bit.point2D,'elevation':float,'extrusion':bit.point3D,'thickness':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_trace(dwg_entity):
	"""Class for dwg_trace"""
	__slots__=['thickness','elevation','corner1','corner2','corner3','corner4','extrusion']
	def __setattr__(self,name,value):
		A_Types={'corner1':bit.point2D,'corner2':bit.point2D,'corner3':bit.point2D,'corner4':bit.point2D,'elevation':float,'extrusion':bit.point3D,'thickness':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_shape(dwg_entity):
	"""Class for dwg_shape"""
	__slots__=['insertion_point','scale','rotation','width_factor','oblique','thickness','shapeno','extrusion','shapefile']
	def __setattr__(self,name,value):
		A_Types={'extrusion':bit.point3D,'insertion_point':bit.point3D,'oblique':float,'rotation':float,'scale':float,'shapefile':bit.handle,'shapeno':float,'thickness':float,'width_factor':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_viewport(dwg_entity):
	"""Class for dwg_viewport"""
	__slots__=['center','width','height','view_target','view_direction','view_twist_angle','view_height','lens_height','front_clip_z','back_clip_z','snap_angle','view_center','snap_base','snap_spacing','grid_spacing','circle_zoom','grid_major','frozen_layer_count','status_flag','style_sheet','render_mode','ucs_at_origin','ucs_per_viewport','ucs_origin','ucs_x_axis','ucs_y_axis','ucs_elevation','ucs_ortho_view_type','shade_plot_mode','use_def_lights','def_lighting_type','brightness','contrast','ambient_light_color','viewport_ent_header','frozen_layers','clip_boundary','named_ucs','base_ucs','background','visual_style','shadeplot_id','sun']
	def __setattr__(self,name,value):
		A_Types={'ambient_light_color':bit.color,'back_clip_z':float,'background':bit.handle,'base_ucs':bit.handle,'brightness':float,'center':bit.point3D,'circle_zoom':float,'clip_boundary':bit.handle,'contrast':float,'def_lighting_type':int,'front_clip_z':float,'frozen_layer_count':float,'frozen_layers':list,'grid_major':float,'grid_spacing':bit.point2D,'height':float,'lens_height':float,'named_ucs':bit.handle,'render_mode':int,'shade_plot_mode':float,'shadeplot_id':bit.handle,'snap_angle':float,'snap_base':bit.point2D,'snap_spacing':bit.point2D,'status_flag':float,'style_sheet':str,'sun':bit.handle,'ucs_at_origin':int,'ucs_elevation':float,'ucs_origin':bit.point3D,'ucs_ortho_view_type':float,'ucs_per_viewport':int,'ucs_x_axis':bit.point3D,'ucs_y_axis':bit.point3D,'use_def_lights':int,'view_center':bit.point2D,'view_direction':bit.point3D,'view_height':float,'view_target':bit.point3D,'view_twist_angle':float,'viewport_ent_header':bit.handle,'visual_style':bit.handle,'width':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ellipse(dwg_entity):
	"""Class for dwg_ellipse"""
	__slots__=['center','sm_axis_vector','extrusion','axis_ratio','starting_angle','ending_angle']
	def __setattr__(self,name,value):
		A_Types={'axis_ratio':float,'center':bit.point3D,'ending_angle':float,'extrusion':bit.point3D,'sm_axis_vector':bit.point3D,'starting_angle':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_spline(dwg_entity):
	"""Class for dwg_spline"""
	__slots__=['scenario','spline_flag_1','knot_parameter','degree','fit_tolerence','tan_vector_begin','tan_vector_end','num_fit_points','rational','closed','periodic','knot_tol','ctrl_tol','num_knots','num_ctrl_points','weight','knot','control_points','fit_points']
	def __setattr__(self,name,value):
		A_Types={'closed':int,'control_points':list,'ctrl_tol':float,'degree':float,'fit_points':list,'fit_tolerence':float,'knot':list,'knot_parameter':float,'knot_tol':float,'num_ctrl_points':float,'num_fit_points':float,'num_knots':float,'periodic':int,'rational':int,'scenario':float,'spline_flag_1':float,'tan_vector_begin':bit.point3D,'tan_vector_end':bit.point3D,'weight':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_region(dwg_entity):
	"""Class for dwg_region"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_3dsolid(dwg_entity):
	"""Class for dwg_3dsolid"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_body(dwg_entity):
	"""Class for dwg_body"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ray(dwg_entity):
	"""Class for dwg_ray"""
	__slots__=['point','vector']
	def __setattr__(self,name,value):
		A_Types={'point':bit.point3D,'vector':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_xline(dwg_entity):
	"""Class for dwg_xline"""
	__slots__=['point','vector']
	def __setattr__(self,name,value):
		A_Types={'point':bit.point3D,'vector':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dictionary(dwg_non_entity):
	"""Class for dwg_dictionary"""
	__slots__=['num_entries','unknown','cloning_flag','hard_owner_flag','text','handle_refs','reactors','xdicobjhandle','itemhandles']
	def __setattr__(self,name,value):
		A_Types={'cloning_flag':float,'handle_refs':bit.handle,'hard_owner_flag':int,'itemhandles':list,'num_entries':float,'reactors':list,'text':list,'unknown':int,'xdicobjhandle':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dictionarywdflt(dwg_non_entity):
	"""Class for dwg_dictionarywdflt"""
	__slots__=['num_entries','unknown','cloning_flag','hard_owner_flag','text','handle_refs','reactors','xdicobjhandle','itemhandles','default']
	def __setattr__(self,name,value):
		A_Types={'cloning_flag':float,'default':bit.handle,'handle_refs':bit.handle,'hard_owner_flag':int,'itemhandles':list,'num_entries':float,'reactors':list,'text':list,'unknown':int,'xdicobjhandle':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_mtext(dwg_entity):
	"""Class for dwg_mtext"""
	__slots__=['insertion_point','extrusion','x_axis_direction','rectangle_width','rectangle_height','text_height','attachment','brawing_direction','extents_height','extents_width','text','linespacing_style','linespacing_factor','unknown_bit','background_flags','background_scale_factor','background_color','background_transparency','not_annotative','version','default','registered_application','attachment_point','x_direction','unknown']
	def __setattr__(self,name,value):
		A_Types={'attachment':float,'attachment_point':float,'background_color':bit.color,'background_flags':float,'background_scale_factor':float,'background_transparency':float,'brawing_direction':float,'default':int,'extents_height':float,'extents_width':float,'extrusion':bit.point3D,'insertion_point':bit.point3D,'linespacing_factor':float,'linespacing_style':float,'not_annotative':int,'rectangle_height':float,'rectangle_width':float,'registered_application':bit.handle,'text':str,'text_height':float,'unknown':bit.handle,'unknown_bit':int,'version':float,'x_axis_direction':bit.point3D,'x_direction':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_leader(dwg_entity):
	"""Class for dwg_leader"""
	__slots__=['unknown1','annotation_type','pth_type','num_points','point','origin','extrusion','x_direction','offset_block_ins_point','end_point_projection','dim_gap','box_height','box_weidth','hook_line_on_x_dir','arrowhead_flag','arrowhead_type','dim_asz','unknown2','unknown3','unknown4','byblockcolor','unknown5','unknown6','unknown7','unknown8','unknown9','associated_annotation','dim_style']
	def __setattr__(self,name,value):
		A_Types={'annotation_type':float,'arrowhead_flag':int,'arrowhead_type':float,'associated_annotation':bit.handle,'box_height':float,'box_weidth':float,'byblockcolor':float,'dim_asz':float,'dim_gap':float,'dim_style':bit.handle,'end_point_projection':bit.point3D,'extrusion':bit.point3D,'hook_line_on_x_dir':int,'num_points':float,'offset_block_ins_point':bit.point3D,'origin':bit.point3D,'point':bit.point3D,'pth_type':float,'unknown1':int,'unknown2':int,'unknown3':int,'unknown4':float,'unknown5':int,'unknown6':int,'unknown7':float,'unknown8':int,'unknown9':int,'x_direction':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_tolerance(dwg_entity):
	"""Class for dwg_tolerance"""
	__slots__=['unknown1','height','dim_gap','ins_point','x_direction','extruision','text_string','dim_style']
	def __setattr__(self,name,value):
		A_Types={'dim_gap':float,'dim_style':bit.handle,'extruision':bit.point3D,'height':float,'ins_point':bit.point3D,'text_string':float,'unknown1':float,'x_direction':bit.point3D}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_mline(dwg_entity):
	"""Class for dwg_mline"""
	__slots__=['scale','justification','base_point','extrusion','open','line_in_style','num_vertex','mline_style']
	def __setattr__(self,name,value):
		A_Types={'base_point':bit.point3D,'extrusion':bit.point3D,'justification':int,'line_in_style':int,'mline_style':bit.handle,'num_vertex':float,'open':float,'scale':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_block_control(dwg_non_entity):
	"""Class for dwg_block_control"""
	__slots__=['xdic_missing','num_entries','handle_null','handle_xdicobjhandle','handles','model_space_handle','paper_space_handle']
	def __setattr__(self,name,value):
		A_Types={'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'handles':list,'model_space_handle':bit.handle,'num_entries':float,'paper_space_handle':bit.handle,'xdic_missing':int}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_block_header(dwg_non_entity):
	"""Class for dwg_block_header"""
	__slots__=['entry_name','flag_64','xrefindex_1','xdep','anonymous','has_atts','is_ref','xref_overlaid','loaded_bit','owned_object_count','base_point','xref_path_name','insert_count','block_description','preview_size','preview_data','insert_units','explodable','block_scaling','block_control','reactors','xdicobjhandle','handle_null','block_entity','first_entry','last_entry','owned_object_handles','endblk_entity','insert_handles','layout_handle']
	def __setattr__(self,name,value):
		A_Types={'anonymous':int,'base_point':bit.point3D,'block_control':bit.handle,'block_description':str,'block_entity':bit.handle,'block_scaling':int,'endblk_entity':bit.handle,'entry_name':str,'explodable':int,'first_entry':bit.handle,'flag_64':int,'handle_null':bit.handle,'has_atts':int,'insert_count':int,'insert_handles':list,'insert_units':float,'is_ref':int,'last_entry':bit.handle,'layout_handle':bit.handle,'loaded_bit':int,'owned_object_count':float,'owned_object_handles':bit.handle,'preview_data':list,'preview_size':float,'reactors':list,'xdep':int,'xdicobjhandle':bit.handle,'xref_overlaid':int,'xref_path_name':str,'xrefindex_1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_layer_control(dwg_non_entity):
	"""Class for dwg_layer_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','layer_objhandles']
	def __setattr__(self,name,value):
		A_Types={'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'layer_objhandles':list,'num_entries':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_layer(dwg_non_entity):
	"""Class for dwg_layer"""
	__slots__=['name','flag_64','xrefindex1','xdep','frozen','on','frozen_in_new','locked','values','color','layer_control','reactors','xdicobjhandle','exref_block_handle','plotstyle','material','linetype']
	def __setattr__(self,name,value):
		A_Types={'color':bit.color,'exref_block_handle':bit.handle,'flag_64':int,'frozen':int,'frozen_in_new':int,'layer_control':bit.handle,'linetype':bit.handle,'locked':int,'material':bit.handle,'name':str,'on':int,'plotstyle':bit.handle,'reactors':list,'values':float,'xdep':int,'xdicobjhandle':bit.handle,'xrefindex1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_shapefile_control(dwg_non_entity):
	"""Class for dwg_shapefile_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','shapefile_objhandles']
	def __setattr__(self,name,value):
		A_Types={'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float,'shapefile_objhandles':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_shapefile(dwg_non_entity):
	"""Class for dwg_shapefile"""
	__slots__=['name','flag64','xrefindex1','xdep','vertical','shape_file','fixed_height','width_factor','oblique_angle','generation','last_height','font_name','big_font_name','shapefile','reactors','xdicobjhandle','xref_block']
	def __setattr__(self,name,value):
		A_Types={'big_font_name':str,'fixed_height':float,'flag64':int,'font_name':str,'generation':int,'last_height':float,'name':str,'oblique_angle':float,'reactors':list,'shape_file':int,'shapefile':bit.handle,'vertical':int,'width_factor':float,'xdep':int,'xdicobjhandle':bit.handle,'xref_block':bit.handle,'xrefindex1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ltype_control(dwg_non_entity):
	"""Class for dwg_ltype_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','byblock_ltype','bylayer_ltype','ltypes']
	def __setattr__(self,name,value):
		A_Types={'byblock_ltype':bit.handle,'bylayer_ltype':bit.handle,'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'ltypes':list,'num_entries':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ltype(dwg_non_entity):
	"""Class for dwg_ltype"""
	__slots__=['name','flag_64','xrefindex1','xdep','desc','pattern_len','alignment','numdashes','dash_length','complex_shapecode','offset_x','offset_y','scale','rotation','shapeflag','string_area','test_data','ltype','reactors','xdicobj','xref','shapefile_dash']
	def __setattr__(self,name,value):
		A_Types={'alignment':int,'complex_shapecode':list,'dash_length':list,'desc':str,'flag_64':int,'ltype':bit.handle,'name':str,'numdashes':int,'offset_x':list,'offset_y':list,'pattern_len':float,'reactors':list,'rotation':list,'scale':list,'shapefile_dash':list,'shapeflag':list,'string_area':list,'test_data':list,'xdep':int,'xdicobj':bit.handle,'xref':bit.handle,'xrefindex1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_view_control(dwg_non_entity):
	"""Class for dwg_view_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','views']
	def __setattr__(self,name,value):
		A_Types={'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float,'views':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_view(dwg_non_entity):
	"""Class for dwg_view"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ucs_control(dwg_non_entity):
	"""Class for dwg_ucs_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','ucs_handles']
	def __setattr__(self,name,value):
		A_Types={'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float,'ucs_handles':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ucs(dwg_non_entity):
	"""Class for dwg_ucs"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vport_control(dwg_non_entity):
	"""Class for dwg_vport_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','vport_handles']
	def __setattr__(self,name,value):
		A_Types={'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float,'vport_handles':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vport(dwg_non_entity):
	"""Class for dwg_vport"""
	__slots__=['name','flag_64','xrefindex1','xdep','view_height','aspect_ratio','view_center','view_target','view_dir','view_twist','lens_length','front_clip','back_clip','view_mode','render_mode','use_default_lights','default_lighting_type','brightness','contrast','ambient_color','lower_left','upper_right','ucs_follow','circle_zoom','fast_zoom','ucsicon','grid_on','frid_spacing','snap_on','snap_style','snap_isopair','span_rot','snap_base','snap_spacing','unknown','ucs_per_viewport','ucs_origin','ucs_x_axis','ucs_y_axis','ucs_elevation','ucs_orthographic_type','grid_flags','grid_major','vport_control','reactors','xdicobjhandle','xref','background','visual_style','sun','names_ucs','nase_ucs']
	def __setattr__(self,name,value):
		A_Types={'ambient_color':bit.color,'aspect_ratio':float,'back_clip':float,'background':bit.handle,'brightness':float,'circle_zoom':float,'contrast':float,'default_lighting_type':int,'fast_zoom':int,'flag_64':int,'frid_spacing':bit.point2D,'front_clip':float,'grid_flags':float,'grid_major':float,'grid_on':int,'lens_length':float,'lower_left':bit.point2D,'name':str,'names_ucs':bit.handle,'nase_ucs':bit.handle,'reactors':list,'render_mode':int,'snap_base':bit.point2D,'snap_isopair':float,'snap_on':int,'snap_spacing':bit.point2D,'snap_style':int,'span_rot':float,'sun':bit.handle,'ucs_elevation':float,'ucs_follow':int,'ucs_origin':bit.point3D,'ucs_orthographic_type':float,'ucs_per_viewport':int,'ucs_x_axis':bit.point3D,'ucs_y_axis':bit.point3D,'ucsicon':list,'unknown':int,'upper_right':bit.point2D,'use_default_lights':int,'view_center':bit.point2D,'view_dir':bit.point3D,'view_height':float,'view_mode':list,'view_target':bit.point3D,'view_twist':float,'visual_style':bit.handle,'vport_control':bit.handle,'xdep':int,'xdicobjhandle':bit.handle,'xref':bit.handle,'xrefindex1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_appid_control(dwg_non_entity):
	"""Class for dwg_appid_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','appid_handles']
	def __setattr__(self,name,value):
		A_Types={'appid_handles':list,'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_appid(dwg_non_entity):
	"""Class for dwg_appid"""
	__slots__=['name','flag_64','xrefinde1','xdep','unknown','app_control','reactors','xdicobjhandle','xref']
	def __setattr__(self,name,value):
		A_Types={'app_control':bit.handle,'flag_64':int,'name':str,'reactors':list,'unknown':int,'xdep':int,'xdicobjhandle':bit.handle,'xref':bit.handle,'xrefinde1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimstyle_control(dwg_non_entity):
	"""Class for dwg_dimstyle_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','dimstyle_handles']
	def __setattr__(self,name,value):
		A_Types={'dimstyle_handles':list,'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dimstyle(dwg_non_entity):
	"""Class for dwg_dimstyle"""
	__slots__=['name','flag_64','xrefindex1','xdep','dimtol','dimlim','dimtih','dimtoh','dimse1','dimse2','dimalt','dimtofl','dimsah','dimtix','dimsoxd','dimaltd','dimzin','dimsd1','dimsd2','dimtolj','dimjust','dimfit','dimupt','dimtzin','dimaltz','dimalttz','dimtad','dimunit','dimaunit','dimdec','dimtdec','dimaltu','dimalttd','dimscale','dimasz','dimexo','dimdli','dimexe','dimrnd','dimdle','dimtp','dimtm','dimtxt','dimcen','dimtsz','dimaltf','dimlfac','dimtvp','dimtfac','dimgap','dimpost','dimapost','dimblk','dimblk1','dimblk2','dimclrd','dimclre','dimclrt','dimfxl','dimjogang','dimtfill','dimtfillclr','dimazin','dimarcsym','dimaltrnd','dimadec','dimfrac','dimlunit','dimdsep','dimtmove','dimfxlon','dimtxtdirection','dimaltmzf','dimaltmzs','dimmzs','dimmzf','dimlwd','dimlwe','unknown','dimstyle','reactors','xdicobj','xref','shapefile','leader','dimltype','dimltex1','dimltex2']
	def __setattr__(self,name,value):
		A_Types={'dimadec':float,'dimalt':int,'dimaltd':float,'dimaltf':float,'dimaltmzf':float,'dimaltmzs':str,'dimaltrnd':float,'dimalttd':float,'dimalttz':float,'dimaltu':float,'dimaltz':float,'dimapost':str,'dimarcsym':float,'dimasz':float,'dimaunit':float,'dimazin':float,'dimblk':bit.handle,'dimblk1':bit.handle,'dimblk2':bit.handle,'dimcen':float,'dimclrd':float,'dimclre':float,'dimclrt':float,'dimdec':float,'dimdle':float,'dimdli':float,'dimdsep':float,'dimexe':float,'dimexo':float,'dimfit':float,'dimfrac':float,'dimfxl':float,'dimfxlon':int,'dimgap':float,'dimjogang':float,'dimjust':float,'dimlfac':float,'dimlim':int,'dimltex1':bit.handle,'dimltex2':bit.handle,'dimltype':bit.handle,'dimlunit':float,'dimlwd':float,'dimlwe':float,'dimmzf':float,'dimmzs':str,'dimpost':str,'dimrnd':float,'dimsah':int,'dimscale':float,'dimsd1':int,'dimsd2':int,'dimse1':int,'dimse2':int,'dimsoxd':int,'dimstyle':bit.handle,'dimtad':float,'dimtdec':float,'dimtfac':float,'dimtfill':float,'dimtfillclr':bit.color,'dimtih':int,'dimtix':int,'dimtm':float,'dimtmove':float,'dimtofl':int,'dimtoh':int,'dimtol':int,'dimtolj':float,'dimtp':float,'dimtsz':float,'dimtvp':float,'dimtxt':float,'dimtxtdirection':int,'dimtzin':float,'dimunit':float,'dimupt':int,'dimzin':float,'flag_64':int,'leader':bit.handle,'name':str,'reactors':list,'shapefile':bit.handle,'unknown':int,'xdep':int,'xdicobj':bit.handle,'xref':bit.handle,'xrefindex1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vp_ent_hdr_control(dwg_non_entity):
	"""Class for dwg_vp_ent_hdr_control"""
	__slots__=['num_entries','handle_null','handle_xdicobjhandle','dimstyle_handles']
	def __setattr__(self,name,value):
		A_Types={'dimstyle_handles':list,'handle_null':bit.handle,'handle_xdicobjhandle':bit.handle,'num_entries':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vp_ent_hdr(dwg_non_entity):
	"""Class for dwg_vp_ent_hdr"""
	__slots__=['entry_name','flag_64','xrefindex1','xdep','flag_1','viewport_entity_control','handle_xdicobjhandle','xref_handle','viewport_entity','prv_vport']
	def __setattr__(self,name,value):
		A_Types={'entry_name':str,'flag_1':int,'flag_64':int,'handle_xdicobjhandle':bit.handle,'prv_vport':bit.handle,'viewport_entity':bit.handle,'viewport_entity_control':bit.handle,'xdep':int,'xref_handle':bit.handle,'xrefindex1':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_group(dwg_non_entity):
	"""Class for dwg_group"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_mlinestyle(dwg_non_entity):
	"""Class for dwg_mlinestyle"""
	__slots__=['name','desc','flags','fillcolor','start_angle','end_angle','num_lines','offset','color','line_type_index','line_type_handle','parent','reactors','xdicobj']
	def __setattr__(self,name,value):
		A_Types={'color':list,'desc':str,'end_angle':float,'fillcolor':bit.color,'flags':float,'line_type_handle':list,'line_type_index':list,'name':str,'num_lines':int,'offset':list,'parent':bit.handle,'reactors':bit.handle,'start_angle':float,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_ole2frame(dwg_non_entity):
	"""Class for dwg_ole2frame"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dummy(dwg_non_entity):
	"""Class for dwg_dummy"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_long_transaction(dwg_non_entity):
	"""Class for dwg_long_transaction"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_lwpline(dwg_entity):
	"""Class for dwg_lwpline"""
	__slots__=['flag','constwidth','elevation','thickness','normal','num_points','num_bulges','vertexidcount','numwidths','coords','bulge','vertexid','widths']
	def __setattr__(self,name,value):
		A_Types={'bulge':list,'constwidth':float,'coords':list,'elevation':float,'flag':float,'normal':bit.point3D,'num_bulges':float,'num_points':float,'numwidths':float,'thickness':float,'vertexid':list,'vertexidcount':float,'widths':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_hatch1(dwg_entity):
	"""Class for dwg_hatch1"""
	__slots__=['gradient_fill_flag','reserved','gradient_angle','gradient_shift','single_color_grad','gradient_tint','num_gradient_colors','unknown_double','unknown_short','rgb_color','ignored_color_byte','gradient_name','z_coord','extrusion','name','solid_fill','associative','numpaths','hatch_paths','style','patterntype','angle','scale_or_spacing','double_hatch','num_defination_lines']
	def __setattr__(self,name,value):
		A_Types={'angle':float,'associative':int,'double_hatch':int,'extrusion':bit.point3D,'gradient_angle':float,'gradient_fill_flag':float,'gradient_name':int,'gradient_shift':float,'gradient_tint':float,'hatch_paths':list,'ignored_color_byte':list,'name':str,'num_defination_lines':float,'num_gradient_colors':float,'numpaths':float,'patterntype':float,'reserved':float,'rgb_color':list,'scale_or_spacing':float,'single_color_grad':float,'solid_fill':int,'style':float,'unknown_double':list,'unknown_short':list,'z_coord':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_xrecord(dwg_non_entity):
	"""Class for dwg_xrecord"""
	__slots__=['num_databytes','databytes','cloning_flag','parent','reactors','xdic']
	def __setattr__(self,name,value):
		A_Types={'cloning_flag':float,'databytes':list,'num_databytes':float,'parent':bit.handle,'reactors':list,'xdic':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_placeholder(dwg_non_entity):
	"""Class for dwg_placeholder"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_vba_project(dwg_entity):
	"""Class for dwg_vba_project"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_layout(dwg_non_entity):
	"""Class for dwg_layout"""
	__slots__=['page_setup_name','printer_config','plot_layout_flags','margin_left','margin_bottom','margin_right','margin_top','paper_width','paper_height','paper_size','plot_origin','paper_units','plot_rotation','plot_type','window_min','window_max','plot_view_name','real_world_units','drawing_units','current_style_sheet','scale_type','scale_factor','paper_image_origin','shade_plot_mode','shade_plot_res_level','shade_plot_custom','layout_name','tab_order','flag','ucs_origin','lim_min','lim_max','ins_point','ucs_axis_x','ucs_axis_y','elevation','ortho_view_type','ext_min','ext_max','viewport_count','parent','reactors','xdicobj','plot_view','visual_style_handle','assoc_paperspace_block_record','last_active_viewport','base_ucs','named_ucs','viewport']
	def __setattr__(self,name,value):
		A_Types={'assoc_paperspace_block_record':bit.handle,'base_ucs':bit.handle,'current_style_sheet':str,'drawing_units':float,'elevation':float,'ext_max':bit.point3D,'ext_min':bit.point3D,'flag':float,'ins_point':bit.point3D,'last_active_viewport':bit.handle,'layout_name':str,'lim_max':bit.point2D,'lim_min':bit.point2D,'margin_bottom':float,'margin_left':float,'margin_right':float,'margin_top':float,'named_ucs':bit.handle,'ortho_view_type':float,'page_setup_name':str,'paper_height':float,'paper_image_origin':bit.point2D,'paper_size':str,'paper_units':float,'paper_width':float,'parent':bit.handle,'plot_layout_flags':float,'plot_origin':bit.point2D,'plot_rotation':float,'plot_type':float,'plot_view':bit.handle,'plot_view_name':str,'printer_config':str,'reactors':list,'real_world_units':float,'scale_factor':float,'scale_type':float,'shade_plot_custom':float,'shade_plot_mode':float,'shade_plot_res_level':float,'tab_order':float,'ucs_axis_x':bit.point3D,'ucs_axis_y':bit.point3D,'ucs_origin':bit.point3D,'viewport':list,'viewport_count':int,'visual_style_handle':bit.handle,'window_max':bit.point2D,'window_min':bit.point2D,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_acad_proxy_entity(dwg_non_entity):
	"""Class for dwg_acad_proxy_entity"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_acad_proxy_object(dwg_non_entity):
	"""Class for dwg_acad_proxy_object"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_unknown(dwg_non_entity):
	"""Class for dwg_unknown"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_rastervariables(dwg_non_entity):
	"""Class for dwg_rastervariables"""
	__slots__=['classver','dispfrm','dispqual','units','parent','reactors','xdicobj']
	def __setattr__(self,name,value):
		A_Types={'classver':float,'dispfrm':float,'dispqual':float,'parent':bit.handle,'reactors':list,'units':float,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_scale(dwg_non_entity):
	"""Class for dwg_scale"""
	__slots__=['unknown','name','paper_units','drawing_units','unit_scale_flag','parent','reactors','xdicobj']
	def __setattr__(self,name,value):
		A_Types={'drawing_units':float,'name':str,'paper_units':float,'parent':bit.handle,'reactors':bit.handle,'unit_scale_flag':int,'unknown':float,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_acdbplaceholder(dwg_non_entity):
	"""Class for dwg_acdbplaceholder"""
	__slots__=['parent','reactors','xdicobj']
	def __setattr__(self,name,value):
		A_Types={'parent':bit.handle,'reactors':bit.handle,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_dictionaryvar(dwg_non_entity):
	"""Class for dwg_dictionaryvar"""
	__slots__=['int_val','str','parent','reactor','xdicobj']
	def __setattr__(self,name,value):
		A_Types={'int_val':int,'parent':bit.handle,'reactor':list,'str':str,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_mleaderstyle(dwg_non_entity):
	"""Class for dwg_mleaderstyle"""
	__slots__=['version','content_type','draw_multileader_order','draw_leader_order','maximum_number_of_points','first_segment_angle','leader_type','leader_line_color','leader_line_type_handle','leader_line_weight','is_landing_enabled','landing_gap','auto_include_landing','landing_distance','style_description','arrow_head_block_handle','arrow_head_size','text_default','text_style_handle','left_attachment','right_attachment']
	def __setattr__(self,name,value):
		A_Types={'arrow_head_block_handle':bit.handle,'arrow_head_size':float,'auto_include_landing':int,'content_type':float,'draw_leader_order':float,'draw_multileader_order':float,'first_segment_angle':float,'is_landing_enabled':int,'landing_distance':float,'landing_gap':float,'leader_line_color':bit.color,'leader_line_type_handle':bit.handle,'leader_line_weight':float,'leader_type':float,'left_attachment':float,'maximum_number_of_points':float,'right_attachment':float,'style_description':str,'text_default':str,'text_style_handle':bit.handle,'version':float}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_sortentstable(dwg_non_entity):
	"""Class for dwg_sortentstable"""
	__slots__=['xdic_missing','num_entries','sort_handles','parent','reactor','xdicobj','owner_handle','entities']
	def __setattr__(self,name,value):
		A_Types={'entities':list,'num_entries':float,'owner_handle':bit.handle,'parent':bit.handle,'reactor':list,'sort_handles':list,'xdic_missing':int,'xdicobj':bit.handle}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_acdb_blkrefobjectcontextdata_class(dwg_non_entity):
	"""Class for dwg_acdb_blkrefobjectcontextdata_class"""
	__slots__=[]
	def __setattr__(self,name,value):
		A_Types={}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput



class dwg_sun(dwg_non_entity):
	"""Class for dwg_sun"""
	__slots__=['reactor']
	def __setattr__(self,name,value):
		A_Types={'reactor':list}
		if name in A_Types:
			if not isinstance(value, A_Types[name]):
				raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
		object.__setattr__(self, name, value)
	def __repr__(self):
		TempOutput=''
		for i in dir(self):
			if not i.startswith('__') and hasattr(self,i):
				TempOutput=TempOutput+'\t\t'+str(i)+' : '+repr(getattr(self,i))+'\n'
		return TempOutput
DataTypeList={'B':'int','B':'int','2BD':'bit.point2D','2RD':'bit.point2D','3B':'bit.point3D','3BD':'bit.point3D','3DD':'bit.point3D','3RD':'bit.point3D','BB':'float','BD':'float','BE':'int','BL':'float','BLL':'int','BS':'float','BT':'int','CMC':'bit.color','DD':'float','H':'bit.handle','MC':'int','MS':'int','RC':'int','RD':'float','RL':'int','RS':'int','SN':'int','T':'str','TC':'int','TU':'int','TV':'str','U':'float'}

class bitData(object):
	"""Bitwise Data for dwg file."""
	def __init__(self, chain="",byte=0,size=0,bit=0):
		if not isinstance(byte, int): raise TypeError("For class bitData byte attribute must be set to an integer")
		if not isinstance(size, int): raise TypeError("For class bitData size attribute must be set to an integer")
		if not isinstance(bit, int): raise TypeError("For class bitData bit attribute must be set to an integer")
		self.chain = chain
		self.byte = byte
		self.size = size
		self.bit = bit

class gpdwgData(object):
	"""Data strucutre for DWG output"""
	class gpdwgClass(object):
		"""Class for gpdwg Class strucutre """
		__slots__=['CLASS_NUM','VERSION','APPNAME','CPLUSPLUSCLASSNAME','CLASSDXFNAME','WASAZOMBIE','ITEMCLASSID','PROXY_FLAGS','NUM_OF_OBJECTS','DWG_VERSION','MAINTENANCE_VERSION','UNKNOWN1','UNKNOWN2']
		def __setattr__(self,name,value):
			A_Types={'CLASS_NUM':float,'VERSION':float,'APPNAME':str,'CPLUSPLUSCLASSNAME':str,'CLASSDXFNAME':str,'WASAZOMBIE':int,'ITEMCLASSID':float,'PROXY_FLAGS':float,'NUM_OF_OBJECTS':float,'DWG_VERSION':float,'MAINTENANCE_VERSION':float,'UNKNOWN1':float,'UNKNOWN2':float}
			if name in A_Types:
				if not isinstance(value, A_Types[name]):
					raise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))
			object.__setattr__(self, name, value)
		def __repr__(self):
			TempOutput=""
			for i in dir(self):
				if not i.startswith('__') and hasattr(self,i):
					TempOutput=TempOutput+"\t"+str(i)+' : '+repr(getattr(self,i))+'\n'
			return TempOutput


	def __init__(self, v=gpdwgVariables(), ver=0, h={'section': {}, 'sectionCount':0},c=[],cc=0,o={},oc=0):
		self.header = h
		self.variable = v
		self.classes = c
		self.classcount = cc
		self.version = ver
		self.objects = o
		self.objectcount=oc
	def __repr__(self):
		print("Header")
		print
		print(repr(self.header['ACADMAINTVER']))
		print("")
		print(repr(self.variable))
		TempOutput=""
		for i in range(len(self.classes)):
			TempOutput=TempOutput+"\nClass No "+str(i+500)+":\n"+repr(self.classes[i])
		TempOutput=TempOutput+"\n\nObjects\n"+str(self.objectcount) + " objects found.\n\n"
		for i in self.objects.keys():
			TempOutput=TempOutput+"\n\t"+str(i)+": " + str(type(self.objects[i]).__name__) + "\n"
			TempOutput=TempOutput+repr(self.objects[i])
		'''
		
		for object in self.objects.items():
			TempOutput=TempOutput+"\n\t: " + str(type(object)) + "\n"
			TempOutput=TempOutput+repr(object)
		'''

		return TempOutput

def read(dwgFilePath):
	if not os.path.isfile(dwgFilePath):
		logger.error( "File %s not found." % dwgFilePath)
		quit()
	if not dwgFilePath.lower().endswith('.dwg'):
		logger.error( "Only files with .dwg extension can be decoded.")
		quit()

	dat=bitData() #Variable that will hold dwg files bitwise data
	gpdwg=gpdwgData() #Variable that will hold data output
	with open(dwgFilePath,"r+b") as f:
		dat.size = os.path.getsize(dwgFilePath)
		#logger.error(str(os.path.getsize(dwgFilePath)))
		dat.chain= mmap.mmap(f.fileno(), 0)

	gpdwg.header['ACADMAINTVER']=dat.chain[0:6].decode("utf-8")
	gpdwg.header['ACADVER']=Versions[gpdwg.header['ACADMAINTVER']]
	dat.version=Versions[gpdwg.header['ACADMAINTVER']]

	if gpdwg.header['ACADMAINTVER']=='AC1015':
		import version
		version.decode2000(gpdwg,dat)
	return gpdwg

def getPreview(dwgFilePath):
	if not os.path.isfile(dwgFilePath):
		quit()
	if not dwgFilePath.lower().endswith('.dwg'):
		logger.error( "Only files with .dwg extension can be decoded.")
		quit()

	dat=bitData() #Variable that will hold dwg files bitwise data
	with open(dwgFilePath,"r+b") as f:
		dat.size = os.path.getsize(dwgFilePath)
		#logger.error(str(os.path.getsize(dwgFilePath)))
		dat.chain= mmap.mmap(f.fileno(), 0)
	if dat.chain[0:6].decode("utf-8") == 'AC1015':
		dat.byte=71
		Section5Start=bit.readwithlog("RL",dat,"Section 5 Address",1)
		Section5Size=bit.readwithlog("RL",dat,"Section 5 Size",1)
		dat.byte=Section5Start+Section5Size
	elif dat.chain[0:6].decode("utf-8") == 'AC1018' or dat.chain[0:6].decode("utf-8") == 'AC1021' or  dat.chain[0:6].decode("utf-8") == 'AC1024' or  dat.chain[0:6].decode("utf-8") == 'AC1027' or  dat.chain[0:6].decode("utf-8") == 'AC1032':
		dat.byte=13
		PreviewStart=bit.readwithlog("RL",dat,"Preview Start",1)
		dat.byte=PreviewStart

	if bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_PICTURE_BEGIN'))):
		Preview_Size=bit.readwithlog('RL',dat,'Preview_Size',1)
		Image_Present=bit.readwithlog('RC',dat,'Image_Present',1)
		from PIL import Image
		for i in range(Image_Present):
			Code=bit.readwithlog('RC',dat,'Code',1)
			if Code == 1 :
				Header_Start = bit.readwithlog('RL',dat,'Header Start',1)
				Header_Size = bit.readwithlog('RL',dat,'Header Size',1)
			elif Code == 2 :
				bmp_Start = bit.readwithlog('RL',dat,'BMP Start',1)
				bmp_Size = bit.readwithlog('RL',dat,'BMP Size',1)
				dat.byte=bmp_Start
				Preview_BMP_Header_Size=bit.readwithlog('RL',dat,'Header Size',1)
				Preview_BMP_Image_Width=bit.readwithlog('RL',dat,'Image Width',1)	
				Preview_BMP_Image_Height=bit.readwithlog('RL',dat,'Image Height',1)	
				Preview_BMP_Color_Plane=bit.readwithlog('RS',dat,'Color Plane',1)	
				Preview_BMP_Bits_Per_Pixel=bit.readwithlog('RS',dat,'Bits per pixel',1)
				Preview_BMP_Compression=bit.readwithlog('RL',dat,'BMP Compression',1)
				Preview_BMP_Image_Size=bit.readwithlog('RL',dat,'BMP Image Size',1)
				Preview_BMP_Res_Hor=bit.readwithlog('RL',dat,'BMP Resolution Horizontal',1)
				Preview_BMP_Res_Ver=bit.readwithlog('RL',dat,'BMP Resolution Vertical',1)
				Preview_BMP_Num_Colors=bit.readwithlog('RL',dat,'BMP Number of colors',1)
				Preview_BMP_Num_Imp_Colors=bit.readwithlog('RL',dat,'BMP Number of important colors',1)
				ColorTable=[]
				for i in range(256):
					R=bit.read_RC(dat)
					G=bit.read_RC(dat)
					B=bit.read_RC(dat)
					bit.read_RC(dat)
					ColorTable.append((R,G,B))
				logger.debug(dat.byte)
				img = Image.new( 'RGB', (Preview_BMP_Image_Width,Preview_BMP_Image_Height))
				PNG_pixels = img.load()
				for i in range(Preview_BMP_Image_Height):
					for j in range(Preview_BMP_Image_Width):
						PNG_pixels[j,i]=ColorTable[bit.read_RC(dat)]
				if bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_PICTURE_END'))):
					return img
			elif Code == 3:
				wmf_Start = bit.readwithlog('RL',dat,'WMF Start',1)
				wmf_Size = bit.readwithlog('RL',dat,'WMF Size',1)
			elif Code == 6:
				PNG_Start = bit.readwithlog('RL',dat,'PNG Start',1)
				PNG_Size = bit.readwithlog('RL',dat,'PNG Size',1)
				dat.byte=PNG_Start
				f = open("demofile.png", "wb")
				import struct, io
				TempBytes=bytearray(PNG_Size)
				for i  in range(PNG_Size):
					struct.pack_into("B",TempBytes,i,bit.read_RC(dat))
				img = Image.open(io.BytesIO(TempBytes))
				if bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_PICTURE_END'))):
					return img
			else:
				logger.error("Unknown Preview Code found.")
