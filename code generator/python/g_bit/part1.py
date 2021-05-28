# Code reference bit.c from libdwg written by Felipe Castro

import logging, struct, string
logger = logging.getLogger("gpdwg_logger")
BigEndian=False

class handle(object):
	"""Date Strucutre for Handle."""
	def __init__(self, code=0,size=0,value=0):
		self.code = code
		self.size = size
		self.value = value
	def __repr__(self):
		return "Handle(%i,%i,%i)" % (self.code,self.size,self.value)

class color(object):
	"""Date Strucutre for Color."""
	def __init__(self, index=0,name="",book_name="",rgb=0,byte=0):
		self.index = index
		self.name = name
		self.book_name = book_name
		self.rgb = rgb
		self.byte = byte
	def __repr__(self):
		return "Color(%i,%s,%s,%i,%i)" % (self.index,self.name,self.book_name,self.rgb,self.byte)

class point3D(object):
	"""Data Strucutre for 3D Point """
	def __init__(self, x=0,y=0,z=0):
		self.x = x
		self.y = y
		self.x = z
	def __repr__(self):
		return "3DPoint(%f,%f,%f)" % (self.x,self.y,self.z)

class point2D(object):
	"""Data Strucutre for 2D Point """
	def __init__(self, x=0,y=0):
		self.x = x
		self.y = y
	def __repr__(self):
		return "2DPoint(%i,%i)" % (self.x,self.y)

class point3DList(object):
	"""Data Strucutre for 3D Point """
	def __init__(self, x=0,y=0,z=0):
		self.x = x
		self.y = y
		self.x = z
	def __repr__(self):
		return "3DPoint(%f,%f,%f)" % (self.x,self.y,self.z)

def DwgSentinel(str):
	if str =='DWG_SENTINEL_HEADER_END':
		return 0
	if str =='DWG_SENTINEL_PICTURE_BEGIN':
		return 1
	if str =='DWG_SENTINEL_PICTURE_END':
		return 2
	if str =='DWG_SENTINEL_VARIABLE_BEGIN':
		return 3
	if str =='DWG_SENTINEL_VARIABLE_END':
		return 4
	if str =='DWG_SENTINEL_CLASS_BEGIN':
		return 5
	if str =='DWG_SENTINEL_CLASS_END':
		return 6
	if str =='DWG_SENTINEL_SECOND_HEADER_BEGIN':
		return 7
	if str =='DWG_SENTINEL_SECOND_HEADER_END':
		return 8

def sentinel (Dwg_Sentinel_Index):
    sentinels= (('0x95', '0xA0', '0x4E', '0x28', '0x99', '0x82', '0x1A', '0xE5', '0x5E', '0x41', '0xE0', '0x5F','0x9D', '0x3A', '0x4D', '0x00'),
        ('0x1F', '0x25', '0x6D', '0x07', '0xD4', '0x36', '0x28', '0x28', '0x9D', '0x57', '0xCA', '0x3F','0x9D', '0x44', '0x10', '0x2B'),
        ('0xE0', '0xDA', '0x92', '0xF8', '0x2B', '0xc9', '0xD7', '0xD7', '0x62', '0xA8', '0x35', '0xC0','0x62', '0xBB', '0xEF', '0xD4'),
        ('0xCF', '0x7B', '0x1F', '0x23', '0xFD', '0xDE', '0x38', '0xA9', '0x5F', '0x7C', '0x68', '0xB8','0x4E', '0x6D', '0x33', '0x5F'),
        ('0x30', '0x84', '0xE0', '0xDC', '0x02', '0x21', '0xC7', '0x56', '0xA0', '0x83', '0x97', '0x47','0xB1', '0x92', '0xCC', '0xA0'),
        ('0x8D', '0xA1', '0xC4', '0xB8', '0xC4', '0xA9', '0xF8', '0xC5', '0xC0', '0xDC', '0xF4', '0x5F','0xE7', '0xCF', '0xB6', '0x8A'),
        ('0x72', '0x5E', '0x3B', '0x47', '0x3B', '0x56', '0x07', '0x3A', '0x3F', '0x23', '0x0B', '0xA0','0x18', '0x30', '0x49', '0x75'),
        ('0xD4', '0x7B', '0x21', '0xCE', '0x28', '0x93', '0x9F', '0xBF', '0x53', '0x24', '0x40', '0x09','0x12', '0x3C', '0xAA', '0x01'),
        ('0x2B', '0x84', '0xDE', '0x31', '0xD7', '0x6C', '0x60', '0x40', '0xAC', '0xDB', '0xBF', '0xF6','0xED', '0xC3', '0x55', '0xFE'))
    return (sentinels[Dwg_Sentinel_Index])

