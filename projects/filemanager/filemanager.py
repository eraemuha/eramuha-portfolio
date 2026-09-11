# import statement
# os for interacting with the operating system
import os

# assignment statement
current_directory = os.getcwd()  # get current working directory
# listdir() returns a list of all files and directories in the specified path
directory_contents = os.listdir(current_directory)

# method call
# show directory contents
print("Current Directory:", current_directory)
print("Directory Contents:", directory_contents)

# extract filenames from the directory contents
def extract_place_1(filename):
    first = filename.find("_")
    partial = filename[first+1:]
    second = partial.find("_")
    return partial[:second]

# Here are some calls you can use for testing:
print(extract_place_1("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place_1("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place_1("2018-01_Scotland_11/51/27.jpg"))

# extract place long version
def extract_place_2(filename):
    parts = filename.split("_") # Get a list containing all the parts
    place_name = parts[1] # Use the index operator to select the second list item
    return place_name

# extract place short version
def extract_place_2(filename):
    return filename.split("_")[1]

# Here are some calls you can use for testing:
print(extract_place_2("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place_2("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place_2("2018-01_Scotland_11/51/27.jpg"))