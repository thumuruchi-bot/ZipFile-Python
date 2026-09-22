import zipfile

with zipfile.ZipFile("files.zip", "w") as zip_file:
    zip_file.write("sample.txt")

print("ZIP File Created Successfully")
