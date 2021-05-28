
def add_to_list(Tempobject,item,value):
	TempList=[]
	if not hasattr(Tempobject , item):
		setattr(Tempobject, item, TempList)
	TempList=getattr(Tempobject, item)
	TempList.append(value)
	setattr(Tempobject, item, TempList)




def check_handle(Temp_H):
	if isinstance(Temp_H,basestring):
		TempLog(10,"Error reading Header")
		return False
	if Temp_H.code != 0:
		TempLog(10,"Header Code is not 0")
		return False
	if Temp_H.value == 0:
		TempLog(10,"Header Value is 0")
		return False
	return True

def check_obj_crc(dat,size):
	if dat.bit > 0:
		crc2 = bit.read_crc8 ('0xc0c1', dat.chain, size + 2, dat.byte - (size + 1) )
		TempLog(20,"CRCA reading at " + str(dat.byte - (size + 1)))
		dat.byte = dat.byte + 1
		dat.bit = 0

	else:
		crc2 = bit.read_crc8 ('0xc0c1', dat.chain, size + 2, dat.byte - (size + 2) )
		TempLog(20,"CRCB reading at " + str(dat.byte - (size + 2)))

	crc = bit.readwithlog("RS",dat, "CRC",2)	
	if (crc != crc2):
		TempLog(20,'CRC Mismatch ' + str(crc2) + " " + str(crc) + '\n\n')
		return False
	else:
		TempLog(20,'CRC Match\n\n')
		return True
		
def decode_proxy_graphic(gpdwg,dat): # TODO: Need to be worked.
	if Picture_Size < 210210:
		dat.byte = int(dat.byte+int(Picture_Size))
	else:
		TempLog(10,"Picture_Size Failure")
		return False

def decode_eed(gpdwg,dat): # TODO: Need to be reworked.
	length = gpdwg.objects['temp'].xdatalength
	i=0
	while(length!=0):
		if length > 1000 or length < 0 :
			TempLog(10,"Incorrect length of xdata")
			return False
		Temp_H2=bit.readwithlog('H',dat,"Temp_H2",4)
		if isinstance(Temp_H2,basestring):
			TempLog(10,"Xdata Error reading Header")
			return False
			'''
		if Temp_H2.code != 0:
			TempLog(10,"Xdata Header Code is not 0")
			return False
			'''
		if Temp_H2.value == 0:
			TempLog(10,"Xdata Header Value is 0")
			return False
		bit.shift_pos(dat,int(length * 8))
		Temp_Byte=int(dat.byte)
		bit.shift_pos(dat,int(length * -8))
		gpdwg.objects['temp'].xdata={}
		gpdwg.objects['temp'].xdata[i]={}
		gpdwg.objects['temp'].xdata[i]['handle']=Temp_H2
		while (dat.byte < Temp_Byte):
			Gcode=bit.readwithlog('RC',dat,"Gcode "+str(i),4)
			if Gcode == 0:
				if dat.version <= 2004:
					length2=bit.readwithlog('RC',dat,"Value "+str(i),4)
					bit.read_RS(dat)
					bit.shift_pos(dat,length2 * 8)
					gpdwg.objects['temp'].xdata[i][Gcode]=length2
			elif Gcode == 2:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
			elif Gcode in [3,5]:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.shift_pos(dat,8 * 8)	
			elif Gcode in [11,12,13,24]:
				gpdwg.objects['temp'].xdata[i][Gcode][1]=bit.readwithlog('RD',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode][2]=bit.readwithlog('RD',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode][3]=bit.readwithlog('RD',dat,"Value "+str(i),4)
			elif Gcode in [40,41,42]:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RD',dat,"Value "+str(i),4)
			elif Gcode ==70:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RS',dat,"Value "+str(i),4)
			elif Gcode ==71:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RL',dat,"Value "+str(i),4)
			else:
				TempLog(20,"Unknown Xdata Group Code")
				return False
		dat.byte = int(Temp_Byte)
		i+=1
		length=bit.readwithlog("BS",dat,"Length",3)


