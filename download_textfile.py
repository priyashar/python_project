import urllib.request
# url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
url='https://www.w3.org/TR/PNG/iso_8859-1.txt'
# filename = 'Example1.txt'
filename= 'iso_8859-1.txt'
urllib.request.urlretrieve(url, filename)
# Download Example file
# Read the Example1.txt

example1 = "iso_8859-1.txt"
file1 = open(example1, "r")
print(file1.name)
print(file1.mode)
FileContent = file1.read()
print(FileContent)