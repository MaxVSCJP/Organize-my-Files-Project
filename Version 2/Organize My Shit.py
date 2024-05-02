import shutil
import os
import datetime as dt
import mutagen
""" from mutagen.easyid3 import EasyID3 
from mutagen.id3 import ID3NoHeaderError """


workingDir = os.getcwd()
toBeOrganizedDir = os.listdir(workingDir)

toBeOrganizedDir = [os.path.join(workingDir, i) for i in toBeOrganizedDir]

monthDic = {"January" : "01",
            "February" : "02",
            "March" : "03",
            "April" : "04",
            "May" : "05",
            "June" : "06",
            "July" : "07",
            "August" : "08",
            "September" : "09",
            "October" : "10",
            "November" : "11",
            "December" : "12"}

def fileSizeMB(file):
    return os.stat(file).st_size / 1048576


def fileSizeKB(file):
    return os.stat(file).st_size / 1024


def moving(file,dirName):
    os.makedirs(dirName, exist_ok = True)
    try:
        shutil.move(file, dirName)
    except shutil.Error:
        pass


def getArtists(file):
    try:
        audio = mutagen.EasyID3(file)
        return (audio['artist'][0])
    except mutagen.ID3NoHeaderError or KeyError:
        return False


def getAlbum(file):
    try:    
        audio = mutagen.EasyID3(file)
        return (audio['album'][0])
    except mutagen.ID3NoHeaderError or KeyError:
        return False
    

def getDateTaken(file, dest):
    mod_timestamp = os.path.getmtime(file)
    mod_datetime = str(dt.date.fromtimestamp(mod_timestamp)).split("-")
    dest = os.path.join(dest, mod_datetime[0])
    for month, num in monthDic.items():
        if mod_datetime[1] == num:
            dest = os.path.join(dest, month)
            break
    return dest


