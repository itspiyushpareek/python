#Task 1
# try:
#     file = open("sample.txt","w")
#     writw = file.write("Line 1 : This is a sample file \nLine 2: It contains multiple lines")
#     file.close()
# except FileNotFoundError:
#     print("Error : The file 'sample.txt' was not found.")

#Task 2
use = input("Enter Text to write to the file : ")
file = open("output.txt","r+")
file.write(use)
print("Data written successfully")
file.close()
append = input("Enter additional text to append : ")
file = open("output.txt","a")
file.write(append)
file.close()
