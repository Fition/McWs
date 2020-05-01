def main(pos,name,file_name):
	localpos = ""
	for each in pos:
		if pos[each] == 0:
			localpos += "~"
		else:
			localpos += "~" + str(pos[each])
	
	name = name.replace("minecraft:","")
	with open(file_name,"a") as f:
		f.write(f"setblock {localpos} {name}\n")
