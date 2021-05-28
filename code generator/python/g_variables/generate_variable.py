import csv
import tabulate
VariableFile=open('src/python/variables.py','w')
VariableDocFile=open('doc/python/source/variables.rst','w')
ObjectClassFIle=open('code generator/python/g_gpdwg/classes.py','w')
Slots={'CELWEIGHT':'int','ENDCAPS':'int','JOINSTYLE':'int','LWDISPLAY':'int','XEDIT':'int','EXTNAMES':'int','PSTYLEMODE':'int','OLESTARTUP':'int'}
DataTypeList={'B':'int','B':'int','2BD':'bit.point2D','2RD':'bit.point2D','3B':'bit.point3D','3BD':'bit.point3D','3DD':'bit.point3D','3RD':'bit.point3D','BB':'float','BD':'float','BE':'int','BL':'float','BLL':'int','BS':'float','BT':'int','CMC':'bit.color','DD':'float','H':'bit.handle','MC':'int','MS':'int','RC':'int','RD':'float','RL':'int','RS':'int','SN':'int','T':'str','TC':'int','TU':'int','TV':'str','U':'float'}
#ObjectClassFIle.write("from commonObjectClass import *\nimport bit, dwg, log\n")
CommonCondition=False
IfCondition=False
SpecialSlots=['DIMTOL','DIMLIM','DIMTIH','DIMTOH','DIMSE1','DIMSE2','DIMTAD','DIMZIN','DIMPOST','DIMAPOST','DIMALT','DIMALTD','DIMTOFL','DIMSAH','DIMTIX','DIMSOXD','DIMDEC','DIMTDEC','DIMALTU','DIMALTTD','DIMAUNIT','DIMJUST','DIMSD1','DIMSD2','DIMTOLJ','DIMTOLJ','DIMTZIN','DIMALTZ','DIMALTTZ','DIMUPT','DIMTXSTY','DIMBLK','DIMBLK1','DIMBLK2']


class Error(Exception):
   """Base class for other exceptions"""
   pass

def writeObjectClass(Code):
	global ObjectClassFIle
	ObjectClassFIle.write('\n\n')
	ObjectClassFIle.write('\n\n'+Code)


def writevariableDecode(Code):
	global VariableFile
	VariableFile.write('\n'+Code)

def ProcessVariable(Property):
	Property=Property.split("(")[0]
	Property=Property.strip()
	Property=Property.strip(".")
	Property=Property.replace(" ","_")
	Property=Property.upper()
	return Property

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
	TempClassData=TempClassData+"\tdef __repr__(self):\n\t\tprint('Variables')\n\t\tfor i in dir(self):\n\t\t\tif not i.startswith('__') and hasattr(self,i):\n\t\t\t\tprint('\\t'+str(i)+' : '+repr(getattr(self,i)))\n\t\treturn \"\""
	writeObjectClass(TempClassData)

def AddVariableToDecode():
	Property=ProcessVariable(row[7])
	DataType=ProcessVariable(row[9])
	TempCode = ""
	if not CommonCondition : TempCode = '\t'+TempCode
	if  IfCondition : TempCode = '\t'+TempCode
	TempCode = TempCode + '\t'
	if len(row[8].strip())==0:
		TempCode = TempCode + "TempObj."
	TempCode = TempCode + Property +" = bit.readwithlog('"+DataType+"',dat,'"
	if len(row[13].strip())==0:
		TempCode = TempCode + Property
	else:
		TempCode = TempCode + row[13]
	if len(row[11].strip())==0:
		TempCode = TempCode + "',1)"
	else:
		TempCode = TempCode + "',1,"+ row[11] + ")"
	writevariableDecode(TempCode)

def AddPropertyToClass():
	Property=ProcessVariable(row[7])
	DataType=ProcessVariable(row[9])
	if Property.split(".")[0] not in Slots:
		if len(row[14].strip())>0:
			Slots[Property]=str(row[14])
		else:
			Slots[Property]=DataTypeList[DataType]
	else:
		if len(row[14].strip())>0:
			Slots[Property]=str(row[14])

