=arp
 w17x17
 3
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [0.27815881725346747, 0.8344764517604024, 2.5034293552812072, 7.510288065843621, 22.530864197530864, 67.5925925925926, 202.77777777777777, 608.3333333333334, 1825.0] 1710]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[540 [540.0015241579027, 540.0045724737083, 540.0137174211249, 540.0411522633744, 540.1234567901234, 540.3703703703703, 541.1111111111111, 543.3333333333334, 550.0] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[1110 [1110.0015241579028, 1110.0045724737083, 1110.0137174211247, 1110.0411522633744, 1110.1234567901236, 1110.3703703703704, 1111.111111111111, 1113.3333333333333, 1120.0] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[1680 [1680.2781588172534, 1680.8344764517603, 1682.5034293552812, 1687.5102880658437, 1702.530864197531, 1747.5925925925926, 1882.7777777777778, 2288.3333333333335, 3505.0] 8325]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 12.346
 12.346
 12.346
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 12.346]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 12.346]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 18.519
 18.519
 18.519
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 18.519]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 18.519]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 3
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=3000 u236=276 u238=96190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 4
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=4000 u236=276 u238=95190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
=arp
 w17x17
 5
 3
 540
 540
 540
 24.691
 24.691
 24.691
 1
 1
 1
 0.723
 interp_lib.f33
end
=origen
bounds{
    gamma=[100L 1.0e7 1.0e-3]
    neutron=[1e6 1e3 1]
}
options{
    digits=6
} 
case(Cycle: 1 Up) {
    lib{
        file="w17x17.f33"
        pos=1
    }
    time{
        units="days"
        t=[0 8I 540]
    }
    power=[10R 24.691]
    mat{
        units="grams"
        iso=[o=1.2e5 u234=534 u235=5000 u236=276 u238=94190]
    }
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 1 Down) {
    time{
        t=[ ['540.002', '540.005', '540.014', '540.041', '540.123', '540.370', '541.111', '543.333', '550.000'] 570]
    }
    print{
        cutoffs=[all=0.05]
    }
}

case(Cycle: 2 Up) {
    lib{
        pos=2
    }
    time{
        t=[570 8I 1110]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 2 Down) {
    time{
        t=[ ['1110.002', '1110.005', '1110.014', '1110.041', '1110.123', '1110.370', '1111.111', '1113.333', '1120.000'] 1140]
    }
case(Cycle: 3 Up) {
    lib{
        pos=3
    }
    time{
        t=[1140 8I 1680]
    }
    power=[10R 24.691]
    print{
        cutoffs=[all=1.0e-5]
    }
}
case(Cycle: 3 Down) {
    time{
        units="days"
        t=[ ['1680.278', '1680.834', '1682.503', '1687.510', '1702.531', '1747.593', '1882.778', '2288.333', '3505.000'] 7155]
    }
    neutron=yes
    gamma=yes
    print{
        rel_cutoffs=yes
        cutoffs=[ALL=1.0e-2 MOLES=1.0e-6 GRAMS=1.0e-6]
        nuc{
            sublibs=[AC]
            units=[MOLES]
            total = no
        }
        ele{
            sublibs=[AC]
            units=[MOLES]
            total=no
        }
        ele{
            sublibs=[FP]
            units=[GRAMS CURIES WATTS G-WATTS M3_AIR M3_WATER]
            total=no
        }
        neutron{
            summary=yes
            spectra=yes
        }
    }
save{
        steps=[8 LAST]
}
}
end
=opus
 library="w17x17.f33"
 units=grams
 title="Multicycle Sample"
 symnuc=u-235 u-238 sr-90 ag-110m am-241 ba-137m cf-252 cm-242 cm-244 end
end
=opus
 library="w17x17.f33"
 typarams=gspectrum
 units=intensity
end
=opus
 library="w17x17.f33"
 typarams=nspectrum
 units=intensity
end
