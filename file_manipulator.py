import sys

def main():
	mode = sys.argv[1]
	input_path = sys.argv[2]

	with open(input_path, "r") as f:
		content = f.read()
	
	if mode == "reverse":
		output_path = sys.argv[3]
		with open(output_path, "w") as f:
			f.write(''.join(reversed(content)))
	elif mode == "copy":
		output_path = sys.argv[3]
		with open(output_path, "w") as f:
			f.write(content)
	elif mode == "duplicate-contents":
		times = sys.argv[3]
		with open(input_path, "a") as f:
			for _ in range(int(times)):
				f.write(content)
	elif mode == "replace-string":
		before = sys.argv[3]
		after = sys.argv[4]
		with open(input_path, "w") as f:
			f.write(content.replace(before, after))
	else:
		sys.stdout.write("invalid mode\n")

if __name__=="__main__":
	main()