def getFilesByType():
     
    filetype = ""
    for file in toBeOrganizedDir:
        # for folders
        if os.path.isdir(file):
            javafolder = os.listdir(file)
            for java in javafolder:
                if java[-5:] == ".java":
                    javafile = "C:\\Users\\"+ os.getlogin() +"\\Documents\\Java"
                    moving(file, javafile)
                    break
            else:
                continue


        #gets file type by extension
        for i in range(-1, -len(file), -1):
            if file[i] == ".":
                filetype = file[i:].lower()
                break
        

        # to not move the file that is being executed i.e Organize My Shit.exe / .py
        if os.path.basename(file) == os.path.basename(__file__):
            continue


        # for videos             
        elif filetype in  {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".ts"}:
        
            fsize = fileSizeMB(file)
            
            if(fsize < 15):
                shorts = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Shorts"
                moving(file, shorts)

            elif(fsize < 60 and fsize >= 15):
                videos = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Videos"
                moving(file, videos)

            elif(fsize < 400 and fsize >= 60):
                Series = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Series"
                moving(file, Series)

            elif(fsize >= 400):
                Movies = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Movies"
                moving(file, Movies)


        # for torrent files
        elif filetype == ".torrent":
            torr = os.path.join(workingDir, "Torrents")
            moving(file, torr)


        # for programs or applications
        elif filetype in {".exe", ".apk", ".ipa", ".xapk"}:
            if(filetype == ".exe"):
                try:
                    cpp = "C:\\Users\\"+ os.getlogin() +"\\Documents\\C Suite\\C++"
                    cSuite = set(os.listdir(cpp))
                    if((os.path.basename(file).split(".")[0]) + ".cpp" in cSuite):
                        moving(file, cpp)
                    else:
                        apps = os.path.join(workingDir, "Applications")
                        moving(file, apps)
                except FileNotFoundError:
                    apps = os.path.join(workingDir, "Applications")
                    moving(file, apps)

            elif(filetype == ".apk" or filetype == ".xapk"):
                apks = os.path.join(workingDir, "APKs")
                moving(file, apks)

            elif(filetype == ".ipa"):
                ipas = os.path.join(workingDir, "IPAs")
                moving(file, ipas)


        # for rainmeter skins
        elif filetype in {".rmskin"}:
            rmskins = os.path.join(workingDir, "Rainmeter Skins")
            moving(file, rmskins)
            

        # for subtitle files (put in videos folder)
        elif filetype in {".srt", ".vtt", ".stl", ".ssa", ".sub", ".smi", ".ttml", ".aaf"}:
            subtitle = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Subtitles"
            moving(file, subtitle)


        # for compressed files
        elif filetype in {".zip", ".rar", ".7z", ".arj", ".deb", ".gz", ".pkg", ".sitx", ".z"}:
            compressed = os.path.join(workingDir, "Compressed Files")
            moving(file, compressed)
            

        # for documents
        elif filetype in {".txt", ".pdf", ".docx", ".pptx", ".html", ".doc", ".ppt"} or filetype[1] == "x" :
            if(filetype == ".txt"):
                text = os.path.join(workingDir, "Text Files")
                moving(file, text)

            elif(filetype == ".pdf"):
                pdf = os.path.join(workingDir, "PDF's")
                moving(file, pdf)

            elif(filetype == ".docx"):
                docs = os.path.join(workingDir, "Word Documents")
                moving(file, docs)

            elif(filetype == ".pptx"):
                ppoints = os.path.join(workingDir, "PowerPoints")
                moving(file, ppoints)

            elif(filetype == ".html"):
                html = os.path.join(workingDir, "Web Pages")
                moving(file, html)

            elif(filetype[1] == "x"):
                xcel = os.path.join(workingDir, "Excel Files")
                moving(file, xcel)


        # for music
        elif filetype in {".mp3", ".m4a", ".m4r", ".m3u8", ".aif", ".mid", ".wav", ".flac", ".ape", ".wv", ".tta", ".wma"}:
            if(filetype == ".m4r"):
                tones = "C:\\Users\\"+ os.getlogin() +"\\Music\\Tones"
                moving(file, tones)

            else:
                music = "C:\\Users\\"+ os.getlogin() +"\\Music"
                artist = getArtists(file)
                album = getAlbum(file)
                if not artist:
                    moving(file, music)
                else:
                    if not album:
                        moving(file, os.path.join(music,artist))
                    else:
                        moving(file, os.path.join(music,artist,album))


        # for photos
        elif filetype in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".ai", ".eps", ".psd", ".heic"}:
            if(filetype == ".gif"):
                gifs = "C:\\Users\\"+ os.getlogin() +"\\Pictures\\GIFs"
                gifs = getDateTaken(file, gifs)
                moving(file, gifs)

            elif(filetype == ".webp"):
                webp = "C:\\Users\\"+ os.getlogin() +"\\Pictures\\Web Images"
                webp = getDateTaken(file, webp)
                moving(file, webp)

            else:
                photos = "C:\\Users\\"+ os.getlogin() +"\\Pictures"
                photos = getDateTaken(file, photos)
                moving(file, photos)


        # for code files
        elif filetype in {".cpp", ".py", ".html", ".css", ".js", ".java", ".class", ".c"}:
            if(filetype == ".py"):
                python = "C:\\Users\\"+ os.getlogin() +"\\Documents\\Python"
                moving(file, python)
            elif(filetype in {".html", ".css", ".js"}):
                webs = "C:\\Users\\"+ os.getlogin() +"\\Documents\\Websites"
                moving(file, webs)
            elif(filetype in {".java", ".class"}):
                javafile = "C:\\Users\\"+ os.getlogin() +"\\Documents\\Java"
                moving(file, javafile)
            elif(filetype == ".cpp"):
                cpp = "C:\\Users\\"+ os.getlogin() +"\\Documents\\C Suite\\C++"
                moving(file,cpp)
            elif(filetype == ".c"):
                justC = "C:\\Users\\"+ os.getlogin() +"\\Documents\\C Suite\\C"
                moving(file,justC)


        # for other file types 
        else:
            others = os.path.join(workingDir, "Others")
            moving(file, others)


getFilesByType()