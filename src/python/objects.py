
#############################################################################
#  gpdwg - free python package to read .dwg files.                          #
#                                                                           #
#  Copyright (C) 2018 Guruprasad Rane <raneguruprasad@gmail.com>            #
#                                                                           #
#  This library is free software, licensed under the terms of the GNU       #
#  General Public License version 3. You should have received a copy of     #
#  the GNU General Public License along with this program.                  #
#                                                                           #
#############################################################################

#!/usr/bin/env python3
import bit, logging, libgpdwg
logger = logging.getLogger("gpdwg_logger")
Temp=""
def decode_TEXT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_text()
	TempLog(20,'TEXT Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version >= 2000:
		gpdwg.objects['temp'].data_flags=bit.readwithlog2('RC',dat,'data_flags')
		if not int(gpdwg.objects['temp'].data_flags) & 0x01:
			gpdwg.objects['temp'].elevation=bit.readwithlog2('RD', dat,'elevation')
		gpdwg.objects['temp'].insertion_point=bit.readwithlog2('2RD',dat,'insertion_point')
		if not int(gpdwg.objects['temp'].data_flags) & 0x02:
			gpdwg.objects['temp'].alignment_point=bit.readwithlog2('2DD', dat,'alignment_point', [10,20])
		gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
		gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
		if not int(gpdwg.objects['temp'].data_flags) & 0x04:
			gpdwg.objects['temp'].oblique_angle=bit.readwithlog2('RD', dat,'oblique_angle')
		if not int(gpdwg.objects['temp'].data_flags) & 0x08:
			gpdwg.objects['temp'].rotation_angle=bit.readwithlog2('RD', dat,'rotation_angle')
		gpdwg.objects['temp'].height=bit.readwithlog2('RD',dat,'height')
		if not int(gpdwg.objects['temp'].data_flags) & 0x10:
			gpdwg.objects['temp'].width_factor=bit.readwithlog2('RD', dat,'width_factor')
		gpdwg.objects['temp'].text_value=bit.readwithlog2('TV',dat,'text_value')
		if not int(gpdwg.objects['temp'].data_flags) & 0x20:
			gpdwg.objects['temp'].generation=bit.readwithlog2('BS', dat,'generation')
		if not int(gpdwg.objects['temp'].data_flags) & 0x40:
			gpdwg.objects['temp'].horizontal_align=bit.readwithlog2('BS', dat,'horizontal_align')
		if not int(gpdwg.objects['temp'].data_flags) & 0x80:
			gpdwg.objects['temp'].vertical_align=bit.readwithlog2('BS', dat,'vertical_align')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].style=bit.readwithlog2('H',dat,'style')
	TempLog(20,'TEXT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ATTRIB(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_attrib()
	TempLog(20,'ATTRIB Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version >= 2000:
		gpdwg.objects['temp'].data_flags=bit.readwithlog2('RC',dat,'data_flags')
		if not int(gpdwg.objects['temp'].data_flags) & 0x01:
			gpdwg.objects['temp'].elevation=bit.readwithlog2('RD', dat,'elevation')
		gpdwg.objects['temp'].insertion_point=bit.readwithlog2('2RD',dat,'insertion_point')
		if not int(gpdwg.objects['temp'].data_flags) & 0x02:
			gpdwg.objects['temp'].alignment_point=bit.readwithlog2('2DD', dat,'alignment_point')
		gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
		gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
		if not int(gpdwg.objects['temp'].data_flags) & 0x04:
			gpdwg.objects['temp'].oblique_angle=bit.readwithlog2('RD', dat,'oblique_angle')
		if not int(gpdwg.objects['temp'].data_flags) & 0x08:
			gpdwg.objects['temp'].rotation_angle=bit.readwithlog2('RD', dat,'rotation_angle')
		gpdwg.objects['temp'].height=bit.readwithlog2('RD',dat,'height')
		if not int(gpdwg.objects['temp'].data_flags) & 0x10:
			gpdwg.objects['temp'].width_factor=bit.readwithlog2('RD', dat,'width_factor')
		gpdwg.objects['temp'].text_value=bit.readwithlog2('TV',dat,'text_value')
		if not int(gpdwg.objects['temp'].data_flags) & 0x20:
			gpdwg.objects['temp'].generation=bit.readwithlog2('BS', dat,'generation')
		if not int(gpdwg.objects['temp'].data_flags) & 0x40:
			gpdwg.objects['temp'].horizontal_align=bit.readwithlog2('BS', dat,'horizontal_align')
		if not int(gpdwg.objects['temp'].data_flags) & 0x80:
			gpdwg.objects['temp'].vertical_align=bit.readwithlog2('BS', dat,'vertical_align')
	if dat.version >= 2010:
		gpdwg.objects['temp'].version=bit.readwithlog2('RC',dat,'version')
	gpdwg.objects['temp'].tag=bit.readwithlog2('TV',dat,'tag')
	gpdwg.objects['temp'].field_length=bit.readwithlog2('BS',dat,'field_length')
	gpdwg.objects['temp'].flags=bit.readwithlog2('RC',dat,'flags')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].style=bit.readwithlog2('H',dat,'style')
	TempLog(20,'ATTRIB End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ATTDEF(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_attdef()
	TempLog(20,'ATTDEF Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version >= 2000:
		gpdwg.objects['temp'].data_flags=bit.readwithlog2('RC',dat,'data_flags')
		if not int(gpdwg.objects['temp'].data_flags) & 0x01:
			gpdwg.objects['temp'].elevation=bit.readwithlog2('RD', dat,'elevation')
		gpdwg.objects['temp'].insertion_point=bit.readwithlog2('2RD',dat,'insertion_point')
		if not int(gpdwg.objects['temp'].data_flags) & 0x02:
			gpdwg.objects['temp'].alignment_point=bit.readwithlog2('2DD', dat,'alignment_point')
		gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
		gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
		if not int(gpdwg.objects['temp'].data_flags) & 0x04:
			gpdwg.objects['temp'].oblique_angle=bit.readwithlog2('RD', dat,'oblique_angle')
		if not int(gpdwg.objects['temp'].data_flags) & 0x08:
			gpdwg.objects['temp'].rotation_angle=bit.readwithlog2('RD', dat,'rotation_angle')
		gpdwg.objects['temp'].height=bit.readwithlog2('RD',dat,'height')
		if not int(gpdwg.objects['temp'].data_flags) & 0x10:
			gpdwg.objects['temp'].width_factor=bit.readwithlog2('RD', dat,'width_factor')
		gpdwg.objects['temp'].text_value=bit.readwithlog2('TV',dat,'text_value')
		if not int(gpdwg.objects['temp'].data_flags) & 0x20:
			gpdwg.objects['temp'].generation=bit.readwithlog2('BS', dat,'generation')
		if not int(gpdwg.objects['temp'].data_flags) & 0x40:
			gpdwg.objects['temp'].horizontal_align=bit.readwithlog2('BS', dat,'horizontal_align')
		if not int(gpdwg.objects['temp'].data_flags) & 0x80:
			gpdwg.objects['temp'].vertical_align=bit.readwithlog2('BS', dat,'vertical_align')
	if dat.version >= 2010:
		gpdwg.objects['temp'].version=bit.readwithlog2('RC',dat,'version')
	gpdwg.objects['temp'].tag=bit.readwithlog2('TV',dat,'tag')
	gpdwg.objects['temp'].field_length=bit.readwithlog2('BS',dat,'field_length')
	gpdwg.objects['temp'].flags=bit.readwithlog2('RC',dat,'flags')
	gpdwg.objects['temp'].prompt=bit.readwithlog2('TV',dat,'prompt')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].style=bit.readwithlog2('H',dat,'style')
	TempLog(20,'ATTDEF End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_BLOCK(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_block()
	TempLog(20,'BLOCK Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].block_name=bit.readwithlog2('TV',dat,'block_name')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'BLOCK End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ENDBLK(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_endblk()
	TempLog(20,'ENDBLK Start')
	if not decode_entity(gpdwg,dat): return False
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'ENDBLK End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SEQEND(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_seqend()
	TempLog(20,'SEQEND Start')
	if not decode_entity(gpdwg,dat): return False
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'SEQEND End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_INSERT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_insert()
	TempLog(20,'INSERT Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].insertion_point=bit.readwithlog2('3BD',dat,'insertion_point')
	if dat.version <= 14:
		gpdwg.objects['temp'].scale_x=bit.readwithlog2('BD',dat,'scale_x')
		gpdwg.objects['temp'].scale_y=bit.readwithlog2('BD',dat,'scale_y')
		gpdwg.objects['temp'].scale_z=bit.readwithlog2('BD',dat,'scale_z')
	if dat.version >= 2000:
		gpdwg.objects['temp'].scale_flag=bit.readwithlog2('BB',dat,'scale_flag')

		#custom output for insert begin.
		CustomData=bit.point3D()
		if gpdwg.objects['temp'].scale_flag == 3:
			CustomData.x=1
			CustomData.y=1
			CustomData.z=1
		elif gpdwg.objects['temp'].scale_flag == 1:
			CustomData.x=1
			CustomData.y=bit.readwithlog("DD",dat,"Scale Y",1,1)
			CustomData.z=bit.readwithlog("DD",dat,"Scale Z",1,1)
		elif gpdwg.objects['temp'].scale_flag == 2:
			CustomData.x=bit.readwithlog("RD",dat,"Scale X",1)
			CustomData.y=CustomData.x
			CustomData.z=CustomData.x
		else:
			CustomData.x=bit.readwithlog("RD",dat,"Scale X",1)
			CustomData.y=bit.readwithlog("DD",dat,"Scale Y",1,CustomData.x)
			CustomData.z=bit.readwithlog("DD",dat,"Scale Z",1,CustomData.x)
		#custom output for insert end.
		gpdwg.objects['temp'].scale=CustomData
	gpdwg.objects['temp'].rotation=bit.readwithlog2('BD',dat,'rotation')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].attribute_flag=bit.readwithlog2('B',dat,'attribute_flag')
	if dat.version >= 2004:
		gpdwg.objects['temp'].num_objects=bit.readwithlog2('BL',dat,'num_objects')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].block_header=bit.readwithlog2('H',dat,'block_header')
	if dat.version <= 2000:
		if gpdwg.objects['temp'].attribute_flag == 1:
			gpdwg.objects['temp'].attrib_first=bit.readwithlog2('H', dat,'attrib_first')
			gpdwg.objects['temp'].attrib_last=bit.readwithlog2('H', dat,'attrib_last')
	if dat.version == 2004:
		for i in range(int(gpdwg.objects['temp'].num_objects)):
			add_to_list(gpdwg.objects['temp'], 'attribs', bit.readwithlog2('H', dat,' attribs '+str(i)))
	if gpdwg.objects['temp'].attribute_flag == 1:
		gpdwg.objects['temp'].seqend=bit.readwithlog2('H', dat,'seqend')
	TempLog(20,'INSERT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MINSERT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_minsert()
	TempLog(20,'MINSERT Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].ins_point=bit.readwithlog2('3BD',dat,'ins_point')
	if dat.version <= 14:
		gpdwg.objects['temp'].scale_x=bit.readwithlog2('BD',dat,'scale_x')
		gpdwg.objects['temp'].scale_y=bit.readwithlog2('BD',dat,'scale_y')
		gpdwg.objects['temp'].scale_z=bit.readwithlog2('BD',dat,'scale_z')
	if dat.version >= 2000:
		gpdwg.objects['temp'].scale_flags=bit.readwithlog2('BB',dat,'scale_flags')

		#custom output for insert begin.
		CustomData=bit.point3D()
		if gpdwg.objects['temp'].scale_flag == 3:
			CustomData.x=1
			CustomData.y=1
			CustomData.z=1
		elif gpdwg.objects['temp'].scale_flag == 1:
			CustomData.x=1
			CustomData.y=bit.readwithlog("DD",dat,"Scale Y",1,1)
			CustomData.z=bit.readwithlog("DD",dat,"Scale Z",1,1)
		elif gpdwg.objects['temp'].scale_flag == 2:
			CustomData.x=bit.readwithlog("RD",dat,"Scale X",1)
			CustomData.y=CustomData.x
			CustomData.z=CustomData.x
		else:
			CustomData.x=bit.readwithlog("RD",dat,"Scale X",1)
			CustomData.y=bit.readwithlog("DD",dat,"Scale Y",1,CustomData.x)
			CustomData.z=bit.readwithlog("DD",dat,"Scale Z",1,CustomData.x)
		#custom output for insert end.
		gpdwg.objects['temp'].scale=CustomData
	gpdwg.objects['temp'].rotation=bit.readwithlog2('BD',dat,'rotation')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].attribute_flag=bit.readwithlog2('B',dat,'attribute_flag')
	if dat.version >= 2004:
		gpdwg.objects['temp'].num_objects=bit.readwithlog2('BL',dat,'num_objects')
	gpdwg.objects['temp'].num_cols=bit.readwithlog2('BS',dat,'num_cols')
	gpdwg.objects['temp'].num_rows=bit.readwithlog2('BS',dat,'num_rows')
	gpdwg.objects['temp'].col_spacing=bit.readwithlog2('BD',dat,'col_spacing')
	gpdwg.objects['temp'].row_spacing=bit.readwithlog2('BD',dat,'row_spacing')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].block_header=bit.readwithlog2('H',dat,'block_header')
	if dat.version <= 2000:
		if gpdwg.objects['temp'].attribute_flag == 1:
			gpdwg.objects['temp'].attrib_first=bit.readwithlog2('H', dat,'attrib_first')
			gpdwg.objects['temp'].attrib_last=bit.readwithlog2('H', dat,'attrib_last')
	if dat.version == 2004:
		for i in range(int(gpdwg.objects['temp'].num_objects)):
			add_to_list(gpdwg.objects['temp'], 'attribs', bit.readwithlog2('H', dat,' attribs '+str(i)))
	if gpdwg.objects['temp'].attribute_flag == 1:
		gpdwg.objects['temp'].seqend=bit.readwithlog2('H', dat,'seqend')
	TempLog(20,'MINSERT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_UNKNOWN(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_unknown()
	TempLog(20,'UNKNOWN Start')
def decode_VERTEX_2D(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vertex_2d()
	TempLog(20,'VERTEX_2D Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flags=bit.readwithlog2('RC',dat,'flags')
	gpdwg.objects['temp'].point=bit.readwithlog2('3BD',dat,'point')
	gpdwg.objects['temp'].start_width=bit.readwithlog2('BD',dat,'start_width')
	gpdwg.objects['temp'].bulge=bit.readwithlog2('BD',dat,'bulge')
	if dat.version >= 2010:
		gpdwg.objects['temp'].vertex_id=bit.readwithlog2('BL',dat,'vertex_id')
	gpdwg.objects['temp'].tangent_direction=bit.readwithlog2('BD',dat,'tangent_direction')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'VERTEX_2D End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_3D(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vertex_3d()
	TempLog(20,'VERTEX_3D Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flags=bit.readwithlog2('RC',dat,'flags')
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'VERTEX_3D End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_MESH(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vertex_mesh()
	TempLog(20,'VERTEX_MESH Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flags=bit.readwithlog2('RC',dat,'flags')
	gpdwg.objects['temp'].point=bit.readwithlog2('3BD',dat,'point')
	TempLog(20,'VERTEX_MESH End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_PFACE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vertex_pface()
	TempLog(20,'VERTEX_PFACE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flags=bit.readwithlog2('RC',dat,'flags')
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'VERTEX_PFACE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VERTEX_PFACE_FACE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vertex_pface_face()
	TempLog(20,'VERTEX_PFACE_FACE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].vertex_index_1=bit.readwithlog2('BS',dat,'vertex_index_1')
	gpdwg.objects['temp'].vertex_index_2=bit.readwithlog2('BS',dat,'vertex_index_2')
	gpdwg.objects['temp'].vertex_index_3=bit.readwithlog2('BS',dat,'vertex_index_3')
	gpdwg.objects['temp'].vertex_index_4=bit.readwithlog2('BS',dat,'vertex_index_4')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'VERTEX_PFACE_FACE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POLYLINE_2D(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_polyline_2d()
	TempLog(20,'POLYLINE_2D Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flags=bit.readwithlog2('BS',dat,'flags')
	gpdwg.objects['temp'].curve_type=bit.readwithlog2('BS',dat,'curve_type')
	gpdwg.objects['temp'].start_width=bit.readwithlog2('BD',dat,'start_width')
	gpdwg.objects['temp'].end_width=bit.readwithlog2('BD',dat,'end_width')
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].elevation=bit.readwithlog2('BD',dat,'elevation')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	if dat.version >= 2004:
		gpdwg.objects['temp'].num_objects=bit.readwithlog2('BL',dat,'num_objects')
	if not decode_entity_handles(gpdwg,dat): return False
	if dat.version <= 2000:
		gpdwg.objects['temp'].vertex_first=bit.readwithlog2('H',dat,'vertex_first')
		gpdwg.objects['temp'].vertex_last=bit.readwithlog2('H',dat,'vertex_last')
	if dat.version >= 2004:
		for i in range(int(gpdwg.objects['temp'].num_objects)):
			add_to_list(gpdwg.objects['temp'], 'vertex', bit.readwithlog2('H', dat,' vertex '+str(i)))
	gpdwg.objects['temp'].seqend=bit.readwithlog2('H',dat,'seqend')
	TempLog(20,'POLYLINE_2D End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POLYLINE_3D(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_polyline_3d()
	TempLog(20,'POLYLINE_3D Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].spline_flags=bit.readwithlog2('RC',dat,'spline_flags')
	gpdwg.objects['temp'].closed_flags=bit.readwithlog2('RC',dat,'closed_flags')
	if dat.version >= 2004:
		gpdwg.objects['temp'].num_objects=bit.readwithlog2('BL',dat,'num_objects')
	if not decode_entity_handles(gpdwg,dat): return False
	if dat.version <= 2000:
		gpdwg.objects['temp'].vertex_first=bit.readwithlog2('H',dat,'vertex_first')
		gpdwg.objects['temp'].vertex_last=bit.readwithlog2('H',dat,'vertex_last')
	if dat.version >= 2004:
		for i in range(int(gpdwg.objects['temp'].num_objects)):
			add_to_list(gpdwg.objects['temp'], 'vertex', bit.readwithlog2('H', dat,' vertex '+str(i)))
	gpdwg.objects['temp'].seqend=bit.readwithlog2('H',dat,'seqend')
	TempLog(20,'POLYLINE_3D End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ARC(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_arc()
	TempLog(20,'ARC Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].center=bit.readwithlog2('3BD',dat,'center')
	gpdwg.objects['temp'].radius=bit.readwithlog2('BD',dat,'radius')
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	gpdwg.objects['temp'].angle_start=bit.readwithlog2('BD',dat,'angle_start')
	gpdwg.objects['temp'].angle_end=bit.readwithlog2('BD',dat,'angle_end')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'ARC End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_CIRCLE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_circle()
	TempLog(20,'CIRCLE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].center=bit.readwithlog2('3BD',dat,'center')
	gpdwg.objects['temp'].radius=bit.readwithlog2('BD',dat,'radius')
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'CIRCLE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LINE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_line()
	TempLog(20,'LINE Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version <= 14:
		gpdwg.objects['temp'].start_point=bit.readwithlog2('3BD',dat,'start_point')
		gpdwg.objects['temp'].end_point=bit.readwithlog2('3BD',dat,'end_point')
	if dat.version >= 2000:
		gpdwg.objects['temp'].z_flag=bit.readwithlog2('B',dat,'z_flag')
		gpdwg.objects['temp'].start_point_x=bit.readwithlog2('RD',dat,'start_point_x')
		gpdwg.objects['temp'].end_point_x=bit.readwithlog2('DD',dat,'end_point_x', 10)
		gpdwg.objects['temp'].start_point_y=bit.readwithlog2('RD',dat,'start_point_y')
		gpdwg.objects['temp'].end_point_y=bit.readwithlog2('DD',dat,'end_point_y', 20)
		if gpdwg.objects['temp'].z_flag == 0:
			gpdwg.objects['temp'].start_point_z=bit.readwithlog2('RD', dat,'start_point_z')
			gpdwg.objects['temp'].end_point_z=bit.readwithlog2('DD', dat,'end_point_z', 30)
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'LINE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_ORDINATE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_ordinate()
	TempLog(20,'DIMENSION_ORDINATE Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	gpdwg.objects['temp'].point_13=bit.readwithlog2('3BD',dat,'point_13')
	gpdwg.objects['temp'].point_14=bit.readwithlog2('3BD',dat,'point_14')
	gpdwg.objects['temp'].flag_2=bit.readwithlog2('RC',dat,'flag_2')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_ORDINATE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_LINEAR(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_linear()
	TempLog(20,'DIMENSION_LINEAR Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_13=bit.readwithlog2('3BD',dat,'point_13')
	gpdwg.objects['temp'].point_14=bit.readwithlog2('3BD',dat,'point_14')
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	gpdwg.objects['temp'].extension_line_rotation=bit.readwithlog2('BD',dat,'extension_line_rotation')
	gpdwg.objects['temp'].dimension_rotation=bit.readwithlog2('BD',dat,'dimension_rotation')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_LINEAR End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_ALIGNED(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_aligned()
	TempLog(20,'DIMENSION_ALIGNED Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_13=bit.readwithlog2('3BD',dat,'point_13')
	gpdwg.objects['temp'].point_14=bit.readwithlog2('3BD',dat,'point_14')
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	gpdwg.objects['temp'].extension_line_rotation=bit.readwithlog2('BD',dat,'extension_line_rotation')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_ALIGNED End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_ANG3PT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_ang3pt()
	TempLog(20,'DIMENSION_ANG3PT Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	gpdwg.objects['temp'].point_13=bit.readwithlog2('3BD',dat,'point_13')
	gpdwg.objects['temp'].point_14=bit.readwithlog2('3BD',dat,'point_14')
	gpdwg.objects['temp'].point_15=bit.readwithlog2('3BD',dat,'point_15')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_ANG3PT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_ANG2LN(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_ang2ln()
	TempLog(20,'DIMENSION_ANG2LN Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_16=bit.readwithlog2('2RD',dat,'point_16')
	gpdwg.objects['temp'].point_13=bit.readwithlog2('3BD',dat,'point_13')
	gpdwg.objects['temp'].point_14=bit.readwithlog2('3BD',dat,'point_14')
	gpdwg.objects['temp'].point_15=bit.readwithlog2('3BD',dat,'point_15')
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_ANG2LN End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_RADIUS(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_radius()
	TempLog(20,'DIMENSION_RADIUS Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3RD',dat,'point_10')
	gpdwg.objects['temp'].point_15=bit.readwithlog2('3BD',dat,'point_15')
	gpdwg.objects['temp'].leader_length=bit.readwithlog2('BD',dat,'leader_length')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_RADIUS End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMENSION_DIAMETER(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimension_diameter()
	TempLog(20,'DIMENSION_DIAMETER Start')
	if not decode_entity(gpdwg,dat): return False
	decode_common_dimension(gpdwg,dat)
	gpdwg.objects['temp'].point_15=bit.readwithlog2('3RD',dat,'point_15')
	gpdwg.objects['temp'].point_10=bit.readwithlog2('3BD',dat,'point_10')
	gpdwg.objects['temp'].leader_length=bit.readwithlog2('BD',dat,'leader_length')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	gpdwg.objects['temp'].anonymous_block=bit.readwithlog2('H',dat,'anonymous_block')
	TempLog(20,'DIMENSION_DIAMETER End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POINT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_point()
	TempLog(20,'POINT Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].point=bit.readwithlog2('3BD',dat,'point')
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	gpdwg.objects['temp'].x_axis_angle=bit.readwithlog2('BD',dat,'x_axis_angle')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'POINT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_3D_FACE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_3d_face()
	TempLog(20,'3D_FACE Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version <= 14:
		gpdwg.objects['temp'].corner1=bit.readwithlog2('3BD',dat,'corner1')
		gpdwg.objects['temp'].corner2=bit.readwithlog2('3BD',dat,'corner2')
		gpdwg.objects['temp'].corner3=bit.readwithlog2('3BD',dat,'corner3')
		gpdwg.objects['temp'].corner4=bit.readwithlog2('3BD',dat,'corner4')
		gpdwg.objects['temp'].invisible=bit.readwithlog2('BS',dat,'invisible')
	if dat.version >= 2000:
		gpdwg.objects['temp'].no_flag=bit.readwithlog2('B',dat,'no_flag')
		gpdwg.objects['temp'].z_flag=bit.readwithlog2('B',dat,'z_flag')
		gpdwg.objects['temp'].point1_x=bit.readwithlog2('RD',dat,'point1_x')
		gpdwg.objects['temp'].point1_y=bit.readwithlog2('RD',dat,'point1_y')
		if gpdwg.objects['temp'].z_flag == 0:
			gpdwg.objects['temp'].point1_z=bit.readwithlog2('RD', dat,'point1_z')
		gpdwg.objects['temp'].point2=bit.readwithlog2('3DD',dat,'point2', 10)
		gpdwg.objects['temp'].point3=bit.readwithlog2('3DD',dat,'point3', 11)
		gpdwg.objects['temp'].point4=bit.readwithlog2('3DD',dat,'point4', 12)
		if gpdwg.objects['temp'].no_flag == 0:
			gpdwg.objects['temp'].invisible=bit.readwithlog2('BS', dat,'invisible')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'3D_FACE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POLYLINE_PFACE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_polyline_pface()
	TempLog(20,'POLYLINE_PFACE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_vertices=bit.readwithlog2('BS',dat,'num_vertices')
	gpdwg.objects['temp'].num_faces=bit.readwithlog2('BS',dat,'num_faces')
	if dat.version >= 2004:
		gpdwg.objects['temp'].owned_object_count=bit.readwithlog2('BL',dat,'owned_object_count')
	if not decode_entity_handles(gpdwg,dat): return False
	if dat.version <= 2000:
		gpdwg.objects['temp'].first_vertex=bit.readwithlog2('H',dat,'first_vertex')
		gpdwg.objects['temp'].last_vertex=bit.readwithlog2('H',dat,'last_vertex')
	if dat.version >= 2004:
		for i in range(int(gpdwg.objects['temp'].owned_object_count)):
			add_to_list(gpdwg.objects['temp'], 'vertex', bit.readwithlog2('H', dat,' vertex '+str(i)))
	gpdwg.objects['temp'].seqend=bit.readwithlog2('H',dat,'seqend')
	TempLog(20,'POLYLINE_PFACE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_POLYLINE_MESH(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_polyline_mesh()
	TempLog(20,'POLYLINE_MESH Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flags=bit.readwithlog2('BS',dat,'flags')
	gpdwg.objects['temp'].curve_type=bit.readwithlog2('BS',dat,'curve_type')
	gpdwg.objects['temp'].m_vertex_count=bit.readwithlog2('BS',dat,'m_vertex_count')
	gpdwg.objects['temp'].n_vertex_count=bit.readwithlog2('BS',dat,'n_vertex_count')
	gpdwg.objects['temp'].m_density=bit.readwithlog2('BS',dat,'m_density')
	gpdwg.objects['temp'].n_density=bit.readwithlog2('BS',dat,'n_density')
	if dat.version >= 2004:
		gpdwg.objects['temp'].owned_object_count=bit.readwithlog2('BL',dat,'owned_object_count')
	if not decode_entity_handles(gpdwg,dat): return False
	if dat.version <= 2000:
		gpdwg.objects['temp'].first_vertex=bit.readwithlog2('H',dat,'first_vertex')
		gpdwg.objects['temp'].last_vertex=bit.readwithlog2('H',dat,'last_vertex')
	if dat.version >= 2004:
		for i in range(int(gpdwg.objects['temp'].owned_object_count)):
			add_to_list(gpdwg.objects['temp'], 'vertex', bit.readwithlog2('H', dat,' vertex '+str(i)))
	gpdwg.objects['temp'].seqend=bit.readwithlog2('H',dat,'seqend')
	TempLog(20,'POLYLINE_MESH End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SOLID(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_solid()
	TempLog(20,'SOLID Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].elevation=bit.readwithlog2('BD',dat,'elevation')
	gpdwg.objects['temp'].corner1=bit.readwithlog2('2RD',dat,'corner1')
	gpdwg.objects['temp'].corner2=bit.readwithlog2('2RD',dat,'corner2')
	gpdwg.objects['temp'].corner3=bit.readwithlog2('2RD',dat,'corner3')
	gpdwg.objects['temp'].corner4=bit.readwithlog2('2RD',dat,'corner4')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'SOLID End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_TRACE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_trace()
	TempLog(20,'TRACE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BT',dat,'thickness')
	gpdwg.objects['temp'].elevation=bit.readwithlog2('BD',dat,'elevation')
	gpdwg.objects['temp'].corner1=bit.readwithlog2('2RD',dat,'corner1')
	gpdwg.objects['temp'].corner2=bit.readwithlog2('2RD',dat,'corner2')
	gpdwg.objects['temp'].corner3=bit.readwithlog2('2RD',dat,'corner3')
	gpdwg.objects['temp'].corner4=bit.readwithlog2('2RD',dat,'corner4')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('BE',dat,'extrusion')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'TRACE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SHAPE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_shape()
	TempLog(20,'SHAPE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].insertion_point=bit.readwithlog2('3BD',dat,'insertion_point')
	gpdwg.objects['temp'].scale=bit.readwithlog2('BD',dat,'scale')
	gpdwg.objects['temp'].rotation=bit.readwithlog2('BD',dat,'rotation')
	gpdwg.objects['temp'].width_factor=bit.readwithlog2('BD',dat,'width_factor')
	gpdwg.objects['temp'].oblique=bit.readwithlog2('BD',dat,'oblique')
	gpdwg.objects['temp'].thickness=bit.readwithlog2('BD',dat,'thickness')
	gpdwg.objects['temp'].shapeno=bit.readwithlog2('BS',dat,'shapeno')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].shapefile=bit.readwithlog2('H',dat,'shapefile')
	TempLog(20,'SHAPE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VIEWPORT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_viewport()
	TempLog(20,'VIEWPORT Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].center=bit.readwithlog2('3BD',dat,'center')
	gpdwg.objects['temp'].width=bit.readwithlog2('BD',dat,'width')
	gpdwg.objects['temp'].height=bit.readwithlog2('BD',dat,'height')
	if dat.version >= 2000:
		gpdwg.objects['temp'].view_target=bit.readwithlog2('3BD',dat,'view_target')
		gpdwg.objects['temp'].view_direction=bit.readwithlog2('3BD',dat,'view_direction')
		gpdwg.objects['temp'].view_twist_angle=bit.readwithlog2('BD',dat,'view_twist_angle')
		gpdwg.objects['temp'].view_height=bit.readwithlog2('BD',dat,'view_height')
		gpdwg.objects['temp'].lens_height=bit.readwithlog2('BD',dat,'lens_height')
		gpdwg.objects['temp'].front_clip_z=bit.readwithlog2('BD',dat,'front_clip_z')
		gpdwg.objects['temp'].back_clip_z=bit.readwithlog2('BD',dat,'back_clip_z')
		gpdwg.objects['temp'].snap_angle=bit.readwithlog2('BD',dat,'snap_angle')
		gpdwg.objects['temp'].view_center=bit.readwithlog2('2RD',dat,'view_center')
		gpdwg.objects['temp'].snap_base=bit.readwithlog2('2RD',dat,'snap_base')
		gpdwg.objects['temp'].snap_spacing=bit.readwithlog2('2RD',dat,'snap_spacing')
		gpdwg.objects['temp'].grid_spacing=bit.readwithlog2('2RD',dat,'grid_spacing')
		gpdwg.objects['temp'].circle_zoom=bit.readwithlog2('BS',dat,'circle_zoom')
	if dat.version >= 2007:
		gpdwg.objects['temp'].grid_major=bit.readwithlog2('BS',dat,'grid_major')
	if dat.version >= 2000:
		gpdwg.objects['temp'].frozen_layer_count=bit.readwithlog2('BL',dat,'frozen_layer_count')
		gpdwg.objects['temp'].status_flag=bit.readwithlog2('BL',dat,'status_flag')
		gpdwg.objects['temp'].style_sheet=bit.readwithlog2('TV',dat,'style_sheet')
		gpdwg.objects['temp'].render_mode=bit.readwithlog2('RC',dat,'render_mode')
		gpdwg.objects['temp'].ucs_at_origin=bit.readwithlog2('B',dat,'ucs_at_origin')
		gpdwg.objects['temp'].ucs_per_viewport=bit.readwithlog2('B',dat,'ucs_per_viewport')
		gpdwg.objects['temp'].ucs_origin=bit.readwithlog2('3BD',dat,'ucs_origin')
		gpdwg.objects['temp'].ucs_x_axis=bit.readwithlog2('3BD',dat,'ucs_x_axis')
		gpdwg.objects['temp'].ucs_y_axis=bit.readwithlog2('3BD',dat,'ucs_y_axis')
		gpdwg.objects['temp'].ucs_elevation=bit.readwithlog2('BD',dat,'ucs_elevation')
		gpdwg.objects['temp'].ucs_ortho_view_type=bit.readwithlog2('BS',dat,'ucs_ortho_view_type')
	if dat.version >= 2004:
		gpdwg.objects['temp'].shade_plot_mode=bit.readwithlog2('BS',dat,'shade_plot_mode')
	if dat.version >= 2007:
		gpdwg.objects['temp'].use_def_lights=bit.readwithlog2('B',dat,'use_def_lights')
		gpdwg.objects['temp'].def_lighting_type=bit.readwithlog2('RC',dat,'def_lighting_type')
		gpdwg.objects['temp'].brightness=bit.readwithlog2('BD',dat,'brightness')
		gpdwg.objects['temp'].contrast=bit.readwithlog2('BD',dat,'contrast')
		gpdwg.objects['temp'].ambient_light_color=bit.readwithlog2('CMC',dat,'ambient_light_color')
	if not decode_entity_handles(gpdwg,dat): return False
	if dat.version <= 14:
		gpdwg.objects['temp'].viewport_ent_header=bit.readwithlog2('H',dat,'viewport_ent_header')
	if dat.version >= 2000:
		for i in range(int(gpdwg.objects['temp'].frozen_layer_count)):
			add_to_list(gpdwg.objects['temp'], 'frozen_layers', bit.readwithlog2('H', dat,' frozen_layers '+str(i)))
		gpdwg.objects['temp'].clip_boundary=bit.readwithlog2('H',dat,'clip_boundary')
	if dat.version == 2000:
		gpdwg.objects['temp'].viewport_ent_header=bit.readwithlog2('H',dat,'viewport_ent_header')
	if dat.version >= 2000:
		gpdwg.objects['temp'].named_ucs=bit.readwithlog2('H',dat,'named_ucs')
		gpdwg.objects['temp'].base_ucs=bit.readwithlog2('H',dat,'base_ucs')
	if dat.version >= 2007:
		gpdwg.objects['temp'].background=bit.readwithlog2('H',dat,'background')
		gpdwg.objects['temp'].visual_style=bit.readwithlog2('H',dat,'visual_style')
		gpdwg.objects['temp'].shadeplot_id=bit.readwithlog2('H',dat,'shadeplot_id')
		gpdwg.objects['temp'].sun=bit.readwithlog2('H',dat,'sun')
	TempLog(20,'VIEWPORT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ELLIPSE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ellipse()
	TempLog(20,'ELLIPSE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].center=bit.readwithlog2('3BD',dat,'center')
	gpdwg.objects['temp'].sm_axis_vector=bit.readwithlog2('3BD',dat,'sm_axis_vector')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].axis_ratio=bit.readwithlog2('BD',dat,'axis_ratio')
	gpdwg.objects['temp'].starting_angle=bit.readwithlog2('BD',dat,'starting_angle')
	gpdwg.objects['temp'].ending_angle=bit.readwithlog2('BD',dat,'ending_angle')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'ELLIPSE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SPLINE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_spline()
	TempLog(20,'SPLINE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].scenario=bit.readwithlog2('BL',dat,'scenario')
	if dat.version >= 2013:
		gpdwg.objects['temp'].spline_flag_1=bit.readwithlog2('BL',dat,'spline_flag_1')
		gpdwg.objects['temp'].knot_parameter=bit.readwithlog2('BL',dat,'knot_parameter')
	if gpdwg.objects['temp'].scenario == 2:
		gpdwg.objects['temp'].degree=bit.readwithlog2('BL', dat,'degree')
		gpdwg.objects['temp'].fit_tolerence=bit.readwithlog2('BD', dat,'fit_tolerence')
		gpdwg.objects['temp'].tan_vector_begin=bit.readwithlog2('3BD', dat,'tan_vector_begin')
		gpdwg.objects['temp'].tan_vector_end=bit.readwithlog2('3BD', dat,'tan_vector_end')
		gpdwg.objects['temp'].num_fit_points=bit.readwithlog2('BL', dat,'num_fit_points')
	if gpdwg.objects['temp'].scenario == 1:
		gpdwg.objects['temp'].rational=bit.readwithlog2('B', dat,'rational')
		gpdwg.objects['temp'].closed=bit.readwithlog2('B', dat,'closed')
		gpdwg.objects['temp'].periodic=bit.readwithlog2('B', dat,'periodic')
		gpdwg.objects['temp'].knot_tol=bit.readwithlog2('BD', dat,'knot_tol')
		gpdwg.objects['temp'].ctrl_tol=bit.readwithlog2('BD', dat,'ctrl_tol')
		gpdwg.objects['temp'].num_knots=bit.readwithlog2('BL', dat,'num_knots')
		gpdwg.objects['temp'].num_ctrl_points=bit.readwithlog2('BL', dat,'num_ctrl_points')
		gpdwg.objects['temp'].weight=bit.readwithlog2('B', dat,'weight')
	for i in range(int(gpdwg.objects['temp'].num_knots)):
		add_to_list(gpdwg.objects['temp'], 'knot', bit.readwithlog2('BD', dat,' knot '+str(i)))
	for i in range(int(gpdwg.objects['temp'].num_ctrl_points)):
		add_to_list(gpdwg.objects['temp'], 'control_points', bit.readwithlog2('3BD', dat,' control_points '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'weight', bit.readwithlog2('BD', dat,' weight '+str(i)))
	for i in range(int(gpdwg.objects['temp'].num_fit_points)):
		add_to_list(gpdwg.objects['temp'], 'fit_points', bit.readwithlog2('3BD', dat,' fit_points '+str(i)))
	if not decode_entity(gpdwg,dat): return False
	TempLog(20,'SPLINE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_REGION(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_region()
	TempLog(20,'REGION Start')
	if not decode_entity(gpdwg,dat): return False
	TempLog(20,'REGION End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_3DSOLID(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_3dsolid()
	TempLog(20,'3DSOLID Start')
	if not decode_entity(gpdwg,dat): return False
	TempLog(20,'3DSOLID End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_BODY(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_body()
	TempLog(20,'BODY Start')
	if not decode_entity(gpdwg,dat): return False
	TempLog(20,'BODY End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_RAY(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ray()
	TempLog(20,'RAY Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].point=bit.readwithlog2('3BD',dat,'point')
	gpdwg.objects['temp'].vector=bit.readwithlog2('3BD',dat,'vector')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'RAY End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_XLINE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_xline()
	TempLog(20,'XLINE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].point=bit.readwithlog2('3BD',dat,'point')
	gpdwg.objects['temp'].vector=bit.readwithlog2('3BD',dat,'vector')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'XLINE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DICTIONARY(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dictionary()
	TempLog(20,'DICTIONARY Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	if dat.version == 14:
		gpdwg.objects['temp'].unknown=bit.readwithlog2('RC',dat,'unknown')
	if dat.version >= 2000:
		gpdwg.objects['temp'].cloning_flag=bit.readwithlog2('BS',dat,'cloning_flag')
		gpdwg.objects['temp'].hard_owner_flag=bit.readwithlog2('RC',dat,'hard_owner_flag')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'text', bit.readwithlog2('TV', dat,' text '+str(i)))
	gpdwg.objects['temp'].handle_refs=bit.readwithlog2('H',dat,'handle_refs')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'itemhandles', bit.readwithlog2('H', dat,' itemhandles '+str(i)))
	TempLog(20,'DICTIONARY End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DICTIONARYWDFLT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dictionarywdflt()
	TempLog(20,'DICTIONARYWDFLT Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	if dat.version == 14:
		gpdwg.objects['temp'].unknown=bit.readwithlog2('RC',dat,'unknown')
	if dat.version >= 2000:
		gpdwg.objects['temp'].cloning_flag=bit.readwithlog2('BS',dat,'cloning_flag')
		gpdwg.objects['temp'].hard_owner_flag=bit.readwithlog2('RC',dat,'hard_owner_flag')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'text', bit.readwithlog2('TV', dat,' text '+str(i)))
	gpdwg.objects['temp'].handle_refs=bit.readwithlog2('H',dat,'handle_refs')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'itemhandles', bit.readwithlog2('H', dat,' itemhandles '+str(i)))
	gpdwg.objects['temp'].default=bit.readwithlog2('H',dat,'default')
	TempLog(20,'DICTIONARYWDFLT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MTEXT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_mtext()
	TempLog(20,'MTEXT Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].insertion_point=bit.readwithlog2('3BD',dat,'insertion_point')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].x_axis_direction=bit.readwithlog2('3BD',dat,'x_axis_direction')
	gpdwg.objects['temp'].rectangle_width=bit.readwithlog2('BD',dat,'rectangle_width')
	if dat.version >= 2007:
		gpdwg.objects['temp'].rectangle_height=bit.readwithlog2('BD',dat,'rectangle_height')
	gpdwg.objects['temp'].text_height=bit.readwithlog2('BD',dat,'text_height')
	gpdwg.objects['temp'].attachment=bit.readwithlog2('BS',dat,'attachment')
	gpdwg.objects['temp'].brawing_direction=bit.readwithlog2('BS',dat,'brawing_direction')
	gpdwg.objects['temp'].extents_height=bit.readwithlog2('BD',dat,'extents_height')
	gpdwg.objects['temp'].extents_width=bit.readwithlog2('BD',dat,'extents_width')
	gpdwg.objects['temp'].text=bit.readwithlog2('TV',dat,'text')
	if dat.version >= 2000:
		gpdwg.objects['temp'].linespacing_style=bit.readwithlog2('BS',dat,'linespacing_style')
		gpdwg.objects['temp'].linespacing_factor=bit.readwithlog2('BD',dat,'linespacing_factor')
		gpdwg.objects['temp'].unknown_bit=bit.readwithlog2('B',dat,'unknown_bit')
	if dat.version >= 2004:
		gpdwg.objects['temp'].background_flags=bit.readwithlog2('BL',dat,'background_flags')
		if gpdwg.objects['temp'].background_flags == 0x01:
			gpdwg.objects['temp'].background_scale_factor=bit.readwithlog2('BL', dat,'background_scale_factor')
			gpdwg.objects['temp'].background_color=bit.readwithlog2('CMC', dat,'background_color')
			gpdwg.objects['temp'].background_transparency=bit.readwithlog2('BL', dat,'background_transparency')
	if dat.version >= 2008:
		gpdwg.objects['temp'].not_annotative=bit.readwithlog2('B',dat,'not_annotative')
		if gpdwg.objects['temp'].not_annotative == 1:
			gpdwg.objects['temp'].version=bit.readwithlog2('BS', dat,'version')
		gpdwg.objects['temp'].default=bit.readwithlog2('B',dat,'default')
		gpdwg.objects['temp'].registered_application=bit.readwithlog2('H',dat,'registered_application')
		gpdwg.objects['temp'].attachment_point=bit.readwithlog2('BL',dat,'attachment_point')
		gpdwg.objects['temp'].x_direction=bit.readwithlog2('3BD',dat,'x_direction')
		gpdwg.objects['temp'].insertion_point=bit.readwithlog2('3BD',dat,'insertion_point')
		gpdwg.objects['temp'].rectangle_width=bit.readwithlog2('BD',dat,'rectangle_width')
		gpdwg.objects['temp'].rectangle_height=bit.readwithlog2('BD',dat,'rectangle_height')
		gpdwg.objects['temp'].extents_width=bit.readwithlog2('BD',dat,'extents_width')
		gpdwg.objects['temp'].extents_height=bit.readwithlog2('BD',dat,'extents_height')
	gpdwg.objects['temp'].unknown=bit.readwithlog2('H',dat,'unknown')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'MTEXT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LEADER(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_leader()
	TempLog(20,'LEADER Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].unknown1=bit.readwithlog2('B',dat,'unknown1')
	gpdwg.objects['temp'].annotation_type=bit.readwithlog2('BS',dat,'annotation_type')
	gpdwg.objects['temp'].pth_type=bit.readwithlog2('BS',dat,'pth_type')
	gpdwg.objects['temp'].num_points=bit.readwithlog2('BL',dat,'num_points')
	gpdwg.objects['temp'].point=bit.readwithlog2('3BD',dat,'point')
	gpdwg.objects['temp'].origin=bit.readwithlog2('3BD',dat,'origin')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].x_direction=bit.readwithlog2('3BD',dat,'x_direction')
	gpdwg.objects['temp'].offset_block_ins_point=bit.readwithlog2('3BD',dat,'offset_block_ins_point')
	if dat.version >= 14:
		gpdwg.objects['temp'].end_point_projection=bit.readwithlog2('3BD',dat,'end_point_projection')
	if dat.version <= 14:
		gpdwg.objects['temp'].dim_gap=bit.readwithlog2('BD',dat,'dim_gap')
	gpdwg.objects['temp'].box_height=bit.readwithlog2('BD',dat,'box_height')
	gpdwg.objects['temp'].box_weidth=bit.readwithlog2('BD',dat,'box_weidth')
	gpdwg.objects['temp'].hook_line_on_x_dir=bit.readwithlog2('B',dat,'hook_line_on_x_dir')
	gpdwg.objects['temp'].arrowhead_flag=bit.readwithlog2('B',dat,'arrowhead_flag')
	if dat.version <= 14:
		gpdwg.objects['temp'].arrowhead_type=bit.readwithlog2('BS',dat,'arrowhead_type')
		gpdwg.objects['temp'].dim_asz=bit.readwithlog2('BD',dat,'dim_asz')
		gpdwg.objects['temp'].unknown2=bit.readwithlog2('B',dat,'unknown2')
		gpdwg.objects['temp'].unknown3=bit.readwithlog2('B',dat,'unknown3')
		gpdwg.objects['temp'].unknown4=bit.readwithlog2('BS',dat,'unknown4')
		gpdwg.objects['temp'].byblockcolor=bit.readwithlog2('BS',dat,'byblockcolor')
		gpdwg.objects['temp'].unknown5=bit.readwithlog2('B',dat,'unknown5')
		gpdwg.objects['temp'].unknown6=bit.readwithlog2('B',dat,'unknown6')
	if dat.version >= 2000:
		gpdwg.objects['temp'].unknown7=bit.readwithlog2('BS',dat,'unknown7')
		gpdwg.objects['temp'].unknown8=bit.readwithlog2('B',dat,'unknown8')
		gpdwg.objects['temp'].unknown9=bit.readwithlog2('B',dat,'unknown9')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].associated_annotation=bit.readwithlog2('H',dat,'associated_annotation')
	gpdwg.objects['temp'].dim_style=bit.readwithlog2('H',dat,'dim_style')
	TempLog(20,'LEADER End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_TOLERANCE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_tolerance()
	TempLog(20,'TOLERANCE Start')
	if not decode_entity(gpdwg,dat): return False
	if dat.version <= 14:
		gpdwg.objects['temp'].unknown1=bit.readwithlog2('BS',dat,'unknown1')
		gpdwg.objects['temp'].height=bit.readwithlog2('BD',dat,'height')
		gpdwg.objects['temp'].dim_gap=bit.readwithlog2('BD',dat,'dim_gap')
	gpdwg.objects['temp'].ins_point=bit.readwithlog2('3BD',dat,'ins_point')
	gpdwg.objects['temp'].x_direction=bit.readwithlog2('3BD',dat,'x_direction')
	gpdwg.objects['temp'].extruision=bit.readwithlog2('3BD',dat,'extruision')
	gpdwg.objects['temp'].text_string=bit.readwithlog2('BS',dat,'text_string')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].dim_style=bit.readwithlog2('H',dat,'dim_style')
	TempLog(20,'TOLERANCE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MLINE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_mline()
	TempLog(20,'MLINE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].scale=bit.readwithlog2('BD',dat,'scale')
	gpdwg.objects['temp'].justification=bit.readwithlog2('RC',dat,'justification')
	gpdwg.objects['temp'].base_point=bit.readwithlog2('3BD',dat,'base_point')
	gpdwg.objects['temp'].extrusion=bit.readwithlog2('3BD',dat,'extrusion')
	gpdwg.objects['temp'].open=bit.readwithlog2('BS',dat,'open')
	gpdwg.objects['temp'].line_in_style=bit.readwithlog2('RC',dat,'line_in_style')
	gpdwg.objects['temp'].num_vertex=bit.readwithlog2('BS',dat,'num_vertex')
	if not decode_entity_handles(gpdwg,dat): return False
	gpdwg.objects['temp'].mline_style=bit.readwithlog2('H',dat,'mline_style')
	TempLog(20,'MLINE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_BLOCK_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_block_control()
	TempLog(20,'BLOCK_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	if dat.version >= 2004:
		gpdwg.objects['temp'].xdic_missing=bit.readwithlog2('B',dat,'xdic_missing')
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'handles', bit.readwithlog2('H', dat,' handles '+str(i)))
	gpdwg.objects['temp'].model_space_handle=bit.readwithlog2('H',dat,'model_space_handle')
	gpdwg.objects['temp'].paper_space_handle=bit.readwithlog2('H',dat,'paper_space_handle')
	TempLog(20,'BLOCK_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_BLOCK_HEADER(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_block_header()
	TempLog(20,'BLOCK_HEADER Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].entry_name=bit.readwithlog2('TV',dat,'entry_name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefindex_1=bit.readwithlog2('BS',dat,'xrefindex_1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	gpdwg.objects['temp'].anonymous=bit.readwithlog2('B',dat,'anonymous')
	gpdwg.objects['temp'].has_atts=bit.readwithlog2('B',dat,'has_atts')
	gpdwg.objects['temp'].is_ref=bit.readwithlog2('B',dat,'is_ref')
	gpdwg.objects['temp'].xref_overlaid=bit.readwithlog2('B',dat,'xref_overlaid')
	if dat.version >= 2000:
		gpdwg.objects['temp'].loaded_bit=bit.readwithlog2('B',dat,'loaded_bit')
	if dat.version >= 2004:
		gpdwg.objects['temp'].owned_object_count=bit.readwithlog2('BL',dat,'owned_object_count')
	gpdwg.objects['temp'].base_point=bit.readwithlog2('3BD',dat,'base_point')
	gpdwg.objects['temp'].xref_path_name=bit.readwithlog2('TV',dat,'xref_path_name')
	if dat.version >= 2000:
		gpdwg.objects['temp'].insert_count=bit.readwithlog2('INSCOUNT',dat,'insert_count')
		gpdwg.objects['temp'].block_description=bit.readwithlog2('TV',dat,'block_description')
		gpdwg.objects['temp'].preview_size=bit.readwithlog2('BL',dat,'preview_size')
		for i in range(int(gpdwg.objects['temp'].preview_size)):
			add_to_list(gpdwg.objects['temp'], 'preview_data', bit.readwithlog2('RC', dat,' preview_data '+str(i)))
	if dat.version >= 2007:
		gpdwg.objects['temp'].insert_units=bit.readwithlog2('BS',dat,'insert_units')
		gpdwg.objects['temp'].explodable=bit.readwithlog2('B',dat,'explodable')
		gpdwg.objects['temp'].block_scaling=bit.readwithlog2('RC',dat,'block_scaling')
	gpdwg.objects['temp'].block_control=bit.readwithlog2('H',dat,'block_control')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].block_entity=bit.readwithlog2('H',dat,'block_entity')
	if dat.version <= 2000:
		if not gpdwg.objects['temp'].xref_overlaid and not gpdwg.objects['temp'].is_ref == True:
			gpdwg.objects['temp'].first_entry=bit.readwithlog2('H', dat,'first_entry')
			gpdwg.objects['temp'].last_entry=bit.readwithlog2('H', dat,'last_entry')
	if dat.version >= 2004:
		gpdwg.objects['temp'].owned_object_handles=bit.readwithlog2('H',dat,'owned_object_handles')
	gpdwg.objects['temp'].endblk_entity=bit.readwithlog2('H',dat,'endblk_entity')
	if dat.version >= 2000:
		for i in range(int(gpdwg.objects['temp'].insert_count)):
			add_to_list(gpdwg.objects['temp'], 'insert_handles', bit.readwithlog2('H', dat,' insert_handles '+str(i)))
		gpdwg.objects['temp'].layout_handle=bit.readwithlog2('H',dat,'layout_handle')
	TempLog(20,'BLOCK_HEADER End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LAYER_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_layer_control()
	TempLog(20,'LAYER_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'layer_objhandles', bit.readwithlog2('H', dat,' layer_objhandles '+str(i)))
	TempLog(20,'LAYER_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LAYER(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_layer()
	TempLog(20,'LAYER Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog2('BS',dat,'xrefindex1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	if dat.version <= 14:
		gpdwg.objects['temp'].frozen=bit.readwithlog2('B',dat,'frozen')
		gpdwg.objects['temp'].on=bit.readwithlog2('B',dat,'on')
		gpdwg.objects['temp'].frozen_in_new=bit.readwithlog2('B',dat,'frozen_in_new')
		gpdwg.objects['temp'].locked=bit.readwithlog2('B',dat,'locked')
	if dat.version >= 2000:
		gpdwg.objects['temp'].values=bit.readwithlog2('BS',dat,'values')
	gpdwg.objects['temp'].color=bit.readwithlog2('CMC',dat,'color')
	gpdwg.objects['temp'].layer_control=bit.readwithlog2('H',dat,'layer_control')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	gpdwg.objects['temp'].exref_block_handle=bit.readwithlog2('H',dat,'exref_block_handle')
	if dat.version >= 2000:
		gpdwg.objects['temp'].plotstyle=bit.readwithlog2('H',dat,'plotstyle')
	if dat.version >= 2007:
		gpdwg.objects['temp'].material=bit.readwithlog2('H',dat,'material')
	gpdwg.objects['temp'].linetype=bit.readwithlog2('H',dat,'linetype')
	TempLog(20,'LAYER End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SHAPEFILE_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_shapefile_control()
	TempLog(20,'SHAPEFILE_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'shapefile_objhandles', bit.readwithlog2('H', dat,' shapefile_objhandles '+str(i)))
	TempLog(20,'SHAPEFILE_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SHAPEFILE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_shapefile()
	TempLog(20,'SHAPEFILE Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].flag64=bit.readwithlog2('B',dat,'flag64')
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog2('BS',dat,'xrefindex1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	gpdwg.objects['temp'].vertical=bit.readwithlog2('B',dat,'vertical')
	gpdwg.objects['temp'].shape_file=bit.readwithlog2('B',dat,'shape_file')
	gpdwg.objects['temp'].fixed_height=bit.readwithlog2('BD',dat,'fixed_height')
	gpdwg.objects['temp'].width_factor=bit.readwithlog2('BD',dat,'width_factor')
	gpdwg.objects['temp'].oblique_angle=bit.readwithlog2('BD',dat,'oblique_angle')
	gpdwg.objects['temp'].generation=bit.readwithlog2('RC',dat,'generation')
	gpdwg.objects['temp'].last_height=bit.readwithlog2('BD',dat,'last_height')
	gpdwg.objects['temp'].font_name=bit.readwithlog2('TV',dat,'font_name')
	gpdwg.objects['temp'].big_font_name=bit.readwithlog2('TV',dat,'big_font_name')
	gpdwg.objects['temp'].shapefile=bit.readwithlog2('H',dat,'shapefile')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	gpdwg.objects['temp'].xref_block=bit.readwithlog2('H',dat,'xref_block')
	TempLog(20,'SHAPEFILE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LTYPE_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ltype_control()
	TempLog(20,'LTYPE_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	gpdwg.objects['temp'].byblock_ltype=bit.readwithlog2('H',dat,'byblock_ltype')
	gpdwg.objects['temp'].bylayer_ltype=bit.readwithlog2('H',dat,'bylayer_ltype')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'ltypes', bit.readwithlog2('H', dat,' ltypes '+str(i)))
	TempLog(20,'LTYPE_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LTYPE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ltype()
	TempLog(20,'LTYPE Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog2('BS',dat,'xrefindex1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	gpdwg.objects['temp'].desc=bit.readwithlog2('TV',dat,'desc')
	gpdwg.objects['temp'].pattern_len=bit.readwithlog2('BD',dat,'pattern_len')
	gpdwg.objects['temp'].alignment=bit.readwithlog2('RC',dat,'alignment')
	gpdwg.objects['temp'].numdashes=bit.readwithlog2('RC',dat,'numdashes')
	for i in range(int(gpdwg.objects['temp'].numdashes)):
		add_to_list(gpdwg.objects['temp'], 'dash_length', bit.readwithlog2('BD', dat,' dash_length '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'complex_shapecode', bit.readwithlog2('BS', dat,' complex_shapecode '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'offset_x', bit.readwithlog2('RD', dat,' offset_x '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'offset_y', bit.readwithlog2('RD', dat,' offset_y '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'scale', bit.readwithlog2('BD', dat,' scale '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'rotation', bit.readwithlog2('BD', dat,' rotation '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'shapeflag', bit.readwithlog2('BS', dat,' shapeflag '+str(i)))
	if dat.version <= 2004:
		for i in range(int(256)):
			add_to_list(gpdwg.objects['temp'], 'string_area', bit.readwithlog2('RC', dat,' string_area '+str(i)))
	if dat.version >= 2007:
			add_to_list(gpdwg.objects['temp'], 'test_data', bit.readwithlog2('RC', dat,' test_data '+str(i)))
	gpdwg.objects['temp'].ltype=bit.readwithlog2('H',dat,'ltype')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	gpdwg.objects['temp'].xref=bit.readwithlog2('H',dat,'xref')
	for i in range(int(gpdwg.objects['temp'].numdashes)):
		add_to_list(gpdwg.objects['temp'], 'shapefile_dash', bit.readwithlog2('H', dat,' shapefile_dash '+str(i)))
	TempLog(20,'LTYPE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VIEW_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_view_control()
	TempLog(20,'VIEW_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'views', bit.readwithlog2('H', dat,' views '+str(i)))
	TempLog(20,'VIEW_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VIEW(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_view()
	TempLog(20,'VIEW Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'VIEW End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_UCS_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ucs_control()
	TempLog(20,'UCS_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'ucs_handles', bit.readwithlog2('H', dat,' ucs_handles '+str(i)))
	TempLog(20,'UCS_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_UCS(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ucs()
	TempLog(20,'UCS Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'UCS End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VPORT_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vport_control()
	TempLog(20,'VPORT_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'vport_handles', bit.readwithlog2('H', dat,' vport_handles '+str(i)))
	TempLog(20,'VPORT_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VPORT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vport()
	TempLog(20,'VPORT Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog2('BS',dat,'xrefindex1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	gpdwg.objects['temp'].view_height=bit.readwithlog2('BD',dat,'view_height')
	gpdwg.objects['temp'].aspect_ratio=bit.readwithlog2('BD',dat,'aspect_ratio')
	gpdwg.objects['temp'].view_center=bit.readwithlog2('2RD',dat,'view_center')
	gpdwg.objects['temp'].view_target=bit.readwithlog2('3BD',dat,'view_target')
	gpdwg.objects['temp'].view_dir=bit.readwithlog2('3BD',dat,'view_dir')
	gpdwg.objects['temp'].view_twist=bit.readwithlog2('BD',dat,'view_twist')
	gpdwg.objects['temp'].lens_length=bit.readwithlog2('BD',dat,'lens_length')
	gpdwg.objects['temp'].front_clip=bit.readwithlog2('BD',dat,'front_clip')
	gpdwg.objects['temp'].back_clip=bit.readwithlog2('BD',dat,'back_clip')
	for i in range(int(4)):
		add_to_list(gpdwg.objects['temp'], 'view_mode', bit.readwithlog2('B', dat,' view_mode '+str(i)))
	if dat.version >= 2000:
		gpdwg.objects['temp'].render_mode=bit.readwithlog2('RC',dat,'render_mode')
	if dat.version >= 2007:
		gpdwg.objects['temp'].use_default_lights=bit.readwithlog2('B',dat,'use_default_lights')
		gpdwg.objects['temp'].default_lighting_type=bit.readwithlog2('RC',dat,'default_lighting_type')
		gpdwg.objects['temp'].brightness=bit.readwithlog2('BD',dat,'brightness')
		gpdwg.objects['temp'].contrast=bit.readwithlog2('BD',dat,'contrast')
		gpdwg.objects['temp'].ambient_color=bit.readwithlog2('CMC',dat,'ambient_color')
	gpdwg.objects['temp'].lower_left=bit.readwithlog2('2RD',dat,'lower_left')
	gpdwg.objects['temp'].upper_right=bit.readwithlog2('2RD',dat,'upper_right')
	gpdwg.objects['temp'].ucs_follow=bit.readwithlog2('B',dat,'ucs_follow')
	gpdwg.objects['temp'].circle_zoom=bit.readwithlog2('BS',dat,'circle_zoom')
	gpdwg.objects['temp'].fast_zoom=bit.readwithlog2('B',dat,'fast_zoom')
	for i in range(int(2)):
		add_to_list(gpdwg.objects['temp'], 'ucsicon', bit.readwithlog2('B', dat,' ucsicon '+str(i)))
	gpdwg.objects['temp'].grid_on=bit.readwithlog2('B',dat,'grid_on')
	gpdwg.objects['temp'].frid_spacing=bit.readwithlog2('2RD',dat,'frid_spacing')
	gpdwg.objects['temp'].snap_on=bit.readwithlog2('B',dat,'snap_on')
	gpdwg.objects['temp'].snap_style=bit.readwithlog2('B',dat,'snap_style')
	gpdwg.objects['temp'].snap_isopair=bit.readwithlog2('BS',dat,'snap_isopair')
	gpdwg.objects['temp'].span_rot=bit.readwithlog2('BD',dat,'span_rot')
	gpdwg.objects['temp'].snap_base=bit.readwithlog2('2RD',dat,'snap_base')
	gpdwg.objects['temp'].snap_spacing=bit.readwithlog2('2RD',dat,'snap_spacing')
	if dat.version >= 2000:
		gpdwg.objects['temp'].unknown=bit.readwithlog2('B',dat,'unknown')
		gpdwg.objects['temp'].ucs_per_viewport=bit.readwithlog2('B',dat,'ucs_per_viewport')
		gpdwg.objects['temp'].ucs_origin=bit.readwithlog2('3BD',dat,'ucs_origin')
		gpdwg.objects['temp'].ucs_x_axis=bit.readwithlog2('3BD',dat,'ucs_x_axis')
		gpdwg.objects['temp'].ucs_y_axis=bit.readwithlog2('3BD',dat,'ucs_y_axis')
		gpdwg.objects['temp'].ucs_elevation=bit.readwithlog2('BD',dat,'ucs_elevation')
		gpdwg.objects['temp'].ucs_orthographic_type=bit.readwithlog2('BS',dat,'ucs_orthographic_type')
	if dat.version >= 2007:
		gpdwg.objects['temp'].grid_flags=bit.readwithlog2('BS',dat,'grid_flags')
		gpdwg.objects['temp'].grid_major=bit.readwithlog2('BS',dat,'grid_major')
	gpdwg.objects['temp'].vport_control=bit.readwithlog2('H',dat,'vport_control')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	gpdwg.objects['temp'].xref=bit.readwithlog2('H',dat,'xref')
	if dat.version >= 2007:
		gpdwg.objects['temp'].background=bit.readwithlog2('H',dat,'background')
		gpdwg.objects['temp'].visual_style=bit.readwithlog2('H',dat,'visual_style')
		gpdwg.objects['temp'].sun=bit.readwithlog2('H',dat,'sun')
	if dat.version >= 2000:
		gpdwg.objects['temp'].names_ucs=bit.readwithlog2('H',dat,'names_ucs')
		gpdwg.objects['temp'].nase_ucs=bit.readwithlog2('H',dat,'nase_ucs')
		TempLog(20,'VPORT End\n\n')
		TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
		return Check_Obj_CRC(dat,Obj_Size)

def decode_APPID_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_appid_control()
	TempLog(20,'APPID_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'appid_handles', bit.readwithlog2('H', dat,' appid_handles '+str(i)))
	TempLog(20,'APPID_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_APPID(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_appid()
	TempLog(20,'APPID Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefinde1=bit.readwithlog2('BS',dat,'xrefinde1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	gpdwg.objects['temp'].unknown=bit.readwithlog2('RC',dat,'unknown')
	gpdwg.objects['temp'].app_control=bit.readwithlog2('H',dat,'app_control')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobjhandle=bit.readwithlog2('H',dat,'xdicobjhandle')
	gpdwg.objects['temp'].xref=bit.readwithlog2('H',dat,'xref')
	TempLog(20,'APPID End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMSTYLE_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimstyle_control()
	TempLog(20,'DIMSTYLE_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries+2)):
		add_to_list(gpdwg.objects['temp'], 'dimstyle_handles', bit.readwithlog2('H', dat,' dimstyle_handles '+str(i)))
	TempLog(20,'DIMSTYLE_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DIMSTYLE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dimstyle()
	TempLog(20,'DIMSTYLE Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog2('BS',dat,'xrefindex1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	if dat.version <= 14:
		gpdwg.objects['temp'].dimtol=bit.readwithlog2('B',dat,'dimtol')
		gpdwg.objects['temp'].dimlim=bit.readwithlog2('B',dat,'dimlim')
		gpdwg.objects['temp'].dimtih=bit.readwithlog2('B',dat,'dimtih')
		gpdwg.objects['temp'].dimtoh=bit.readwithlog2('B',dat,'dimtoh')
		gpdwg.objects['temp'].dimse1=bit.readwithlog2('B',dat,'dimse1')
		gpdwg.objects['temp'].dimse2=bit.readwithlog2('B',dat,'dimse2')
		gpdwg.objects['temp'].dimalt=bit.readwithlog2('B',dat,'dimalt')
		gpdwg.objects['temp'].dimtofl=bit.readwithlog2('B',dat,'dimtofl')
		gpdwg.objects['temp'].dimsah=bit.readwithlog2('B',dat,'dimsah')
		gpdwg.objects['temp'].dimtix=bit.readwithlog2('B',dat,'dimtix')
		gpdwg.objects['temp'].dimsoxd=bit.readwithlog2('B',dat,'dimsoxd')
		gpdwg.objects['temp'].dimaltd=bit.readwithlog2('RC',dat,'dimaltd')
		gpdwg.objects['temp'].dimzin=bit.readwithlog2('RC',dat,'dimzin')
		gpdwg.objects['temp'].dimsd1=bit.readwithlog2('B',dat,'dimsd1')
		gpdwg.objects['temp'].dimsd2=bit.readwithlog2('B',dat,'dimsd2')
		gpdwg.objects['temp'].dimtolj=bit.readwithlog2('RC',dat,'dimtolj')
		gpdwg.objects['temp'].dimjust=bit.readwithlog2('RC',dat,'dimjust')
		gpdwg.objects['temp'].dimfit=bit.readwithlog2('RC',dat,'dimfit')
		gpdwg.objects['temp'].dimupt=bit.readwithlog2('B',dat,'dimupt')
		gpdwg.objects['temp'].dimtzin=bit.readwithlog2('RC',dat,'dimtzin')
		gpdwg.objects['temp'].dimaltz=bit.readwithlog2('RC',dat,'dimaltz')
		gpdwg.objects['temp'].dimalttz=bit.readwithlog2('RC',dat,'dimalttz')
		gpdwg.objects['temp'].dimtad=bit.readwithlog2('RC',dat,'dimtad')
		gpdwg.objects['temp'].dimunit=bit.readwithlog2('BS',dat,'dimunit')
		gpdwg.objects['temp'].dimaunit=bit.readwithlog2('BS',dat,'dimaunit')
		gpdwg.objects['temp'].dimdec=bit.readwithlog2('BS',dat,'dimdec')
		gpdwg.objects['temp'].dimtdec=bit.readwithlog2('BS',dat,'dimtdec')
		gpdwg.objects['temp'].dimaltu=bit.readwithlog2('BS',dat,'dimaltu')
		gpdwg.objects['temp'].dimalttd=bit.readwithlog2('BS',dat,'dimalttd')
		gpdwg.objects['temp'].dimscale=bit.readwithlog2('BD',dat,'dimscale')
		gpdwg.objects['temp'].dimasz=bit.readwithlog2('BD',dat,'dimasz')
		gpdwg.objects['temp'].dimexo=bit.readwithlog2('BD',dat,'dimexo')
		gpdwg.objects['temp'].dimdli=bit.readwithlog2('BD',dat,'dimdli')
		gpdwg.objects['temp'].dimexe=bit.readwithlog2('BD',dat,'dimexe')
		gpdwg.objects['temp'].dimrnd=bit.readwithlog2('BD',dat,'dimrnd')
		gpdwg.objects['temp'].dimdle=bit.readwithlog2('BD',dat,'dimdle')
		gpdwg.objects['temp'].dimtp=bit.readwithlog2('BD',dat,'dimtp')
		gpdwg.objects['temp'].dimtm=bit.readwithlog2('BD',dat,'dimtm')
		gpdwg.objects['temp'].dimtxt=bit.readwithlog2('BD',dat,'dimtxt')
		gpdwg.objects['temp'].dimcen=bit.readwithlog2('BD',dat,'dimcen')
		gpdwg.objects['temp'].dimtsz=bit.readwithlog2('BD',dat,'dimtsz')
		gpdwg.objects['temp'].dimaltf=bit.readwithlog2('BD',dat,'dimaltf')
		gpdwg.objects['temp'].dimlfac=bit.readwithlog2('BD',dat,'dimlfac')
		gpdwg.objects['temp'].dimtvp=bit.readwithlog2('BD',dat,'dimtvp')
		gpdwg.objects['temp'].dimtfac=bit.readwithlog2('BD',dat,'dimtfac')
		gpdwg.objects['temp'].dimgap=bit.readwithlog2('BD',dat,'dimgap')
		gpdwg.objects['temp'].dimpost=bit.readwithlog2('T',dat,'dimpost')
		gpdwg.objects['temp'].dimapost=bit.readwithlog2('T',dat,'dimapost')
		gpdwg.objects['temp'].dimblk=bit.readwithlog2('T',dat,'dimblk')
		gpdwg.objects['temp'].dimblk1=bit.readwithlog2('T',dat,'dimblk1')
		gpdwg.objects['temp'].dimblk2=bit.readwithlog2('T',dat,'dimblk2')
		gpdwg.objects['temp'].dimclrd=bit.readwithlog2('BS',dat,'dimclrd')
		gpdwg.objects['temp'].dimclre=bit.readwithlog2('BS',dat,'dimclre')
		gpdwg.objects['temp'].dimclrt=bit.readwithlog2('BS',dat,'dimclrt')
	if dat.version >= 2000:
		gpdwg.objects['temp'].dimpost=bit.readwithlog2('TV',dat,'dimpost')
		gpdwg.objects['temp'].dimapost=bit.readwithlog2('TV',dat,'dimapost')
		gpdwg.objects['temp'].dimscale=bit.readwithlog2('BD',dat,'dimscale')
		gpdwg.objects['temp'].dimasz=bit.readwithlog2('BD',dat,'dimasz')
		gpdwg.objects['temp'].dimexo=bit.readwithlog2('BD',dat,'dimexo')
		gpdwg.objects['temp'].dimdli=bit.readwithlog2('BD',dat,'dimdli')
		gpdwg.objects['temp'].dimexe=bit.readwithlog2('BD',dat,'dimexe')
		gpdwg.objects['temp'].dimrnd=bit.readwithlog2('BD',dat,'dimrnd')
		gpdwg.objects['temp'].dimdle=bit.readwithlog2('BD',dat,'dimdle')
		gpdwg.objects['temp'].dimtp=bit.readwithlog2('BD',dat,'dimtp')
		gpdwg.objects['temp'].dimtm=bit.readwithlog2('BD',dat,'dimtm')
	if dat.version >= 2007:
		gpdwg.objects['temp'].dimfxl=bit.readwithlog2('BD',dat,'dimfxl')
		gpdwg.objects['temp'].dimjogang=bit.readwithlog2('BD',dat,'dimjogang')
		gpdwg.objects['temp'].dimtfill=bit.readwithlog2('BS',dat,'dimtfill')
		gpdwg.objects['temp'].dimtfillclr=bit.readwithlog2('CMC',dat,'dimtfillclr')
	if dat.version >= 2000:
		gpdwg.objects['temp'].dimtol=bit.readwithlog2('B',dat,'dimtol')
		gpdwg.objects['temp'].dimlim=bit.readwithlog2('B',dat,'dimlim')
		gpdwg.objects['temp'].dimtih=bit.readwithlog2('B',dat,'dimtih')
		gpdwg.objects['temp'].dimtoh=bit.readwithlog2('B',dat,'dimtoh')
		gpdwg.objects['temp'].dimse1=bit.readwithlog2('B',dat,'dimse1')
		gpdwg.objects['temp'].dimse2=bit.readwithlog2('B',dat,'dimse2')
		gpdwg.objects['temp'].dimtad=bit.readwithlog2('BS',dat,'dimtad')
		gpdwg.objects['temp'].dimzin=bit.readwithlog2('BS',dat,'dimzin')
		gpdwg.objects['temp'].dimazin=bit.readwithlog2('BS',dat,'dimazin')
	if dat.version >= 2007:
		gpdwg.objects['temp'].dimarcsym=bit.readwithlog2('BS',dat,'dimarcsym')
	if dat.version >= 2000:
		gpdwg.objects['temp'].dimtxt=bit.readwithlog2('BD',dat,'dimtxt')
		gpdwg.objects['temp'].dimcen=bit.readwithlog2('BD',dat,'dimcen')
		gpdwg.objects['temp'].dimtsz=bit.readwithlog2('BD',dat,'dimtsz')
		gpdwg.objects['temp'].dimaltf=bit.readwithlog2('BD',dat,'dimaltf')
		gpdwg.objects['temp'].dimlfac=bit.readwithlog2('BD',dat,'dimlfac')
		gpdwg.objects['temp'].dimtvp=bit.readwithlog2('BD',dat,'dimtvp')
		gpdwg.objects['temp'].dimtfac=bit.readwithlog2('BD',dat,'dimtfac')
		gpdwg.objects['temp'].dimgap=bit.readwithlog2('BD',dat,'dimgap')
		gpdwg.objects['temp'].dimaltrnd=bit.readwithlog2('BD',dat,'dimaltrnd')
		gpdwg.objects['temp'].dimalt=bit.readwithlog2('B',dat,'dimalt')
		gpdwg.objects['temp'].dimaltd=bit.readwithlog2('BS',dat,'dimaltd')
		gpdwg.objects['temp'].dimtofl=bit.readwithlog2('B',dat,'dimtofl')
		gpdwg.objects['temp'].dimsah=bit.readwithlog2('B',dat,'dimsah')
		gpdwg.objects['temp'].dimtix=bit.readwithlog2('B',dat,'dimtix')
		gpdwg.objects['temp'].dimsoxd=bit.readwithlog2('B',dat,'dimsoxd')
		gpdwg.objects['temp'].dimclrd=bit.readwithlog2('BS',dat,'dimclrd')
		gpdwg.objects['temp'].dimclre=bit.readwithlog2('BS',dat,'dimclre')
		gpdwg.objects['temp'].dimclrt=bit.readwithlog2('BS',dat,'dimclrt')
		gpdwg.objects['temp'].dimadec=bit.readwithlog2('BS',dat,'dimadec')
		gpdwg.objects['temp'].dimdec=bit.readwithlog2('BS',dat,'dimdec')
		gpdwg.objects['temp'].dimtdec=bit.readwithlog2('BS',dat,'dimtdec')
		gpdwg.objects['temp'].dimaltu=bit.readwithlog2('BS',dat,'dimaltu')
		gpdwg.objects['temp'].dimalttd=bit.readwithlog2('BS',dat,'dimalttd')
		gpdwg.objects['temp'].dimaunit=bit.readwithlog2('BS',dat,'dimaunit')
		gpdwg.objects['temp'].dimfrac=bit.readwithlog2('BS',dat,'dimfrac')
		gpdwg.objects['temp'].dimlunit=bit.readwithlog2('BS',dat,'dimlunit')
		gpdwg.objects['temp'].dimdsep=bit.readwithlog2('BS',dat,'dimdsep')
		gpdwg.objects['temp'].dimtmove=bit.readwithlog2('BS',dat,'dimtmove')
		gpdwg.objects['temp'].dimjust=bit.readwithlog2('BS',dat,'dimjust')
		gpdwg.objects['temp'].dimsd1=bit.readwithlog2('B',dat,'dimsd1')
		gpdwg.objects['temp'].dimsd2=bit.readwithlog2('B',dat,'dimsd2')
		gpdwg.objects['temp'].dimtolj=bit.readwithlog2('BS',dat,'dimtolj')
		gpdwg.objects['temp'].dimtzin=bit.readwithlog2('BS',dat,'dimtzin')
		gpdwg.objects['temp'].dimaltz=bit.readwithlog2('BS',dat,'dimaltz')
		gpdwg.objects['temp'].dimalttz=bit.readwithlog2('BS',dat,'dimalttz')
		gpdwg.objects['temp'].dimupt=bit.readwithlog2('B',dat,'dimupt')
		gpdwg.objects['temp'].dimfit=bit.readwithlog2('BS',dat,'dimfit')
	if dat.version >= 2007:
		gpdwg.objects['temp'].dimfxlon=bit.readwithlog2('B',dat,'dimfxlon')
	if dat.version >= 2010:
		gpdwg.objects['temp'].dimtxtdirection=bit.readwithlog2('B',dat,'dimtxtdirection')
		gpdwg.objects['temp'].dimaltmzf=bit.readwithlog2('BD',dat,'dimaltmzf')
		gpdwg.objects['temp'].dimaltmzs=bit.readwithlog2('T',dat,'dimaltmzs')
		gpdwg.objects['temp'].dimmzs=bit.readwithlog2('T',dat,'dimmzs')
		gpdwg.objects['temp'].dimmzf=bit.readwithlog2('BD',dat,'dimmzf')
	if dat.version >= 2000:
		gpdwg.objects['temp'].dimlwd=bit.readwithlog2('BS',dat,'dimlwd')
		gpdwg.objects['temp'].dimlwe=bit.readwithlog2('BS',dat,'dimlwe')
	gpdwg.objects['temp'].unknown=bit.readwithlog2('B',dat,'unknown')
	gpdwg.objects['temp'].dimstyle=bit.readwithlog2('H',dat,'dimstyle')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	gpdwg.objects['temp'].xref=bit.readwithlog2('H',dat,'xref')
	gpdwg.objects['temp'].shapefile=bit.readwithlog2('H',dat,'shapefile')
	if dat.version >= 2000:
		gpdwg.objects['temp'].leader=bit.readwithlog2('H',dat,'leader')
		gpdwg.objects['temp'].dimblk=bit.readwithlog2('H',dat,'dimblk')
		gpdwg.objects['temp'].dimblk1=bit.readwithlog2('H',dat,'dimblk1')
		gpdwg.objects['temp'].dimblk2=bit.readwithlog2('H',dat,'dimblk2')
	if dat.version >= 2007:
		gpdwg.objects['temp'].dimltype=bit.readwithlog2('H',dat,'dimltype')
		gpdwg.objects['temp'].dimltex1=bit.readwithlog2('H',dat,'dimltex1')
		gpdwg.objects['temp'].dimltex2=bit.readwithlog2('H',dat,'dimltex2')
	TempLog(20,'DIMSTYLE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VP_ENT_HDR_CONTROL(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vp_ent_hdr_control()
	TempLog(20,'VP_ENT_HDR_CONTROL Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	gpdwg.objects['temp'].handle_null=bit.readwithlog2('H',dat,'handle_null')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'dimstyle_handles', bit.readwithlog2('H', dat,' dimstyle_handles '+str(i)))
	TempLog(20,'VP_ENT_HDR_CONTROL End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VP_ENT_HDR(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vp_ent_hdr()
	TempLog(20,'VP_ENT_HDR Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].entry_name=bit.readwithlog2('TV',dat,'entry_name')
	gpdwg.objects['temp'].flag_64=bit.readwithlog2('B',dat,'flag_64')
	gpdwg.objects['temp'].xrefindex1=bit.readwithlog2('BS',dat,'xrefindex1')
	gpdwg.objects['temp'].xdep=bit.readwithlog2('B',dat,'xdep')
	gpdwg.objects['temp'].flag_1=bit.readwithlog2('B',dat,'flag_1')
	gpdwg.objects['temp'].viewport_entity_control=bit.readwithlog2('H',dat,'viewport_entity_control')
	gpdwg.objects['temp'].handle_xdicobjhandle=bit.readwithlog2('H',dat,'handle_xdicobjhandle')
	gpdwg.objects['temp'].xref_handle=bit.readwithlog2('H',dat,'xref_handle')
	gpdwg.objects['temp'].viewport_entity=bit.readwithlog2('H',dat,'viewport_entity')
	gpdwg.objects['temp'].prv_vport=bit.readwithlog2('H',dat,'prv_vport')
	TempLog(20,'VP_ENT_HDR End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_GROUP(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_group()
	TempLog(20,'GROUP Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'GROUP End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MLINESTYLE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_mlinestyle()
	TempLog(20,'MLINESTYLE Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].desc=bit.readwithlog2('TV',dat,'desc')
	gpdwg.objects['temp'].flags=bit.readwithlog2('BS',dat,'flags')
	gpdwg.objects['temp'].fillcolor=bit.readwithlog2('CMC',dat,'fillcolor')
	gpdwg.objects['temp'].start_angle=bit.readwithlog2('BD',dat,'start_angle')
	gpdwg.objects['temp'].end_angle=bit.readwithlog2('BD',dat,'end_angle')
	gpdwg.objects['temp'].num_lines=bit.readwithlog2('RC',dat,'num_lines')
	for i in range(int(gpdwg.objects['temp'].num_lines)):
		add_to_list(gpdwg.objects['temp'], 'offset', bit.readwithlog2('BD', dat,' offset '+str(i)))
		add_to_list(gpdwg.objects['temp'], 'color', bit.readwithlog2('CMC', dat,' color '+str(i)))
		if dat.version < 2008:
			add_to_list(gpdwg.objects['temp'], 'line_type_index', bit.readwithlog2('BS', dat,' line_type_index '+str(i)))
		if dat.version >= 2008:
			add_to_list(gpdwg.objects['temp'], 'line_type_handle', bit.readwithlog2('H', dat,' line_type_handle '+str(i)))
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	gpdwg.objects['temp'].reactors=bit.readwithlog2('H',dat,'reactors')
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	TempLog(20,'MLINESTYLE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_OLE2FRAME(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_ole2frame()
	TempLog(20,'OLE2FRAME Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'OLE2FRAME End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DUMMY(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dummy()
	TempLog(20,'DUMMY Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'DUMMY End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LONG_TRANSACTION(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_long_transaction()
	TempLog(20,'LONG_TRANSACTION Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'LONG_TRANSACTION End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LWPLINE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_lwpline()
	TempLog(20,'LWPLINE Start')
	if not decode_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].flag=bit.readwithlog2('BS',dat,'flag')
	gpdwg.objects['temp'].constwidth=float(0)
	if int(gpdwg.objects['temp'].flag) & 4:
		gpdwg.objects['temp'].constwidth=bit.readwithlog2('BD', dat,'constwidth')
	gpdwg.objects['temp'].elevation=float(0)
	if int(gpdwg.objects['temp'].flag) & 8:
		gpdwg.objects['temp'].elevation=bit.readwithlog2('BD', dat,'elevation')
	gpdwg.objects['temp'].thickness=float(0)
	if int(gpdwg.objects['temp'].flag) & 2:
		gpdwg.objects['temp'].thickness=bit.readwithlog2('BD', dat,'thickness')
	gpdwg.objects['temp'].normal=bit.point3D()
	if int(gpdwg.objects['temp'].flag) & 1:
		gpdwg.objects['temp'].normal=bit.readwithlog2('3BD', dat,'normal')
	gpdwg.objects['temp'].num_points=bit.readwithlog2('BL',dat,'num_points')
	gpdwg.objects['temp'].num_bulges=float(0)
	if int(gpdwg.objects['temp'].flag) & 16:
		gpdwg.objects['temp'].num_bulges=bit.readwithlog2('BL', dat,'num_bulges')
	if dat.version >= 2010:
		if int(gpdwg.objects['temp'].flag) & 1024:
			gpdwg.objects['temp'].vertexidcount=bit.readwithlog2('BL', dat,'vertexidcount')
		if int(gpdwg.objects['temp'].flag) & 32:
			gpdwg.objects['temp'].numwidths=bit.readwithlog2('BL', dat,'numwidths')
	if dat.version >= 2000:

		#custom output 1 for lwpline begin.
		CustomData=[]
		CustomData.append(bit.readwithlog2("2RD",dat,"First point"))
		for x in range(1,int(gpdwg.objects['temp'].num_points)):
			TempPoint=bit.point2D()
			DefaultValue=CustomData[x-1].x
			TempPoint.x=bit.readwithlog2("DD",dat,"X coord of point "+str(x),DefaultValue)
			DefaultValue=CustomData[x-1].y
			TempPoint.y=bit.readwithlog2("DD",dat,"Y coord of point "+str(x),DefaultValue)
			CustomData.append(TempPoint)
		#custom output 1 for lwpline end.
		gpdwg.objects['temp'].coords=CustomData
	for i in range(int(gpdwg.objects['temp'].num_bulges)):
		add_to_list(gpdwg.objects['temp'], 'bulge', bit.readwithlog2('BD', dat,' bulge '+str(i)))
	if dat.version >= 2010:
		for i in range(int(gpdwg.objects['temp'].vertexidcount)):
			add_to_list(gpdwg.objects['temp'], 'vertexid', bit.readwithlog2('BL', dat,' vertexid '+str(i)))
		for i in range(int(gpdwg.objects['temp'].numwidths)):
			add_to_list(gpdwg.objects['temp'], 'widths', bit.readwithlog2('2BD', dat,' widths '+str(i)))
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'LWPLINE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_HATCH1(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_hatch1()
	TempLog(20,'HATCH1 Start')
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
		add_to_list(gpdwg.objects['temp'], 'hatch_paths', decode_hatch_path(dat))
	gpdwg.objects['temp'].style=bit.readwithlog2('BS',dat,'style')
	gpdwg.objects['temp'].patterntype=bit.readwithlog2('BS',dat,'patterntype')
	gpdwg.objects['temp'].angle=bit.readwithlog2('BD',dat,'angle')
	gpdwg.objects['temp'].scale_or_spacing=bit.readwithlog2('BD',dat,'scale_or_spacing')
	gpdwg.objects['temp'].double_hatch=bit.readwithlog2('B',dat,'double_hatch')
	gpdwg.objects['temp'].num_defination_lines=bit.readwithlog2('BS',dat,'num_defination_lines')
	if not decode_entity_handles(gpdwg,dat): return False
	TempLog(20,'HATCH1 End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_XRECORD(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_xrecord()
	TempLog(20,'XRECORD Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].num_databytes=bit.readwithlog2('BL',dat,'num_databytes')
	for i in range(int(gpdwg.objects['temp'].num_databytes)):
		add_to_list(gpdwg.objects['temp'], 'databytes', bit.readwithlog2('RC', dat,' databytes '+str(i)))
	if dat.version >= 2000:
		gpdwg.objects['temp'].cloning_flag=bit.readwithlog2('BS',dat,'cloning_flag')
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdic=bit.readwithlog2('H',dat,'xdic')
	TempLog(20,'XRECORD End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_PLACEHOLDER(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_placeholder()
	TempLog(20,'PLACEHOLDER Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'PLACEHOLDER End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_VBA_PROJECT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_vba_project()
	TempLog(20,'VBA_PROJECT Start')
	if not decode_entity(gpdwg,dat): return False
	TempLog(20,'VBA_PROJECT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_LAYOUT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_layout()
	TempLog(20,'LAYOUT Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].page_setup_name=bit.readwithlog2('TV',dat,'page_setup_name')
	gpdwg.objects['temp'].printer_config=bit.readwithlog2('TV',dat,'printer_config')
	gpdwg.objects['temp'].plot_layout_flags=bit.readwithlog2('BS',dat,'plot_layout_flags')
	gpdwg.objects['temp'].margin_left=bit.readwithlog2('BD',dat,'margin_left')
	gpdwg.objects['temp'].margin_bottom=bit.readwithlog2('BD',dat,'margin_bottom')
	gpdwg.objects['temp'].margin_right=bit.readwithlog2('BD',dat,'margin_right')
	gpdwg.objects['temp'].margin_top=bit.readwithlog2('BD',dat,'margin_top')
	gpdwg.objects['temp'].paper_width=bit.readwithlog2('BD',dat,'paper_width')
	gpdwg.objects['temp'].paper_height=bit.readwithlog2('BD',dat,'paper_height')
	gpdwg.objects['temp'].paper_size=bit.readwithlog2('TV',dat,'paper_size')
	gpdwg.objects['temp'].plot_origin=bit.readwithlog2('2BD',dat,'plot_origin')
	gpdwg.objects['temp'].paper_units=bit.readwithlog2('BS',dat,'paper_units')
	gpdwg.objects['temp'].plot_rotation=bit.readwithlog2('BS',dat,'plot_rotation')
	gpdwg.objects['temp'].plot_type=bit.readwithlog2('BS',dat,'plot_type')
	gpdwg.objects['temp'].window_min=bit.readwithlog2('2BD',dat,'window_min')
	gpdwg.objects['temp'].window_max=bit.readwithlog2('2BD',dat,'window_max')
	if dat.version <= 2000:
		gpdwg.objects['temp'].plot_view_name=bit.readwithlog2('TV',dat,'plot_view_name')
	gpdwg.objects['temp'].real_world_units=bit.readwithlog2('BD',dat,'real_world_units')
	gpdwg.objects['temp'].drawing_units=bit.readwithlog2('BD',dat,'drawing_units')
	gpdwg.objects['temp'].current_style_sheet=bit.readwithlog2('TV',dat,'current_style_sheet')
	gpdwg.objects['temp'].scale_type=bit.readwithlog2('BS',dat,'scale_type')
	gpdwg.objects['temp'].scale_factor=bit.readwithlog2('BD',dat,'scale_factor')
	gpdwg.objects['temp'].paper_image_origin=bit.readwithlog2('2BD',dat,'paper_image_origin')
	if dat.version >= 2004:
		gpdwg.objects['temp'].shade_plot_mode=bit.readwithlog2('BS',dat,'shade_plot_mode')
		gpdwg.objects['temp'].shade_plot_res_level=bit.readwithlog2('BS',dat,'shade_plot_res_level')
		gpdwg.objects['temp'].shade_plot_custom=bit.readwithlog2('BS',dat,'shade_plot_custom')
	gpdwg.objects['temp'].layout_name=bit.readwithlog2('TV',dat,'layout_name')
	gpdwg.objects['temp'].tab_order=bit.readwithlog2('BL',dat,'tab_order')
	gpdwg.objects['temp'].flag=bit.readwithlog2('BS',dat,'flag')
	gpdwg.objects['temp'].ucs_origin=bit.readwithlog2('3BD',dat,'ucs_origin')
	gpdwg.objects['temp'].lim_min=bit.readwithlog2('2RD',dat,'lim_min')
	gpdwg.objects['temp'].lim_max=bit.readwithlog2('2RD',dat,'lim_max')
	gpdwg.objects['temp'].ins_point=bit.readwithlog2('3BD',dat,'ins_point')
	gpdwg.objects['temp'].ucs_axis_x=bit.readwithlog2('3BD',dat,'ucs_axis_x')
	gpdwg.objects['temp'].ucs_axis_y=bit.readwithlog2('3BD',dat,'ucs_axis_y')
	gpdwg.objects['temp'].elevation=bit.readwithlog2('BD',dat,'elevation')
	gpdwg.objects['temp'].ortho_view_type=bit.readwithlog2('BS',dat,'ortho_view_type')
	gpdwg.objects['temp'].ext_min=bit.readwithlog2('3BD',dat,'ext_min')
	gpdwg.objects['temp'].ext_max=bit.readwithlog2('3BD',dat,'ext_max')
	if dat.version >= 2004:
		gpdwg.objects['temp'].viewport_count=bit.readwithlog2('RL',dat,'viewport_count')
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	if dat.version >= 2004:
		gpdwg.objects['temp'].plot_view=bit.readwithlog2('H',dat,'plot_view')
	if dat.version >= 2007:
		gpdwg.objects['temp'].visual_style_handle=bit.readwithlog2('H',dat,'visual_style_handle')
	gpdwg.objects['temp'].assoc_paperspace_block_record=bit.readwithlog2('H',dat,'assoc_paperspace_block_record')
	gpdwg.objects['temp'].last_active_viewport=bit.readwithlog2('H',dat,'last_active_viewport')
	gpdwg.objects['temp'].base_ucs=bit.readwithlog2('H',dat,'base_ucs')
	gpdwg.objects['temp'].named_ucs=bit.readwithlog2('H',dat,'named_ucs')
	if dat.version >= 2004:
		for i in range(int(gpdwg.objects['temp'].viewport_count)):
			add_to_list(gpdwg.objects['temp'], 'viewport', bit.readwithlog2('H', dat,' viewport '+str(i)))
	TempLog(20,'LAYOUT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ACAD_PROXY_ENTITY(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_acad_proxy_entity()
	TempLog(20,'ACAD_PROXY_ENTITY Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'ACAD_PROXY_ENTITY End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ACAD_PROXY_OBJECT(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_acad_proxy_object()
	TempLog(20,'ACAD_PROXY_OBJECT Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'ACAD_PROXY_OBJECT End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_UNKNOWN(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_unknown()
	TempLog(20,'UNKNOWN Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'UNKNOWN End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_RASTERVARIABLES(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_rastervariables()
	TempLog(20,'RASTERVARIABLES Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].classver=bit.readwithlog2('BL',dat,'classver')
	gpdwg.objects['temp'].dispfrm=bit.readwithlog2('BS',dat,'dispfrm')
	gpdwg.objects['temp'].dispqual=bit.readwithlog2('BS',dat,'dispqual')
	gpdwg.objects['temp'].units=bit.readwithlog2('BS',dat,'units')
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactors', bit.readwithlog2('H', dat,' reactors '+str(i)))
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	TempLog(20,'RASTERVARIABLES End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SCALE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_scale()
	TempLog(20,'SCALE Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].unknown=bit.readwithlog2('BS',dat,'unknown')
	gpdwg.objects['temp'].name=bit.readwithlog2('TV',dat,'name')
	gpdwg.objects['temp'].paper_units=bit.readwithlog2('BD',dat,'paper_units')
	gpdwg.objects['temp'].drawing_units=bit.readwithlog2('BD',dat,'drawing_units')
	gpdwg.objects['temp'].unit_scale_flag=bit.readwithlog2('B',dat,'unit_scale_flag')
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	gpdwg.objects['temp'].reactors=bit.readwithlog2('H',dat,'reactors')
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	TempLog(20,'SCALE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ACDBPLACEHOLDER(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_acdbplaceholder()
	TempLog(20,'ACDBPLACEHOLDER Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	gpdwg.objects['temp'].reactors=bit.readwithlog2('H',dat,'reactors')
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	TempLog(20,'ACDBPLACEHOLDER End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_DICTIONARYVAR(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_dictionaryvar()
	TempLog(20,'DICTIONARYVAR Start')
	if not decode_non_entity(gpdwg,dat): return False
	gpdwg.objects['temp'].int_val=bit.readwithlog2('RC',dat,'int_val')
	gpdwg.objects['temp'].str=bit.readwithlog2('TV',dat,'str')
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactor', bit.readwithlog2('H', dat,' reactor '+str(i)))
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	TempLog(20,'DICTIONARYVAR End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_MLEADERSTYLE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_mleaderstyle()
	TempLog(20,'MLEADERSTYLE Start')
	if not decode_non_entity(gpdwg,dat): return False
	if dat.version == 2010:
		gpdwg.objects['temp'].version=bit.readwithlog2('BS',dat,'version')
	gpdwg.objects['temp'].content_type=bit.readwithlog2('BS',dat,'content_type')
	gpdwg.objects['temp'].draw_multileader_order=bit.readwithlog2('BS',dat,'draw_multileader_order')
	gpdwg.objects['temp'].draw_leader_order=bit.readwithlog2('BS',dat,'draw_leader_order')
	gpdwg.objects['temp'].maximum_number_of_points=bit.readwithlog2('BL',dat,'maximum_number_of_points')
	gpdwg.objects['temp'].first_segment_angle=bit.readwithlog2('BD',dat,'first_segment_angle')
	gpdwg.objects['temp'].leader_type=bit.readwithlog2('BS',dat,'leader_type')
	gpdwg.objects['temp'].leader_line_color=bit.readwithlog2('CMC',dat,'leader_line_color')
	gpdwg.objects['temp'].leader_line_type_handle=bit.readwithlog2('H',dat,'leader_line_type_handle')
	gpdwg.objects['temp'].leader_line_weight=bit.readwithlog2('BL',dat,'leader_line_weight')
	gpdwg.objects['temp'].is_landing_enabled=bit.readwithlog2('B',dat,'is_landing_enabled')
	gpdwg.objects['temp'].landing_gap=bit.readwithlog2('BD',dat,'landing_gap')
	gpdwg.objects['temp'].auto_include_landing=bit.readwithlog2('B',dat,'auto_include_landing')
	gpdwg.objects['temp'].landing_distance=bit.readwithlog2('BD',dat,'landing_distance')
	gpdwg.objects['temp'].style_description=bit.readwithlog2('TV',dat,'style_description')
	gpdwg.objects['temp'].arrow_head_block_handle=bit.readwithlog2('H',dat,'arrow_head_block_handle')
	gpdwg.objects['temp'].arrow_head_size=bit.readwithlog2('BD',dat,'arrow_head_size')
	gpdwg.objects['temp'].text_default=bit.readwithlog2('TV',dat,'text_default')
	gpdwg.objects['temp'].text_style_handle=bit.readwithlog2('H',dat,'text_style_handle')
	gpdwg.objects['temp'].left_attachment=bit.readwithlog2('BS',dat,'left_attachment')
	gpdwg.objects['temp'].right_attachment=bit.readwithlog2('BS',dat,'right_attachment')
	TempLog(20,'MLEADERSTYLE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SORTENTSTABLE(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_sortentstable()
	TempLog(20,'SORTENTSTABLE Start')
	if not decode_non_entity(gpdwg,dat): return False
	if dat.version >= 2004:
		gpdwg.objects['temp'].xdic_missing=bit.readwithlog2('B',dat,'xdic_missing')
	gpdwg.objects['temp'].num_entries=bit.readwithlog2('BL',dat,'num_entries')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'sort_handles', bit.readwithlog2('H', dat,' sort_handles '+str(i)))
	gpdwg.objects['temp'].parent=bit.readwithlog2('H',dat,'parent')
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactor', bit.readwithlog2('H', dat,' reactor '+str(i)))
	gpdwg.objects['temp'].xdicobj=bit.readwithlog2('H',dat,'xdicobj')
	gpdwg.objects['temp'].owner_handle=bit.readwithlog2('H',dat,'owner_handle')
	for i in range(int(gpdwg.objects['temp'].num_entries)):
		add_to_list(gpdwg.objects['temp'], 'entities', bit.readwithlog2('H', dat,' entities '+str(i)))
	TempLog(20,'SORTENTSTABLE End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_ACDB_BLKREFOBJECTCONTEXTDATA_CLASS(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_acdb_blkrefobjectcontextdata_class()
	TempLog(20,'ACDB_BLKREFOBJECTCONTEXTDATA_CLASS Start')
	if not decode_non_entity(gpdwg,dat): return False
	TempLog(20,'ACDB_BLKREFOBJECTCONTEXTDATA_CLASS End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

def decode_SUN(gpdwg,dat):
	Obj_Size=gpdwg.objects['temp']['size']
	gpdwg.objects['temp']=libgpdwg.dwg_sun()
	TempLog(20,'SUN Start')
	if not decode_non_entity(gpdwg,dat): return False
	for i in range(int(gpdwg.objects['temp'].num_reactors)):
		add_to_list(gpdwg.objects['temp'], 'reactor', bit.readwithlog2('H', dat,' reactor '+str(i)))
	TempLog(20,'SUN End\n\n')
	TempLog(20,str(dat.byte)+'\t'+str(dat.bit))
	return Check_Obj_CRC(dat,Obj_Size)

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