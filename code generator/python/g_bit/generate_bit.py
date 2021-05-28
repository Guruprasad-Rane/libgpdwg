LicenseFile=open('code generator/python/license.txt','r')
LicenseText=LicenseFile.read()

bitFIle=open('src/python/bit.py','w')
bitFIle.write(LicenseText)

bitPart1File=open('code generator/python/g_bit/part1.py','r')
bitPart1=bitPart1File.read()
bitFIle.write(bitPart1)
bitFIle.close()
bitPart1File.close()
