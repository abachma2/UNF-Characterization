import io
import numpy as np

BU=[20,25,30,35,40,45,50,55,60]
EN = np.genfromtxt("EN_values.txt",usecols=(0,1,2,3,4,5))

CoolingTimes = 6
initSkip = 6
numNB = 4 # number of neutron energy bins
numGB = 201 #number of gamma energy bins
data = np.array([])
data_string = ''

with io.open("data.txt",'w') as f:
    for x in range(0,len(BU)):
        en_value = EN[x]
        for y in np.nditer(en_value):       
            GSkip = initSkip
            NSkip = initSkip
            for t in range(CoolingTimes):
                #Gamma Spectrum 
                file_name1 = "w17x17." + str(BU[x]) + '.' + str(y) + ".000000000000000001.plt"
                gamma_tmp = np.genfromtxt(str(file_name1), skip_header=GSkip, usecols=1, max_rows=numGB)
                # Take every other row from gamma (due to repeats)
                data_string = data_string + ' '.join(map(str,gamma_tmp[0::2])) + ' '
                GSkip = GSkip + numGB + 2
                  
                #Neutron Spectrum
                file_name2 = "w17x17." + str(BU[x]) + '.' + str(y) + ".000000000000000002.plt"
                neutron_tmp = np.genfromtxt(str(file_name2), skip_header=NSkip,usecols=1, max_rows=numNB)
                # Take every other row from neutrons (due to repeats)
                data_string = data_string + ' '.join(map(str,neutron_tmp[0::2])) + "\n"
                NSkip = NSkip + numNB + 1
                    
    f.write(data_string)
f.close()