def decode_common_entity_data(gpdwg,dat):
	if dat.version >= 2000: Obj_size = bit.readwithlog("RL",dat,"Bsize",3)
	Temp_H=bit.readwithlog("H",dat,"Handle",3)
	if CheckHandle(Temp_H): gpdwg.objects['temp'].handle=Temp_H
	gpdwg.objects['temp'].xdatalength=bit.readwithlog("BS",dat,"Length",3)
	if not decode_EED(gpdwg,dat): return False
	Graphic_Exist=bit.readwithlog("B",dat,"Graphic Exist",2)
	if Graphic_Exist:
		Graphic_Size=bit.readwithlog("RL",dat,"PicSize",2)
	else:
		Graphic_Size=0
	if not decode_Proxy_Graphic(gpdwg,dat): return False
	gpdwg.objects['temp'].Graphic_Exist=bool(Graphic_Exist)
	gpdwg.objects['temp'].Graphic_Size=Graphic_Size
	if dat.version <= 14: 
		gpdwg.objects['temp'].object_size=bit.readwithlog("RL",dat,"Object Size",2)
	Entmode=bit.readwithlog("BB",dat,"Entity Mode",2)
	if Entmode == 3:
		TempLog(10,"Incorrect Entmode")
		return False
	gpdwg.objects['temp'].Entmode=Entmode
	NumReactors=int(bit.readwithlog("BL",dat,"NumReactors",2))
	if NumReactors > 0x001000:
		TempLog(10,"Incorrect NumReactors")
		return False
	gpdwg.objects['temp'].NumReactors=NumReactors
	if dat.version >= 2004: gpdwg.objects['temp'].XDic_Missing=bool(bit.readwithlog("B",dat,"XDic Missing Flag",2))
	if dat.version >= 2013: gpdwg.objects['temp'].DS_Binary=bool(bit.readwithlog("B",dat,"DS Binary Flag",2))
	if dat.version <= 14: gpdwg.objects['temp'].Isbylayerlt=bool(bit.readwithlog("B",dat,"Is bylayer linetype",2))
	gpdwg.objects['temp'].NoLinks=bool(bit.readwithlog("B",dat,"NoLink",2))
	gpdwg.objects['temp'].EntColor=bit.readwithlog("CMC",dat,"Color",2)
	gpdwg.objects['temp'].LineTypeScale=bit.readwithlog("BD",dat,"LTScale",2)
	if gpdwg.objects['temp'].LineTypeScale > 1.0e6 or gpdwg.objects['temp'].LineTypeScale < 1.0e-6:
		TempLog(10,"LineTypeScale Error")
		return False
	if dat.version >= 2000:
		gpdwg.objects['temp'].LineTypeFlag=bit.readwithlog("BB",dat,"LTFlag",2)
		gpdwg.objects['temp'].PlotStyleFlag=bit.readwithlog("BB",dat,"PSFlag",2)
	if dat.version >=2007:
		gpdwg.objects['temp'].MaterialFlag=bit.readwithlog("BB",dat,"Material Flag",2)
		gpdwg.objects['temp'].ShadowFlag=bit.readwithlog("BB",dat,"Shadow Flag",2)
	gpdwg.objects['temp'].Invisible=bit.readwithlog("BS",dat,"Invisible",2)
	if dat.version >= 2000: gpdwg.objects['temp'].LineWeight=bit.readwithlog("RC",dat,"Lweight",2)
	return True

