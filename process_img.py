import shutil
import os

# path = "../data/data_full"
#
# couter = 0
# for dir in os.listdir(path):
#     path_dir = "{}/{}".format(path,dir)
#
#     path_dir_name = path_dir.split('/')[3]
#     os.rename(path_dir_name, str(couter))
#
#     couter +=1 ;
#     # for file_name in os.listdir(path_dir):
#     #     path_file = "{}/{}/{}".format(path,dir, file_name)
#     #     name = path_file.split('.')[3]
#     #
#     #     if(name == 'xml'):
#     #         os.remove(path_file)
#     #     else:
#     #         continue;
#
#     # if os.path.isfile(path_file):
#     #     os.rename(path_file, path_file_res)


import os

path = "../data/test/"

couter = 0
for file_name in range(0,26):
    os.mkdir(path + str(file_name))


