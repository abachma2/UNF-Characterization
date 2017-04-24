import re

days=540
cycles=3

BU=[20,25,30,35,40,45,50,55,60]
CoolingTimes=[5,6.5,8,10,15,25]

nLibs=1
modDens= 0.723

enString = ''
import io
import numpy as np    
#Calculating Enrichment based on burnup value
EN=np.array([])
en = np.array([])
with io.open(str('BUandEN.txt'),'w') as f:
    for x in BU:
        CalcEn=np.power(x,0.65)*.31
        en_minus_10 = CalcEn*0.9
        en = np.append(en,en_minus_10)
        en_minus_5 = CalcEn*.95
        en = np.append(en,en_minus_5)
        en = np.append(en,CalcEn)
        en_plus_5 = CalcEn*1.05
        en = np.append(en,en_plus_5)
        en_plus_10 = CalcEn*1.10
        en = np.append(en,en_plus_10)
        en_plus_15 = CalcEn*1.15
        en = np.append(en,en_plus_15)

    EN = np.append(EN,en)
    EN = np.around(EN,decimals=3)
    EN.shape = (9,6)
    
    #Putting BU, EN, and cooling times into matrix to use for data analysis
    for x in range(0,len(BU)):
        enTemp = EN[x]
        for y in enTemp:
            for t in CoolingTimes:
                enString = enString + str(BU[x]) + ' ' + str(y) + ' ' + str(t) + "\n"  
    f.write(enString)
f.close()

#Different Constant strings in the input file
reactor='w17x17.'
file_end='.inp'

Power=[]
U235=[]
U238=[]

arp_prefix = "=arp\n" + \
             " w17x17\n "
arp_suffix = str(modDens) + "\n" + \
                            " w17x17.f33\n" + \
                            "end"
cycle_starts = [0, 570, 1140]
cycle_down = 30

origen_prefix='=origen\n' +\
              'options{\n' +\
              '    digits=6\n' +\
              '}\n' +\
              'bounds{\n' + \
              '    gamma=[1024i 4.0e6 100.0e3]\n' + \
              '    neutron=[1e6 1e3 1]\n' +\
              '}' 
opus_isotopes='=opus\n library="w17x17.f33"\n units=grams\n' + \
              ' title="Multicycle Sample"\n' + \
              ' symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end\nend\n'
opus_gamma='=opus\n library="w17x17.f33"\n typarams=gspectrum\n units=intensity\nend\n'
opus_neutron='=opus\n library="w17x17.f33"\n typarams=nspectrum\n units=intensity\nend'
origen_print_up='    print{\n' +\
                '        cutoffs=[all=1.0e-5]\n' +\
                '    }\n}'
lib='    lib{\n'
w17x17='        file="w17x17.f33"\n'
pos='        pos='
origen_string=''
time='    time{\n'
units='        units="days"\n'
t_brack='        t=['

up_1=' 8i '

mat='    mat{\n        units="grams"\n        iso=[o=1.2e5 '
U234='u234=534 '
U236=' u236=276 '
print_down='    print{\n'+\
           '        cutoffs=[all=0.05]\n' +\
           '    }\n' +\
           '}'
save= '    neutron=yes\n' + \
      '    gamma=yes\n' +\
      '    print{\n' +\
      '        rel_cutoff=yes\n' +\
      '        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]\n' +\
      '        nuc{\n' +\
      '            sublibs=[AC]\n' +\
      '            units=[MOLES]\n' +\
      '            total = no\n' +\
      '        }\n'+\
      '        ele{\n' +\
      '            sublibs=[AC]\n' +\
      '            units=[MOLES]\n' +\
      '            total=no\n' +\
      '        }\n' +\
      '        ele{\n'+\
      '            sublibs=[FP]\n' +\
      '            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]\n' +\
      '            total=no\n' +\
      '        }\n'+\
      '        neutron{\n' +\
      '            summary=yes\n' +\
      '            spectra=yes\n' +\
      '        }\n' +\
      '    }\n' +\
      '    save{\n' +\
      '        steps=last\n' +\
      '    }\n' +\
      '}' 

t=[9,8,7,6,5,4,3,2,1]

downTimeString = ''
d_1=''
d_2=''
d_3=''
down_len = [30,30,1825]
for i in range(1,cycles+1):
    for a in t:
        d_t = eval('cycle_starts[i-1]+days + (down_len[i-1] / float(3 ** a))')
        d_t = ("%7.3f"% d_t)
        if i == 1:
            d_1 = d_1 + d_t + ' '
        elif i==2:
            d_2 = d_2 + d_t + ' '
        else:
            d_3 = d_3 + d_t + ' '

#Last, extended down time. Hardoced to ensure that desired times are included
Down_Time = '3505.185 3505.556 3506.669 3510.007 3520.021 3550.062 3640.185 3910.556 4052.5 4600 5330 7155 10805'