#Read 1 bit
def read_B(dat):
	byteObject=struct.pack('B',dat.chain[dat.byte])
	byte = struct.unpack('B',byteObject)[0]
	result = (byte & (int('0x80',16) >> dat.bit)) >> (7 - dat.bit)
	shift_pos(dat,1)
	return int(result)

# Read 2 bits
def read_BB(dat):
	if BigEndian == True:
		Format=">B"
	else:
		Format="B"
	byte = struct.unpack(Format,dat.chain[dat.byte : (dat.byte+1)])[0]
	if (dat.bit < 7):
		result = (byte & (int('0xc0',16) >> dat.bit)) >> (6 - dat.bit)
	else:
		result = (byte & int('0x01',16)) << 1
		if (dat.byte < (dat.size - 1)):
			byte = struct.unpack(Format,dat.chain[(dat.byte+1): (dat.byte+2)])[0]
			result = result | ((byte & int('0x80',16)) >> 7)
	shift_pos(dat,2)
	return int(result)

def read_3B(dat):
	logger.info("read_3B function need to be workedout.")

#Read 1 bitshort
def read_BS(dat):
	result=0
	two_bit_code=read_BB(dat)
	if two_bit_code == 0:
		result=read_RS(dat)
		return float(result)
	elif two_bit_code==1:
		result=read_RC(dat)
		return float(result)
	elif two_bit_code==2:
		return float(0.0)
	else:
		return float(256)

def shift_pos(dat,shift):
	endpos = dat.bit + shift;
	if (dat.byte >= dat.size - 1) and (endpos > 7):
		dat.bit = 7;
		return
	dat.bit = endpos % 8
	dat.byte += int(endpos / 8)

# Read 1 byte (raw char)
def read_RC(dat):
	if BigEndian == True:
		Format=">B"
	else:
		Format="B"
	byte = struct.unpack_from(Format,dat.chain,dat.byte)[0]
	if dat.bit == 0 :
		result = byte
	else:
		result = (byte << dat.bit)  & 255
		if dat.byte < (dat.size - 1):
			byte = struct.unpack_from(Format,dat.chain,dat.byte+1)[0]
			result = result | byte >> (8 - dat.bit)
	shift_pos(dat,8)
	return int(result)

# Read serie of 1 byte (raw char)
def read_RCS(dat):
	result = ""
	for x in range(6):
		RC = read_RC(dat)
		result = result + chr(RC)
	'''
	while RC > 0:
		result = result + chr(RC)
		RC = read_RC(dat)
	'''
	return result

# Read 1 raw double (8 bytes)
def read_RD (dat):
	ByteList={}
	for i in range(0,8):
		ByteList[i] = read_RC(dat)
	DoubleByte=struct.pack('8B',ByteList[0],ByteList[1],ByteList[2],ByteList[3],ByteList[4],ByteList[5],ByteList[6],ByteList[7])
	result = struct.unpack('d',DoubleByte[0:8])[0]
	return float(result)

# Read 1 word (raw short)
def read_RS(dat):
	byte1 = read_RC(dat)
	byte2 = read_RC(dat)
	if BigEndian == True:
		return ((byte1 << 8) | byte2)
	else:
		return ((byte2 << 8) | byte1)


# Read 1 raw long (2 words) 
def read_RL(dat):
	word1 = read_RS(dat)
	word2 = read_RS(dat)
	return word2 << 16 | word1

# Read 1 raw long (2 words) LE
def read_RL_LE(dat):
	word1 = read_RS(dat)
	word2 = read_RS(dat)
	return word1 << 16 | word2

