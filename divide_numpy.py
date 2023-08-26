'''
Jessica Wen
Colgate Summer research 2023
calculating ratios between love and rayleigh waves using numpy arrays
'''
import pandas as pd

df_ray = pd.read_csv("mod3.mod", delimiter = r"\s+", names = ('Long_r', 'Lat_r', 'Depth_r', 'Velocity_r'))
df_love = pd.read_csv("love_sort_test.csv", names = ('Long_l', 'Lat_l', 'Depth_l', 'Velocity_l'))

velocity_ray = df_ray['Velocity_r'].to_numpy() #array
velocity_love = df_love['Velocity_l'].to_numpy() #array
depth_ray = df_ray['Depth_r'].to_numpy()
depth_love = df_love['Depth_l'].to_numpy()

# velocity_radial = velocity_love/velocity_ray #divide array by array

velocity_radial = []
for i in range(len(velocity_ray)):
    if velocity_love[i] == 0:
        velocity_radial.append(0)
    elif depth_love[i] == 30: #check at depth 30
        if velocity_love[i]/velocity_ray[i] > 25: #create a limit at this depth
            ratio = 25
        else:
            ratio = (((velocity_love[i]/velocity_ray[i])**2) - 1) * 100 #radial anistropy equation
        velocity_radial.append(ratio)
        #print(ratio)
    else:
        ratio = (((velocity_love[i]/velocity_ray[i])**2) - 1) * 100
        velocity_radial.append(ratio)

#check for zeros
# for i in range(len(velocity_radial)):
#     if velocity_radial[i] == 0:
#         if df_love['Velocity_l'][i] == 0: 
#             print(df_love['Long_l'][i],'\t', df_love['Lat_l'][i], '\t', df_love['Depth_l'][i], '\t', df_love['Velocity_l'][i],
#             '\t', df_ray['Velocity_r'][i])

#printing commands
#print ratios
# df_radial = pd.DataFrame(velocity_radial, columns = ['Vsh/Vsv']) #make into a dataframe
# df_radial.to_csv('ratios.csv') #print out to csv file

#print all information
# df_info = df_ray[['Long_r']].copy()
# df_info = df_info.join(df_love['Long_l'])
# df_info = df_info.join(df_ray['Lat_r'])
# df_info = df_info.join(df_love['Lat_l'])
# df_info = df_info.join(df_ray['Depth_r'])
# df_info = df_info.join(df_love['Depth_l'])
# df_info = df_info.join(df_love['Velocity_l'])
# df_info = df_info.join(df_ray['Velocity_r'])
# df_radial = pd.DataFrame(velocity_radial, columns = ['Vsh/Vsv']) 
# df_info = df_info.join(df_radial['Vsh/Vsv'])
# df_info.to_csv('ratio_information_sort_test.csv', index = False)

##print just the lat, long and ratios; this format used to plot in gmt next
# df_coord = df_info = df_ray[['Long_r', 'Lat_r', 'Depth_r']].copy()
# df_coord['Velocity'] = velocity_radial
# df_ray_info = df_coord.rename(columns={'Long_r': 'Longitude', 'Lat_r': 'Latitude', 'Depth_r': 'Depth', 'Velocity': 'Vsh/Vsv'})
# df_ray_info.to_csv('radial_anistropy_velocity_fix30.csv', index = False)