def decode_common_entity_handle_data(gpdwg,dat):
	if gpdwg.objects['temp'].Entmode==0:
		gpdwg.objects['temp'].subentry=bit.readwithlog("H",dat,"subentry",2)
	if gpdwg.objects['temp'].NumReactors>0:
		gpdwg.objects['temp'].reactors={}
		for Num in range(0,gpdwg.objects['temp'].NumReactors-1):
			gpdwg.objects['temp'].reactors[Num]=bit.readwithlog("H",dat,"reactors",2)
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog("H",dat,"xdicobjhandle",2)
	if dat.version <= 14:
		gpdwg.objects['temp'].layer=bit.readwithlog("H",dat,"Layer",2)
		if gpdwg.objects['temp'].Isbylayerlt: gpdwg.objects['temp'].LineType=bit.readwithlog("H",dat,"LineType",2)
	if dat.version <= 2000:
		if not gpdwg.objects['temp'].NoLinks:
			gpdwg.objects['temp'].prvEntity=bit.readwithlog("H",dat,"Previous Entry",2)
			gpdwg.objects['temp'].nxtEntity=bit.readwithlog("H",dat,"Next Entry",2)
	if dat.version >= 2004:
		gpdwg.objects['temp'].color_handle=bit.readwithlog("H",dat,"Color handle",2)
	if dat.version >= 2000:
		gpdwg.objects['temp'].layer=bit.readwithlog("H",dat,"Layer",2)
		if gpdwg.objects['temp'].LineTypeFlag ==3:
			gpdwg.objects['temp'].LineType=bit.readwithlog("H",dat,"LineType",2)
	if dat.version >= 2007:
		if gpdwg.objects['temp'].MaterialFlag==3:
			gpdwg.objects['temp'].Material=bit.readwithlog("H",dat,"Material",2)
	if dat.version >= 2000:
		if gpdwg.objects['temp'].PlotStyleFlag ==3:
			gpdwg.objects['temp'].PlotStyle=bit.readwithlog("H",dat,"PlotStyle",2)
#	if dat.version >= 2010: TODO: Need to workout.
	return True	


def decode_common_non_entity_data(gpdwg,dat):
	if dat.version >= 2000: Obj_size = bit.readwithlog("RL",dat,"Bsize",3)
	Temp_H=bit.readwithlog("H",dat,"Handle",3)
	if CheckHandle(Temp_H): gpdwg.objects['temp'].handle=Temp_H
	gpdwg.objects['temp'].xdatalength=bit.readwithlog("BS",dat,"Length",3)
	if not decode_EED(gpdwg,dat): return False
	if dat.version <= 14: 
		gpdwg.objects['temp'].object_size=bit.readwithlog("RL",dat,"Object Size",2)
		gpdwg.objects['temp'].reactors_attached=bit.readwithlog("BL",dat,"Object Size",2)
	if dat.version >= 2004: 
		gpdwg.objects['temp'].no_xdic=bool(bit.readwithlog("B",dat,"No XDictionary",2))
	if dat.version >= 2013: 
		gpdwg.objects['temp'].binary_data=bool(bit.readwithlog("B",dat,"Binary Data",2))


