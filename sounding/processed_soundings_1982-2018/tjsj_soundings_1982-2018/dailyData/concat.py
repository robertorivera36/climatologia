wpath = 'C:/Users/Roberto/Desktop/'
outputFileName = 'output.csv'

unwantedLine = "PRES,HGHT,TEMP,DWPT,RELH,MIXR,DRCT,SKNT,THTA,THTE,THTV,DATE,TIME\n"
unwantedLine1 = "hPa,m,C,C,%,g/kg,deg,knot,K,K,K,YYYY-MM-DD,HHMMSS\n"

count = 0

filenames = ['1982010300Z_obs.txt', '1982010312Z_obs.txt']

with open(wpath+outputFileName, 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                if (line == unwantedLine or line == unwantedLine1) and count == 0:
                	print(line)
                	outfile.write(line)
                	count = count + 1
                elif line == unwantedLine or line == unwantedLine1:
                	continue
                else:
                	print(line)
                	outfile.write(line)
