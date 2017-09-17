import os

path = 'filefolder'
# Am I in the correct directory?
# print(os.getcwd())

# print(dir(os))

# Print all the current file names
for f in sorted(os.listdir(path)):
    
    file_name, file_ext = os.path.splitext(f)
    print file_name,file_ext 
    f_title,f_number = file_name.split('-')


    # Need to remove whitespace
    f_title = f_title.strip()
    f_number = int(f_number.strip())
    
    print('{:02}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{:02}-{}{}'.format(f_number, f_title, file_ext)

    os.rename(path+'/'+str(f), path+'/'+new_name)

#restore to previous file names

# for f in sorted(os.listdir(path)):
#     file_name,file_ext = os.path.splitext(f)
#     print file_name,file_ext
#     f_number,f_title = file_name.split('-')

#     # Need to remove whitespace
#     f_title = f_title.strip()
#     f_number = int(f_number.strip())

#     print('{}-{:02}{}'.format(f_title.strip(),f_number, file_ext.strip()))

#     new_name = '{}-{:02}{}'.format(f_title,f_number, file_ext)

#     os.rename(path+'/'+str(f), path+'/'+new_name)

