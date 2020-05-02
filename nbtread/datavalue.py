import traceback
from nbtread.datadicts import *

def getBlockValue(block_name,block_id,proto):
	# 加特殊值
	if "stair" in block_name:
		try:
			block_face = proto["palette"][block_id]["Properties"]["facing"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = stairs[block_face] + stairs[block_half]
			block_name += " "+str(block_value)
			return block_name
		except:
			return block_name

	elif "trapdoor" in block_name:
		try:
			block_face = proto["palette"][block_id]["Properties"]["facing"].value
			block_open = proto["palette"][block_id]["Properties"]["open"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = trapdoor[block_face] + trapdoor[block_half] + trapdoor[block_open]
			block_name += " "+str(block_value)
			return block_name
		except:
			return block_name

	elif ":wooden_slab" in block_name:
		try:
			block_variant = proto["palette"][block_id]["Properties"]["variant"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = wooden_slab[block_variant] + wooden_slab[block_half]
			block_name += " "+str(block_value)
			return block_name
		except:
			traceback.print_exc()
			return block_name

	elif ":stone_slab2" in block_name:
		try:
			block_variant = proto["palette"][block_id]["Properties"]["variant"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = stone_slab2[block_variant] + stone_slab2[block_half]
			block_name += " "+str(block_value)
			return block_name
		except:
			traceback.print_exc()
			return block_name

	elif ":stone_slab3" in block_name:
		try:
			block_variant = proto["palette"][block_id]["Properties"]["variant"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = stone_slab3[block_variant] + stone_slab3[block_half]
			block_name += " "+str(block_value)
			return block_name
		except:
			traceback.print_exc()
			return block_name

	elif ":stone_slab4" in block_name:
		try:
			block_variant = proto["palette"][block_id]["Properties"]["variant"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = stone_slab4[block_variant] + stone_slab4[block_half]
			block_name += " "+str(block_value)
			return block_name
		except:
			traceback.print_exc()
			return block_name

	elif ":stone_slab" in block_name:
		try:
			block_variant = proto["palette"][block_id]["Properties"]["variant"].value
			block_half = proto["palette"][block_id]["Properties"]["half"].value
			block_value = stone_slab[block_variant] + stone_slab[block_half]
			block_name += " "+str(block_value)
			return block_name
		except:
			traceback.print_exc()
			return block_name

	else:
		return block_name
