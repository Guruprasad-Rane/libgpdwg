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