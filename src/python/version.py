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
import os.path, logging
import bit, variables, objects

logger = logging.getLogger("gpdwg_logger")

def Check_Obj_CRC(dat,size):
	if dat.bit > 0:
		crc2 = bit.read_crc8 ('0xc0c1', dat.chain, size + 2, dat.byte - (size + 1) )
		logger.debug("CRCA reading at " + str(dat.byte - (size + 1)))
		dat.byte = dat.byte + 1
		dat.bit = 0

	else:
		crc2 = bit.read_crc8 ('0xc0c1', dat.chain, size + 2, dat.byte - (size + 2) )
		logger.debug("CRCB reading at " + str(dat.byte - (size + 2)))

	crc = bit.readwithlog("RS",dat, "CRC",2)	
	if (crc != crc2):
		logger.debug('CRC Mismatch ' + str(crc2) + " " + str(crc) + '\n\n')
		return False
	else:
		logger.debug('CRC Match ------------------------------------------------------------------------------------------------------')
		return True

def decode2000(gpdwg,dat):
	"Decodes version 2000 dwg file."
	#Decode Codepage
	logger.info("Dwg file of size "+str(dat.size)+" bytes")
	SectionInfo=["Variables", "Classes", "ObjectMap", "UnknownSection1", "Measurement", "UnknownSection2"]
	dat.byte=int('0x13',16)
	gpdwg.header['codepage']= bit.readwithlog("RS",dat,"Codepage",1)
	logger.info("Reading codepage done.")

	#Decode section locator records.
	logger.info("")
	logger.info("---- Decode Sections ----")
	dat.byte=int('0x15',16)
	gpdwg.header['sectionCount']=bit.readwithlog("RL",dat,"Section Count",1)#bit.read_RL(dat)
	logger.info("Reading section count done.")
	logger.info("Total "+str(gpdwg.header['sectionCount'])+" sections found.")
	for i in range(gpdwg.header['sectionCount']):
		gpdwg.header['section'][i]={}
		gpdwg.header['section'][i]['number']=bit.readwithlog("RC",dat,"Section "+str(i)+" Number",1) #bit.read_RC(dat)
		gpdwg.header['section'][i]['address']=bit.readwithlog("RL",dat,"Section "+str(i)+" Address",1) #(bit.read_RL(dat))
		gpdwg.header['section'][i]['size']=bit.readwithlog("RL",dat,"Section "+str(i)+" Size",1) #bit.read_RL(dat)	
	for x in range(0,gpdwg.header['sectionCount']):
		logger.debug("Section No."+str(x)+"\t\tStart:"+str(gpdwg.header['section'][x]['address'])+"\t\tEnd:"+str(gpdwg.header['section'][x]['address']+gpdwg.header['section'][x]['size']-1)+"\t\tSize:"+str(gpdwg.header['section'][x]['size'])+"\t\tData:"+SectionInfo[x])
	logger.info("Reading Section details done.")
	crc1 = bit.read_crc8 ('0xc0c1', dat.chain, dat.byte)
	crc2 = bit.readwithlog("RS",dat,"CRC2",1)
	if (crc1 == crc2):
		logger.info("CRC matched.")
	else:
		logger.error("CRC mismatch CRC1:" + str(crc1) + " CRC2:" + str(crc2))
	logger.info("Checking Header Sentinal.")
	bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_HEADER_END')))

	#Decode Header Variables
	logger.info("")
	logger.info("---- Decode Variables ----")
	logger.debug("Shifting dat.byte to section 0 address i.e. "+str(dat.byte)+"-"+str(dat.bit)+" to "+str(gpdwg.header['section'][0]['address'])+"-0" )
	dat.byte=gpdwg.header['section'][0]['address']
	dat.bit=0
	logger.info("Checking Variable Begin Sentinal.")
	bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_VARIABLE_BEGIN')))

	SentinelByte=dat.byte
	logger.debug("Start Reading Varialbles "+str(dat.byte)+" "+str(dat.bit))
	size = bit.readwithlog("RL",dat,"Section Size",1)

	variables.readall(gpdwg,dat)
	logger.info("Reading variables done.")
	if dat.byte < SentinelByte + size + 4:
		logger.debug(" " + str(dat.byte)+ " " + str(dat.bit)+ " ODA seems to write one extra unknown byte here. Shifting one byte.")
		dat.byte+=1
	crc1 = bit.read_crc8 ('0xc0c1', dat.chain, size + 4  , SentinelByte )	
	crc2 = bit.readwithlog("RS",dat,"CRC2",1)

	if (crc1 == crc2):
		logger.info("CRC matched.")
	else:
		logger.error("CRC mismatch CRC1:" + str(crc1) + " CRC2:" + str(crc2))
	logger.info("Checking Variable End Sentinal.")
	bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_VARIABLE_END')))

	#Decode Classes
	logger.info("")
	logger.info("---- Decode Classes ----")
	logger.debug("Shifting dat.byte to section 1 address i.e. "+str(dat.byte)+"-"+str(dat.bit)+" to "+str(gpdwg.header['section'][1]['address'])+"-0" )
	dat.byte=gpdwg.header['section'][1]['address']
	dat.bit=0
	logger.info("Checking Class Begin Sentinal.")
	bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_CLASS_BEGIN')))

	logger.debug(str(dat.byte)+" "+str(dat.bit) + "\tStart Reading Classes ")
	size = bit.readwithlog2('RL', dat,'size')
	dat.bit=0
	last = dat.byte + size
	classCount=0
	while dat.byte < (last -1 ):
		logger.debug("\t --------------------------------------------------------- Class No " + str(classCount) )
		TempClass=gpdwg.gpdwgClass()
		TempClass.CLASS_NUM=bit.readwithlog2('BS', dat,'CLASS_NUM')
		TempClass.VERSION=bit.readwithlog2('BS', dat,'version')
		TempClass.APPNAME=bit.readwithlog2('TV', dat,'APPNAME')
		TempClass.CPLUSPLUSCLASSNAME=bit.readwithlog2('TV', dat,'CPLUSPLUSCLASSNAME')
		TempClass.CLASSDXFNAME=bit.readwithlog2('TV', dat,'CLASSDXFNAME')
		TempClass.WASAZOMBIE= bit.readwithlog2('B', dat,'WASAZOMBIE')
		TempClass.ITEMCLASSID=bit.readwithlog2('BS', dat,'ITEMCLASSID')

		classCount = classCount+ 1
		#gpdwg.classes['count']=classCount
		gpdwg.classes.append(TempClass)

	logger.info("Reading Classes done.")
	logger.info(str(classCount)+ " classes found.")
	logger.debug(str(dat.byte)+" "+str(dat.bit) + "\tStop Reading Classes ")
	gpdwg.classcount=classCount
	if dat.bit > 0:
		dat.byte += 1
		dat.bit=0
	crc2 = bit.readwithlog("RS",dat,"CRC2",1) #bit.read_RS (dat)
	crc1 = bit.read_crc8('0xc0c1', dat.chain, gpdwg.header['section'][1]['size'] - 34,gpdwg.header['section'][1]['address'] + 16)
	if (crc1 == crc2):
		logger.info("CRC matched.")
	else:
		logger.error("CRC mismatch CRC1:" + str(crc1) + " CRC2:" + str(crc2))
	'''
	# Start Scanning Objects
	logger.info("")
	logger.info("---- Decode Objects ----")
	ObjectFoundFlag=0 #temp to be removed later....
	objectcount=0
	intObjectBegin=gpdwg.header['section'][1]['address']+gpdwg.header['section'][1]['size']+512
	intObjectEnd=gpdwg.header['section'][2]['address']
	logger.debug("Scan begins at "+str(intObjectBegin)+" and ends at "+str(intObjectEnd))
	dat.bit=0
	dat.byte = intObjectBegin
	while dat.byte < intObjectEnd:
		prvbyte=dat.byte
		if objects.add(gpdwg,dat):
			gpdwg.objects[objectcount]=gpdwg.objects['temp']
			logger.debug("\t\t\t\t\t\t\t\t Object Found ------------------------------------------------------------")
			#dat.byte=dat.byte+2
			#gpdwg.objects[objectcount]['start-byte']=prvbyte
			#gpdwg.objects[objectcount]['end-byte']=dat.byte
			gpdwg.objectcount += 1
			objectcount += 1
			ObjectFoundFlag=1
		else:
			logger.debug("\tObject Not Found")
			dat.byte=prvbyte+1
			if ObjectFoundFlag == 1:
				break
		#dat.byte=prvbyte+1
		dat.bit=0
		gpdwg.objects.pop('temp')
	logger.info("Scanning Objects done.")
	logger.info(str(objectcount)+" objects found in scan.")
	'''
	
	#Object Map Begin
	logger.info("")
	logger.info("---- Decode Object Map ----")
	logger.debug("Shifting dat.byte to section 2 address i.e. "+str(dat.byte)+"-"+str(dat.bit)+" to "+str(gpdwg.header['section'][2]['address'])+"-0" )
	dat.byte=gpdwg.header['section'][2]['address']
	dat.bit=0
	intObjectMapStart=gpdwg.header['section'][2]['address']
	intObjectMapEnd=gpdwg.header['section'][2]['address'] + gpdwg.header['section'][2]['size'] 
	logger.debug("Section starts at "+str(intObjectMapStart)+" and ends at "+str(intObjectMapEnd)+" with total length of "+str(gpdwg.header['section'][2]['size']))
	ObjectMapCount=0
	while dat.byte < intObjectMapEnd-2:
		SectionStart=dat.byte
		bit.BigEndian=True
		OnjectMapSectionSize=bit.readwithlog2('RS', dat,'Size of Map section')
		bit.BigEndian=False
		LastHeader=0
		LastObjectPos=0
		
		while dat.byte - SectionStart < OnjectMapSectionSize:
			HeaderOffsetPos=bit.readwithlog2('UMC', dat,'Header Offset')
			ObjOffsetPos=bit.readwithlog2('MC', dat,'Location Offset')
			CurHeader=LastHeader+HeaderOffsetPos
			CurObjectPos=LastObjectPos+ObjOffsetPos
			prvbyte=dat.byte
			dat.byte=CurObjectPos
			if objects.add(gpdwg,dat):
				gpdwg.objects[CurHeader]=gpdwg.objects['temp']
				logger.debug("\t\t\t\t\t\t\t\t Object added "+str(gpdwg.objects['temp'].__class__.__name__))
				ObjectMapCount += 1
				LastHeader=CurHeader
				LastObjectPos=CurObjectPos
				gpdwg.objectcount += 1
			else:
				if not str(gpdwg.objects['temp'].__class__.__name__) == "dict":
					logger.error("\t\t\t\t\t\t\t\t Could not read object "+str(gpdwg.objects['temp'].__class__.__name__))
				LastHeader=CurHeader
				LastObjectPos=CurObjectPos
			dat.byte=prvbyte
			dat.bit=0
		bit.BigEndian=True
		crc2 = bit.readwithlog("RS",dat,"CRC2",1) #bit.read_RS (dat)
		bit.BigEndian=False
		crc1 = bit.read_crc8 ('0xc0c1',dat.chain, OnjectMapSectionSize, SectionStart )
		if (crc1 != crc2):
			logger.error('CRC Mismatch ' + str(crc2) + " " + str(crc1) + '\n\n')
		else:
			logger.debug('CRC Match ------------------------------------------------------------------------------------------------------')
	logger.info(str(ObjectMapCount)+" objects found in object map.")


	#Second Header Begins
	logger.info("")
	logger.info("---- Decode Second Header ----")
	logger.debug("Shifting dat.byte to section 3 end i.e. "+str(dat.byte)+"-"+str(dat.bit)+" to "+str(gpdwg.header['section'][3]['address']+gpdwg.header['section'][3]['size'])+"-0" )
	dat.bit=0
	dat.byte=gpdwg.header['section'][3]['address']+gpdwg.header['section'][3]['size']
	logger.info("Checking Second Header Begin Sentinal.")
	bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_SECOND_HEADER_BEGIN')))
	SectionStart=dat.byte
	SectionSize=bit.readwithlog2('RL', dat,'Size of Second Header section')

	bit.readwithlog2('BL', dat,'Location of Second Header section')
	bit.readwithlog2('RCS', dat,'Version')
	for x in range(6):
		bit.readwithlog2('RC', dat,str(x)+'-0s')
	for x in range(4):
		bit.readwithlog2('B', dat,str(x)+'-0s')
	bit.readwithlog2('RC', dat,'Unknown')
	bit.readwithlog2('RC', dat,'Unknown')
	Temp=list()
	checkDict=[24,120,1,6]
	for x in range(4):
		Temp.append(bit.readwithlog2('RC', dat,'Check'+str(x)))
	if Temp == checkDict:
		logger.info("Check Ok.")

	bit.readwithlog2('RC', dat,'Index')
	bit.readwithlog2('BL', dat,'Header Section Address')
	bit.readwithlog2('BL', dat,'Header Section Size')
	bit.readwithlog2('RC', dat,'Index')
	bit.readwithlog2('BL', dat,'Class Section Address')
	bit.readwithlog2('BL', dat,'Class Section Size')
	bit.readwithlog2('RC', dat,'Index')
	bit.readwithlog2('BL', dat,'Object Map Section Address')
	bit.readwithlog2('BL', dat,'Object Map Section Size')
	bit.readwithlog2('RC', dat,'Index')
	bit.readwithlog2('BL', dat,'Unknown Section Address')
	bit.readwithlog2('BL', dat,'Unknown Section Size')
	bit.readwithlog2('RC', dat,'index')
	bit.readwithlog2('BL', dat,'Unknown Section Address')
	bit.readwithlog2('BL', dat,'Unknown Section Size')
	bit.readwithlog2('RC', dat,'index')
	bit.readwithlog2('BL', dat,'Unknown Section Address')
	bit.readwithlog2('BL', dat,'Unknown Section Size')
	bit.readwithlog2('BS', dat,'index')
	for x in range(14):
		Temp=bit.readwithlog2('RC', dat,'size')
		bit.readwithlog2('RC', dat,'index')
		for x in range(Temp):
			bit.readwithlog2('RC', dat,'data-'+str(x))
	dat.byte += 8
	crc2 = bit.readwithlog("RS",dat,"CRC2",1)
	crc1 = bit.read_crc8 ('0xc0c1',dat.chain, SectionSize, SectionStart )
	if (crc1 != crc2):
		logger.error('CRC Mismatch ' + str(crc2) + " " + str(crc1) + '\n\n')
	else:
		logger.debug('CRC Match ------------------------------------------------------------------------------------------------------')
	logger.info("Checking Second Header End Sentinal.")
	bit.check_Sentinel (dat, bit.sentinel (bit.DwgSentinel('DWG_SENTINEL_SECOND_HEADER_END')))
	bit.readwithlog2('RC', dat,'index')
	bit.readwithlog2('RC', dat,'index')
	bit.readwithlog2('RC', dat,'index')
	bit.readwithlog2('RC', dat,'index')
	logger.info("")
	logger.info("Finished Decoding dwg file.")