# Read 1 bitdouble (compacted data) 
def read_BD(dat):
	result=0
	two_bit_code=read_BB(dat)
	if two_bit_code == 0:
		result=read_RD(dat)
		return float(result)
	elif two_bit_code==1:
		return float(1.0)
	elif two_bit_code==2:
		return float(0.0)
	else:
		logger.error(str(dat.byte)+ " " + str(dat.bit) + " bit.read_BD: unexpected 2 bit code: " + str(two_bit_code))
		return float(result)

# 8-bit CRC 
def read_crc8(dx,adr,n,y=0):
	StartByte=y
	NoOfSteps=n
	intdx=int(dx,16)
	intPad=int("0xFF", 16)
	ckrtable = ['0x0000', '0xC0C1', '0xC181', '0x0140', '0xC301', '0x03C0', '0x0280', '0xC241', '0xC601', '0x06C0', '0x0780', '0xC741', '0x0500', '0xC5C1', '0xC481', '0x0440', '0xCC01', '0x0CC0','0x0D80', '0xCD41', '0x0F00', '0xCFC1', '0xCE81', '0x0E40', '0x0A00', '0xCAC1', '0xCB81','0x0B40', '0xC901', '0x09C0', '0x0880', '0xC841', '0xD801', '0x18C0', '0x1980', '0xD941','0x1B00', '0xDBC1', '0xDA81', '0x1A40', '0x1E00', '0xDEC1', '0xDF81', '0x1F40', '0xDD01','0x1DC0', '0x1C80', '0xDC41', '0x1400', '0xD4C1', '0xD581', '0x1540', '0xD701', '0x17C0', '0x1680', '0xD641', '0xD201', '0x12C0', '0x1380', '0xD341', '0x1100', '0xD1C1', '0xD081', '0x1040', '0xF001', '0x30C0', '0x3180', '0xF141', '0x3300', '0xF3C1', '0xF281', '0x3240', '0x3600', '0xF6C1', '0xF781', '0x3740', '0xF501', '0x35C0', '0x3480', '0xF441', '0x3C00', '0xFCC1', '0xFD81', '0x3D40', '0xFF01', '0x3FC0', '0x3E80', '0xFE41', '0xFA01', '0x3AC0', '0x3B80', '0xFB41', '0x3900', '0xF9C1', '0xF881', '0x3840', '0x2800', '0xE8C1', '0xE981', '0x2940', '0xEB01', '0x2BC0', '0x2A80', '0xEA41', '0xEE01', '0x2EC0', '0x2F80', '0xEF41', '0x2D00', '0xEDC1', '0xEC81', '0x2C40', '0xE401', '0x24C0', '0x2580', '0xE541', '0x2700', '0xE7C1', '0xE681', '0x2640', '0x2200', '0xE2C1', '0xE381', '0x2340', '0xE101', '0x21C0', '0x2080', '0xE041', '0xA001', '0x60C0', '0x6180', '0xA141', '0x6300', '0xA3C1', '0xA281', '0x6240', '0x6600', '0xA6C1', '0xA781', '0x6740', '0xA501', '0x65C0', '0x6480', '0xA441', '0x6C00', '0xACC1', '0xAD81', '0x6D40', '0xAF01', '0x6FC0', '0x6E80', '0xAE41', '0xAA01', '0x6AC0', '0x6B80', '0xAB41', '0x6900', '0xA9C1', '0xA881', '0x6840', '0x7800', '0xB8C1', '0xB981', '0x7940', '0xBB01', '0x7BC0', '0x7A80', '0xBA41', '0xBE01', '0x7EC0', '0x7F80', '0xBF41', '0x7D00', '0xBDC1', '0xBC81', '0x7C40', '0xB401', '0x74C0', '0x7580', '0xB541', '0x7700', '0xB7C1', '0xB681', '0x7640', '0x7200', '0xB2C1', '0xB381', '0x7340', '0xB101', '0x71C0', '0x7080', '0xB041', '0x5000', '0x90C1', '0x9181', '0x5140', '0x9301', '0x53C0', '0x5280', '0x9241', '0x9601', '0x56C0', '0x5780', '0x9741', '0x5500', '0x95C1', '0x9481', '0x5440', '0x9C01', '0x5CC0', '0x5D80', '0x9D41', '0x5F00', '0x9FC1', '0x9E81', '0x5E40', '0x5A00', '0x9AC1', '0x9B81', '0x5B40', '0x9901', '0x59C0', '0x5880', '0x9841', '0x8801', '0x48C0', '0x4980', '0x8941', '0x4B00', '0x8BC1', '0x8A81', '0x4A40', '0x4E00', '0x8EC1', '0x8F81', '0x4F40', '0x8D01', '0x4DC0', '0x4C80', '0x8C41', '0x4400', '0x84C1', '0x8581', '0x4540', '0x8701', '0x47C0', '0x4680', '0x8641', '0x8201', '0x42C0', '0x4380', '0x8341', '0x4100', '0x81C1', '0x8081', '0x4040']
	while (n > 0):
		intadr = struct.unpack('B',adr[y: y+1])[0]
		al = intadr ^ (intdx & intPad)
		intdx = (intdx >> 8) & intPad
		intdx = intdx ^ int(ckrtable[(al  & intPad)],16)
		y = y +1
		n = n - 1
	logger.debug("Reading CRC from "+str(StartByte)+" for "+str(NoOfSteps)+" bytes = "+str(intdx))#             str(dat.byte)+"\t"+str(dat.bit)+"\tCRC1\t"+str(crc1))
	return intdx

