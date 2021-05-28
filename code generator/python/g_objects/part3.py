def decode_TEXT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_text()
	global Temp
	TempLog(9,Temp+"	"+"TEXT")
	TempLog(20,"Text Start")
	if not decode_entity(gpdwg,dat): return False
	decode_Common_TEXT(gpdwg,dat)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Style=bit.readwithlog("H",dat,"Style",1)
	TempLog(20,"Text End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_VERTEX_MESH(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_VertexMesh()
	TempLog(20,"VertexMesh Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Flags=bit.readwithlog("RC",dat,"Flags",1)
	gpdwg.objects['temp'].Point=bit.readwithlog("3BD",dat,"Point",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"VertexMesh End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_POLYLINE_PFACE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_PolylinePface()
	TempLog(20,'PolylinePface Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Numverts=bit.readwithlog('BS',dat,'Numverts',1)
	gpdwg.objects['temp'].Numfaces=bit.readwithlog('BS',dat,'Numfaces',1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Vertex_First=bit.readwithlog('H',dat,'First Vertex',1)
	gpdwg.objects['temp'].Vertex_Last=bit.readwithlog('H',dat,'Last Vertex',1)
	gpdwg.objects['temp'].Seqend=bit.readwithlog('H',dat,'Seqend',1)
	TempLog(20,'PolylinePface End\n\n')
	raise TypeError("Found object which we were not able to create :-)")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MTEXT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Mtext()
	TempLog(20,'Mtext Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Insertion=bit.readwithlog('3BD',dat,'Insertion Point',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('3BD',dat,'Extrusion',1)
	gpdwg.objects['temp'].Axis_X_Direction=bit.readwithlog('3BD',dat,'Axis X Direction',1)
	gpdwg.objects['temp'].Rect_Width=bit.readwithlog('BD',dat,'Rect Width',1)
	gpdwg.objects['temp'].Text_Height=bit.readwithlog('BD',dat,'Text Height',1)
	gpdwg.objects['temp'].Attachment=bit.readwithlog('BS',dat,'Attachment',1)
	gpdwg.objects['temp'].Draw_Direction=bit.readwithlog('BS',dat,'Draw Direction',1)
	gpdwg.objects['temp'].Extents=bit.readwithlog('BD',dat,'Extents',1)
	gpdwg.objects['temp'].Extents_Width=bit.readwithlog('BD',dat,'Extents Width',1)
	gpdwg.objects['temp'].Text=bit.readwithlog('TV',dat,'Text',1)
	gpdwg.objects['temp'].Style=bit.readwithlog('H',dat,'Style',1)
	gpdwg.objects['temp'].Line_Spacing_Style=bit.readwithlog('BS',dat,'Line Spacing Style',1)
	gpdwg.objects['temp'].Line_Spacing_Factor=bit.readwithlog('BD',dat,'Line Spacing Factor',1)
	gpdwg.objects['temp'].Unknown_Bit=bit.readwithlog('B',dat,'Unknown Bit',1)
	TempLog(20,'Mtext End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def old_decode_BLOCK_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_Block_Control()
	TempLog(20,'Block_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BL",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Layer_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Model Space',1))
	gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Paper Space',1))
	TempLog(20,'Block_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LAYER_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Layer_Control()
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit)+' Layer_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Layer_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'Layer_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VPORT_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Vport_Control()
	TempLog(20,'Vport_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Vport_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Vport_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'Vport_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_LTYPE_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Layer_Control()
	TempLog(20,'LTYPE_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Layer_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Handle '+"ByBlock",1))
	gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Handle '+"ByLayer",1))
	TempLog(20,'LTYPE_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMSTYLE_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Dimstyle_Control()
	TempLog(20,'Dimstyle_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Dimstyle_Handle=[]
	for i in xrange(Num_Entries+1):
		gpdwg.objects['temp'].Dimstyle_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'Dimstyle_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SHAPEFILE_CONTROL(gpdwg,dat):
	#'Num_Entries','Null_Handle_Refs','xdic_obj_handle','Layer_Handle'
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Layer_Control()
	TempLog(20,'SHAPE_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Layer_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Layer_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'SHAPE_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode__3DFACE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_3DFace()
	TempLog(20,"3DFace Start")
	if not decode_entity(gpdwg,dat): return False
	No_Flags=bit.readwithlog("B",dat,"No_Flags",1)
	gpdwg.objects['temp'].No_Flags=No_Flags
	Flag_Z=bit.readwithlog("B",dat,"Flag_Z",1)
	gpdwg.objects['temp'].Flag_Z=Flag_Z
	gpdwg.objects['temp'].Point1_X=bit.readwithlog("RD",dat,"Point1_X",1)
	gpdwg.objects['temp'].Point1_Y=bit.readwithlog("RD",dat,"Point1_Y",1)
	if Flag_Z == 0:
		gpdwg.objects['temp'].Point1_Z=bit.readwithlog("RD",dat,"Point1_Z",1)
	gpdwg.objects['temp'].Point2=bit.readwithlog("3DD",dat,"Point2",1,10)
	gpdwg.objects['temp'].Point3=bit.readwithlog("3DD",dat,"Point3",1,20)
	gpdwg.objects['temp'].Point4=bit.readwithlog("3DD",dat,"Point4",1,30)
	if No_Flags == 0:
		gpdwg.objects['temp'].Invisible_Flags=bit.readwithlog("BD",dat,"Invisible_Flags",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"3DFace End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_RAY(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Ray()
	TempLog(20,'Ray Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Point=bit.readwithlog('3BD',dat,'',1)
	gpdwg.objects['temp'].Vector=bit.readwithlog('3BD',dat,'',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Ray End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_DIMENSION_ANG2LN(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Ang2Ln()
	TempLog(20,"Dim Ang2Ln Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_16=bit.readwithlog("2RD",dat,"Point_16",1)
	gpdwg.objects['temp'].Point_13=bit.readwithlog("3BD",dat,"Point_13",1)
	gpdwg.objects['temp'].Point_14=bit.readwithlog("3BD",dat,"Point_14",1)
	gpdwg.objects['temp'].Point_15=bit.readwithlog("3BD",dat,"Point_15",1)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim Ang2Ln End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ENDBLK(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_endblk()
	global Temp
	TempLog(9,Temp+"	"+"ENDBLK")
	TempLog(20,"ENDBLK Start")
	if not decode_entity(gpdwg,dat): return False
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"ENDBLK End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SEQEND(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_seqend()
	global Temp
	TempLog(9,Temp+"	"+"SEQEND")
	TempLog(20,"SEQEND Start")
	if not decode_entity(gpdwg,dat): return False
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"SEQEND End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)
	
def decode_INSERT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_insert()
	global Temp
	TempLog(9,Temp+"	"+"Insert")
	TempLog(20,"Insert Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].InsertionPoint=bit.readwithlog("3BD",dat,"InsertionPoint",1)
	Scale_Flag=bit.readwithlog("BB",dat,"Scale Flag",1)
	gpdwg.objects['temp'].Scale_Flag=Scale_Flag
	TempScale=bit.point3D()
	if Scale_Flag == 3:
		TempScale.x=1
		TempScale.y=1
		TempScale.z=1
	elif Scale_Flag == 1:
		TempScale.x=1
		TempScale.y=bit.readwithlog("DD",dat,"Scale Y",1,1)
		TempScale.z=bit.readwithlog("DD",dat,"Scale Z",1,1)
	elif Scale_Flag == 2:
		TempScale.x=bit.readwithlog("RD",dat,"Scale X",1)
		TempScale.y=TempScale.x
		TempScale.z=TempScale.x
	else:
		TempScale.x=bit.readwithlog("RD",dat,"Scale X",1)
		TempScale.y=bit.readwithlog("DD",dat,"Scale Y",1,TempScale.x)
		TempScale.z=bit.readwithlog("DD",dat,"Scale Z",1,TempScale.x)
	gpdwg.objects['temp'].Scale=TempScale
	gpdwg.objects['temp'].Rotation=bit.readwithlog("BD",dat,"Rotation",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("3BD",dat,"Extrusion",1)
	Attrib_Flag=bool(bit.readwithlog("B",dat,"Attrib_Flag",1))
	gpdwg.objects['temp'].Attrib_Flag=Attrib_Flag
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Block_Header=bit.readwithlog("H",dat,"Block_Header",1)
	if Attrib_Flag:
		gpdwg.objects['temp'].First_Attrib=bit.readwithlog("H",dat,"First_Attrib",1)
		gpdwg.objects['temp'].Last_Attrib=bit.readwithlog("H",dat,"Last_Attrib",1)
		gpdwg.objects['temp'].Seqend=bit.readwithlog("H",dat,"Seqend",1)
	TempLog(20,"Insert End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_POLYLINE_3D(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Polyline3D()
	TempLog(20,"Polyline3D Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Spline_Flag=bit.readwithlog("RC",dat,"Spline Flags",1)
	gpdwg.objects['temp'].Closed_Flag=bit.readwithlog("RC",dat,"Closed Flags",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Vertex_First=bit.readwithlog("H",dat,"Vertex First",1)
	gpdwg.objects['temp'].Vertex_Last=bit.readwithlog("H",dat,"Vertex Last",1)
	gpdwg.objects['temp'].Seqend=bit.readwithlog("H",dat,"Seqend",1)
	TempLog(20,"Polyline3D End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)




def decode_ARC(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Arc()
	TempLog(20,"Arc Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Center=bit.readwithlog("3BD",dat,"Center",1)
	gpdwg.objects['temp'].Radius=bit.readwithlog("BD",dat,"Radius",1)
	gpdwg.objects['temp'].Thickness=bit.readwithlog("BT",dat,"Thickness",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("BE",dat,"Extrusion",1)
	gpdwg.objects['temp'].Start_Angle=bit.readwithlog("BD",dat,"Start_Angle",1)
	gpdwg.objects['temp'].End_Angle=bit.readwithlog("BD",dat,"End_Angle",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Arc End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)



def decode_SPLINE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Spline()
	TempLog(20,'Spline Start')
	if not decode_entity(gpdwg,dat): return False
	Scenario=bit.readwithlog('BL',dat,'Scenario',1)
	gpdwg.objects['temp'].Scenario=Scenario
	gpdwg.objects['temp'].Degree=bit.readwithlog('BL',dat,'Degree',1)
	if Scenario == 2:
		gpdwg.objects['temp'].Fit_Tol=bit.readwithlog('BD',dat,'Fit Tol',1)
		gpdwg.objects['temp'].Beg_Tangent_Vector=bit.readwithlog('3BD',dat,'Beg tan vec',1)
		gpdwg.objects['temp'].End_Tangent_Vector=bit.readwithlog('3BD',dat,'End tan vec',1)
		Num_Fit_Points=bit.readwithlog('BL',dat,'num fit pts',1)
		gpdwg.objects['temp'].Num_Fit_Points=Num_Fit_Points

	if Scenario == 1:
		gpdwg.objects['temp'].Rational=bit.readwithlog('B',dat,'Rational',1)
		gpdwg.objects['temp'].Closed=bit.readwithlog('B',dat,'Closed',1)
		gpdwg.objects['temp'].Periodic=bit.readwithlog('B',dat,'Periodic',1)
		gpdwg.objects['temp'].Knot_Tol=bit.readwithlog('BD',dat,'Knot tol',1)
		gpdwg.objects['temp'].Ctrl_tol=bit.readwithlog('BD',dat,'Ctrl tol',1)
		Num_Knots=bit.readwithlog('BL',dat,'Num_Knots',1)
		gpdwg.objects['temp'].Num_Knots=Num_Knots
		Num_Ctrl_Points=bit.readwithlog('BL',dat,'Num_Ctrl_Pts',1)
		gpdwg.objects['temp'].Num_Ctrl_Points=Num_Ctrl_Points
		gpdwg.objects['temp'].Weight=bit.readwithlog('B',dat,'Weight',1)
		gpdwg.objects['temp'].Knot={}
		gpdwg.objects['temp'].Ctrl_Point={}
		gpdwg.objects['temp'].Weight={}
		for i in xrange(int(Num_Knots)):
			gpdwg.objects['temp'].Knot[i]=bit.readwithlog('BD',dat,'Knot',1)
		for i in xrange(int(Num_Ctrl_Points)):
			gpdwg.objects['temp'].Ctrl_Point[i]=bit.readwithlog('3BD',dat,'Control_Pt',1)
			gpdwg.objects['temp'].Weight[i]=bit.readwithlog('BD',dat,'Weight',1)
	if Scenario == 2:
		gpdwg.objects['temp'].Fit_Point={}
		for i in xrange(int(Num_Fit_Points)):
			gpdwg.objects['temp'].Fit_Point[i]=bit.readwithlog('3BD',dat,'Fit pt '+str(i),2)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Spline End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_ORDINATE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Ordinate()
	TempLog(20,"Dim Ordinate Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	gpdwg.objects['temp'].Point_13=bit.readwithlog("3BD",dat,"Point_13",1)
	gpdwg.objects['temp'].Point_14=bit.readwithlog("3BD",dat,"Point_14",1)
	gpdwg.objects['temp'].Flag2=bit.readwithlog("RC",dat,"Flag2",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim Ordinate End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)



def decode_DIMENSION_LINEAR(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Linear()
	TempLog(20,"Dim Linear Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_13=bit.readwithlog("3BD",dat,"Point_13",1)
	gpdwg.objects['temp'].Point_14=bit.readwithlog("3BD",dat,"Point_14",1)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	gpdwg.objects['temp'].Ext_Line_Rot=bit.readwithlog("BD",dat,"Ext_Line_Rot",1)
	gpdwg.objects['temp'].Dim_Rot=bit.readwithlog("BD",dat,"Dim_Rot",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim Linear End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_BLOCK(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_block()
	global Temp
	TempLog(9,Temp+"	"+"BLOCK")
	TempLog(20,"Block Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Name=bit.readwithlog("TV",dat,"Name",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Block End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_DIMENSION_ALIGNED(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Aligned()
	TempLog(20,"Dim Aligned Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_13=bit.readwithlog("3BD",dat,"Point_13",1)
	gpdwg.objects['temp'].Point_14=bit.readwithlog("3BD",dat,"Point_14",1)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	gpdwg.objects['temp'].Ext_Line_Rot=bit.readwithlog("BD",dat,"Ext_Line_Rot",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim Aligned End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_DIMENSION_RADIUS(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Radius()
	TempLog(20,"Dim Radius Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	gpdwg.objects['temp'].Point_15=bit.readwithlog("3BD",dat,"Point_15",1)
	gpdwg.objects['temp'].Leader_Length=bit.readwithlog("BD",dat,"Leader_Length",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim Radius End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_DIAMETER(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Diameter()
	TempLog(20,"Dim Diameter Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_15=bit.readwithlog("3BD",dat,"Point_15",1)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	gpdwg.objects['temp'].Leader_Length=bit.readwithlog("BD",dat,"Leader_Length",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim RDiameter End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POINT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Point()
	TempLog(20,"Point Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Point=bit.readwithlog("3BD",dat,"Point",1)
	gpdwg.objects['temp'].Thickness=bit.readwithlog("BT",dat,"Thickness",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("BE",dat,"Extrusion",1)
	gpdwg.objects['temp'].Angle_X=bit.readwithlog("BD",dat,"Angle_X",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Point End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POLYLINE_MESH(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_PolylineMesh()
	TempLog(20,'PolylineMesh Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Flags=bit.readwithlog('BS',dat,'Flags',1)
	gpdwg.objects['temp'].Curve_Type=bit.readwithlog('BS',dat,'Curve Type',1)
	gpdwg.objects['temp'].M_Vert_Count=bit.readwithlog('BS',dat,'M Vertex count',1)
	gpdwg.objects['temp'].N_Vert_Count=bit.readwithlog('BS',dat,'N Vertex count',1)
	gpdwg.objects['temp'].M_Density=bit.readwithlog('BS',dat,'M density',1)
	gpdwg.objects['temp'].N_Density=bit.readwithlog('BS',dat,'N density',1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Vertex_First=bit.readwithlog('H',dat,'First Vertex',1)
	gpdwg.objects['temp'].Vertex_Last=bit.readwithlog('H',dat,'Last Vertex',1)
	gpdwg.objects['temp'].Seqend=bit.readwithlog('H',dat,'Seqend',1)
	TempLog(20,'PolylineMesh End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_SOLID(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Solid()
	TempLog(20,'Solid Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Thickness=bit.readwithlog('BT',dat,'Thickness',1)
	gpdwg.objects['temp'].Elevation=bit.readwithlog('BD',dat,'Elevation',1)
	gpdwg.objects['temp'].Corner_1=bit.readwithlog('2RD',dat,'1st corner',1)
	gpdwg.objects['temp'].Corner_2=bit.readwithlog('2RD',dat,'2nd corner',1)
	gpdwg.objects['temp'].Corner_3=bit.readwithlog('2RD',dat,'3rd corner',1)
	gpdwg.objects['temp'].Corner_4=bit.readwithlog('2RD',dat,'4th corner',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('BE',dat,'Extrusion',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Solid End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_ELLIPSE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Ellipse()
	TempLog(20,'Ellipse Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Center=bit.readwithlog('3BD',dat,'Center',1)
	gpdwg.objects['temp'].SM_Axis_Vector=bit.readwithlog('3BD',dat,'SM axis vec',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('3BD',dat,'Extrusion',1)
	gpdwg.objects['temp'].Axis_Ratio=bit.readwithlog('BD',dat,'Axis ratio',1)
	gpdwg.objects['temp'].Beg_Angle=bit.readwithlog('BD',dat,'Beg angle',1)
	gpdwg.objects['temp'].End_Angle=bit.readwithlog('BD',dat,'End angle',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Ellipse End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_REGION(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Region()
	TempLog(20,'Region Start')
	if not decode_entity(gpdwg,dat): return False
	ACIS_Flag = bit.readwithlog('B',dat,'ACIS Empty Bit',1)
	gpdwg.objects['temp'].ACIS_Flag=ACIS_Flag
	Unknown_Bit = bit.readwithlog('B',dat,'Unknown Bit',1)
	gpdwg.objects['temp'].Unknown_Bit=Unknown_Bit
	Version = bit.readwithlog('BS',dat,'Version',1)
	gpdwg.objects['temp'].Version=Version
	gpdwg.objects['temp'].SAT=gpdwg.dwg_SAT()
	Block_Size=1
	if Version == 1:
		while Block_Size>0:
			TempSAT=[]
			Block_Size=int(bit.readwithlog('BL',dat,'Block_Size',1))
			for i in xrange(Block_Size):
				TempSAT.append(bit.read_RC(dat)) #Dont know what to be done with this data.
			gpdwg.objects['temp'].SAT.append(TempSAT)
	if Version == 2:
		raise Exception("SAB File found.")
		SAB_File_End=[69,110,100,14,2,111,102,14,4,65,67,73,83,13,4,100,97,116,97] #  End\x0E\x02of\x0E\x04ACIS\x0D\x04data
		SAB_File_End_Test=[19]
		while SAB_File_End != SAB_File_End_Test:
			SAB_File_End_Test.pop(18)
			SAB_File_End_Test.append(bit.readwithlog('RC',dat,'SAB Data',1))
	WireFrame_Flag=bit.readwithlog('B',dat,'WireFrame_Flag',1)
	gpdwg.objects['temp'].WireFrame_Flag=WireFrame_Flag
	if WireFrame_Flag == 1:
		raise Exception("Wireframe found.")
		Point_Flag==bit.readwithlog('B',dat,'Point_Flag',1)
		gpdwg.objects['temp'].Point_Flag=Point_Flag
		if Point_Flag == 1:
			gpdwg.objects['temp'].Point=bit.readwithlog('3BD',dat,'Point',1)
		else:
			gpdwg.objects['temp'].Point=bit.point3D(0,0,0)
		gpdwg.objects['temp'].Num_IsoLines=bit.readwithlog('BL',dat,'Num IsoLines',1)
		IsoLines_Flag=bit.readwithlog('B',dat,'IsoLines_Flag',1)
		if IsoLines_Flag == 1:
			Num_Wires=bit.readwithlog('BL',dat,'Num of Wires',1)
			for i in xrange(Num_Wires):
				gpdwg.objects['temp'].Wire_Type[i]=bit.readwithlog('RC',dat,'Wire Type',1)
				gpdwg.objects['temp'].Wire_Selection_Marker[i]=bit.readwithlog('BL',dat,'Wire Selection Marker',1)
				gpdwg.objects['temp'].Wire_Color[i]=bit.readwithlog('BS',dat,'Wire Color',1)
				gpdwg.objects['temp'].Wire_ACIS_Index[i]=bit.readwithlog('BL',dat,'Wire ACIS Index',1)
				gpdwg.objects['temp'].Wire_No_Points[i]=bit.readwithlog('BL',dat,'Wire No of Points',1)
				gpdwg.objects['temp'].Wire_Type[i]=bit.readwithlog('RC',dat,'Wire Type',1)
				gpdwg.objects['temp'].WirePoints=[]
				for i in xrange(Wire_No_Points):
					gpdwg.objects['temp'].WirePoints.append(bit.readwithlog('3BD',dat,'Wire Point',1))
				Transform_Flag=bit.readwithlog('B',dat,'Transform Flag',1)
				gpdwg.objects['temp'].Transform_Flag=Transform_Flag
				if Transform_Flag == 1:
					gpdwg.objects['temp'].Axis_X=bit.readwithlog('3BD',dat,'X Axis',1)
					gpdwg.objects['temp'].Axis_Y=bit.readwithlog('3BD',dat,'Y Axis',1)
					gpdwg.objects['temp'].Axis_Z=bit.readwithlog('3BD',dat,'Z Axis',1)
					gpdwg.objects['temp'].Translation=bit.readwithlog('3BD',dat,'Translation',1)
					gpdwg.objects['temp'].Scale=bit.readwithlog('BD',dat,'Scale',1)
					gpdwg.objects['temp'].Rotation=bit.readwithlog('B',dat,'Rotation',1)
					gpdwg.objects['temp'].Reflection=bit.readwithlog('B',dat,'Reflection',1)
					gpdwg.objects['temp'].Shear=bit.readwithlog('B',dat,'Shear',1)
			Num_Silhouettes=bit.readwithlog('BL',dat,'Num_Silhouettes',1)	
			gpdwg.objects['temp'].Num_Silhouettes=Num_Silhouettes
			for i in xrange(Num_Silhouettes):
				gpdwg.objects['temp'].VP_ID=bit.readwithlog('BL',dat,'VP ID',1)
				gpdwg.objects['temp'].VP_Target=bit.readwithlog('BL',dat,'VP ID',1)
				gpdwg.objects['temp'].VP_Target_Direction=bit.readwithlog('BL',dat,'VP ID',1)
				gpdwg.objects['temp'].VP_Up_Direction=bit.readwithlog('BL',dat,'VP ID',1)
				gpdwg.objects['temp'].VP_Perspective=bit.readwithlog('BL',dat,'VP ID',1)
				gpdwg.objects['temp'].Num_Wires=bit.readwithlog('BL',dat,'VP ID',1)



	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Region End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_3DSOLID(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"3DSOLID")
	#if not decode_entity(gpdwg,dat): return False
def decode_BODY(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"BODY")
	#if not decode_entity(gpdwg,dat): return False


def decode_MINSERT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_m_insert()
	TempLog(20,"M_Insert Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].InsertionPoint=bit.readwithlog("3BD",dat,"InsertionPoint",1)
	Scale_Flag=bit.readwithlog("BB",dat,"Scale Flag",1)
	gpdwg.objects['temp'].Scale_Flag=Scale_Flag
	TempScale=bit.point3D()
	if Scale_Flag == 3:
		TempScale.x=1
		TempScale.y=1
		TempScale.z=1
	elif Scale_Flag == 1:
		TempScale.x=1
		TempScale.y=bit.readwithlog("DD",dat,"Scale Y",1,1)
		TempScale.z=bit.readwithlog("DD",dat,"Scale Z",1,1)
	elif Scale_Flag == 2:
		TempScale.x=bit.readwithlog("RD",dat,"Scale X",1)
		TempScale.y=TempScale.x
		TempScale.z=TempScale.x
	else:
		TempScale.x=bit.readwithlog("RD",dat,"Scale X",1)
		TempScale.y=bit.readwithlog("DD",dat,"Scale Y",1,TempScale.x)
		TempScale.z=bit.readwithlog("DD",dat,"Scale Z",1,TempScale.x)
	gpdwg.objects['temp'].Scale=TempScale
	gpdwg.objects['temp'].Rotation=bit.readwithlog("BD",dat,"Rotation",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("3BD",dat,"Extrusion",1)
	Attrib_Flag=bool(bit.readwithlog("B",dat,"Attrib_Flag",1))
	gpdwg.objects['temp'].Attrib_Flag=Attrib_Flag
	gpdwg.objects['temp'].Columns=bit.readwithlog("BS",dat,"Columns",1)
	gpdwg.objects['temp'].Rows=bit.readwithlog("BS",dat,"Rows",1)
	gpdwg.objects['temp'].Column_Spacing=bit.readwithlog("BD",dat,"Column Spacing",1)
	gpdwg.objects['temp'].Row_Spacing=bit.readwithlog("BD",dat,"Row Spacing",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Block_Header=bit.readwithlog("H",dat,"Block_Header",1)
	if Attrib_Flag:
		gpdwg.objects['temp'].First_Attrib=bit.readwithlog("H",dat,"First_Attrib",1)
		gpdwg.objects['temp'].Last_Attrib=bit.readwithlog("H",dat,"Last_Attrib",1)
		gpdwg.objects['temp'].Seqend=bit.readwithlog("H",dat,"Seqend",1)
	TempLog(20,"M_Insert End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_VIEW_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_View_Control()
	TempLog(20,'VIEW_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].View_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].View_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'VIEW_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ATTRIB(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_attrib()
	global Temp
	TempLog(9,Temp+"	"+"Attrib")
	TempLog(20,"Attrib Start")
	if not decode_entity(gpdwg,dat): return False
	decode_Common_ATTRIB(gpdwg,dat)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Style=bit.readwithlog("H",dat,"Style",1)
	TempLog(20,"Attrib End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_2D(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Vertex2D()
	TempLog(20,"Vertex2D Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Flags=bit.readwithlog("RC",dat,"Flags",1)
	gpdwg.objects['temp'].Point=bit.readwithlog("3BD",dat,"Point",1)
	Start_Width=bit.readwithlog("BD",dat,"Start_Width",1)
	if Start_Width < 0:
		gpdwg.objects['temp'].Start_Width=abs(Start_Width)
		gpdwg.objects['temp'].End_Width=abs(Start_Width)
	else:
		gpdwg.objects['temp'].End_Width=bit.readwithlog("BD",dat,"End_Width",1)
	gpdwg.objects['temp'].Bulge=bit.readwithlog("BD",dat,"Bulge",1)
	gpdwg.objects['temp'].Tangent=bit.readwithlog("BD",dat,"Tangent",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Vertex2D End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_Common_ATTRIB(gpdwg,dat):
	decode_Common_TEXT(gpdwg,dat)
	gpdwg.objects['temp'].Tag=bit.readwithlog("TV",dat,"Tag",1)
	gpdwg.objects['temp'].Field_Length=bit.readwithlog("BS",dat,"Field_Length",1)
	gpdwg.objects['temp'].Flags=bit.readwithlog("RC",dat,"Flags",1)


def decode_ATTDEF(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_attdef()
	global Temp
	TempLog(9,Temp+"	"+"ATTDEF")
	TempLog(20,"Attdef Start")
	if not decode_entity(gpdwg,dat): return False
	decode_Common_ATTRIB(gpdwg,dat)
	gpdwg.objects['temp'].Prompt=bit.readwithlog("TV",dat,"Prompt",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Style=bit.readwithlog("H",dat,"Style",1)
	TempLog(20,"Attdef End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)



def decode_UNKNOWN(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"UNKNOWN")
	#if not decode_entity(gpdwg,dat): return False



def decode_VERTEX_3D(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Vertex3D()
	TempLog(20,"Vertex3D Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Flags=bit.readwithlog("RC",dat,"Flags",1)
	gpdwg.objects['temp'].Point=bit.readwithlog("3BD",dat,"Point",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Vertex3D End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_PFACE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Vertex_Pface()
	TempLog(20,"VertexPface Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Flags=bit.readwithlog("RC",dat,"Flags",1)
	gpdwg.objects['temp'].Point=bit.readwithlog("3BD",dat,"Point",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"VertexPface End\n\n")
	raise TypeError("Found object which we were not able to create :-)")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_PFACE_FACE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Vertex_Pface_Face()
	TempLog(20,"VertexPfaceFace Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].VertexIndex0=bit.readwithlog("BS",dat,"Vertex Index 0",1)
	gpdwg.objects['temp'].VertexIndex1=bit.readwithlog("BS",dat,"Vertex Index 1",1)
	gpdwg.objects['temp'].VertexIndex2=bit.readwithlog("BS",dat,"Vertex Index 2",1)
	gpdwg.objects['temp'].VertexIndex3=bit.readwithlog("BS",dat,"Vertex Index 3",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"VertexPfaceFace End\n\n")
	raise TypeError("Found object which we were not able to create :-)")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POLYLINE_2D(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Polyline2D()
	TempLog(20,"Polyline2D Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Flags=bit.readwithlog("BS",dat,"Flags",1)
	gpdwg.objects['temp'].Curve_Type=bit.readwithlog("BS",dat,"Curve Type",1)
	gpdwg.objects['temp'].Start_Width=bit.readwithlog("BD",dat,"Start_Width",1)
	gpdwg.objects['temp'].End_Width=bit.readwithlog("BD",dat,"End_Width",1)
	gpdwg.objects['temp'].Thickness=bit.readwithlog("BT",dat,"Thickness",1)
	gpdwg.objects['temp'].Elevation=bit.readwithlog("BD",dat,"Elevation",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("BE",dat,"Extrusion",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Vertex_First=bit.readwithlog("H",dat,"Vertex First",1)
	gpdwg.objects['temp'].Vertex_Last=bit.readwithlog("H",dat,"Vertex Last",1)
	gpdwg.objects['temp'].Seqend=bit.readwithlog("H",dat,"Seqend",1)
	TempLog(20,"Polyline2D End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_CIRCLE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Circle()
	TempLog(20,"Circle Start")
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Center=bit.readwithlog("3BD",dat,"Center",1)
	gpdwg.objects['temp'].Radius=bit.readwithlog("BD",dat,"Radius",1)
	gpdwg.objects['temp'].Thickness=bit.readwithlog("BT",dat,"Thickness",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("BE",dat,"Extrusion",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Circle End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LINE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Line()
	TempLog(20,"Line Start")
	if not decode_entity(gpdwg,dat): return False
	Z_Flag=bit.readwithlog("B",dat,"Z Flags",1)
	gpdwg.objects['temp'].Z_Flag=Z_Flag
	gpdwg.objects['temp'].Start_X=bit.readwithlog("RD",dat,"Start X",1)
	gpdwg.objects['temp'].End_X=bit.readwithlog("DD",dat,"End X",1,10)
	gpdwg.objects['temp'].Start_Y=bit.readwithlog("RD",dat,"Start Y",1)
	gpdwg.objects['temp'].End_Y=bit.readwithlog("DD",dat,"End Y",1,20)
	if Z_Flag == 0:
		gpdwg.objects['temp'].Start_Z=bit.readwithlog("RD",dat,"Start Z",1)
		gpdwg.objects['temp'].End_Z=bit.readwithlog("DD",dat,"End Z",1,30)
	gpdwg.objects['temp'].Thickness=bit.readwithlog("BT",dat,"Thickness",1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog("BE",dat,"Extrusion",1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,"Line End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_DIMENSION_ANG3PT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dim_Ang3pt()
	TempLog(20,"Dim Ang3pt Start")
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].Point_10=bit.readwithlog("3BD",dat,"Point_10",1)
	gpdwg.objects['temp'].Point_13=bit.readwithlog("3BD",dat,"Point_13",1)
	gpdwg.objects['temp'].Point_14=bit.readwithlog("3BD",dat,"Point_14",1)
	gpdwg.objects['temp'].Point_15=bit.readwithlog("3BD",dat,"Point_15",1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Dimstyle=bit.readwithlog("H",dat,"Dimstyle",1)
	gpdwg.objects['temp'].Anonymous_Block=bit.readwithlog("H",dat,"Anonymous_Block",1)
	TempLog(20,"Dim Ang3pt End\n\n")
	return Check_Obj_CRC(dat,Obj_Size)



def decode_TRACE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Trace()
	TempLog(20,'Trace Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Thickness=bit.readwithlog('BT',dat,'Thickness',1)
	gpdwg.objects['temp'].Elevation=bit.readwithlog('BD',dat,'Elevation',1)
	gpdwg.objects['temp'].Corner_1=bit.readwithlog('2RD',dat,'1st corner',1)
	gpdwg.objects['temp'].Corner_2=bit.readwithlog('2RD',dat,'2nd corner',1)
	gpdwg.objects['temp'].Corner_3=bit.readwithlog('2RD',dat,'3rd corner',1)
	gpdwg.objects['temp'].Corner_4=bit.readwithlog('2RD',dat,'4th corner',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('BE',dat,'Extrusion',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Trace End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_SHAPE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Shape()
	TempLog(20,'Shape Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Ins_Pt=bit.readwithlog('3BD',dat,'Insertion Point',1)
	gpdwg.objects['temp'].Scale=bit.readwithlog('BD',dat,'Scale',1)
	gpdwg.objects['temp'].Rotation=bit.readwithlog('BD',dat,'Rotation',1)
	gpdwg.objects['temp'].Width_Factor=bit.readwithlog('BD',dat,'Width Factor',1)
	gpdwg.objects['temp'].Oblique=bit.readwithlog('BD',dat,'Oblique',1)
	gpdwg.objects['temp'].Thickness=bit.readwithlog('BD',dat,'Thickness',1)
	gpdwg.objects['temp'].Shape_No=bit.readwithlog('BS',dat,'Shape File No',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('3BD',dat,'Extrusion',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Shape End\n\n')
	raise TypeError("Found object which we were not able to create :-)")
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VIEWPORT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Viewport()
	TempLog(20,'Viewport Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Center=bit.readwithlog('3BD',dat,'',1)
	gpdwg.objects['temp'].Width=bit.readwithlog('BD',dat,'',1)
	gpdwg.objects['temp'].Height=bit.readwithlog('BD',dat,'',1)
	gpdwg.objects['temp'].View_Target=bit.readwithlog('3BD',dat,'View Target',1)
	gpdwg.objects['temp'].View_Direction=bit.readwithlog('3BD',dat,'View Direction',1)
	gpdwg.objects['temp'].View_Twist_Angle=bit.readwithlog('BD',dat,'View Twist Angle',1)
	gpdwg.objects['temp'].View_Height=bit.readwithlog('BD',dat,'View Height',1)
	gpdwg.objects['temp'].Lens_Length=bit.readwithlog('BD',dat,'Lens Length',1)
	gpdwg.objects['temp'].Front_Clip_Z=bit.readwithlog('BD',dat,'Front Clip Z',1)
	gpdwg.objects['temp'].Back_Clip_Z=bit.readwithlog('BD',dat,'Back Clip Z',1)
	gpdwg.objects['temp'].Snap_Angle=bit.readwithlog('BD',dat,'Snap Angle',1)
	gpdwg.objects['temp'].View_Center=bit.readwithlog('2RD',dat,'View Center',1)
	gpdwg.objects['temp'].Snap_Base=bit.readwithlog('2RD',dat,'Snap Base',1)
	gpdwg.objects['temp'].Snap_Spacing=bit.readwithlog('2RD',dat,'Snap Spacing',1)
	gpdwg.objects['temp'].Grid_Spacing=bit.readwithlog('2RD',dat,'Grid Spacing',1)
	gpdwg.objects['temp'].Circle_Zoom=bit.readwithlog('BS',dat,'Circle Zoom',1)
	gpdwg.objects['temp'].Frozen_Layer_Count=bit.readwithlog('BL',dat,'Frozen Layer Count',1)
	gpdwg.objects['temp'].Status_Flags=bit.readwithlog('BL',dat,'Status Flags',1)
	gpdwg.objects['temp'].Style_Sheet=bit.readwithlog('TV',dat,'Style Sheet',1)
	gpdwg.objects['temp'].Render_Mode=bit.readwithlog('RC',dat,'Render Mode',1)
	gpdwg.objects['temp'].UCS_At_Origin=bit.readwithlog('B',dat,'UCS at origin',1)
	gpdwg.objects['temp'].UCS_Per_Viewport=bit.readwithlog('B',dat,'UCS per Viewport',1)
	gpdwg.objects['temp'].UCS_Origin=bit.readwithlog('3BD',dat,'UCS Origin',1)
	gpdwg.objects['temp'].UCS_X_Axis=bit.readwithlog('3BD',dat,'UCS X Axis',1)
	gpdwg.objects['temp'].UCS_Y_Axis=bit.readwithlog('3BD',dat,'UCS Y Axis',1)
	gpdwg.objects['temp'].UCS_Elevation=bit.readwithlog('BD',dat,'UCS Elevation',1)
	gpdwg.objects['temp'].UCS_Ortho_View_Type=bit.readwithlog('BS',dat,'UCS Ortho View Type',1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Frozen_Layer_Handle=[]
	for i in xrange(int(gpdwg.objects['temp'].Frozen_Layer_Count)):
		gpdwg.objects['temp'].Frozen_Layer_Handle.append(bit.readwithlog('H',dat,'Frozen Layer Handle',1))

	gpdwg.objects['temp'].Clip_Boundary_Handle=bit.readwithlog('H',dat,'Clip Boundary Handle',1)
	gpdwg.objects['temp'].Viewport_Ent_Header=bit.readwithlog('H',dat,'Viewport Ent Header',1)
	gpdwg.objects['temp'].Named_UCS_Handle=bit.readwithlog('H',dat,'Named UCS Handle',1)
	gpdwg.objects['temp'].Base_UCS_Handle=bit.readwithlog('H',dat,'Base UCS Handle',1) # To be checked once again.
	TempLog(20,'Viewport End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)







def decode_XLINE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Xline()
	TempLog(20,'Ray Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Point=bit.readwithlog('3BD',dat,'',1)
	gpdwg.objects['temp'].Vector=bit.readwithlog('3BD',dat,'',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Ray End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DICTIONARY(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Dictionary()
	TempLog(20,'Dictionary Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BL",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Cloning_Flag=bit.readwithlog("BS",dat,'Cloning_Flag',1)
	gpdwg.objects['temp'].Hard_Owner_Flag=bit.readwithlog("RC",dat,'Hard_Owner_Flag',1)
	gpdwg.objects['temp'].Name=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Name.append(bit.readwithlog("TV",dat,'Name '+str(i),1))
	gpdwg.objects['temp'].ParentHandle = bit.readwithlog("H",dat,'ParentHandle',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].ItemsHandle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].ItemsHandle.append(bit.readwithlog("H",dat,'ItemsHandle ' +str(i),1))
	TempLog(20,'Dictionary End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_OLEFRAME(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"OLEFRAME")
	#if not decode_entity(gpdwg,dat): return False

def decode_LEADER(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Leader()
	TempLog(20,'Leader Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Unknown_Bit=bit.readwithlog('B',dat,'Unknown bit',1)
	gpdwg.objects['temp'].Annotation_Type=bit.readwithlog('BS',dat,'Annot type',1)
	gpdwg.objects['temp'].Path_Type=bit.readwithlog('BS',dat,'path type',1)
	Num_Points=int(bit.readwithlog('BL',dat,'numpts',1))
	gpdwg.objects['temp'].Num_Points=Num_Points
	gpdwg.objects['temp'].Points=[]
	for i in xrange(Num_Points):
		gpdwg.objects['temp'].Points.append(bit.readwithlog('3BD',dat,'point',1))
	gpdwg.objects['temp'].Origin=bit.readwithlog('3BD',dat,'Origin',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('3BD',dat,'Extrusion',1)
	gpdwg.objects['temp'].Direction_X=bit.readwithlog('3BD',dat,'x direction',1)
	gpdwg.objects['temp'].offsettoblockinspt=bit.readwithlog('3BD',dat,'offsettoblockinspt',1)
	gpdwg.objects['temp'].EndPoint_Projection=bit.readwithlog('3BD',dat,'Endptproj',1)
	gpdwg.objects['temp'].Box_Height=bit.readwithlog('BD',dat,'Box height',1)
	gpdwg.objects['temp'].Box_Width=bit.readwithlog('BD',dat,'Box width',1)
	gpdwg.objects['temp'].Hooklineonxdir=bit.readwithlog('B',dat,'Hooklineonxdir',1)
	gpdwg.objects['temp'].Arrowheadon=bit.readwithlog('B',dat,'Arrowheadon',1)
	gpdwg.objects['temp'].Unknown1=bit.readwithlog('BS',dat,'Unknown',1)
	gpdwg.objects['temp'].Unknown2=bit.readwithlog('B',dat,'Unknown',1)
	gpdwg.objects['temp'].Unknown3=bit.readwithlog('B',dat,'Unknown',1)
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].Associated_Annotation=bit.readwithlog('H',dat,'Associated annotation',1)
	gpdwg.objects['temp'].DimStyle=bit.readwithlog('H',dat,'DIMSTYLE',1)
	TempLog(20,'Leader End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_TOLERANCE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Tolerance()
	TempLog(20,'Tolerance Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Insertion=bit.readwithlog('3BD',dat,'Ins pt',1)
	gpdwg.objects['temp'].Direction_X=bit.readwithlog('3BD',dat,'X direction',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('3BD',dat,'Extrusion',1)
	gpdwg.objects['temp'].Text=bit.readwithlog('BS',dat,'Text string',1)
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Tolerance End\n\n')
	raise Exception("Tolerance found.")
	return Check_Obj_CRC(dat,Obj_Size)


def decode_MLINE(gpdwg,dat):

	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Mline()
	TempLog(20,'Mline Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Scale=bit.readwithlog('BD',dat,'Scale',1)
	gpdwg.objects['temp'].Justification=bit.readwithlog('RC',dat,'Just',1)
	gpdwg.objects['temp'].Base_Point=bit.readwithlog('3BD',dat,'Base point',1)
	gpdwg.objects['temp'].Extrusion=bit.readwithlog('3BD',dat,'Extrusion',1)
	gpdwg.objects['temp'].OpenClosed=bit.readwithlog('BS',dat,'Openclosed',1)
	Lines_in_Style=int(bit.readwithlog('RC',dat,'Linesinstyle',1))
	gpdwg.objects['temp'].Lines_in_Style=Lines_in_Style
	Num_Vertex=int(bit.readwithlog('BS',dat,'Numverts',1))
	gpdwg.objects['temp'].Num_Vertex=Num_Vertex
	gpdwg.objects['temp'].Vertex=[]
	for i in xrange(Num_Vertex):
		TempMlineVertex=gpdwg.dwg_Mline_Vertex()
		TempMlineVertex.Position=bit.readwithlog('3BD',dat,'vertex',2)
		TempMlineVertex.Direction=bit.readwithlog('3BD',dat,'vertex direction',2)
		TempMlineVertex.Miter_Direction=bit.readwithlog('3BD',dat,'miter direction',2)

		for j in xrange(Lines_in_Style):
			Num_Seg_Parms=int(bit.readwithlog('BS',dat,'numsegparms',3))
			TempMlineVertex.Seg_Parms=[]
			for k in xrange(Num_Seg_Parms):
				TempMlineVertex.Seg_Parms.append(bit.readwithlog('BD',dat,'segparm',4))
			Num_Area_Fill_Parms=int(bit.readwithlog('BS',dat,'numareafillparms',4))
			for l in xrange(Num_Area_Fill_Parms):
				TempMlineVertex.Area_Fill_Parms.append(bit.readwithlog('BD',dat,'areafillparm',4))
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'Mline End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_BLOCK_HEADER(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=gpdwg.dwg_Block_Header()
	TempLog(20,'Block_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Name=bit.readwithlog('TV',dat,'Entry name',1)
	gpdwg.objects['temp'].flag64=bit.readwithlog('B',dat,'64-flag',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex+1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].Anonymous=bit.readwithlog('B',dat,'Anonymous',1)
	gpdwg.objects['temp'].Hasatts=bit.readwithlog('B',dat,'Hasatts',1)
	Blkisxref=bit.readwithlog('B',dat,'Blkisxref',1)
	gpdwg.objects['temp'].Blkisxref=Blkisxref
	Xrefoverlaid=bit.readwithlog('B',dat,'Xrefoverlaid',1)
	gpdwg.objects['temp'].Xrefoverlaid=Xrefoverlaid
	gpdwg.objects['temp'].Loaded_Bit=bit.readwithlog('B',dat,'Loaded_Bit',1)
	gpdwg.objects['temp'].Base_Pt=bit.readwithlog('3BD',dat,'Base pt',1)
	gpdwg.objects['temp'].Xref_Pname=bit.readwithlog('TV',dat,'Xref pname',1)
	Temp = bit.readwithlog('RC',dat,'InsertCount',1)
	InsertCount=0
	while  Temp > 0:
		InsertCount = InsertCount + Temp
		Temp = bit.readwithlog('RC',dat,'InsertCount',1)
	gpdwg.objects['temp'].InsertCount=InsertCount
	gpdwg.objects['temp'].Block_Description=bit.readwithlog('TV',dat,'Block Description',1)
	Size_of_preview_data=int(bit.readwithlog('BL',dat,'Size of preview data',1))
	gpdwg.objects['temp'].Size_of_preview_data=Size_of_preview_data
	for i in xrange(Size_of_preview_data):
		gpdwg.objects['temp'].Binary_Preview_Data.append(gpdwg.objects['temp'].Binary_Preview_Data + bit.readwithlog('RC',dat,'Binary Preview Data ',1))
	gpdwg.objects['temp'].Block_Control_Handle=bit.readwithlog('H',dat,'Block Control Handle',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].xdicobjhandle =bit.readwithlog('H',dat,'xdicobjhandle ',1)
	gpdwg.objects['temp'].Null_Handle=bit.readwithlog('H',dat,'Null Handle',1)
	gpdwg.objects['temp'].Block_Entity_Handle=bit.readwithlog('H',dat,'Block Entity Handle',1)
	if (not Blkisxref) and (not Xrefoverlaid):
		gpdwg.objects['temp'].First_Entity_Handle=bit.readwithlog('H',dat,'First Entity Handle',1)
		gpdwg.objects['temp'].Last_Entity_Handle=bit.readwithlog('H',dat,'Last Entity Handle',1)
	gpdwg.objects['temp'].EndBlk_Entity_Handle=bit.readwithlog('H',dat,'EndBlk Entity Handle',1)
	gpdwg.objects['temp'].Insert_Handles=[]
	for i in xrange(InsertCount):
		gpdwg.objects['temp'].Insert_Handles.append(bit.readwithlog('H',dat,'Insert Handles',1))
	gpdwg.objects['temp'].Layout_Handles=bit.readwithlog('H',dat,'Layout Handle',1)
	TempLog(20,'Block_Header End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LAYER(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Layer()
	TempLog(20,'Layer Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog("TV",dat,'Entry_Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog("B",dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog("BS",dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog("B",dat,'Xdep',1)
	gpdwg.objects['temp'].Values=bit.readwithlog("BS",dat,'Values',1)
	gpdwg.objects['temp'].Color=bit.readwithlog("CMC",dat,'Color',1)
	gpdwg.objects['temp'].Handle_refs=bit.readwithlog("H",dat,'Handle_refs',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdic_obj_handle',1)
	gpdwg.objects['temp'].Layer_Handle=bit.readwithlog("H",dat,'Layer_Handle',1)	
	gpdwg.objects['temp'].Plot_Style=bit.readwithlog("H",dat,'Plot_Style',1)
	gpdwg.objects['temp'].LineType=bit.readwithlog("H",dat,'LineType',1)
	#gpdwg.objects['temp'].Uknown=bit.readwithlog("H",dat,'Uknown',1)
	TempLog(20,'Layer End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SHAPEFILE(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"SHAPEFILE")
	#if not decode_entity(gpdwg,dat): return False

def decode_UNKNOWN(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"UNKNOWN")
	#if not decode_entity(gpdwg,dat): return False
def decode_UNKNOWN(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"UNKNOWN")
	#if not decode_entity(gpdwg,dat): return False

def decode_LTYPE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_LType()
	TempLog(20,'LType Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].Description=bit.readwithlog('TV',dat,'Description',1)
	gpdwg.objects['temp'].Pattern_Len=bit.readwithlog('BD',dat,'Pattern_Len',1)
	gpdwg.objects['temp'].Alignment=bit.readwithlog('RC',dat,'Alignment',1)
	gpdwg.objects['temp'].Numdashes=bit.readwithlog('RC',dat,'Numdashes',1)
	gpdwg.objects['temp'].Dashes=list()
	for i in xrange(gpdwg.objects['temp'].Numdashes):
		TempDash=gpdwg.dwg_LType_Dash()
		TempDash.Dash_Length=bit.readwithlog('BD',dat,'Dash_Length',1)
		TempDash.Complex_Shapecode=bit.readwithlog('BS',dat,'Complex_Shapecode',1)
		TempDash.Offset_X=bit.readwithlog('RD',dat,'X-offset',1)
		TempDash.Offset_Y=bit.readwithlog('RD',dat,'Y-offset',1)
		TempDash.Scale=bit.readwithlog('BD',dat,'Scale',1)
		TempDash.Rotation=bit.readwithlog('BD',dat,'Rotation',1)
		TempDash.Shapeflag=bit.readwithlog('BS',dat,'Shapeflag',1)
		gpdwg.objects['temp'].Dashes.append(TempDash)
	StrArea=""
	for i in xrange(256):
		tempStr=bit.read_RC(dat)
		if tempStr > 0:
			StrArea=StrArea + str(chr(tempStr))
	TempLog(20,'\t\t\t\tString Area\t'+StrArea)
	gpdwg.objects['temp'].Strings_Area = StrArea
	gpdwg.objects['temp'].Ltype_Control=bit.readwithlog('H',dat,'Ltype_Control',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('H',dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('H',dat,'XrefBlockHandle',1)
	gpdwg.objects['temp'].ShapeFileHeader=[]
	for i in xrange(gpdwg.objects['temp'].Numdashes):
		gpdwg.objects['temp'].ShapeFileHeader.append(bit.readwithlog('H',dat,'ShapeFileHeader',1))
	TempLog(20,'LType End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)


def decode_UNKNOWN(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"UNKNOWN")
	#if not decode_entity(gpdwg,dat): return False
def decode_UNKNOWN(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"UNKNOWN")
	#if not decode_entity(gpdwg,dat): return False

def decode_VIEW(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_View()
	TempLog(20,'View Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].View_Height=bit.readwithlog('BD',dat,'View_Height',1)
	gpdwg.objects['temp'].View_Width=bit.readwithlog('BD',dat,'View_Width',1)
	gpdwg.objects['temp'].View_Center=bit.readwithlog('2RD',dat,'View_Center',1)
	gpdwg.objects['temp'].Target=bit.readwithlog('3BD',dat,'Target',1)
	gpdwg.objects['temp'].View_Dir=bit.readwithlog('3BD',dat,'View_Dir',1)
	gpdwg.objects['temp'].Twist_Angle=bit.readwithlog('BD',dat,'Twist_Angle',1)
	gpdwg.objects['temp'].Lens_Length=bit.readwithlog('BD',dat,'Lens_Length',1)
	gpdwg.objects['temp'].Front_Clip=bit.readwithlog('BD',dat,'Front_Clip',1)
	gpdwg.objects['temp'].Back_Clip=bit.readwithlog('BD',dat,'Back_Clip',1)
	TempViewMode=0
	for i in range(3,0,-1):
		TempViewMode=TempViewMode + bit.readwithlog('B',dat,'View_Mode',1) * 2 ^ i
	gpdwg.objects['temp'].View_Mode=TempViewMode
	gpdwg.objects['temp'].Render_Mode=bit.readwithlog('RC',dat,'Render_Mode',1)
	gpdwg.objects['temp'].Pspace_Flag=bit.readwithlog('B',dat,'Pspace_Flag',1)
	gpdwg.objects['temp'].Associated_UCS=bit.readwithlog('B',dat,'Associated_UCS',1)
	gpdwg.objects['temp'].Origin=bit.readwithlog('3BD',dat,'Origin',1)
	gpdwg.objects['temp'].Direction_X=bit.readwithlog('3BD',dat,'Direction_X',1)
	gpdwg.objects['temp'].Direction_Y=bit.readwithlog('3BD',dat,'Direction_Y',1)
	gpdwg.objects['temp'].Elevation=bit.readwithlog('BD',dat,'Elevation',1)
	gpdwg.objects['temp'].OrthographicViewType=bit.readwithlog('BS',dat,'OrthographicViewType',1)
	gpdwg.objects['temp'].View_Control_Object=bit.readwithlog('H',dat,'View_Control_Object',1)
	gpdwg.objects['temp'].Reactors=bit.readwithlog('H',dat,'Reactors',1)
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('H',dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('H',dat,'XrefBlockHandle',1)
	gpdwg.objects['temp'].Base_UCS_Handle=bit.readwithlog('H',dat,'Base_UCS_Handle',1)
	gpdwg.objects['temp'].Named_UCS_Handle=bit.readwithlog('H',dat,'Named_UCS_Handle',1)
	TempLog(20,'View End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_UCS_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_UCS_Control()
	TempLog(20,'UCS_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].UCS_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].UCS_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'UCS_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_UCS(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_UCS()
	TempLog(20,'UCS Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry_Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].Origin=bit.readwithlog('BD',dat,'View_Height',1)
	gpdwg.objects['temp'].Direction_X=bit.readwithlog('BD',dat,'View_Width',1)
	gpdwg.objects['temp'].Direction_Y=bit.readwithlog('2RD',dat,'View_Center',1)
	gpdwg.objects['temp'].Elevation=bit.readwithlog('3BD',dat,'Target',1)
	gpdwg.objects['temp'].OrthographicViewType=bit.readwithlog('3BD',dat,'View_Dir',1)
	gpdwg.objects['temp'].OrthographicType=bit.readwithlog('BD',dat,'Twist_Angle',1)
	gpdwg.objects['temp'].UCS_Control_Object=bit.readwithlog('BD',dat,'Lens_Length',1)
	gpdwg.objects['temp'].Reactors=bit.readwithlog('BD',dat,'Front_Clip',1)
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('BD',dat,'Back_Clip',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('B',dat,'View_Mode',1)
	gpdwg.objects['temp'].Base_UCS_Handle=bit.readwithlog('RC',dat,'Render_Mode',1)
	gpdwg.objects['temp'].Named_UCS_Handle=bit.readwithlog('B',dat,'Pspace_Flag',1)
	TempLog(20,'UCS End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VPORT(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Vport()
	TempLog(20,'Vport Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry_Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].View_Height=bit.readwithlog('BD',dat,'View_Height',1)
	gpdwg.objects['temp'].Aspect_Ratio=bit.readwithlog('BD',dat,'Aspect_Ratio',1)
	gpdwg.objects['temp'].View_Center=bit.readwithlog('2RD',dat,'View_Center',1)
	gpdwg.objects['temp'].View_Target=bit.readwithlog('3BD',dat,'View_Target',1)
	gpdwg.objects['temp'].View_Dir=bit.readwithlog('3BD',dat,'View_Dir',1)
	gpdwg.objects['temp'].View_Twist=bit.readwithlog('BD',dat,'View_Twist',1)
	gpdwg.objects['temp'].Lens_Length=bit.readwithlog('BD',dat,'Lens_Length',1)
	gpdwg.objects['temp'].Front_Clip=bit.readwithlog('BD',dat,'Front_Clip',1)
	gpdwg.objects['temp'].Back_Clip=bit.readwithlog('BD',dat,'Back_Clip',1)
	gpdwg.objects['temp'].View_Mode=bit.readwithlog('B',dat,'View_Mode1',1)
	gpdwg.objects['temp'].View_Mode=bit.readwithlog('B',dat,'View_Mode2',1)
	gpdwg.objects['temp'].View_Mode=bit.readwithlog('B',dat,'View_Mode3',1)
	gpdwg.objects['temp'].View_Mode=bit.readwithlog('B',dat,'View_Mode4',1)
	gpdwg.objects['temp'].Render_Mode=bit.readwithlog('RC',dat,'Render_Mode',1)
	gpdwg.objects['temp'].Lower_Left=bit.readwithlog('2RD',dat,'Lower_Left',1)
	gpdwg.objects['temp'].Upper_Right=bit.readwithlog('2RD',dat,'Upper_Right',1)
	gpdwg.objects['temp'].UCSFOLLOW=bit.readwithlog('B',dat,'UCSFOLLOW',1)
	gpdwg.objects['temp'].Circle_Zoom=bit.readwithlog('BS',dat,'Circle_Zoom',1)
	gpdwg.objects['temp'].Fast_Zoom=bit.readwithlog('B',dat,'Fast_Zoom',1)

	#TempUCSICON=0
	#for i in range(1,0,-1):
	#	TempUCSICON=TempUCSICON + bit.readwithlog('B',dat,'Icon',1) * 2 ^ i

	bit.readwithlog('B',dat,'Icon1',1)
	bit.readwithlog('B',dat,'Icon2',1)
	#gpdwg.objects['temp'].UCSICON=TempUCSICON
	gpdwg.objects['temp'].Grid_On_Off=bit.readwithlog('B',dat,'Grid_On_Off',1)
	gpdwg.objects['temp'].Grd_Spacing=bit.readwithlog('2RD',dat,'Grd_Spacing',1)
	gpdwg.objects['temp'].Snap_On_Off=bit.readwithlog('B',dat,'Snap_On_Off',1)
	gpdwg.objects['temp'].Snap_Style=bit.readwithlog('B',dat,'Snap_Style',1)
	gpdwg.objects['temp'].Snap_isopair=bit.readwithlog('BS',dat,'Snap_isopair',1)
	gpdwg.objects['temp'].Snap_Rot=bit.readwithlog('BD',dat,'Snap_Rot',1)
	gpdwg.objects['temp'].Snap_Base=bit.readwithlog('2RD',dat,'Snap_Base',1)
	gpdwg.objects['temp'].Snap_Spacing=bit.readwithlog('2RD',dat,'Snap_Spacing',1)
	gpdwg.objects['temp'].Unknown=bit.readwithlog('B',dat,'Unknown',1)
	gpdwg.objects['temp'].UCS_Per_Viewport=bit.readwithlog('B',dat,'UCS_Per_Viewport',1)
	gpdwg.objects['temp'].UCS_Origin=bit.readwithlog('3BD',dat,'UCS_Origin',1)
	gpdwg.objects['temp'].UCS_X=bit.readwithlog('3BD',dat,'UCS_X',1)
	gpdwg.objects['temp'].UCS_Y=bit.readwithlog('3BD',dat,'UCS_Y',1)
	gpdwg.objects['temp'].UCS_Elevation=bit.readwithlog('BD',dat,'UCS_Elevation',1)
	gpdwg.objects['temp'].UCS_Orthographic_Type=bit.readwithlog('BS',dat,'UCS_Orthographic_Type ',1)
	gpdwg.objects['temp'].Vport_Control_Object=bit.readwithlog('H',dat,'Vport_Control_Object',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('H',dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('H',dat,'XrefBlockHandle',1)
	gpdwg.objects['temp'].Base_UCS_Handle=bit.readwithlog('H',dat,'Base_UCS_Handle',1)
	gpdwg.objects['temp'].Named_UCS_Handle=bit.readwithlog('H',dat,'Named_UCS_Handle',1)
	TempLog(20,'Vport End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)



def decode_APPID_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Appid_Control()
	TempLog(20,'Appid_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].Appid_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].Appid_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'Appid_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_APPID(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Appid()
	TempLog(20,'Appid Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry_Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].Unknown=bit.readwithlog('RC',dat,'Unknown',1)
	gpdwg.objects['temp'].Appid_Control_Object=bit.readwithlog('H',dat,'Appid_Control_Object',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('H',dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('H',dat,'XrefBlockHandle',1)
	TempLog(20,'Appid End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMSTYLE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_Dimstyle()
	TempLog(20,'Dimstyle Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry_Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].DIMPOST=bit.readwithlog('TV',dat,'DIMPOST',1)
	gpdwg.objects['temp'].DIMAPOST=bit.readwithlog('TV',dat,'DIMAPOST',1)
	gpdwg.objects['temp'].DIMSCALE=bit.readwithlog('BD',dat,'DIMSCALE',1)
	gpdwg.objects['temp'].DIMASZ=bit.readwithlog('BD',dat,'DIMASZ',1)
	gpdwg.objects['temp'].DIMEXO=bit.readwithlog('BD',dat,'DIMEXO',1)
	gpdwg.objects['temp'].DIMDLI=bit.readwithlog('BD',dat,'DIMDLI',1)
	gpdwg.objects['temp'].DIMEXE=bit.readwithlog('BD',dat,'DIMEXE',1)
	gpdwg.objects['temp'].DIMRND=bit.readwithlog('BD',dat,'DIMRND',1)
	gpdwg.objects['temp'].DIMDLE=bit.readwithlog('BD',dat,'DIMDLE',1)
	gpdwg.objects['temp'].DIMTP=bit.readwithlog('BD',dat,'DIMTP',1)
	gpdwg.objects['temp'].DIMTM=bit.readwithlog('BD',dat,'DIMTM',1)
	gpdwg.objects['temp'].DIMTOL=bit.readwithlog('B',dat,'DIMTOL',1)
	gpdwg.objects['temp'].DIMLIM=bit.readwithlog('B',dat,'DIMLIM',1)
	gpdwg.objects['temp'].DIMTIH=bit.readwithlog('B',dat,'DIMTIH',1)
	gpdwg.objects['temp'].DIMTOH=bit.readwithlog('B',dat,'DIMTOH',1)
	gpdwg.objects['temp'].DIMSE1=bit.readwithlog('B',dat,'DIMSE1',1)
	gpdwg.objects['temp'].DIMSE2=bit.readwithlog('B',dat,'DIMSE2',1)
	gpdwg.objects['temp'].DIMTAD=bit.readwithlog('BS',dat,'DIMTAD',1)
	gpdwg.objects['temp'].DIMZIN=bit.readwithlog('BS',dat,'DIMZIN',1)
	gpdwg.objects['temp'].DIMAZIN=bit.readwithlog('BS',dat,'DIMAZIN',1)
	gpdwg.objects['temp'].DIMTXT=bit.readwithlog('BD',dat,'DIMTXT',1)
	gpdwg.objects['temp'].DIMCEN=bit.readwithlog('BD',dat,'DIMCEN',1)
	gpdwg.objects['temp'].DIMTSZ=bit.readwithlog('BD',dat,'DIMTSZ',1)
	gpdwg.objects['temp'].DIMALTF=bit.readwithlog('BD',dat,'DIMALTF',1)
	gpdwg.objects['temp'].DIMLFAC=bit.readwithlog('BD',dat,'DIMLFAC',1)
	gpdwg.objects['temp'].DIMTVP=bit.readwithlog('BD',dat,'DIMTVP',1)
	gpdwg.objects['temp'].DIMTFAC=bit.readwithlog('BD',dat,'DIMTFAC',1)
	gpdwg.objects['temp'].DIMGAP=bit.readwithlog('BD',dat,'DIMGAP',1)
	gpdwg.objects['temp'].DIMALTRND=bit.readwithlog('BD',dat,'DIMALTRND',1)
	gpdwg.objects['temp'].DIMALT=bit.readwithlog('B',dat,'DIMALT',1)
	gpdwg.objects['temp'].DIMALTD=bit.readwithlog('BS',dat,'DIMALTD',1)
	gpdwg.objects['temp'].DIMTOFL=bit.readwithlog('B',dat,'DIMTOFL',1)
	gpdwg.objects['temp'].DIMSAH=bit.readwithlog('B',dat,'DIMSAH',1)
	gpdwg.objects['temp'].DIMTIX=bit.readwithlog('B',dat,'DIMTIX',1)
	gpdwg.objects['temp'].DIMSOXD=bit.readwithlog('B',dat,'DIMSOXD',1)
	gpdwg.objects['temp'].DIMCLRD=bit.readwithlog('BS',dat,'DIMCLRD',1)
	gpdwg.objects['temp'].DIMCLRE=bit.readwithlog('BS',dat,'DIMCLRE',1)
	gpdwg.objects['temp'].DIMCLRT=bit.readwithlog('BS',dat,'DIMCLRT',1)
	gpdwg.objects['temp'].DIMADEC=bit.readwithlog('BS',dat,'DIMADEC',1)
	gpdwg.objects['temp'].DIMDEC=bit.readwithlog('BS',dat,'DIMDEC',1)
	gpdwg.objects['temp'].DIMTDEC=bit.readwithlog('BS',dat,'DIMTDEC',1)
	gpdwg.objects['temp'].DIMALTU=bit.readwithlog('BS',dat,'DIMALTU',1)
	gpdwg.objects['temp'].DIMALTTD=bit.readwithlog('BS',dat,'DIMALTTD',1)
	gpdwg.objects['temp'].DIMAUNIT=bit.readwithlog('BS',dat,'DIMAUNIT',1)
	gpdwg.objects['temp'].DIMFRAC=bit.readwithlog('BS',dat,'DIMFRAC',1)
	gpdwg.objects['temp'].DIMLUNIT=bit.readwithlog('BS',dat,'DIMLUNIT',1)
	gpdwg.objects['temp'].DIMDSEP=bit.readwithlog('BS',dat,'DIMDSEP',1)
	gpdwg.objects['temp'].DIMTMOVE=bit.readwithlog('BS',dat,'DIMTMOVE',1)
	gpdwg.objects['temp'].DIMJUST=bit.readwithlog('BS',dat,'DIMJUST',1)
	gpdwg.objects['temp'].DIMSD1=bit.readwithlog('B',dat,'DIMSD1',1)
	gpdwg.objects['temp'].DIMSD2=bit.readwithlog('B',dat,'DIMSD2',1)
	gpdwg.objects['temp'].DIMTOLJ=bit.readwithlog('BS',dat,'DIMTOLJ',1)
	gpdwg.objects['temp'].DIMTZIN=bit.readwithlog('BS',dat,'DIMTZIN',1)
	gpdwg.objects['temp'].DIMALTZ=bit.readwithlog('BS',dat,'DIMALTZ',1)
	gpdwg.objects['temp'].DIMALTTZ=bit.readwithlog('BS',dat,'DIMALTTZ',1)
	gpdwg.objects['temp'].DIMUPT=bit.readwithlog('B',dat,'DIMUPT',1)
	gpdwg.objects['temp'].DIMFIT=bit.readwithlog('BS',dat,'DIMFIT',1)
	gpdwg.objects['temp'].DIMLWD=bit.readwithlog('BS',dat,'DIMLWD',1)
	gpdwg.objects['temp'].DIMLWE=bit.readwithlog('BS',dat,'DIMLWE',1)
	gpdwg.objects['temp'].Unknown=bit.readwithlog('B',dat,'Unknown',1)
	gpdwg.objects['temp'].Dimstyle_Control_Object=bit.readwithlog('H',dat,'Dimstyle_Control_Object',1)
	gpdwg.objects['temp'].Reactors=bit.readwithlog('H',dat,'Reactors',1)
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('H',dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('H',dat,'XrefBlockHandle',1)
	gpdwg.objects['temp'].DIMTXSTY=bit.readwithlog('H',dat,'DIMTXSTY',1)
	gpdwg.objects['temp'].DIMLDRBLK=bit.readwithlog('H',dat,'DIMLDRBLK',1)
	gpdwg.objects['temp'].DIMBLK=bit.readwithlog('H',dat,'DIMBLK',1)
	gpdwg.objects['temp'].DIMBLK1=bit.readwithlog('H',dat,'DIMBLK1',1)
	gpdwg.objects['temp'].DIMBLK2=bit.readwithlog('H',dat,'DIMBLK2',1)
	TempLog(20,'DimStyle End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VP_ENT_HDR_CONTROL(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_VP_ENT_HDR_Control()
	TempLog(20,'VP_ENT_HDR_Control Start')
	if not decode_non_entity(gpdwg,dat): return False
	Num_Entries= int(bit.readwithlog("BS",dat,'Num_Entries',1))
	gpdwg.objects['temp'].Num_Entries=Num_Entries
	gpdwg.objects['temp'].Null_Handle_Refs = bit.readwithlog("H",dat,'Null_handle',1)
	gpdwg.objects['temp'].xdic_obj_handle=bit.readwithlog("H",dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].VP_ENT_HDR_Handle=[]
	for i in xrange(Num_Entries):
		gpdwg.objects['temp'].VP_ENT_HDR_Handle.append(bit.readwithlog("H",dat,'Handle '+str(i),1))
	TempLog(20,'VP_ENT_HDR_Control End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VP_ENT_HDR(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_VP_ENT_HDR()
	TempLog(20,'VP_ENT_HDR Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Entry_Name=bit.readwithlog('TV',dat,'Entry_Name',1)
	gpdwg.objects['temp'].Flag_64=bit.readwithlog('B',dat,'Flag_64',1)
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog('BS',dat,'xrefindex1',1)
	gpdwg.objects['temp'].Xdep=bit.readwithlog('B',dat,'Xdep',1)
	gpdwg.objects['temp'].Flag_1=bit.readwithlog('B',dat,'Flag1',1)
	gpdwg.objects['temp'].VP_ENT_HDR_Control_Object=bit.readwithlog('H',dat,'VP_ENT_HDR_Control_Object',1)
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog('H',dat,'xdicobjhandle',1)
	gpdwg.objects['temp'].XrefBlockHandle=bit.readwithlog('H',dat,'XrefBlockHandle',1)
	gpdwg.objects['temp'].VP_ENT_HDR=bit.readwithlog('H',dat,'VP_ENT_HDR',1)
	gpdwg.objects['temp'].Prev_VP_ENT_HDR=bit.readwithlog('H',dat,'Prev_VP_ENT_HDR',1)
	TempLog(20,'VP_ENT_HDR End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_GROUP(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_group()
	TempLog(20,'Group Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Name=bit.readwithlog('TV',dat,'Name',1)
	gpdwg.objects['temp'].Unnamed=bit.readwithlog('BS',dat,'UnNamed',1)
	gpdwg.objects['temp'].Selectable=bit.readwithlog('BS',dat,'Selectable',1)
	NumHandles=int(bit.readwithlog('BL',dat,'Numhandles',1))
	gpdwg.objects['temp'].Numhandles=NumHandles
	gpdwg.objects['temp'].ParentHandle=bit.readwithlog('H',dat,'Parent Handle',1)
	gpdwg.objects['temp'].Reactor_Handle=[]
	for i in xrange(gpdwg.objects['temp'].NumReactors):
		gpdwg.objects['temp'].Reactor_Handle.append(bit.readwithlog('H',dat,'Reactor_Handle ' + str(i),1))
	gpdwg.objects['temp'].GroupEntries_Handle=[]
	for i in xrange(NumHandles):
		gpdwg.objects['temp'].GroupEntries_Handle.append(bit.readwithlog("H",dat,'Group_Entries_Handle '+str(i),1))
	TempLog(20,'Group End\n\n')
	TempLog(20,str(dat.byte)+"\t"+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MLINESTYLE(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_mlinestyle()
	TempLog(20,'MLINEStyle Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].Name=bit.readwithlog('TV',dat,'Name',1)
	gpdwg.objects['temp'].Desc=bit.readwithlog('TV',dat,'Desc',1)
	gpdwg.objects['temp'].Flags=bit.readwithlog('BS',dat,'Flags',1)
	gpdwg.objects['temp'].fillcolor=bit.readwithlog('CMC',dat,'fillcolor',1)
	gpdwg.objects['temp'].startang=bit.readwithlog('BD',dat,'startang',1)
	gpdwg.objects['temp'].endang=bit.readwithlog('BD',dat,'endang',1)
	linesinstyle=bit.readwithlog('RC',dat,'linesinstyle',1)
	gpdwg.objects['temp'].linesinstyle=linesinstyle
	gpdwg.objects['temp'].lines=[]
	for i in xrange(linesinstyle):
		TempLine=gpdwg.dwg_MLS_Line()
		TempLine.Offset=bit.readwithlog('BD',dat,'Offset',1)
		TempLine.Color=bit.readwithlog('CMC',dat,'Color',1)
		TempLine.Ltindex=bit.readwithlog('BS',dat,'Ltindex',1)
		gpdwg.objects['temp'].lines.append(TempLine)
	gpdwg.objects['temp'].parenthandle =bit.readwithlog('H',dat,'parenthandle ',1)
	gpdwg.objects['temp'].Reactors =bit.readwithlog('H',dat,'Reactors ',1)
	gpdwg.objects['temp'].xdicobjhandle =bit.readwithlog('H',dat,'xdicobjhandle ',1)
	TempLog(20,'MLINEStyle End\n\n')
	return Check_Obj_CRC(dat,Obj_Size)

def decode_OLE2FRAME(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"OLE2FRAME")
	#if not decode_entity(gpdwg,dat): return False
def decode_DUMMY(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"DUMMY")
	#if not decode_entity(gpdwg,dat): return False
def decode_LONG_TRANSACTION(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"LONG_TRANSACTION")
	#if not decode_entity(gpdwg,dat): return False
def decode_LWPLINE(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"LWPLINE")
	#if not decode_entity(gpdwg,dat): return False
def decode_HATCH(gpdwg,dat):
	#log.LogOnOff=True
	Obj_Size=gpdwg.objects['temp']['size']
	TempLog(20,'Object Size '+str(Obj_Size))
	gpdwg.objects['temp']=gpdwg.dwg_mlinestyle()
	TempLog(20,'Hatch Start')


def decode_XRECORD(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"XRECORD")
	#if not decode_entity(gpdwg,dat): return False
def decode_PLACEHOLDER(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"PLACEHOLDER")
	#if not decode_entity(gpdwg,dat): return False
def decode_VBA_PROJECT(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"VBA_PROJECT")
	#if not decode_entity(gpdwg,dat): return False
def decode_LAYOUT(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"LAYOUT")
	#if not decode_entity(gpdwg,dat): return False
def decode_ACAD_PROXY_ENTITY(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"ACAD_PROXY_ENTITY")
	#if not decode_entity(gpdwg,dat): return False
def	decode_ACAD_PROXY_OBJECT(gpdwg,dat):
	global Temp
	TempLog(9,Temp+"	"+"ACAD_PROXY_OBJECT")
	#if not decode_entity(gpdwg,dat): return False
