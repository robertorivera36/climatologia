import os

inPath = 'C:/Users/Roberto/Documents/GitHub/climatologia/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/'
outPath = 'C:/Users/Roberto/Documents/GitHub/climatologia/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/concat/'

outputFileName = 'concatSoundings_obs_pre-1989.csv'
outputFileName1 = 'concatSoundings_obs_post-1989.csv'

#--- Pre-1989 Soundings Variables
header = "STATIONID,DATE,TIME,PRES,HGHT,TEMP,DWPT,RELH,MIXR,DRCT,SKNT,THTA,THTE,THTV\n"
variableTypes = "VARCHAR(4),YYYY-MM-DD,HHMMSS,hPa,m,C,C,%,g/kg,deg,knot,K,K,K\n"

#--- Post-1989 Sounding Variables
header1 = "STATIONID,DATE,TIME,PRES,HGHT,TEMP,DWPT,FRPT,RELH,RELI,MIXR,DRCT,SKNT,THTA,THTE,THTV\n"
variableTypes1 = "VARCHAR(4),YYYY-MM-DD,HHMMSS,hPa,m,C,C,C,%,%,g/kg,deg,knot,K,K,K\n"

count = 0
count1 = 0

post89 = False

directory = os.fsencode(inPath)

#with open(outPath+outputFileName, 'w') as outfile:
with open(outPath+outputFileName, 'w') as outfile, open(outPath+outputFileName1, 'w') as outfile1:
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith("_obs.txt"):
			print (filename)
			with open(filename) as infile:
				for line in infile:
					if (line == header) and count == 0:
						#print(line)
						outfile.write(line)
						count = count + 1
					elif (line == header1) and count1 == 0:
						outfile1.write(line)
						count1 = count1 + 1
						post89 = True
					elif line == header or line == variableTypes or line == header1 or line == variableTypes1:
						continue
					else:
						#print(line)
						if post89 == False:
							outfile.write(line)
						elif post89 == True:
							outfile1.write(line)
		else:
			#--- Consider this area for _indices.txt
			continue
