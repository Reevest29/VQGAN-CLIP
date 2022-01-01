import os
PROMPT = "tower to heaven 8k resolution concept art detailed painting trending on artstation vray beautiful behance hd:1"
if __name__ == '__main__':
	
	sizes = [(2000,200), (300,300), (400,400), (500,500), (600,600), (700,700)]	

	for size in sizes:
		command = 	f"python generate.py " \
					f"-p \"{PROMPT}\" " \
					f"-s {size[0]} {size[1]} " \
					f"-i 100 " \
					f"-o output/size_test/{size[0]}_{size[1]}.png"
		print(command)
		try:
			os.system(command)
		except Exception as e:
			print("t3"+e)
		