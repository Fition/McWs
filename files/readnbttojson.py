import python_nbt.nbt as nbt

file_path = input("path:")
proto = nbt.read_from_nbt_file(file_path)
with open(file_path+".json","w") as f:
	f.write(str(proto))
