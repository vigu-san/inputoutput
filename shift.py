# Taking "gfg input file.txt" as input file
# in reading mode
with open("input.txt", "r") as input:

	with open("output.txt", "w") as output:
		for line in input:
			output.write(line)
