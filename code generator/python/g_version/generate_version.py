LicenseFile=open('code generator/python/license.txt','r')
LicenseText=LicenseFile.read()

versionFIle=open('src/python/version.py','w+')
versionFIle.write(LicenseText)

versionPart1File=open('code generator/python/g_version/part1.py','r')
versionPart1=versionPart1File.read()
versionFIle.write(versionPart1)
