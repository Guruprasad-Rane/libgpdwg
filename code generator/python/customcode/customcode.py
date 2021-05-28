def getCustomCode(int,tabs):
	CustomCode={'0':"""
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
#custom output for insert end.""",

'1':"""
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
#custom output 1 for lwpline end.""",
	}
	return CustomCode[int].replace("\n","\n"+tabs)