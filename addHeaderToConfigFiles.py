import sys
import os
import glob

# Inserts the header into the file
def addHeaderToFile(filename, header):

	with open(filename, 'r') as original:
		data = original.read()
	with open(filename, 'w') as modified:
		modified.write(header + data)

	print(filename + "->" + "header added")

# Formats the header based on the brand and environment
def setHeader(brand, env):

	headerFileName = "baseHeader.txt"

	if os.path.isfile(headerFileName):

		with open("baseHeader.txt", 'r') as headerFile:
			base_header = headerFile.read()

		if base_header == "":
			exit("The header file is empty")
	else:
		exit("The header file doens't exists. Make sure the file \"baseHeader.txt\" is in the same folder as this script.")

	header = base_header.replace("<TEXT1>", brand.upper())
	header = header.replace("<TEXT2>", (env.upper() if env != "" else "ALL"))

	return header

# Determines if the file already contains the header
def headerExists(cfgFileName):

	with open(cfgFileName, 'r') as fileToCheck:
		data = fileToCheck.read()

	return data.startswith("#--")

# get the brand to which the file belongs
def getFileBrand(filename):

	brands = ("bf", "pp", "fd_1", "fd_2", "fd_3", "fd_4")
	cur_brand = ""

	for brand in brands:
		if filename.find("_" + brand) != -1:
			cur_brand = brand
			break

	return cur_brand

# get the environment to which the file belongs
def getFileEnvironment(filename):

	environments = ("dly", "rel", "nxt", "qa", "prf", "prd")
	cur_env = ""

	for env in environments:
		if filename.find("_" + env) != -1:
			cur_env = env
			break

	return (cur_env if cur_env != "" else "ALL")

# Main procedure
def main():

	# Get directory to work on:
	if len(sys.argv) == 1:
		sys.exit("Directory path missing. Please execute this script with: \n\tpython" + sys.argv[0] + "<APP_ABSOLUTE_DIRECTORY_PATH>")
	else:
		if len(sys.argv) > 2:
			print("WARN: extra arguments will be ignored.")

		app_cfg_dir = os.path.join( sys.argv[1], "src")

		# TODO: add env variable to make aboslute path unnecessary

		if not os.path.isdir(app_cfg_dir):
			sys.exit('The directory \"' + app_cfg_dir + '\" is not valid, please try again.')

	# Walk throughout the directory:
	for root, dirs, files in os.walk(app_cfg_dir):

		# Loop through the config files only in the current directory:
		for cfgFileName in glob.glob( os.path.join( root, '*.cfg')):

			filename = cfgFileName[ cfgFileName.rfind("/")+1 : ]
			cur_brand = getFileBrand(filename)

			if cur_brand == "":
				# Not a brand config, omit it:
				print(filename + "-> " + "omitted")
				continue

			cur_env = getFileEnvironment(filename)

			#print(cur_brand, cur_env)
			if not headerExists(cfgFileName):

				header = setHeader(cur_brand, cur_env)
				addHeaderToFile(cfgFileName, header)

			else:
				print(filename + "-> " + "header exists")


if __name__ == "__main__":
	main()
