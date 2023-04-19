__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
import shutil
from zipfile import ZipFile
import pathlib

# Exercise 1
absolute_path = os.getcwd()

def clean_cache():
    cache_folder = "cache"
    full_path = os.path.join(absolute_path, cache_folder)
    if os.path.isdir(full_path):    # If path already exist then run:
        shutil.rmtree(full_path)
    
    os.mkdir(full_path)
    print("Succesfully cleaned " + full_path)


clean_cache()

# Exercise 2
zip_file = os.path.join(absolute_path, "data.zip")
destination = os.path.join(absolute_path, "cache")

def cache_zip(zip_path:str, des_path:str):
    with ZipFile(os.path.abspath(zip_path)) as zObject:
    
        zObject.extractall(os.path.abspath(des_path))
    print("Succesfully unzipped " + zip_file)

cache_zip(zip_file, destination)

# Exercise 3
def cached_files():
    cache = pathlib.Path(destination)
    cache_content = []

    # Using os module:
    #cache_content = os.listdir(cache)
    
    for item in cache.iterdir():
        cache_content.append(str(item)) # str() removes the "WindowsPath"-prefix
   
    return cache_content

cache_list = cached_files()

# Exercise 4
def find_password(input):
    for file in input:
            with open(os.path.abspath(file)) as fp:
                lines = fp.readlines()
                for line in lines:
                    word = "password"
                    if word in line:
                        #print("Password found in file: " + file)
                        split_password = line.split(" ")
                        password = split_password[1].replace("\n", "")
                        print("The password = " + password)
                        return password
       
find_password(cache_list)