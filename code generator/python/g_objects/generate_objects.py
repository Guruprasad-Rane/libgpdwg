import csv
import tabulate
from customcode import customcode
DataTypeList={'LIST':'list','B':'int','B':'int','2BD':'bit.point2D','2DD':'bit.point2D','2RD':'bit.point2D','3B':'bit.point3D','3BD':'bit.point3D','3DD':'bit.point3D','3RD':'bit.point3D','BB':'int','BD':'float','BE':'bit.point3D','L':'int','BL':'float','BLL':'int','BS':'float','BT':'float','CMC':'bit.color','DD':'float','H':'bit.handle','MC':'int','MS':'int','RC':'int','RD':'float','RL':'int','RS':'int','SN':'int','T':'str','TC':'int','TU':'int','TV':'str','U':'float','INSCOUNT':'int','HATCH_PATHS':'int'}
Slots={}
ObjectList={}



ObjectsFile=open('src/python/objects.py','w')
ObjectsDocFile=open('doc/python/source/objects.rst','w')
ObjectsDocFile.write("=================\nObjects\n=================\n.. module:: gpdwg\n.. toctree::\n   :maxdepth: 2\n\n")
ObjectClassFIle=open('code generator/python/g_gpdwg/classes.py','a')

def writeObjectClass(Code):
	global ObjectClassFIle
	ObjectClassFIle.write('\n\n')
	ObjectClassFIle.write('\n\n'+Code)

def writeObjectDecode(Code):
	global ObjectsFile
	ObjectsFile.write('\n'+Code)

def ProcessPropertyName(PropertyName):
	PropertyName=PropertyName.split("(")[0]
	PropertyName=PropertyName.strip()
	PropertyName=PropertyName.strip(".")
	PropertyName=PropertyName.replace(" ","_")
	PropertyName=PropertyName.lower()
	return PropertyName

def ProcessPropertyType(PropertyType):
	PropertyType=PropertyType.upper()
	return PropertyType

def ProcessCondition(Condition):
	if Condition.isdigit():
		return Condition
	else:
		ConditionVariables=Condition.split(" & ")
		if len(ConditionVariables) == 1:
			return "gpdwg.objects['temp']."+ProcessPropertyName(ConditionVariables[0])
		else:
			for i in range(len(ConditionVariables)):
				ConditionVariables[i]=ProcessPropertyName(ConditionVariables[i])
				if ConditionVariables[i][0] == "!":
					ConditionVariables[i] = "not gpdwg.objects['temp']."+ ConditionVariables[i][1 : len(ConditionVariables[i])]
				else:
					ConditionVariables[i] = "gpdwg.objects['temp']."+ ConditionVariables[i]
			return " and ".join(ConditionVariables)


def dumpClass(slots,Object):
	Tempslots=["'"+ slot + "'" for slot in slots]
	if len(Object['ParentClass']) == 0:	Object['ParentClass'] = 'dwg_entity_handles'
	TempClassData="class "+Object['Name']+"("+Object['ParentClass']+"):\n\t"
	if len(Object['DocString']) > 0:
		TempClassData=TempClassData+'"""'+Object['DocString']+'"""\n\t'
	else:
		TempClassData=TempClassData+'"""Class for data object '+Object['Name']+'"""\n\t'
	TempClassData=TempClassData+'__slots__=['+",".join(Tempslots)+']\n\t'
	TempClassData=TempClassData+'def __setattr__(self,name,value):\n\t\t'
	Tempslots=[]
	for key,val in sorted(slots.items()):
		Tempslots.append("'"+key+"':"+val)
	TempClassData=TempClassData+'A_Types={'+",".join(Tempslots)+'}\n\t\t'
	TempClassData=TempClassData+"if name in A_Types:\n\t\t\tif not isinstance(value, A_Types[name]):\n\t\t\t\traise TypeError('%s attribute must be set to an instance of %s but found to be %s' % (name, A_Types[name],type(value)))\n\t\tobject.__setattr__(self, name, value)\n"
	TempClassData=TempClassData+"\tdef __repr__(self):\n\t\tTempOutput=''\n\t\tfor i in dir(self):\n\t\t\tif not i.startswith('__') and hasattr(self,i):\n\t\t\t\tTempOutput=TempOutput+'\\t\\t'+str(i)+' : '+repr(getattr(self,i))+'\\n'\n\t\treturn TempOutput"
	writeObjectClass(TempClassData)

def getTabs(TabNos):
	Temp=""
	for _ in range(TabNos):
		Temp=Temp+"\t"
	return Temp