#Search for a sentinel; if found, positions "dat->byte"  immediately after it.
def search_sentinel(dat, sentinel):
	for i in range (0,dat.size):
		for j in range (0,16):
			if struct.unpack('B',dat.chain[i+j: i+j+1])[0] != int(sentinel[j],16):
				break

			if j == 15:
				logger.debug("Sentinel found from "+str(i)+" to "+str(i+j))
				dat.byte = i + j+1
				dat.bit = 0
				return dat

def check_Sentinel(dat,sentinel):
	for j in range (0,16):
		StartPos=dat.byte
		#if readwithlog("RC",dat,"Sentinel "+str(j),1) != int(sentinel[j],16):
		if read_RC(dat) != int(sentinel[j],16):
			logger.error( str(StartPos) + " Sentinel not found at correct location.")
			return False
	logger.info("Sentinel found at correct location.")
	return True


def isprintable(s, codec='ascii'):  # Code to be moved to some other file...
	return all(c in string.printable for c in s)

#Read simple text.
def read_TV(dat):
	length = int(read_BS(dat))
	result = ""
	if length > 5000:  # Dont know why????
		return "NULL"

	for i in range(0,length):
		temp = read_RC(dat)

		if temp == 0:
		#	log.log(9,"readTV: End of String found:" + result)
			break
		if temp == 10:
		#	log.log(9,"readTV: Newline found:" + result)
			break

				# Some confused code comes here....
		if isprintable(str(chr(temp))):
		#	log.log(9,(temp))
			result = result + str(chr(temp))
	return result

#Read 1 bitlong (compacted data)
def read_L(dat):
	return read_RL_LE(dat)


#Read 1 bitlong (compacted data)
def read_BL(dat):
	result=0
	two_bit_code=read_BB(dat)
	if two_bit_code == 0:
		result=read_RL(dat)
		return float(result)
	elif two_bit_code==1:
		result=read_RC(dat) & 0xFF
		return float(result)
	elif two_bit_code==2:
		return float(0.0)
	elif two_bit_code==3:
		return float(256)

#Read handle-references
def read_H(dat):
	result=handle()
	temp=0
	result.code=read_RC(dat)
	result.size=result.code & 0x0f
	result.code=(result.code) >> 4
	for i in range(result.size):
		temp= (temp << 8 ) + read_RC(dat)
	result.value = temp
	return (result)


# Read Color
def read_CMC(dat):
	result=color()
	result.index=read_BS(dat)
	result.name=""
	result.book_name=""
	if dat.version >= 2004:
		result.rgb = read_BL(dat)
		result.byte = read_RC(dat)
		if result.byte & 1:
			result.name = read_TV(dat)
		if result.byte & 2:
			result.book_name = read_TV(dat)
	return result

# Read 3D Point
def read_3BD(dat):
	result=point3D()
	result.x=read_BD(dat)
	result.y=read_BD(dat)
	result.z=read_BD(dat)
	return result

