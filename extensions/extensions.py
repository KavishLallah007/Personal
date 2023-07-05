# Ask user input
file_ext = input("Enter file name: ").lower().strip()

# split input where the is "."
str_split = file_ext.split(".")

# Get index of extension
ext_index = len(str_split) - 1

if str_split[ext_index] == "jpg" or str_split[ext_index] == "jpeg":
    print("image/jpeg")
elif str_split[ext_index] == "gif":
    print("image/gif")
elif str_split[ext_index] == "png":
    print("image/png")
elif str_split[ext_index] == "pdf":
    print("application/pdf")
elif str_split[ext_index] == "txt":
    print("text/plain")
elif str_split[ext_index] == "zip":
    print("application/zip")
else:
    print("application/octet-stream")