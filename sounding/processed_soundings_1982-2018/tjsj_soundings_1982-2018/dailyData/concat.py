import os

inPath = 'C:/Users/Roberto/Documents/Climatología/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/'
outPath = 'C:/Users/Roberto/Documents/Climatología/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/concat/'

outputFileName = 'concatSoundings_obs.csv'

unwantedLine = "STATIONID,DATE,TIME,PRES,HGHT,TEMP,DWPT,RELH,MIXR,DRCT,SKNT,THTA,THTE,THTV\n"
unwantedLine1 = "VARCHAR(4),YYYY-MM-DD,HHMMSS,hPa,m,C,C,%,g/kg,deg,knot,K,K,K\n"

count = 0

directory = os.fsencode(inPath)

with open(outPath+outputFileName, 'w') as outfile:
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith("_obs.txt"):
			print (filename)
			print(count)
			with open(filename) as infile:
				for line in infile:
					#if ('STATIONID' in line) and count == 0:
					if (line == unwantedLine or line == unwantedLine1) and count == 0:
						#print(line)
						outfile.write(line)
						count = count + 1
					#elif 'STATIONID' in line:
					elif line == unwantedLine or line == unwantedLine1:
						continue
					else:
						#print(line)
						outfile.write(line)
		else:
			continue
