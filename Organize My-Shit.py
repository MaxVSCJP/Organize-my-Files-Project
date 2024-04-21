import shutil
import os


workingDir = os.getcwd()
toBeOrganizedDir = os.listdir(workingDir)

toBeOrganizedDir = [os.path.join(workingDir, i) for i in toBeOrganizedDir]


def fileSizeMB(file):
    return os.stat(file).st_size / 1048576

def fileSizeKB(file):
    return os.stat(file).st_size / 1024


def getFilesByType():
     
    filetype = ""
    for file in toBeOrganizedDir:

        if os.path.isdir(file):
        # for folders
            folders = os.path.join(workingDir,"Folders")
            os.makedirs(folders, exist_ok= True)
            try:
                shutil.move(file, folders)
            except shutil.Error:
                pass
            continue


        for i in range(-1, -len(file), -1):
            if file[i] == ".":
                filetype = file[i:].lower()
                break
        
                            
        

        if filetype in  {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".ts"}:
        # for videos
            fsize = fileSizeMB(file)
            
            if(fsize < 15):
                shorts = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Shorts"
                os.makedirs(shorts, exist_ok= True)
                try:
                    shutil.move(file, shorts)
                except shutil.Error:
                    pass
            elif(fsize < 60 and fsize >= 15):
                videos = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Videos"
                os.makedirs(videos, exist_ok= True)
                try:
                    shutil.move(file, videos)
                except shutil.Error:
                    pass
            elif(fsize < 400 and fsize >= 60):
                Series = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Series"
                os.makedirs(Series, exist_ok = True)
                try:
                    shutil.move(file, Series)
                except shutil.Error:
                    pass
            elif(fsize >= 400):
                Movies = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Movies"
                os.makedirs(Movies, exist_ok = True)
                try:
                    shutil.move(file, Movies)
                except shutil.Error:
                    pass



        elif filetype == ".torrent":
        # for torrent files
            torr = os.path.join(workingDir, "Torrents")
            os.makedirs(torr, exist_ok = True)
            try:
                shutil.move(file, torr)
            except shutil.Error:
                    pass


        elif filetype in {".exe", ".apk", ".ipa", ".xapk"}:
        # for programs or applications
            if(filetype == ".exe"):
                apps = os.path.join(workingDir, "Applications")
                os.makedirs(apps, exist_ok = True)
                try:
                    shutil.move(file, apps)
                except shutil.Error:
                    pass 

            elif(filetype == ".apk" or filetype == ".xapk"):
                apks = os.path.join(workingDir, "APKs")
                os.makedirs(apks, exist_ok = True)
                try:
                    shutil.move(file, apks)
                except shutil.Error:
                    pass

            elif(filetype == ".ipa"):
                ipas = os.path.join(workingDir, "IPAs")
                os.makedirs(ipas, exist_ok = True)
                try:
                    shutil.move(file, ipas)
                except shutil.Error:
                    pass


        elif filetype in {".rmskin"}:
        # for rainmeter skins
            rmskins = os.path.join(workingDir, "Rainmeter Skins")
            os.makedirs(rmskins, exist_ok = True)
            try:
                shutil.move(file, rmskins)
            except shutil.Error:
                    pass
            

        elif filetype in {".srt", ".vtt", ".stl", ".ssa", ".sub", ".smi", ".ttml", ".aaf"}:
        # for subtitle files (put in videos folder)
            subtitle = "C:\\Users\\"+ os.getlogin() +"\\Videos\\Subtitles"
            os.makedirs(subtitle, exist_ok = True)
            try:
                shutil.move(file, subtitle)
            except shutil.Error:
                    pass


        elif filetype in {".zip", ".rar", ".7z", ".arj", ".deb", ".gz", ".pkg", ".sitx", ".z"}:
        # for compressed files
            compressed = os.path.join(workingDir, "Compressed Files")
            os.makedirs(compressed, exist_ok = True)
            try:
                shutil.move(file, compressed)
            except shutil.Error:
                    pass
            

        elif filetype in {".txt", ".pdf", ".docx", ".pptx", ".html", ".doc", ".ppt"} or filetype[1] == "x" :
        # for documents
            if(filetype == ".txt"):
                text = os.path.join(workingDir, "Text Files")
                os.makedirs(text, exist_ok = True)
                try:
                    shutil.move(file, text)
                except shutil.Error:
                    pass

            elif(filetype == ".pdf"):
                pdf = os.path.join(workingDir, "PDF's")
                os.makedirs(pdf, exist_ok = True)
                try:
                    shutil.move(file, pdf)
                except shutil.Error:
                    pass

            elif(filetype == ".docx"):
                docs = os.path.join(workingDir, "Word Documents")
                os.makedirs(docs, exist_ok = True)
                try:
                    shutil.move(file, docs)
                except shutil.Error:
                    pass

            elif(filetype == ".pptx"):
                ppoints = os.path.join(workingDir, "PowerPoints")
                os.makedirs(ppoints, exist_ok = True)
                try:
                    shutil.move(file, ppoints)
                except shutil.Error:
                    pass

            elif(filetype == ".html"):
                html = os.path.join(workingDir, "Web Pages")
                os.makedirs(html, exist_ok = True)
                try:
                    shutil.move(file, html)
                except shutil.Error:
                    pass

            elif(filetype[1] == "x"):
                xcel = os.path.join(workingDir, "Excel Files")
                os.makedirs(xcel, exist_ok = True)
                try:
                    shutil.move(file, xcel)
                except shutil.Error:
                    pass


        elif filetype in {".mp3", ".m4a", ".m4r", ".m3u8", ".aif", ".mid", ".wav", ".flac", ".ape", ".wv", ".tta", ".wma"}:
        # for music
            if(filetype == ".m4r"):
                tones = "C:\\Users\\"+ os.getlogin() +"\\Music\\Tones"
                os.makedirs(tones, exist_ok = True)
                try:
                    shutil.move(file, tones)
                except shutil.Error:
                    pass

            else:
                music = "C:\\Users\\"+ os.getlogin() +"\\Music"
                os.makedirs(music, exist_ok = True)
                try:
                    shutil.move(file, music)
                except shutil.Error:
                    pass


        elif filetype in {".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".ai", ".eps", ".psd"}:
        # for photos
            if(filetype == ".gif"):
                gifs = "C:\\Users\\"+ os.getlogin() +"\\Pictures\\GIFs"
                os.makedirs(gifs, exist_ok = True)
                try:
                    shutil.move(file, gifs)
                except shutil.Error:
                    pass
            elif(filetype == ".webp"):
                webp = "C:\\Users\\"+ os.getlogin() +"\\Pictures\\Web Images"
                os.makedirs(webp, exist_ok = True)
                try:
                    shutil.move(file, webp)
                except shutil.Error:
                    pass    
            else:
                photos = "C:\\Users\\"+ os.getlogin() +"\\Pictures"
                os.makedirs(photos, exist_ok = True)
                try:
                    shutil.move(file, photos)
                except shutil.Error:
                    pass


        elif file == os.path.abspath(__file__):
            continue


        else:
            others = os.path.join(workingDir, "Others")
            os.makedirs(others, exist_ok = True)
            try:
                shutil.move(file, others)
            except shutil.Error:
                    pass


getFilesByType()