LicenseFile=open('code generator/python/license.txt','r')
LicenseText=LicenseFile.read()
LicenseFile.close()

gpdwgFIle=open('src/python/libgpdwg.py','w+')
gpdwgFIle.write(LicenseText)

gpdwgPart1File=open('code generator/python/g_gpdwg/part1.py','r')
gpdwgPart1=gpdwgPart1File.read()
gpdwgFIle.write(gpdwgPart1)
gpdwgPart1File.close()

gpdwgClassesFile=open('code generator/python/g_gpdwg/classes.py','r')
gpdwgClasses=gpdwgClassesFile.read()
gpdwgFIle.write(gpdwgClasses+'\n')
gpdwgClassesFile.close()


gpdwgPart2File=open('code generator/python/g_gpdwg/part2.py','r')
gpdwgPart2=gpdwgPart2File.read()
gpdwgFIle.write(gpdwgPart2)
gpdwgPart2File.close()

gpdwgFIle.close()