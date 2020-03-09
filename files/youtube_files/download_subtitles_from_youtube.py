import os

f = open("links.txt", "r")

path_to_youtube_dl_exe = "C:\\Users\\IZZY\\Downloads\\youtube-dl.exe"
options_youtube_dl = "--write-sub --write-auto-sub --sub-lang pt --skip-download -v"

path_to_ffmpeg_exe = "C:\\Users\\IZZY\\Downloads\\ffmpeg-20200306-cfd9a65-win64-static\\bin\\ffmpeg.exe"
options_ffmpeg_exe = "-i"

rootdir = "C:\\Users\\IZZY\\Downloads\\Bolso\\"
extensions = ('.vtt')

for link in f:
    if "https" not in link:
        continue

    command = path_to_youtube_dl_exe + " " + options_youtube_dl + " " + link
    
    #print(command)
    
    os.system(command)
    
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        ext = os.path.splitext(file)[-1].lower()
        if ext in extensions:
            command = path_to_ffmpeg_exe + " " + options_ffmpeg_exe + ' "' + os.path.join(subdir, file) + '" "' + os.path.splitext(os.path.join(subdir, file))[0] + '.srt"'
            #print (command)
            
            os.system(command)