# Read 3D Point
def read_3RD(dat):
	result=point3D()
	result.x=read_RD(dat)
	result.y=read_RD(dat)
	result.z=read_RD(dat)
	return result

# Read 2D Point
def read_2BD(dat):
	result=point2D()
	result.x=read_BD(dat)
	result.y=read_BD(dat)
	return result

# Read 2D Point
def read_2RD(dat):
	result=point2D()
	result.x=read_RD(dat)
	result.y=read_RD(dat)
	return result

# Read bit-extrusion
def read_BE(dat):
	result=point3D()
	if read_B(dat):
		result.x=0
		result.y=0
		result.z=1
	else:
		result.x=read_BD(dat)
		result.y=read_BD(dat)
		result.z=read_BD(dat)
	return result

#Read bit-double with default
def read_DD(dat,Default_value):
	two_bit_code=read_BB(dat)
	ByteList=bytearray(9)
	struct.pack_into('d',ByteList,0, Default_value)
	if two_bit_code== 0:
		return float(Default_value)
	elif two_bit_code == 1:
		ByteList[0]=read_RC(dat)
		ByteList[1]=read_RC(dat)
		ByteList[2]=read_RC(dat)
		ByteList[3]=read_RC(dat)
		DoubleByte=struct.pack('8B',ByteList[0],ByteList[1],ByteList[2],ByteList[3],ByteList[4],ByteList[5],ByteList[6],ByteList[7])
		result = struct.unpack('d',DoubleByte[0:8])[0]
		return float(result)
	elif two_bit_code == 2:
		ByteList[4]=read_RC(dat)
		ByteList[5]=read_RC(dat)
		ByteList[0]=read_RC(dat)
		ByteList[1]=read_RC(dat)
		ByteList[2]=read_RC(dat)
		ByteList[3]=read_RC(dat)
		DoubleByte=struct.pack('8B',ByteList[0],ByteList[1],ByteList[2],ByteList[3],ByteList[4],ByteList[5],ByteList[6],ByteList[7])
		result = struct.unpack('d',DoubleByte[0:8])[0]
		return float(result)
	elif two_bit_code == 3:
		return read_RD(dat)

def read_2DD(dat,Default_value):
	result=point2D()
	result.x=read_DD(dat,Default_value[0])
	result.y=read_DD(dat,Default_value[1])
	return result

def read_3DD(dat,Default_value):
	result=point3D()
	result.x=read_DD(dat,Default_value)
	result.y=read_DD(dat,Default_value)
	result.z=read_DD(dat,Default_value)
	return result

#Read bit-thickness
def read_BT(dat):
	#mode=int(0)
	mode=read_B(dat)
	if mode:
		return 0.0
	else:
		return read_BD(dat)

#Read 1 modular short (max 2 words) 
def read_MS(dat):
	result =0
	j=0
	word={}
	for i in range(1,0,-1):
		word[i]=read_RS(dat)
		if (not (word[i] & 0x8000)):
			result = result | (word[i]<<j)
			return (result)
		else:
			word[i] = word[i] & 0x7fff
			result = result | (word[i] << j)
		j=j+15
	return 0
