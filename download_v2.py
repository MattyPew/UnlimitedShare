print("download_v2.py by MattyPew_ (official extension).")
print()

import requests
import linecache
import os
from filesplit.merge import Merge
from cryptography.fernet import Fernet

cwd = os.getcwd()
cwd_temp = cwd+"\\temp"
cwd_temp_download = cwd_temp+"\\download"
cls = "os.system('cls')"
line_index = 2
input_file = input("Enter input file (directory): ")
os.chdir(cwd_temp_download)
linecache.clearcache()
info = linecache.getline(input_file, 1).rstrip('\n')
exec(cls)
info = info.split(";")
if info[0] != "head":
    print("Not UnlimitedShare supported dictionary!")
else:
    print("File name: "+info[1])
    print("Encryption key: "+info[2])
    print("Final file size (unencrypted): "+str(int(info[3])/1000000)+ " MB")
    print("Download file size (encrypted): "+str(int(info[4])/1000000)+" MB")
    print()

    if input("Continue? (y/n): ").lower() == "y":
        while True:
            line_content = linecache.getline(input_file, line_index).rstrip('\n')
            if line_content == "":
                break
            else:
                file_url = requests.get(line_content, allow_redirects=True)
                file_name = file_url.headers.get('content-disposition').replace("attachment; filename=","")
                print("Downloading: "+file_name)
                with open(file_name, 'wb') as f:
                    f.write(file_url.content)
                    f.close()
                line_index = line_index+1
        merge = Merge(cwd_temp_download, cwd, info[1])
        merge.merge(True, False)
        fernet = Fernet(bytes(info[2], 'UTF-8'))
        os.chdir(cwd)
        with open(info[1], 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(info[1], 'wb') as dec_file:
            dec_file.write(decrypted)
print("Download extension unloaded!")