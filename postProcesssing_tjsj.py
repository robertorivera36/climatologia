#!/usr/bin/env python

#--- Set up the working directory
wpath='C:/Users/Roberto/Documents/Climatología/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/'
#--- Path to dump all the processed files
dpath='C:/Users/Roberto/Documents/Climatología/Sounding/processed_soundings_1982-2018/tjsj_soundings_1982-2018/dailyData/'

#--- Open the files with all the sounding year by year
for year in range(1982,2020,1):
	datafile = 'tjsj_'+str(year)+'.out'
	print (datafile)

	#--- Open the file that contains all the sounding for one year
	data = open(wpath+datafile, 'r')
	#--- Split the data in sections, each section represent a sounding
	data = data.read().split('\n\n')

	#--- Assign a value to NoData
	missingVal = ',null,'

	#--- Work with each sounding dataset
	for raob in data:
		count = 0
		#--- Check each line of the sounding to classify as observations or indeces
		for line in raob.split('\n'):			
			#--- Take the first line to create the filename
			if 'Observations' in line.split():
				date_str = line.split()
				stationID = date_str[0] #--- Extracts station identifier (id)
				months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
				if months[date_str[5]] < 10:
					filename=str(date_str[6])+'0'+str(months[date_str[5]])+str(date_str[4])+str(date_str[3])
					#--- Creates the strings for the date and time columns
					dateCol=str(date_str[6])+'-'+'0'+str(months[date_str[5]])+'-'+str(date_str[4])
					timeCol=str(date_str[3])+'0000'
					#--- Removes the 'Z' character from the timeCol string
					timeCol = timeCol.replace('Z', '')
				else:
					filename=str(date_str[6])+str(months[date_str[5]])+str(date_str[4])+str(date_str[3])
					#--- Creates the strings for the date and time columns
					dateCol=str(date_str[6])+'-'+str(months[date_str[5]])+'-'+str(date_str[4])
					timeCol=str(date_str[3])+'0000'
					#--- Removes the 'Z' character from the timeCol string
					timeCol = timeCol.replace('Z', '')

				#--- Create a file to write the observations at each level/height
				f1 = open(dpath+filename+'_obs.txt', 'a')

			#--- Discard lines that are not useful
			elif len(line.split()) < 2:
				continue
		
			#--- Recognize the part of the file that contains the atmospheric indices
			elif 'indices' in line.split():
				f2 = open(dpath+filename+'_indices.txt', 'a')
		
			#--- Classify and write each atmospheric index	
			elif len(line.split(':')) == 2:
				indexes = line.strip()
				indexes = indexes.split(':')
				text_indexes = ','.join(indexes)
				f2.write(text_indexes+'\n')
		
			#--- Organize the observations to write them in a csv format	
			elif len(line.split()) > 3:
				text_line = [line[i:i+7] for i in range(0,len(line),7)]
				text_csv  = ','.join(text_line)
				text_csv  = text_csv.replace(' ','').replace(',,',missingVal).replace(',,',missingVal)
				if count == 0:
					f1.write('STATIONID,'+'DATE,'+'TIME,'+text_csv+'\n')
				elif count == 1:
					f1.write('VARCHAR(4),'+'YYYY-MM-DD,'+'HHMMSS,'+text_csv+'\n')
				else:
					f1.write(stationID+','+dateCol+','+timeCol+','+text_csv+'\n')
				count = count+1
		f1.close()
		f2.close()
