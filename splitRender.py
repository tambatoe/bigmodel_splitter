import os
import shutil
import subprocess

from math import ceil


# todo parse argline

file_to_split="../02_stl/HarioSkerton-drillAdapter.stl"
destination="splitOut" 
slices_arg = [0, 0, 0]
plate_size = [20, 20, 20]
obj_size = [29, 25, 27]


if not os.path.exists(destination):
   # Create a new directory because it does not exist
   os.makedirs(destination)


slices_num = []
if any(ele == 0 for ele in slices_arg):
    # auto calculate based on plate vs obj size
    slices_num = [ ceil( obj_size[i] / plate_size[i] ) for i in range(0,3) ]
else:
    slices_num = slices_arg

file_counter = 0
half_size = [(plate_size[i]/2) for i in range(0,3) ]

total_build_volume=[ ceil ( slices_num[i] * plate_size[i] ) for i in range(0,3)]
start_points = [ ceil ( 0 - (total_build_volume[i] / 2) + half_size[i] ) for i in range(0,3) ]
end_points = [ceil (total_build_volume[i] / 2 - half_size[i]) for i in range (0,3)]

# print (start_points)
# print (end_points)
rangex = range (start_points[0], end_points[0], plate_size[0])

x = start_points[0]
while x <= end_points[0]:
    y = start_points[1]
    while y <= end_points[1]:
        z = start_points[2]
        while z <= end_points[2]:
            render_stl_array = ['openscad']
            filename = f'split{file_counter}.stl'
            render_stl_array.append(f'-o{filename}')

            render_stl_array.append(f'-Dfile_to_split=\"{file_to_split}\"')
            
            render_stl_array.append(f'-Dcube_posX={x}')
            render_stl_array.append(f'-Dcube_posY={y}')
            render_stl_array.append(f'-Dcube_posZ={z}')

            render_stl_array.append(f'-DcubeszX={plate_size[0]}')
            render_stl_array.append(f'-DcubeszY={plate_size[1]}')
            render_stl_array.append(f'-DcubeszZ={plate_size[2]}')

            render_stl_array.append('splitRender.scad')

            print (render_stl_array)
            subprocess.call(render_stl_array)
            
            shutil.move(filename, os.path.join(destination, filename))

            file_counter += 1
            z += plate_size[2]
        y+=plate_size[1]
    x += plate_size[0]
    print (x)