def decode_hatch_path(dat):
	Output=libgpdwg.hatch_path()
	Output.path_flag=bit.readwithlog2("BL",dat,"Path Type Status")
	if (not(int(Output.path_flag) & 2)):
		Output.num_path_segments=bit.readwithlog2("BL",dat,"Num of path Segments")
		Output.path_segments=[]
		for x in range(int(Output.num_path_segments)):
			PathTypeStatus=bit.readwithlog2("RC",dat,"Path Type Status")
			if PathTypeStatus == 1:
				Line=libgpdwg.hatch_path_line()
				Line.first_endpoint=bit.readwithlog2("2RD",dat,"First Endpoint")
				Line.second_endpoint=bit.readwithlog2("2RD",dat,"Second Endpoint")
				Output.path_segments.append(Line)
			elif PathTypeStatus == 2:
				Arc=libgpdwg.hatch_path_arc()
				Arc.center=bit.readwithlog2("2RD",dat,"Center")
				Arc.radius=bit.readwithlog2("BD",dat,"Radius")
				Arc.start_angle=bit.readwithlog2("BD",dat,"Start Angle")
				Arc.end_angle=bit.readwithlog2("BD",dat,"End Angle")
				Arc.isccw=bool(bit.readwithlog2("B",dat,"Clockwise"))
				Output.path_segments.append(Arc)
			elif PathTypeStatus == 3:
				ElArc=libgpdwg.hatch_path_elarc()
				ElArc.center=bit.readwithlog2("2RD",dat,"Center")
				ElArc.endpoint=bit.readwithlog2("2RD",dat,"Endpoint of major Axis")
				ElArc.maj_min_ratio=bit.readwithlog2("BD",dat,"Major by Minor Ratio")
				ElArc.start_angle=bit.readwithlog2("BD",dat,"Start Angle")
				ElArc.end_angle=bit.readwithlog2("BD",dat,"End Angle")
				ElArc.isccw=bool(bit.readwithlog2("B",dat,"Clockwise"))
				Output.path_segments.append(ElArc)
			elif PathTypeStatus == 4:
				Spline=libgpdwg.hatch_path_spline()
				Spline.degree=bit.readwithlog2("BL",dat,"Degree")
				Spline.rational=bool(bit.readwithlog2("B",dat,"Rational"))
				Spline.periodic=bool(bit.readwithlog2("B",dat,"Periodic"))
				Num_knots=bit.readwithlog2("BL",dat,"Num of Knots")
				Num_clt_points=bit.readwithlog2("BL",dat,"Num of Points")
				Spline.knots=[]
				for x in range(Num_knots):
					Spline.knots.append(bit.readwithlog2("BD",dat,"Knot value "+str(x)))
				Spline.clt_points=[]
				Spline.clt_points_weight=[]
				for x in range(Num_clt_points):
					Spline.clt_points.append(bit.readwithlog2("2RD",dat,"Control Point "+str(x)))
					if Spline.rational:
						Spline.clt_points_weight.append(bit.readwithlog2("BD",dat,"Control Point "+str(x)))
	else:
		Output.bulgespresent=bool(bit.readwithlog2("B",dat,"Bulge Present"))
		Output.closed=bool(bit.readwithlog2("B",dat,"Closed"))
		Output.num_path_segments=bit.readwithlog2("BL",dat,"Num of path Segments")
		Output.path_points=[]
		Output.path_points_bulge=[]
		for x in range(int(Output.num_path_segments)):
			Output.path_points.append(bit.readwithlog2("2RD",dat,"Polyline Point "+str(x)))
			if Output.bulgespresent:
				Output.path_points_bulge.append(bit.readwithlog2("BD",dat,"Bulge for Point " +str(x)))
	Output.num_boundaryobj_handles=bit.readwithlog2("BL",dat,"Num BoundaryObj Handles")
	return Output


def decode_hatch_defination_lines(dat):
	Output=libgpdwg.hatch_defination_lines()
	Output.angle=bit.readwithlog2("BD",dat,"Defination Line Angle")
	Output.point=bit.readwithlog2("2BD",dat,"Pattern origin point")
	Output.offset=bit.readwithlog2("2BD",dat,"Pattern Line Offset")
	num_dashes=bit.readwithlog2("BS",dat,"Num of Dash Items")
	Output.dash_lengths=[]
	for x in range(int(num_dashes)):
		Output.dash_lengths.append(bit.readwithlog2("BD",dat,"Dash Lengths"))
	return Output



