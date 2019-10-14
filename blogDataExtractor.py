"""
	Python script as a solutionn to the Assignment https://hackmd.io/@N7nxXdBFSk6_7dihdnv-xg/SywqoqyJE?type=view
Environment:
	OS : Windows 10 x64
	Languages/framework: 
		- Python 3.7.4 (https://www.python.org/downloads/windows/)
		- https://www.python.org/ftp/python/3.7.4/python-3.7.4-amd64.exe
	Additional Libraries:
		- 
		
	Execution command:
		$ python .\blogDataExtractor.py 
		
Assumptions/warnings/disclaimers:
	Not Using python logging module as this is just a small script. Can suffise with just prints :P
"""
import os
import json

# Name of the blog file to be parsed.
INPUT_FILE = "input.txt"

# Identification/Seperator character sequences
META_DATA_SEPERATOR 	= "---"
SHORT_CONTENT_SEPERATOR = "READMORE"
FIELD_SEPERATOR 		= ":"
FIELD_VALUE_SEPERATOR 	= ","

# Initialising variables and flags required in code

# Dictionary to contain output
OUTPUT_DICT = {}

# flags to keep track of type of data we are reading
isReadingMetaData = False
isReadingShortContent = False
isReadingLongContent = False

# variables to hold read data
inputMetaData = []
inputShortContent = ""
inputLongContent = ""
inputUnparsed = ""

# Read input file
INPUT_FILE = str(INPUT_FILE)
print("INFO: Reading blog file -> " + INPUT_FILE)
if os.path.exists(INPUT_FILE):
	with open(INPUT_FILE, "r") as blog:
		# seperate out contaits of file based on seperating characters
		for line in blog:
			line = str(line).strip()
			if line != '':
				if META_DATA_SEPERATOR in line:
					if not isReadingMetaData:
						isReadingMetaData = True
					else:
						isReadingMetaData = False
						isReadingShortContent = True
				elif SHORT_CONTENT_SEPERATOR in line:
					isReadingShortContent = False
					isReadingLongContent = True
				else:
					if isReadingMetaData:
						inputMetaData.append(line)
					elif isReadingShortContent:
						inputShortContent += line
					elif isReadingLongContent:
						inputLongContent += line
						inputLongContent += " "
					else:
						inputUnparsed += line
			
		# extracted input
		#print("DEBUG: inputMetaData-> ",)
		#print(inputMetaData)
		#print("DEBUG: inputShortContent-> "), print(inputShortContent)
		#print("DEBUG: inputLongContent-> "), print(inputLongContent)
		#print("DEBUG: inputUnparsed-> "), print(inputUnparsed)
else:
	print("ERROR: Unable to open file" + INPUT_FILE)

# extract fields from mata data and add them to output
for fieldLine in inputMetaData:
	# seperate out name and value of the field 
	extractedFieldData = fieldLine.split(FIELD_SEPERATOR, 1)
	fieldName = ''
	fieldValue = ''
	if len(extractedFieldData) > 0:
		fieldName = extractedFieldData[0].strip().replace('"', '')
	if len(extractedFieldData) > 1:
		fieldValue = extractedFieldData[1].strip().replace('"', '')
		# if there are multiple values put them in the list
		if FIELD_VALUE_SEPERATOR in fieldValue:
			fieldValue = fieldValue.split(FIELD_VALUE_SEPERATOR)
			for i in range(0, len(fieldValue)):
				fieldValue[i] = fieldValue[i].strip()
				
	if fieldName != '':
		print("INFO: Adding field to output-> " + str(fieldName) + " : " + str(fieldValue))
		OUTPUT_DICT[fieldName] = fieldValue
		
# seperate out short containt section
print("INFO: Adding short-content to output")
OUTPUT_DICT["short-content"] = inputShortContent.replace('"', "'").strip()

# seperate out long containt section
print("INFO: Adding content to output")
OUTPUT_DICT["content"] = inputLongContent.replace('"', "'").strip()
# IGNORING removal of 'C' at the start of line containt (Don't know why)

print("DEBUG: OUTPUT -> ")
print(OUTPUT_DICT)

# Write disctonary to json output file
with open('output.txt', 'w') as fp:
    json.dump(OUTPUT_DICT, fp)
	
print("DEBUG: Bye")