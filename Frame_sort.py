import numpy as np
work_dir = '/Users/oskarsvensson/Science/FILES/HALRIC/Hst5/' # Needs manual change

file = work_dir + 'Rg.xvg'
Rg_frames = ((np.genfromtxt(file, unpack=True, skip_header=(27), usecols=1))*10)

Rg_range = []
for r in Rg_frames:
    if int(r) not in Rg_range:
        Rg_range.append(int(r))
Rg_range.sort()  
    
counter = 0
for Rg in Rg_range:
    if counter == 0:
        frame_count = np.array([[Rg_range[counter], counter]])
    elif counter == 1:
        frame_count = np.append(arr=frame_count, values=[[Rg_range[counter], counter]], axis=0)
    else:
        frame_count = np.append(arr=frame_count, values=[[Rg_range[counter], counter]], axis=0)
    counter = counter + 1
    
frame_list = []
for Rg in Rg_range:
    counter = 0
    frames = []
    for r in Rg_frames:
        if int(r) == Rg:
            frames.append(counter)
        counter = counter + 1
    frame_list.append(frames)
    
dist_list = []
for List in frame_list:
    dist_list.append(len(List))

with open(work_dir + 'frames.ndx', 'w') as index:
    counter1 = 0
    for Rg in Rg_range:
        index.write('[' + str(Rg_range[counter1]) + ']' + '\n')
        counter2 = 0
        for frame in frame_list[counter1]:
            if counter2 == 6:
                index.write('    ' + str(frame + 1) + '\n')
                counter2 = 0
            else:
                index.write('    ' + str(frame + 1))
                counter2 = counter2 + 1
        index.write('\n')
        counter1 = counter1 + 1