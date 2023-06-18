import os
import shutil
import subprocess
import config
cls = "os.system('cls')"

while True:
    while True:
        action = input("Upload or Download(u/d): ").lower()
        if action == "u":
            action = "split"
            break
        elif action == "d":
            action ="merge"
            break
        else:
            print("Meh.")
            exec(cls)


    cwd = os.getcwd()
    cwd_temp = cwd+"\\temp"
    cwd_temp_copy_original = cwd_temp+"\\copy"
    cwd_temp_upload = cwd_temp+"\\upload"
    cwd_temp_download = cwd_temp+"\\download"

    try:
        shutil.rmtree(cwd_temp)
        os.remove("output.data")
    except:
        print("Directory already deleted.")

    os.chdir(cwd)
    os.mkdir("temp")
    os.chdir(cwd_temp)
    os.mkdir("copy")
    os.mkdir("upload")
    os.mkdir("download")


    if action == "split":
        exec(cls)
        os.chdir(cwd)
        upload = subprocess.Popen(['python.exe', config.upload_extension])
        upload.wait()
        shutil.rmtree(cwd_temp)
        exec(cls)

        

    if action == "merge":
        exec(cls)
        os.chdir(cwd)
        download = subprocess.Popen(['python.exe', config.download_extension])
        download.wait()
        shutil.rmtree(cwd_temp)
        exec(cls)

