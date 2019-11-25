#!/usr/bin/env python

#--- Set up the working directory
wpath='/Users/tsunami/Dropbox/NWS/RAOB_TJSJ/tjsj_soundings_1982-2018/'
#--- Path to dump all the processed files
dpath='/Users/tsunami/Dropbox/NWS/RAOB_TJSJ/tjsj_soundings_1982-2018/dailyData/'


#--- Open the files with all the sounding year by year
for year in range(1982,2020,1):
	datafile = 'tjsj_'+str(year)+'.out'
	print datafile

	#--- Open the file that contains all the sounding for one year
	data = open(wpath+datafile, 'r')
	#--- Split the data in sections, each section represent a sounding
	data = data.read().split('\n\n')

	#--- Assign a value to NoData
	missingVal = ',M,'

	#--- Work with each sounding dataset
	for raob in data:
		#--- Check each line of the sounding to classify as observations or indeces
		for line in raob.split('\n'):
			#--- Take the first line to create the filename
			if 'Observations' in line.split():
				date_str = line.split()
				months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
				if months[date_str[5]] < 10:
					filename=str(date_str[6])+'0'+str(months[date_str[5]])+str(date_str[4])+str(date_str[3])
				else:
					filename=str(date_str[6])+str(months[date_str[5]])+str(date_str[4])+str(date_str[3])

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
				f1.write(text_csv+'\n')
		
		f1.close()
		f2.close()
