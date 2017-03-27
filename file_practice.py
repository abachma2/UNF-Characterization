days=540
cycles=3
BU=[20000,30000,40000]
EN=[3,4,5]
name='w17x17.'
end='.inp'

import io
for x in BU:
    for y in EN:
        with io.open(str(name) + str(x) + str('.') + str(y) + str(end),'w') as f:
            f.write(str('Help me. I really need it'))
		
