
def decode_ACDBDICTIONARYWDFLT(gpdwg,dat):
	return False if not decode_DICTIONARYWDFLT(gpdwg,dat) else True

def decode_SUN_old(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	if gpdwg.header['ACADVER'] >= 2000:
		bsize = bit.readwithlog("RL",dat,"Bsize",3)
	Temp_H=bit.readwithlog("H",dat,"Handle",3)
	logger.info("decode_SUN need to be worked out. Shifting position by "+ str(Obj_Size - 9) +" bytes.")
	bit.shift_pos(dat,int((Obj_Size - 9) * 8))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VISUALSTYLE_old(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	if gpdwg.header['ACADVER'] >= 2000:
		bsize = bit.readwithlog("RL",dat,"Bsize",3)
	Temp_H=bit.readwithlog("H",dat,"Handle",3)
	logger.info("decode_VISUALSTYLE need to be worked out. Shifting position by "+ str(Obj_Size - 9) +" bytes.")
	bit.shift_pos(dat,int((Obj_Size - 9) * 8))
	return Check_Obj_CRC(dat,Obj_Size)

def TempLog(intTemp,strMessage):
	logger.debug(strMessage)

def Check_Obj_CRC(dat,size):
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

def decode_entity(gpdwg,dat):
	TempLog(20,"\tEntity Start")
	if not decode_object(gpdwg,dat): return False
	Picture_Exist=bit.readwithlog("B",dat,"PicExist",2)
	if Picture_Exist:
		Picture_Size=bit.readwithlog("RL",dat,"PicSize",2)
	else:
		Picture_Size=0
	if Picture_Size < 210210:
		dat.byte = int(dat.byte+int(Picture_Size))
	else:
		TempLog(10,"Picture_Size Failure")
		return False
	gpdwg.objects['temp'].Picture_Exist=bool(Picture_Exist)
	gpdwg.objects['temp'].Picture_Size=Picture_Size
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
	gpdwg.objects['temp'].NoLinks=bool(bit.readwithlog("B",dat,"NoLink",2))
	gpdwg.objects['temp'].EntColor=bit.readwithlog("CMC",dat,"Color",2)
	gpdwg.objects['temp'].LineTypeScale=bit.readwithlog("BD",dat,"LTScale",2)
	if gpdwg.objects['temp'].LineTypeScale > 1.0e6 or gpdwg.objects['temp'].LineTypeScale < 1.0e-6:
		TempLog(10,"LineTypeScale Error")
		return False
	gpdwg.objects['temp'].LineTypeFlag=bit.readwithlog("BB",dat,"LTFlag",2)
	gpdwg.objects['temp'].PlotStyleFlag=bit.readwithlog("BB",dat,"PSFlag",2)
	gpdwg.objects['temp'].Invisible=bit.readwithlog("BS",dat,"Invisible",2)
	gpdwg.objects['temp'].LineWeight=bit.readwithlog("RC",dat,"Lweight",2)
	TempLog(20,"\tEntity End")
	return True

def decode_non_entity(gpdwg,dat):
	TempLog(20,"\tNon-Entity Start")
	if not decode_object(gpdwg,dat): return False
	NumReactors=int(bit.readwithlog("BL",dat,"NumReactors",2))
	if NumReactors > 0x001000:
		TempLog(10,"Incorrect NumReactors")
		return False
	gpdwg.objects['temp'].num_reactors=NumReactors
	TempLog(20,"\tNon-Entity End")
	return True

def decode_entity_handles(gpdwg,dat):
	TempLog(20,"\tEntity Handle Start")
	if gpdwg.objects['temp'].Entmode==0:
		gpdwg.objects['temp'].subentry=bit.readwithlog("H",dat,"subentry",2)
	if gpdwg.objects['temp'].NumReactors>0:
		gpdwg.objects['temp'].reactors={}
		for Num in range(gpdwg.objects['temp'].NumReactors):
			gpdwg.objects['temp'].reactors[Num]=bit.readwithlog("H",dat,"reactors",2)
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog("H",dat,"xdicobjhandle",2)
	if not gpdwg.objects['temp'].NoLinks:
		gpdwg.objects['temp'].prvEntity=bit.readwithlog("H",dat,"Previous Entry",2)
		gpdwg.objects['temp'].nxtEntity=bit.readwithlog("H",dat,"Next Entry",2)
	gpdwg.objects['temp'].layer=bit.readwithlog("H",dat,"Layer",2)
	if gpdwg.objects['temp'].LineTypeFlag ==3:
		gpdwg.objects['temp'].LineType=bit.readwithlog("H",dat,"LineType",2)
	if gpdwg.objects['temp'].PlotStyleFlag ==3:
		gpdwg.objects['temp'].PlotStyle=bit.readwithlog("H",dat,"PlotStyle",2)
	TempLog(20,"\tEntity Handle End")
	return True		

def decode_common_dimension(gpdwg,dat):
	TempLog(20,"\tCommon Dimension Start")
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("3BD",dat,"Extrusion",2)
	gpdwg.objects['temp'].Text_Midpt=bit.readwithlog("2RD",dat,"Text Midpt",2)
	gpdwg.objects['temp'].Elevation=bit.readwithlog("BD",dat,"Elevation",2)
	gpdwg.objects['temp'].Flags=bit.readwithlog("RC",dat,"Flags",2)
	gpdwg.objects['temp'].User_Text=bit.readwithlog("TV",dat,"User_Text",2)
	gpdwg.objects['temp'].Text_Rot=bit.readwithlog("BD",dat,"Text_Rot",2)
	gpdwg.objects['temp'].Horiz_Dir=bit.readwithlog("BD",dat,"Horiz_Dir",2)
	gpdwg.objects['temp'].Ins_Scale_X=bit.readwithlog("BD",dat,"Ins_Scale_X",2)
	gpdwg.objects['temp'].Ins_Scale_Y=bit.readwithlog("BD",dat,"Ins_Scale_Y",2)
	gpdwg.objects['temp'].Ins_Scale_Z=bit.readwithlog("BD",dat,"Ins_Scale_Z",2)
	gpdwg.objects['temp'].Ins_Rot=bit.readwithlog("BD",dat,"Ins_Rot",2)
	gpdwg.objects['temp'].Attachment_Point=bit.readwithlog("BS",dat,"Attachment_Point",2)
	gpdwg.objects['temp'].Linespacing_Style=bit.readwithlog("BS",dat,"Linespacing_Style",2)
	gpdwg.objects['temp'].Linespacing_Factor=bit.readwithlog("BD",dat,"Linespacing_Factor",2)
	gpdwg.objects['temp'].Actual_Measurement=bit.readwithlog("BD",dat,"Actual_Measurement",2)
	gpdwg.objects['temp'].Pt12=bit.readwithlog("2RD",dat,"Point_12",2)
	TempLog(20,"\tCommon Dimension End")

def decode_object(gpdwg,dat):
	TempLog(20,"\t\tObject Start")
	if gpdwg.header['ACADVER'] >= 2000:
		bsize = bit.readwithlog("RL",dat,"Bsize",3)
	Temp_H=bit.readwithlog("H",dat,"Handle",3)
	if isinstance(Temp_H,str):
		TempLog(10,"Error reading Header")
		return False
		
	if Temp_H.code != 0:
		TempLog(10,"Header Code is not 0")
		return False
	if Temp_H.value == 0:
		TempLog(10,"Header Value is 0")
		return False
	
	gpdwg.objects['temp'].handle=Temp_H
	length=bit.readwithlog("BS",dat,"Length",3)
	gpdwg.objects['temp'].xdatalength=length
	i=0
	while(length!=0):
		if length > 1000 or length < 0 :
			TempLog(10,"Incorrect length of xdata")
			return False
		Temp_H2=bit.readwithlog('H',dat,"Temp_H2",4)
		if isinstance(Temp_H2,str):
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
		'''
		while (dat.byte < Temp_Byte):
			Gcode=bit.readwithlog('RC',dat,"G1code("+str(i)+")",4)
			if Gcode == 0:
				if gpdwg.header['ACADVER'] <= 2004:
					length2=bit.readwithlog('RC',dat,"Value "+str(i),4)
					bit.read_RS(dat)
					bit.shift_pos(dat,length2 * 8)
					gpdwg.objects['temp'].xdata[i][Gcode]=length2
			elif Gcode == 2:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
			elif Gcode in [3,5]:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)	
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RC',dat,"Value "+str(i),4)
				#gpdwg.objects['temp'].xdata[i][Gcode]=bit.shift_pos(dat,8 * 8)	
			elif Gcode in [11,12,13]:
				#gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('3RD',dat,"Value "+str(i),4)
				
				gpdwg.objects['temp'].xdata[i][Gcode]={}
				gpdwg.objects['temp'].xdata[i][Gcode][1]=bit.readwithlog('RD',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode][2]=bit.readwithlog('RD',dat,"Value "+str(i),4)
				gpdwg.objects['temp'].xdata[i][Gcode][3]=bit.readwithlog('RD',dat,"Value "+str(i),4)
			elif Gcode in [14]:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('3RD',dat,"Value "+str(i),4)

			elif Gcode in [24,111]:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('3RD',dat,"Value "+str(i),4)
				
			elif Gcode in [40,41,42,132]:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RD',dat,"Value "+str(i),4)
			elif Gcode ==70:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RS',dat,"Value "+str(i),4)
			elif Gcode ==71:
				gpdwg.objects['temp'].xdata[i][Gcode]=bit.readwithlog('RL',dat,"Value "+str(i),4)
			else:
				TempLog(20,"Unknown Xdata Group Code " +str(Gcode))
				return False
		'''
		dat.byte = int(Temp_Byte)
		i+=1
		length=bit.readwithlog("BS",dat,"Length-",3)
	TempLog(20,"\t\tObject End")
	return True

def decode_CLASS_OBJECTS(gpdwg,dat,Obj_Type):
	ClassObjeName=gpdwg.classes[int(Obj_Type)-500].CLASSDXFNAME
	logger.debug(ClassObjeName +"\t" + str(Obj_Type))
	return eval("decode_"+ClassObjeName+"(gpdwg,dat)")
	







def add(gpdwg,dat):
	global Temp
	gpdwg.objects['temp']={}
	Byte1=dat.byte
	Bit1=dat.bit
	TempLog(20,"\n------------------New------------------\nObject Read \t"+str(Byte1))
	Obj_Size=bit.readwithlog("MS",dat,"Object Size",1)
	TempLog(20,"Object End \t"+str(Obj_Size+dat.byte))
	gpdwg.objects['temp']['size']=Obj_Size
	Byte2=dat.byte
	Bit2=dat.bit
	Obj_Type=bit.readwithlog("BS",dat,"Object Type",1)
	#log.LogOnOff=True
	#TempLog(20,str(Byte1) + "\t" + str(Bit1) + "\tObject Size " + "\t" + str(Obj_Size) + "\t" + str(Byte2) + "\t" + str(Bit2) + "\tType " + str(Obj_Type))
	##log.LogOnOff=False

	#Temp=Temp+"\t"+str(int(Obj_Type))
	if Obj_Type == 0x00:
		if decode_UNUSED(gpdwg,dat,):
			return True
		else:
			return False
		#return False if not decode_UNUSED(gpdwg,dat) else True
	elif Obj_Type == 0x01: # 1
		return False if not decode_TEXT(gpdwg,dat) else True
	elif Obj_Type == 0x02: # 2
		return False if not decode_ATTRIB(gpdwg,dat) else True
	elif Obj_Type == 0x03: # 3
		return False if not decode_ATTDEF(gpdwg,dat) else True
	elif Obj_Type == 0x04: # 4
		return False if not decode_BLOCK(gpdwg,dat) else True
	elif Obj_Type == 0x05: # 5
		return False if not decode_ENDBLK(gpdwg,dat) else True
	elif Obj_Type == 0x06: # 6
		return False if not decode_SEQEND(gpdwg,dat) else True
	elif Obj_Type == 0x07: # 7
		return False if not decode_INSERT(gpdwg,dat) else True
	elif Obj_Type == 0x08: # 8
		return False if not decode_MINSERT(gpdwg,dat) else True
	elif Obj_Type == 0x09: # 9
		return False if not decode_UNKNOWN(gpdwg,dat) else True
	elif Obj_Type == 0x0a: # 10
		return False if not decode_VERTEX_2D(gpdwg,dat) else True
	elif Obj_Type == 0x0b: # 11
		return False if not decode_VERTEX_3D(gpdwg,dat) else True
	elif Obj_Type == 0x0c: # 12
		return False if not decode_VERTEX_MESH(gpdwg,dat) else True
	elif Obj_Type == 0x0d: # 13
		return False if not decode_VERTEX_PFACE(gpdwg,dat) else True
	elif Obj_Type == 0x0e: # 14
		return False if not decode_VERTEX_PFACE_FACE(gpdwg,dat) else True
	elif Obj_Type == 0x0f: # 15
		return False if not decode_POLYLINE_2D(gpdwg,dat) else True
	elif Obj_Type == 0x10: # 16
		return False if not decode_POLYLINE_3D(gpdwg,dat) else True
	elif Obj_Type == 0x11: # 17
		return False if not decode_ARC(gpdwg,dat) else True
	elif Obj_Type == 0x12: # 18
		return False if not decode_CIRCLE(gpdwg,dat) else True
	elif Obj_Type == 0x13: # 19
		return False if not decode_LINE(gpdwg,dat) else True
	elif Obj_Type == 0x14: # 20
		return False if not decode_DIMENSION_ORDINATE(gpdwg,dat) else True
	elif Obj_Type == 0x15: # 21
		return False if not decode_DIMENSION_LINEAR(gpdwg,dat) else True
	elif Obj_Type == 0x16: # 22
		return False if not decode_DIMENSION_ALIGNED(gpdwg,dat) else True
	elif Obj_Type == 0x17: # 23
		return False if not decode_DIMENSION_ANG3PT(gpdwg,dat) else True
	elif Obj_Type == 0x18: # 24
		return False if not decode_DIMENSION_ANG2LN(gpdwg,dat) else True
	elif Obj_Type == 0x19: # 25
		return False if not decode_DIMENSION_RADIUS(gpdwg,dat) else True
	elif Obj_Type == 0x1a: # 26
		return False if not decode_DIMENSION_DIAMETER(gpdwg,dat) else True
	elif Obj_Type == 0x1b: # 27
		return False if not decode_POINT(gpdwg,dat) else True
	elif Obj_Type == 0x1c: # 28
		return False if not decode_3D_FACE(gpdwg,dat) else True
	elif Obj_Type == 0x1d: # 29
		return False if not decode_POLYLINE_PFACE(gpdwg,dat) else True
	elif Obj_Type == 0x1e: # 30
		return False if not decode_POLYLINE_MESH(gpdwg,dat) else True
	elif Obj_Type == 0x1f: # 31
		return False if not decode_SOLID(gpdwg,dat) else True
	elif Obj_Type == 0x20: # 32
		return False if not decode_TRACE(gpdwg,dat) else True
	elif Obj_Type == 0x21: # 33
		return False if not decode_SHAPE(gpdwg,dat) else True
	elif Obj_Type == 0x22: # 34
		return False if not decode_VIEWPORT(gpdwg,dat) else True
	elif Obj_Type == 0x23: # 35
		return False if not decode_ELLIPSE(gpdwg,dat) else True
	elif Obj_Type == 0x24: # 36
		return False if not decode_SPLINE(gpdwg,dat) else True
	elif Obj_Type == 0x25: # 37
		return False if not decode_REGION(gpdwg,dat) else True
	elif Obj_Type == 0x26: # 38
		return False if not decode_3DSOLID(gpdwg,dat) else True
	elif Obj_Type == 0x27: # 39
		return False if not decode_BODY(gpdwg,dat) else True
	elif Obj_Type == 0x28: # 40
		return False if not decode_RAY(gpdwg,dat) else True
	elif Obj_Type == 0x29: # 41
		return False if not decode_XLINE(gpdwg,dat) else True
	elif Obj_Type == 0x2a: # 42
		return False if not decode_DICTIONARY(gpdwg,dat) else True
	elif Obj_Type == 0x2b: # 43
		return False if not decode_OLEFRAME(gpdwg,dat) else True
	elif Obj_Type == 0x2c: # 44
		return False if not decode_MTEXT(gpdwg,dat) else True
	elif Obj_Type == 0x2d: # 45
		return False if not decode_LEADER(gpdwg,dat) else True
	elif Obj_Type == 0x2e: # 46
		return False if not decode_TOLERANCE(gpdwg,dat) else True
	elif Obj_Type == 0x2f: # 47
		return False if not decode_MLINE(gpdwg,dat) else True
	elif Obj_Type == 0x30: # 48
		return False if not decode_BLOCK_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x31: # 49
		return False if not decode_BLOCK_HEADER(gpdwg,dat) else True
	elif Obj_Type == 0x32: # 50
		return False if not decode_LAYER_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x33: # 51
		return False if not decode_LAYER(gpdwg,dat) else True
	elif Obj_Type == 0x34: # 52
		return False if not decode_SHAPEFILE_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x35: # 53
		return False if not decode_SHAPEFILE(gpdwg,dat) else True
	elif Obj_Type == 0x36: # 54
		return False if not decode_UNKNOWN(gpdwg,dat) else True
	elif Obj_Type == 0x37: # 55
		return False if not decode_UNKNOWN(gpdwg,dat) else True
	elif Obj_Type == 0x38: # 56
		return False if not decode_LTYPE_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x39: # 57
		return False if not decode_LTYPE(gpdwg,dat) else True
	elif Obj_Type == 0x3a: # 58
		return False if not decode_UNKNOWN(gpdwg,dat) else True
	elif Obj_Type == 0x3b: # 59
		return False if not decode_UNKNOWN(gpdwg,dat) else True
	elif Obj_Type == 0x3c: # 60
		return False if not decode_VIEW_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x3d: # 61
		return False if not decode_VIEW(gpdwg,dat) else True
	elif Obj_Type == 0x3e: # 62
		return False if not decode_UCS_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x3f: # 63
		return False if not decode_UCS(gpdwg,dat) else True
	elif Obj_Type == 0x40: # 64
		return False if not decode_VPORT_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x41: # 65
		return False if not decode_VPORT(gpdwg,dat) else True
	elif Obj_Type == 0x42: # 66
		return False if not decode_APPID_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x43: # 67
		return False if not decode_APPID(gpdwg,dat) else True
	elif Obj_Type == 0x44: # 68
		return False if not decode_DIMSTYLE_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x45: # 69
		return False if not decode_DIMSTYLE(gpdwg,dat) else True
	elif Obj_Type == 0x46: # 70
		return False if not decode_VP_ENT_HDR_CONTROL(gpdwg,dat) else True
	elif Obj_Type == 0x47: # 71
		return False if not decode_VP_ENT_HDR(gpdwg,dat) else True
	elif Obj_Type == 0x48: # 72
		return False if not decode_GROUP(gpdwg,dat) else True
	elif Obj_Type == 0x49: # 73
		return False if not decode_MLINESTYLE(gpdwg,dat) else True
	elif Obj_Type == 0x4a: # 74
		return False if not decode_OLE2FRAME(gpdwg,dat) else True
	elif Obj_Type == 0x4b: # 75
		return False if not decode_DUMMY(gpdwg,dat) else True
	elif Obj_Type == 0x4c: # 76
		return False if not decode_LONG_TRANSACTION(gpdwg,dat) else True
	elif Obj_Type == 0x4d: # 77
		return False if not decode_LWPLINE(gpdwg,dat) else True
	elif Obj_Type == 0x4e: # 78
		return False if not decode_HATCH(gpdwg,dat) else True
	elif Obj_Type == 0x4f: # 79
		return False if not decode_XRECORD(gpdwg,dat) else True
	elif Obj_Type == 0x50: # 80
		return False if not decode_PLACEHOLDER(gpdwg,dat) else True
	elif Obj_Type == 0x51: # 81
		return False if not decode_VBA_PROJECT(gpdwg,dat) else True
	elif Obj_Type == 0x52: # 82
		return False if not decode_LAYOUT(gpdwg,dat) else True
	elif Obj_Type == 0x1f2:  # 498
		return False if not decode_ACAD_PROXY_ENTITY(gpdwg,dat) else True
	elif Obj_Type == 0x1f3: # 499
		return False if not decode_ACAD_PROXY_OBJECT(gpdwg,dat) else True
	elif Obj_Type > 0x1f3 and Obj_Type <=  0x1f3+gpdwg.classcount:
		return False if not decode_CLASS_OBJECTS(gpdwg,dat,Obj_Type) else True
	else:
		Obj_beyond_range(gpdwg,dat,Obj_Type);
		return False

def Obj_beyond_range(gpdwg,dat,Obj_Type):
	logger.error("Out of range object with type "+str(Obj_Type)+" found.")
	"""
	global Temp
	if Obj_Type - 500 > gpdwg.classes[count]:
		pass
		#TempLog(9,Temp+"\t\t+range")
	elif Obj_Type - 500 < 0:
		pass
		#TempLog(9,Temp+"\t\t-range")
	else:
		pass
		#Class_Obj_Type=gpdwg.classes[(Obj_Type - 500)]['dxfname']
		#TempLog(9,Temp+"\t"+Class_Obj_Type)
	"""



def decode_UNUSED(gpdwg,dat):
	
	
	#gpdwg.objects['temp']['type']="UNUSED"
	global Temp
	#TempLog(9,Temp+"	"+"UNUSED")
	#if not decode_entity(gpdwg,dat): return False
	#TempLog(19,"Scanned Unused")
	return False
		
def decode_Common_TEXT(gpdwg,dat):
	DataFlag=bit.readwithlog("RC",dat,"DataFlag",1)
	gpdwg.objects['temp'].DataFlag=DataFlag
	if not DataFlag & 0x01:
		gpdwg.objects['temp'].Elevation=bit.readwithlog("RD",dat,"Elevation",1)
	gpdwg.objects['temp'].InsertionPoint=bit.readwithlog("2RD",dat,"Ins",1)
	if not DataFlag & 0x02:
		gpdwg.objects['temp'].AlignmentPoint=bit.point2D()
		gpdwg.objects['temp'].AlignmentPoint.x=bit.readwithlog("DD",dat,"Align",1,10)
		gpdwg.objects['temp'].AlignmentPoint.y=bit.readwithlog("DD",dat,"Align.X",1,20)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("BE",dat,"Extrusion",1)
	gpdwg.objects['temp'].Thickness=bit.readwithlog("BT",dat,"Thickness",1)
	if not DataFlag & 0x04:
		gpdwg.objects['temp'].ObliqueAngle=bit.readwithlog("RD",dat,"ObliqueAngle",1)
	if not DataFlag & 0x08:
		gpdwg.objects['temp'].RotationAngle=bit.readwithlog("RD",dat,"RotationAngle",1)
	gpdwg.objects['temp'].Height=bit.readwithlog("RD",dat,"Height",1)
	if not DataFlag & 0x10:
		gpdwg.objects['temp'].WidthFactor=bit.readwithlog("RD",dat,"WidthFactor",1)
	gpdwg.objects['temp'].TextValue=bit.readwithlog("TV",dat,"Value",1)
	if not DataFlag & 0x20:
		gpdwg.objects['temp'].Generation=bit.readwithlog("BS",dat,"Generation",1)
	if not DataFlag & 0x40:
		gpdwg.objects['temp'].HorAlignment=bit.readwithlog("BS",dat,"Generation",1)
	if not DataFlag & 0x80:
		gpdwg.objects['temp'].VerAlignment=bit.readwithlog("BS",dat,"VerAlignment",1)



#from ObjectDecode import *