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
		for i in range(self.objectcount):
			TempOutput=TempOutput+"\n\t"+str(i)+": " + str(type(self.objects[i]).__name__) + "\n"
			TempOutput=TempOutput+repr(self.objects[i])

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