LicenseFile=open('code generator/python/license.txt','r')
LicenseText=LicenseFile.read()
LicenseFile.close()
writeObjectDecode(LicenseText)
writeObjectDecode("#!/usr/bin/env python3")
writeObjectDecode("import bit, logging, libgpdwg")
writeObjectDecode("logger = logging.getLogger(\"gpdwg_logger\")")
writeObjectDecode("Temp=\"\"")

with open('csv spec/objects_spec.csv','r') as Specfile:
	tabs=""
	TabNos=0
	Prev_Condition=""
	ObjectSpec = csv.reader(Specfile, delimiter=';', quotechar='\'')
	next(ObjectSpec,None)
	next(ObjectSpec,None)
	VariableVersionDocString=""
	TableData=[]

	LineNo=0
	for row in ObjectSpec:
		LineNo+=1
		if len(row[4])>0:
			strDefaultValue=", "+row[4]
		else:
			strDefaultValue=""

		if len(row[0])>0:
			ObjectName=row[0]
			DecodeObjectName=ObjectName.upper()
			ClassObjectName="dwg_"+ObjectName.lower()
			writeObjectDecode('def decode_'+DecodeObjectName+'(gpdwg,dat):')
			tabs="\t"
			TabNos=1
			writeObjectDecode(getTabs(TabNos)+"Obj_Size=gpdwg.objects['temp']['size']")
			writeObjectDecode(getTabs(TabNos)+"gpdwg.objects['temp']=libgpdwg."+ClassObjectName+"()")
			writeObjectDecode(getTabs(TabNos)+"TempLog(20,'"+DecodeObjectName+" Start')")
			ObjectList[row[8]]=ClassObjectName

		elif len(row[1])>0:
			if len(row[6])>0:
				tabs="\t\t"
			else:
				tabs="\t"
			CommonCondition=False
			if row[1] == "R13-14":
				writeObjectDecode(tabs+'if dat.version <= 14:')
				VariableVersionDocString="Available in DWG version 13 and 14 only."
			elif row[1] == "R13-R14":
				writeObjectDecode(tabs+'if dat.version <= 14:')
				VariableVersionDocString="Available in DWG version 13 and 14 only."
			elif row[1] == "R13-15":
				writeObjectDecode(tabs+'if dat.version <= 2000:')
				VariableVersionDocString="Available in DWG version 13, 14 and 2000 only."
			elif row[1] == "R13-R15":
				writeObjectDecode(tabs+'if dat.version <= 2000:')
				VariableVersionDocString="Available in DWG version 13, 14 and 2000 only."
			elif row[1] == "R13-R2000":
				writeObjectDecode(tabs+'if dat.version <= 2000:')
				VariableVersionDocString="Available in DWG version 13, 14 and 2000 only."
			elif row[1] == "R13-R2004":
				writeObjectDecode(tabs+'if dat.version <= 2004:')
				VariableVersionDocString="Available in DWG version 13, 14, 2000 and 2004 only."
			elif row[1] == "R13-18":
				writeObjectDecode(tabs+'if dat.version <= 2004:')
				VariableVersionDocString="Available in DWG version 13, 14, 2000 and 2004 only."
			elif row[1] == "R13-R18":
				writeObjectDecode(tabs+'if dat.version <= 2004:')
				VariableVersionDocString="Available in DWG version 13, 14, 2000 and 2004 only."
			elif row[1] == "R14+":
				writeObjectDecode(tabs+'if dat.version >= 14:')
				VariableVersionDocString="Available in DWG version 14 and above only."
			elif row[1] == "R14":
				writeObjectDecode(tabs+'if dat.version == 14:')
				VariableVersionDocString="Available in DWG version 14 only."
			elif row[1] == "R2000":
				writeObjectDecode(tabs+'if dat.version == 2000:')
				VariableVersionDocString="Available in DWG version 2000 only."
			elif row[1] == "R2000+":
				writeObjectDecode(tabs+'if dat.version >= 2000:')
				VariableVersionDocString="Available in DWG version 2000 and above only."
			elif row[1] == "R2004":
				writeObjectDecode(tabs+'if dat.version == 2004:')
				VariableVersionDocString="Available in DWG version 2004 only."
			elif row[1] == "R2004+":
				writeObjectDecode(tabs+'if dat.version >= 2004:')
				VariableVersionDocString="Available in DWG version 2004 and above only."
			elif row[1] == "R2007":
				writeObjectDecode(tabs+'if dat.version == 2007:')
				VariableVersionDocString="Available in DWG version 2007 only."
			elif row[1] == "R2007+":
				writeObjectDecode(tabs+'if dat.version >= 2007:')
				VariableVersionDocString="Available in DWG version 2007 and above only."
			elif row[1] == "R2008+":
				writeObjectDecode(tabs+'if dat.version >= 2008:')
				VariableVersionDocString="Available in DWG version 2008 and above only."
			elif row[1] == "R2008-":
				writeObjectDecode(tabs+'if dat.version < 2008:')
				VariableVersionDocString="Available in DWG version 2007 and below only."
			elif row[1] == "R2010":
				writeObjectDecode(tabs+'if dat.version == 2010:')
				VariableVersionDocString="Available in DWG version 2010 only."				
			elif row[1] == "R2010+":
				writeObjectDecode(tabs+'if dat.version >= 2010:')
				VariableVersionDocString="Available in DWG version 2010 and above only."
			elif row[1] == "R2013+":
				writeObjectDecode(tabs+'if dat.version >= 2013:')
				VariableVersionDocString="Available in DWG version 2013 and above only."
			elif row[1] == "Common":
				CommonCondition=True
				VariableVersionDocString="Available in all DWG versions."
			else:
				raise NameError("Unknown value "+row[1]+" in Column No 1")

		elif len(row[2])>0 and len(row[3])>0:
			PropertyName=ProcessPropertyName(row[3])
			PropertyType=ProcessPropertyType(row[2])
			if CommonCondition:
				tabs="\t"
			else:
				tabs="\t\t"
				TabNos=TabNos+1

			if PropertyType=="H" and PropertyName=="handle":
				TableData.append([PropertyName,DataTypeList[PropertyType],VariableVersionDocString])
			elif PropertyType=="X" and PropertyName=="eed":
				writeObjectDecode(tabs+"if not decode_non_entity(gpdwg,dat): return False")
				ParentClassName='dwg_non_entity'
			elif PropertyType=="X" and PropertyName=="ced":
				writeObjectDecode(tabs+"if not decode_entity(gpdwg,dat): return False")
				ParentClassName='dwg_entity'
			elif PropertyType=="X" and PropertyName=="cdd":
				writeObjectDecode(tabs+"decode_common_dimension(gpdwg,dat)")
				ParentClassName='dwg_dimension'
			elif PropertyType=="X" and PropertyName=="cehd":
				writeObjectDecode(tabs+"if not decode_entity_handles(gpdwg,dat): return False")
			elif PropertyType=="X" and PropertyName=="ted":
				writeObjectDecode(tabs+"decode_TEXT(gpdwg,dat)")
				ParentClassName='dwg_text'
			elif PropertyType=="X" and PropertyName=="atd":
				writeObjectDecode(tabs+"decode_ATTRIB(gpdwg,dat)")
				ParentClassName='dwg_attrib'
			elif PropertyType=="X" and PropertyName=="crc":
				writeObjectDecode(tabs+"TempLog(20,'"+DecodeObjectName+" End\\n\\n')")
				writeObjectDecode(tabs+"TempLog(20,str(dat.byte)+'\\t'+str(dat.bit))")
				writeObjectDecode(tabs+"return Check_Obj_CRC(dat,Obj_Size)\n")
				tabs=""
				Object={'Name': ClassObjectName,'ParentClass':ParentClassName,'DocString':'Class for '+ClassObjectName}
				dumpClass(Slots,Object)
				Slots={}
			elif len(row[5])>0 or len(row[6])>0:
				ConditionVariable=ProcessCondition(row[5])
				if row[6]=="RANGE":
					ConditionCode="for i in range(int("+ConditionVariable+")):"
					if PropertyType=="X" and PropertyName=="hatch_paths":
						CustomFunction="decode_hatch_path(dat)"
					else:
						CustomFunction= "bit.readwithlog2('"+PropertyType+"', dat,' "+PropertyName+" '+str(i))"

					if PrevConditionCode!=ConditionCode :
						writeObjectDecode(tabs+ConditionCode)
					PrevConditionCode = ConditionCode
					writeObjectDecode(tabs+"\tadd_to_list(gpdwg.objects['temp'], '"+PropertyName+"', "+CustomFunction+")")
					Slots[PropertyName]='list'
				elif row[6]==" == ":
					ConditionCode="if "+ConditionVariable+" == "+row[7]+":"
					if PrevConditionCode!=ConditionCode :
						writeObjectDecode(tabs+ConditionCode)
					PrevConditionCode = ConditionCode
					writeObjectDecode(tabs+"\tgpdwg.objects['temp']."+PropertyName+"=bit.readwithlog2('"+PropertyType+"', dat,'"+PropertyName+"'"+strDefaultValue+")")
					Slots[PropertyName]=DataTypeList[PropertyType]
				elif row[6]==" != ":
					ConditionCode="if "+ConditionVariable+" != "+row[7]+":"
					if PrevConditionCode!=ConditionCode :
						writeObjectDecode(tabs+ConditionCode)
					PrevConditionCode = ConditionCode
					writeObjectDecode(tabs+"\tgpdwg.objects['temp']."+PropertyName+"=bit.readwithlog2('"+PropertyType+"', dat,'"+PropertyName+"'"+strDefaultValue+")")
					Slots[PropertyName]=DataTypeList[PropertyType]
				elif row[6]=="!&":
					ConditionCode="if not int("+ConditionVariable+") & "+row[7]+":"
					if PrevConditionCode!=ConditionCode :
						writeObjectDecode(tabs+ConditionCode)
					PrevConditionCode = ConditionCode
					writeObjectDecode(tabs+"\tgpdwg.objects['temp']."+PropertyName+"=bit.readwithlog2('"+PropertyType+"', dat,'"+PropertyName+"'"+strDefaultValue+")")
					Slots[PropertyName]=DataTypeList[PropertyType]
				elif row[6]=="&":
					ConditionCode="if int("+ConditionVariable+") & "+row[7]+":"
					if PrevConditionCode!=ConditionCode :
						writeObjectDecode(tabs+ConditionCode)
					PrevConditionCode = ConditionCode
					writeObjectDecode(tabs+"\tgpdwg.objects['temp']."+PropertyName+"=bit.readwithlog2('"+PropertyType+"', dat,'"+PropertyName+"'"+strDefaultValue+")")
					Slots[PropertyName]=DataTypeList[PropertyType]
				elif row[6]=="custom":
					writeObjectDecode(customcode.getCustomCode(row[7],tabs))
					writeObjectDecode(tabs+"gpdwg.objects['temp']."+PropertyName+"=CustomData")
					Slots[PropertyName]=DataTypeList[PropertyType]
				elif row[6]=="customvalue":
					writeObjectDecode(tabs+"gpdwg.objects['temp']."+PropertyName+"="+row[7])
					Slots[PropertyName]=DataTypeList[PropertyType]
			else:
				PrevConditionCode=""
				Slots[PropertyName]=DataTypeList[PropertyType]
				if len(row[5])>0:
					#writeObjectDecode(tabs+"if gpdwg.objects['temp']."+str(row[5])+" "+str(row[6])+str(row[7])+":\n"+tabs+"\tgpdwg.variable."+PropertyName+"=bit.readwithlog('"+PropertyType+"',dat,'"+PropertyName+"',1)")
					TableData.append([PropertyName,DataTypeList[PropertyType],VariableVersionDocString])
				else:
					#writevariableDecode(tabs+"gpdwg.header['variables']['"+PropertyName+"']=bit.readwithlog('"+PropertyType+"',dat,'"+PropertyName+"',1)")
					writeObjectDecode(tabs+"gpdwg.objects['temp']."+PropertyName+"=bit.readwithlog2('"+PropertyType+"',dat,'"+PropertyName+"'"+strDefaultValue+")")
					#TableData.append([PropertyName,DataTypeList[PropertyType],VariableVersionDocString])

for key in ObjectList:
	ObjectsDocFile.write("   "+key+" - "+ObjectList[key]+" <objects/"+ObjectList[key]+">\n")
	ObjectsObjectDocFile=open('doc/python/source/objects/'+ObjectList[key]+'.rst','w+')
	ObjectsObjectDocFile.write("================================\n"+ObjectList[key]+"\n================================\n")
	ObjectsObjectDocFile.close()
gpdwgPart1File=open('code generator/python/g_objects/part2.py','r')
gpdwgPart1=gpdwgPart1File.read()
gpdwgPart1File.close()
ObjectsFile.write(gpdwgPart1)
gpdwgPart2File=open('code generator/python/g_objects/part1.py','r')
gpdwgPart2=gpdwgPart2File.read()
gpdwgPart2File.close()
ObjectsFile.write(gpdwgPart2)

Specfile.close()
ObjectsFile.close()
ObjectsDocFile.close()
ObjectClassFIle.close()