'''
BITCODE_MC
bit_read_MC (Bit_Chain *dat)
{
  int i, j;
  int negative;
  unsigned char byte[5];
  BITCODE_UMC result;

  negative = 0;
  result = 0;
  for (i = 4, j = 0; i >= 0; i--, j += 7)
    {
      byte[i] = bit_read_RC (dat);
      CHK_OVERFLOW(__FUNCTION__, 0)
      if (!(byte[i] & 0x80))
        {
          if ((byte[i] & 0x40))
            {
              negative = 1;
              byte[i] &= 0xbf;
            }
          result |= (((BITCODE_UMC)byte[i]) << j);
          return (negative ? -((BITCODE_MC)result) : (BITCODE_MC)result);
        }
      else
        byte[i] &= 0x7f;

      result |= ((BITCODE_UMC)byte[i]) << j;
    }

  loglevel = dat->opts & DWG_OPTS_LOGLEVEL;
  LOG_ERROR (
      "bit_read_MC: error parsing modular char. i=%d, j=%d, result=0x%lx,\n"
      " @%lu.@%u: [0x%x 0x%x 0x%x 0x%x 0x%x]",
      i, j, result, dat->byte - 5, dat->bit, dat->chain[dat->byte - 5],
      dat->chain[dat->byte - 4], dat->chain[dat->byte - 3],
      dat->chain[dat->byte - 2], dat->chain[dat->byte - 1])
  return 0; /* error... */
}
'''
#Read 1 modular char
def read_MC(dat):
	i=0
	j=0
	result=0
	negative=False
	bytesArray=[0,0,0,0,0,0]
	for i in range(4,0,-1):
		bytesArray[i]=read_RC(dat)
		if(not (bytesArray[i] & (int('0x80',16)))):
			if(bytesArray[i] & (int('0x40',16))):
				negative =True
				bytesArray[i] = bytesArray[i] & (int('0xbf',16))
			result = result | (bytesArray[i] << j)
			if negative:
				return result * -1
			else:
				return result
		else:
			bytesArray[i] = bytesArray[i] & (int('0x7f',16))
			result = result | (bytesArray[i] << j)
		j = j + 7		

'''
BITCODE_UMC
bit_read_UMC (Bit_Chain *dat)
{
  int i, j;
  // eg handle FD485E65F
  #define MAX_BYTE_UMC 6
  unsigned char byte[MAX_BYTE_UMC] = { 0, 0, 0, 0, 0, 0 };
  BITCODE_UMC result;

  result = 0;
  for (i = MAX_BYTE_UMC-1, j = 0; i >= 0; i--, j += 7)
    {
      byte[i] = bit_read_RC (dat);
      CHK_OVERFLOW(__FUNCTION__, 0)
      if (!(byte[i] & 0x80))
        {
          result |= (((BITCODE_UMC)byte[i]) << j);
          return result;
        }
      else
        byte[i] &= 0x7f;

      result |= ((BITCODE_UMC)byte[i]) << j;
    }

  loglevel = dat->opts & DWG_OPTS_LOGLEVEL;
  LOG_ERROR (
      "bit_read_UMC: error parsing modular char, i=%d,j=%d,result=0x%lx", i, j,
      result)
  LOG_HANDLE ("  @%lu.%u: [0x%x 0x%x 0x%x 0x%x 0x%x]\n", dat->byte - 5,
            dat->bit, dat->chain[dat->byte - 5], dat->chain[dat->byte - 4],
            dat->chain[dat->byte - 3], dat->chain[dat->byte - 2],
            dat->chain[dat->byte - 1])
  return 0; /* error... */
}
'''

#Read 1 unsigned modular char
def read_UMC(dat):
	i=0
	j=0
	result=0
	bytesArray=[0,0,0,0,0,0]
	for i in range(5,0,-1):
		bytesArray[i]=read_RC(dat)
		if(not (bytesArray[i] & (int('0x80',16)))):
			result = result | (bytesArray[i] << j)
			return result
		else:
			bytesArray[i] = bytesArray[i] & (int('0x7f',16))
			result = result | (bytesArray[i] << j)
		j = j + 7

def read_INSCOUNT(dat):
	Temp1=read_RC(dat)
	result=0
	while Temp1 > 0:
		result = result + Temp1
		Temp1=read_RC(dat)
	return result



def readwithlog2(strType,dat,strName,intDefault=None):
	Temp1=str(dat.byte)+"\t"+str(dat.bit)+"\t"+strName
	if not intDefault==None:
		Temp2=eval("read_"+strType+"(dat,"+str(intDefault)+")")
	else:
		Temp2=eval("read_"+strType+"(dat)")
	logger = logging.getLogger("gpdwg_logger")
	logger.debug(Temp1+"\t"+repr(Temp2))
	return Temp2


def readwithlog(strType,dat,strName,intTabs,intDefault=0):
	Temp1=str(dat.byte)+"\t"+str(dat.bit)+"\t"+strName
	if intDefault:
		Temp2=eval("read_"+strType+"(dat,"+str(intDefault)+")")
	else:
		Temp2=eval("read_"+strType+"(dat)")
	logger = logging.getLogger("gpdwg_logger")
	logger.debug(Temp1+"\t"+repr(Temp2))
	return Temp2