def decode_HATCH(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_hatch()
	TempLog(20,'HATCH Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version >= 2004:
		gpdwg.objects['temp'].gradient_fill_flag=bit.readwithlog2('BL',dat,'gradient_fill_flag')
		gpdwg.objects['temp'].reserved=bit.readwithlog2('BL',dat,'reserved')
		gpdwg.objects['temp'].gradient_angle=bit.readwithlog2('BD',dat,'gradient_angle')
		gpdwg.objects['temp'].gradient_shift=bit.readwithlog2('BD',dat,'gradient_shift')
		gpdwg.objects['temp'].single_color_grad=bit.readwithlog2('BL',dat,'single_color_grad')
		gpdwg.objects['temp'].gradient_tint=bit.readwithlog2('BD',dat,'gradient_tint')
		gpdwg.objects['temp'].num_gradient_colors=bit.readwithlog2('BL',dat,'num_gradient_colors')
		for i in range(int(gpdwg.objects['temp'].num_gradient_colors)):
			add_to_list(gpdwg.objects['temp'], 'unknown_double', bit.readwithlog2('BD', dat,' unknown_double '+str(i)))
			add_to_list(gpdwg.objects['temp'], 'unknown_short', bit.readwithlog2('BS', dat,' unknown_short '+str(i)))
			add_to_list(gpdwg.objects['temp'], 'rgb_color', bit.readwithlog2('BL', dat,' rgb_color '+str(i)))
			add_to_list(gpdwg.objects['temp'], 'ignored_color_byte', bit.readwithlog2('RC', dat,' ignored_color_byte '+str(i)))
		gpdwg.objects['temp'].gradient_name=bit.readwithlog2('RC',dat,'gradient_name')
	gpdwg.objects['temp'].z_coord=bit.readwithlog2('BD',dat,'z_coord')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].solid_fill=bit.readwithlog2('B',dat,'solid_fill')
	gpdwg.objects['temp'].associative=bit.readwithlog2('B',dat,'associative')
	gpdwg.objects['temp'].numpaths=bit.readwithlog2('BL',dat,'numpaths')
	for i in range(int(gpdwg.objects['temp'].numpaths)):
		logger.debug("Path No "+str(i))
		add_to_list(gpdwg.objects['temp'], 'paths', decode_hatch_path(dat))
	logger.debug("Total "+str(i+1)+" paths finished.")
	gpdwg.objects['temp'].style=bit.readwithlog2('BS',dat,'style')
	gpdwg.objects['temp'].patterntype=bit.readwithlog2('BS',dat,'patterntype')
	if not gpdwg.objects['temp'].solid_fill:
		gpdwg.objects['temp'].angle=bit.readwithlog2('BD',dat,'angle')
		gpdwg.objects['temp'].scale_or_spacing=bit.readwithlog2('BD',dat,'scale_or_spacing')
		gpdwg.objects['temp'].double_hatch=bit.readwithlog2('B',dat,'double_hatch')
		gpdwg.objects['temp'].num_defination_lines=bit.readwithlog2('BS',dat,'num_defination_lines')
		for x in range(int(gpdwg.objects['temp'].num_defination_lines)):
			logger.debug("Defination Line No "+str(x))
			add_to_list(gpdwg.objects['temp'], 'defination_lines', decode_hatch_defination_lines(dat))
		logger.debug("Total "+str(x+1)+" defination lines finished")
	gpdwg.objects['temp'].pixelsize=[]
	PixelSize=False
	for paths in gpdwg.objects['temp'].paths:
		if (int(paths.path_flag) & 4):
			PixelSize=True
	if PixelSize:
		gpdwg.objects['temp'].pixelsize.append(bit.readwithlog2('BD',dat,'Pixel Size'))
	num_seed_points=bit.readwithlog2('BL',dat,'Num of Seed Points')
	gpdwg.objects['temp'].seed_point=[]
	for x in range(int(num_seed_points)):
		gpdwg.objects['temp'].seed_point.append(bit.readwithlog2('2RD',dat,'Seed Point'))
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].boundaryobj_handles=[]
	for paths in gpdwg.objects['temp'].paths:
		for x in range(int(paths.num_boundaryobj_handles)):
			gpdwg.objects['temp'].boundaryobj_handles.append(bit.readwithlog2('H',dat,'Boundary handle '+str(x)))

	TempLog(20,'HATCH End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)