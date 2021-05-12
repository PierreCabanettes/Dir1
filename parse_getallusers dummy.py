
import json, csv, sys
# import json file and write CSV output
# works for JSON result of GET all users API call

if sys.argv[1] is not None and sys.argv[2] is not None:

	fileInput = sys.argv[1]
	fileOutput = sys.argv[2]

	inputFile = open(fileInput) #open json file
	outputFile = open(fileOutput, 'w') #load csv file
	data = json.load(inputFile) #load json content
	inputFile.close() #close the input file
	output = csv.writer(outputFile) #create a csv.write

    #table with all keys to extract from json, also header of CSV
	keys_to_extract=["id","email","enabled","team_ids","invitation_pending","created_at","last_sign_in_at"]
	output.writerow(keys_to_extract) # write header row

	#go through records in JSON file
	line=[]
	for row in data["records"]:
		for key in keys_to_extract:
			line.append(str(row[key]))
		#print(line)
		output.writerow(line)
		line=[]

