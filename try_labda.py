import os

#return_list = list((lambda x: os.path.isdir(x) == True, os.listdir()))
return_list = list(filter(lambda x: os.path.isdir(x), os.listdir()))

print(return_list)

