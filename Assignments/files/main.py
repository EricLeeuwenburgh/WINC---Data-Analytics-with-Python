__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
import shutil
from zipfile import ZipFile
import pathlib

# Exercise 1
def clean_cache():
    path = "C:/Users/Eric/Documents/WINC_Data_Analytics_with_Python/Exercises/Module3/files/cache"
    if os.path.isdir(path):
        shutil.rmtree(path)
    
    os.mkdir(path)
    print("Succesfully cleaned " + path)


clean_cache()

# Exercise 2
zip_file = "C:/Users/Eric/Documents/WINC_Data_Analytics_with_Python/Exercises/Module3/files/data.zip"
destination = "C:/Users/Eric/Documents/WINC_Data_Analytics_with_Python/Exercises/Module3/files/cache"

def cache_zip(zip_path:str, des_path:str):
    with ZipFile(os.path.abspath(zip_path)) as zObject:
    
        zObject.extractall(os.path.abspath(des_path))
    print("Succesfully unzipped " + zip_file)

cache_zip(zip_file, destination)

# Exercise 3
def cached_files():
    cache = pathlib.Path(os.path.abspath(destination))
    list = []

    # Using os module:
    #list = os.listdir(cache)
    
    # Using pathlib module:
    #list = list(cache.iterdir())
    
    for item in cache.iterdir():
        list.append(str(item))
    
    return list

cache_list = (cached_files())

# Exercise 4
def find_password(input):
    for file in input:
            with open(os.path.abspath(file)) as fp:
                lines = fp.readlines()
                for line in lines:
                    word = "password"
                    if word in line:
                        print("Password found in file: " + file)
                        split_password = line.split(" ")
                        print(split_password)
                        password = split_password[1].replace("\n", "")
                        print(password)
                        return password
       

find_password(cache_list)