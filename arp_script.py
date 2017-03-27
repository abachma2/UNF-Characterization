BU=[20000,30000,40000] #length=n
days=540
cycles=3
nLibs = 1
modDens = 0.723

Power=[]

EN=[2.5,3,4,5] #length=l
U235=[]
U238=[]

arpPrefix = "=arp\n w17x17\n "
arpSuffix = str(modDens) + "\n interp_lib.f33\nend"

for x in BU:
    for y in EN:
        cyclePow = x/(1.0*days*cycles)
        Power.append(cyclePow)
        U235.append(y*1000)
        U238.append(100000-(y*1000))
        arpString = arpPrefix + str(y) + "\n " + str(cycles) + "\n "
        for n in range(cycles):
            arpString = arpString + str(days) + "\n "
        for n in range(cycles):
            arpString = arpString + str(cyclePow) + "\n "
        for n in range(cycles):
            arpString = arpString + str(nLibs) + "\n "

        arpString = arpString + arpSuffix 
        print(arpString)

print(Power)
print(U235)
print(U238)
#prints the data for each enrichment the same number of times as there are values for the Power

U235=str(U235[0:n+1])
U238=str(U238[0:n+1])