last_down_1='case(c03_down){\n' +\
            '    gamma=yes\n' +\
            '    neutron=yes\n' +\
            '    time{\n' +\
            '        units=DAYS\n' +\
            '        t=['

last_down_2='    }\n' +\
            'save{\n' +\
            '        steps=last\n' +\
            '    }\n' +\
            '}\n'+\
            'end'
last_down_3 = '    }\n' +\
              'save{\n' +\
              '        steps=[9 10 11 12 13]\n' +\
              '    }\n' +\
              '}\n' +\
              'end'

#Begin building input decks
enTmp = np.array([])
import io

for x in range(0,len(BU)):
    if x >= 0:
        enTmp = EN[x]
        for y in enTmp:
            with io.open(str(reactor) + str(BU[x]) + str('.') + str(y) + str(file_end),'w') as f:
                cyclePow = (BU[x]*1000)/(1.0*days*cycles)
                Pow=("{0:.3f}".format(cyclePow))
                Power.append(Pow)
                U235=(y*1000)
                U238=(100000-((y*1000)+534+276))
                #Begin arp file
                arp_string = arp_prefix + str(y) + "\n " + str(cycles) + "\n "
                for n in range(cycles):
                    arp_string = arp_string + str(days) + "\n "
                for n in range(cycles):
                    arp_string = arp_string + str(Pow) + "\n "
                for n in range(cycles):
                    arp_string = arp_string + str(nLibs) + "\n "
                arp_string = arp_string + arp_suffix

            #End arp string; begin origen string
                origen_string = "\n" + origen_prefix    
                for i in range(1,cycles+1):
                    origen_string = origen_string + "\n" + str("case(c0") + str(i) + str("_up) {")
                    origen_string = origen_string + "\n" + str(lib) 
                    if i==1:
                        origen_string = origen_string + str(w17x17)
                    else:
                        origen_string = origen_string
                    origen_string = origen_string + str(pos)+ str(i) + "\n    }"
                    origen_string = origen_string + "\n" + str(time)
                    if i==1:
                        origen_string = origen_string + str(units)
                    else:
                        origen_string = origen_string
                    #Up Cycle time
                    origen_string = origen_string + str(t_brack)
                    origen_string = origen_string + str(up_1) + str(cycle_starts[i-1]+54) + ' '\
                                                  + str(cycle_starts[i-1]+days) + str(' ]') \
                                                  + "\n" + str("    }") 
                    origen_string = origen_string + "\n" + str("    power=[10R") + str(Pow) \
                                                  + str("]") + "\n"
                    #Materails, for cycle 1 only
                    if i == 1:
                        origen_string = origen_string + str(mat) + str(U234) +str("u235=") \
                                                      + str(U235) + str(U236) + str("u238=") \
                                                      + str(U238) + str(']\n    }\n')
                    else:
                        origen_string = origen_string
                    origen_string = origen_string  + str(origen_print_up)
                
                    #Begin Down Cycle string
                    origen_string = origen_string + "\n" + str("case(c0") +str(i) +str("_down) {")
                    origen_string = origen_string + "\n" + str(time) 
                    if i ==3:
                        origen_string = origen_string + str(units)
                    else:
                        origen_string = origen_string
                    #Down Cylce time limits, vaires for each cycle
                    origen_string = origen_string + str(t_brack) 
                    if i ==1:
                       origen_string = origen_string + str(d_1)
                    elif i==2:
                        origen_string = origen_string + str(d_2)
                    else:
                        origen_string = origen_string + str(d_3)
                    if i==3:
                        origen_string = origen_string + str(cycle_starts[i-1]+days+1825) + str(']\n    }')
                    else: 
                        origen_string = origen_string + str(cycle_starts[i-1]+days+cycle_down) \
                                                      + str(']\n    }')
                    if i == 2:
                        origen_string = origen_string + '\n}'
                    else:
                        origen_string = origen_string
                    if i == 1:
                        origen_string = origen_string + "\n" + str(print_down)
                    else:
                        origen_string = origen_string
                    #Saving the last time in the third Doen Cycle
                    if i == 3:
                       origen_string = origen_string + "\n" + str(save)
                    else: 
                        origen_string = origen_string
                    #Adding additional down time, specific times needed
                    if i==3:
                        origen_string = origen_string + '\n' + str(last_down_1) + str(Down_Time) \
                                                      + ']\n' +str(last_down_3)

         
            #End of ORIGEN input; start OPUS blocks
                origen_string = origen_string + "\nend"
                origen_string = origen_string + "\n" + str(opus_isotopes) + str(opus_gamma) \
                                              + str(opus_neutron)    
                origen_script = str(arp_string) + str(origen_string)
                
                f.write(str(origen_script))

f.close()

with io.open(str('EN_values.txt'),'w') as f:
    EN = '\n'.join(' '.join(str(cell) for cell in row) for row in EN)
    f.write(str(EN))
f.close()
