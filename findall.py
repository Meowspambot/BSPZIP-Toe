import argparse
import fileinput
import os

#broken/TODO
#	-OverlayName1-9 doesn't pack looks like "OverlayName1" "custom/effects/static2"
#	-"SpotlightTexture" input for "env_projectedtexture" doesn't pack looks like "OnTrigger" "playerlight_projected,SpotlightTexture,custom/texture/flashlight_02.vtf,0,-1"
#	-comparing items to "materialdir/sounddir/modeldir" with for loop may not be optimal
#	-name vars something other then temp
#	-actually comment my code

def parsefile(input_file,compare_dir,output):
	compare_dirlen = len(args.input_dir.split('\\'))
	print(compare_dirlen)
	outputdirs = ['']
	materialdir = parsedir(compare_dir+'\\materials')
	sounddir = parsedir(compare_dir+'\\sound')
	modeldir = parsedir(compare_dir+'\\models')
	with open(input_file,'r') as f:
		raw = f.read()
	f.closed
	for line in stripdata(raw.splitlines()):
		temp = line.split('"')
		if temp[1] == 'material':
			matdir = ('materials/'+temp[3]).lower()
			for entry in materialdir:
				reldir = commonfixdir(entry,compare_dirlen)
				reldir = reldir.split('.')
				reldir = reldir[0]
				if matdir == reldir.lower():
					print('found',reldir)
					temp4 = entry.split('.')
					addfile(reldir,temp4[0],outputdirs,['.vtf','.vmt'])
					break
		if temp[1] == 'message':
			snddir = ('sound/'+temp[3]).lower()
			for entry in sounddir:
				reldir = commonfixdir(entry,compare_dirlen)
				if snddir == reldir.lower():
					print('found',reldir)
					addfile(reldir,entry,outputdirs)
					break
		if temp[1] == 'model' and len(temp[3].split('.')) >= 2:
			#print(temp)
			temp2 = temp[3].split('.')
			if temp2[1] == 'mdl':
				mdldir = (temp2[0])
				for entry in modeldir:
					reldir = commonfixdir(entry,compare_dirlen)
					reldir = reldir.split('.')
					reldir = reldir[0]
					if mdldir == reldir.lower():
						print('found',reldir)
						temp4 = entry.split('.')
						for dir in parsemdltextures(temp4[0]+'.mdl',compare_dir,materialdir):
							print(dir)
							addfile(dir,compare_dir+'\\'+dir,outputdirs,['.vtf','.vmt'])
							addfile(reldir,temp4[0],outputdirs,['.mdl','.phy','.vvd','.sw.vtx','.dx90.vtx','.dx80.vtx'])
						break
			if temp2[1] == 'vmt':
				sprdir = ('materials/'+temp[3]).lower()
				for entry in materialdir:
					reldir = commonfixdir(entry,compare_dirlen)
					if sprdir == reldir.lower():
						print('found',reldir)
						reldir = reldir.split('.')
						temp4 = entry.split('.')
						addfile(reldir[0],temp4[0],outputdirs,['.vtf','.vmt'])
						break
		if temp[1] == 'skyname':
			skydir = ('materials/skybox/'+temp[3]).lower()
			for entry in parsedir(compare_dir+'\\materials\\skybox'):
				reldir = commonfixdir(entry,compare_dirlen)
				reldir = reldir.split('.')
				reldir = reldir[0][:-2]
				if skydir == reldir.lower():
					print('found',reldir)
					temp4 = entry.split('.')
					addfile(reldir,temp4[0][:-2],outputdirs,['bk.vtf','dn.vtf','ft.vtf','lf.vtf','rt.vtf','up.vtf','bk.vmt','dn.vmt','ft.vmt','lf.vmt','rt.vmt','up.vmt',])
					break
			pass
	writefile(outputdirs,output)

def stripdata(dirinput):
	tempdir = []
	for line in dirinput:
		if line not in tempdir: #forgot i was programming in "python:pseudo-code the language"
			temp = line.split('"')
			if len(temp) >= 2:
				if temp[1] == 'material' or temp[1] == 'message' or temp[1] == 'model' or temp[1] == 'skyname':
					tempdir.append(line)
	return tempdir

def commonfixdir(dir,dir_len,dir_char='/'):
	fixdir = dir.split('\\') #make fixdir be like 'materials/dirname/filename'
	for i in range(dir_len):
		fixdir.pop(0)
	fixdir = dir_char.join(fixdir)
	return fixdir

def parsemdltextures(input_file,compare_dir,materialdir):
	mdlnamelen = len(compare_dir.split('\\'))
	mdlmaterial = []
	bytebuffer = []
	entrypointfound = False
	hookstr = commonfixdir(input_file,mdlnamelen+1,'\\')
	print(hookstr)
	with open(input_file,'rb') as f:
		rawmdl = f.read()
	f.closed
	print(input_file)
	for i in range(len(rawmdl)): #loop over all bytes back-to-front and try to find hookstr
		for j in range(len(hookstr)):
			try:
				bytebuffer.append(rawmdl[(len(rawmdl)-i)+j])
			except:
				pass
			if ("".join(map(chr, bytebuffer))).lower() == hookstr.lower():
				entrypoint = len(rawmdl)-i
				entrypointfound = True
				print("MYBODYISREADY",entrypoint)
				break
		if entrypointfound: #if we find hookstr get material names from the entry point offset and cross reference to make sure its valid
			bytebuffer = []
			for i in range(len(rawmdl)-entrypoint):
				bytebuffer.append(rawmdl[i+entrypoint])
			decoded = "".join(map(chr, bytebuffer))
			print('1',decoded)
			decoded = decoded.strip('\x00')
			decoded = decoded.split('\x00')[1:]
			print('2',decoded)
			for i,thing in enumerate(decoded):
				if not thing == decoded[-1]:
					print(compare_dir + '\\materials\\' + decoded[-1] + decoded[i] + '.vtf')
					if (compare_dir + '\\materials\\' + decoded[-1] + decoded[i] + '.vtf') in materialdir:
						mdlmaterial.append('materials\\' + decoded[-1] + decoded[i]) #decoded[i] = 'materials\\' + decoded[-1] + decoded[i]
				else:
					decoded.pop(i)
			break
		bytebuffer = []
	print(mdlmaterial)
	return mdlmaterial
	
def addfile(filepathrel,filepath,dirlist=[''],nametable=['']):
	for item in nametable:
		if filepathrel+item in dirlist:
			print(filepathrel+item, 'already exists')
			return dirlist
		dirlist.append(filepathrel+item)
		dirlist.append(filepath+item)
		print('added', filepathrel+item)
	return dirlist
	
def parsedir(root_dir):
	coolgay = []
	for root, subdirs, files in os.walk(root_dir):
		for filename in files:
			file_path = os.path.join(root, filename)
			coolgay.append(file_path)
	return coolgay

def writefile(to_write,name):
	to_write.pop(0)
	pathdata = '\n'.join(to_write)
	with open(name,'w') as f:
		f.write(pathdata)
	f.closed

	
parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("input_dir")
parser.add_argument("output_file")
args = parser.parse_args()
parsefile(args.input_file,args.input_dir,args.output_file)