with open('csv spec/variables_spec.csv','r') as Specfile:
	Tabs=0
	Prev_Condition=""
	VariableSpec = csv.reader(Specfile, delimiter=';', quotechar='\'')
	next(VariableSpec,None)
	next(VariableSpec,None)
	writevariableDecode("import logging")
	writevariableDecode("logger = logging.getLogger('gpdwg_logger')")
	writevariableDecode("import bit")
	writevariableDecode("def readall(gpdwg,dat):")
	writevariableDecode('\t"""Reads variables"""')
	writevariableDecode("\tgpdwg.header['variables']={}")
	writevariableDecode("\tver=gpdwg.header['ACADVER']")

	VariableDocFile.write("===============\ngpdwg variables\n===============\n.. module:: gpdwg\n\n.. class:: gpdwgData.gpdwgVariables\n\n   DWG header vaiables are stored in *gpdwgVariables* class. Each variable can be accessed or modified using following attributes.\n\n\n")
	VariableVersionDocString=""
	TableData=[]

	LineNo=0
	for row in VariableSpec:
		LineNo+=1
		if len(row[1])>0:
			CommonCondition=False
			if row[1] == "R13-14":
				writevariableDecode('\tif dat.version <= 14:')
				VariableVersionDocString="Available in DWG version 13 and 14 only."
			elif row[1] == "R13-R14":
				writevariableDecode('\tif dat.version <= 14:')
				VariableVersionDocString="Available in DWG version 13 and 14 only."
			elif row[1] == "R13-15":
				writevariableDecode('\tif dat.version <= 2000:')
				VariableVersionDocString="Available in DWG version 13, 14 and 2000 only."
			elif row[1] == "R13-R15":
				writevariableDecode('\tif dat.version <= 2000:')
				VariableVersionDocString="Available in DWG version 13, 14 and 2000 only."
			elif row[1] == "R13-18":
				writevariableDecode('\tif dat.version <= 2004:')
				VariableVersionDocString="Available in DWG version 13, 14, 2000 and 2004 only."
			elif row[1] == "R13-R18":
				writevariableDecode('\tif dat.version <= 2004:')
				VariableVersionDocString="Available in DWG version 13, 14, 2000 and 2004 only."
			elif row[1] == "R14+":
				writevariableDecode('\tif dat.version >= 14:')
				VariableVersionDocString="Available in DWG version 14 and above only."
			elif row[1] == "R2000+":
				writevariableDecode('\tif dat.version >= 2000:')
				VariableVersionDocString="Available in DWG version 2000 and above only."
			elif row[1] == "R2004+":
				writevariableDecode('\tif dat.version >= 2004:')
				VariableVersionDocString="Available in DWG version 2004 and above only."
			elif row[1] == "R2007":
				writevariableDecode('\tif dat.version == 2007:')
				VariableVersionDocString="Available in DWG version 2007 only."
			elif row[1] == "R2007+":
				writevariableDecode('\tif dat.version >= 2007:')
				VariableVersionDocString="Available in DWG version 2007 and above only."
			elif row[1] == "R2010+":
				writevariableDecode('\tif dat.version >= 2010:')
				VariableVersionDocString="Available in DWG version 2010 and above only."
			elif row[1] == "R2013+":
				writevariableDecode('\tif dat.version >= 2013:')
				VariableVersionDocString="Available in DWG version 2013 and above only."
			elif row[1] == "Common":
				CommonCondition=True
				VariableVersionDocString="Available in all DWG versions."
			else:
				raise Error("Unknown value "+row[1]+" in Column No 1")

		elif len(row[2])>0 and len(row[3])>0:
			
			VariableName=ProcessVariable(row[3])
			VariableType=ProcessVariable(row[2])
			if VariableName in Slots:
				if VariableName not in SpecialSlots:
					exit("Error at line "+str(LineNo)+" in variable spec file: Variable with name "+str(VariableName)+" already in slots.") 

			Slots[VariableName]=DataTypeList[VariableType]

			if CommonCondition:
				tabs="\t"
			else:
				tabs="\t\t"

			if len(row[4])>0:
				writevariableDecode(tabs+"if gpdwg.variable."+str(row[4])+" "+str(row[5])+str(row[6])+":\n"+tabs+"\tgpdwg.variable."+VariableName+"=bit.readwithlog('"+VariableType+"',dat,'"+VariableName+"',1)")
				TableData.append([VariableName,DataTypeList[VariableType],VariableVersionDocString])
			else:
				#writevariableDecode(tabs+"gpdwg.header['variables']['"+VariableName+"']=bit.readwithlog('"+VariableType+"',dat,'"+VariableName+"',1)")
				writevariableDecode(tabs+"gpdwg.variable."+VariableName+"=bit.readwithlog('"+VariableType+"',dat,'"+VariableName+"',1)")
				TableData.append([VariableName,DataTypeList[VariableType],VariableVersionDocString])



	Object={'Name':'gpdwgVariables','ParentClass':'object','DocString':'Class for Variables'}
	dumpClass(Slots,Object)

	VariableFile.write("\n\tlogger.debug('Generating variables from Flags')")
	VariableFile.write("\n\tFlagsValue=int(gpdwg.variable.FLAGS)")
	VariableFile.write("\n\tlogger.debug('CELWEIGHT '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.CELWEIGHT= FlagsValue & 0X001F")
	TableData.append(["CELWEIGHT","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('ENDCAPS '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.ENDCAPS=( FlagsValue & 0X0060) >> 5")
	TableData.append(["ENDCAPS","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('JOINSTYLE '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.JOINSTYLE=( FlagsValue & 0X0180) >> 7")
	TableData.append(["JOINSTYLE","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('LWDISPLAY '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.LWDISPLAY= int(not (FlagsValue & 0X0200))")
	TableData.append(["LWDISPLAY","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('XEDIT '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.XEDIT= int(not (FlagsValue & 0X0400))")
	TableData.append(["XEDIT","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('EXTNAMES '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.EXTNAMES=(FlagsValue & 0X0800) >> 11")
	TableData.append(["EXTNAMES","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('PSTYLEMODE '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.PSTYLEMODE=(FlagsValue & 0X2000) >> 13")
	TableData.append(["PSTYLEMODE","int","Available in all DWG versions."])
	VariableFile.write("\n\tlogger.debug('OLESTARTUP '+str(FlagsValue & 0X001F))")
	VariableFile.write("\n\tgpdwg.variable.OLESTARTUP=(FlagsValue & 0X4000) >> 14")
	TableData.append(["OLESTARTUP","int","Available in all DWG versions."])
	VariableFile.close()
	ObjectClassFIle.close()

	VariableDocFile.write("   "+tabulate.tabulate(TableData, ["Variables","Type","Version"], tablefmt="rst").replace("\n","\n   "))
	VariableDocFile.write("\n\n   .. note::\n      UNKNOWN variables are those which are yet to be reverse engineered.")