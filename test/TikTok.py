import requests
import ffmpeg
import os

#Download video from TikTok
def download(url):
    try:
        response = requests.get(url)
        with open("req_video.mp4", 'wb') as file:
            file.write(response.content)

        return "Done"

    except Exception as ex:
         print(ex)

#Convertation mp4 to gif
def convert():
    try:
        stream = ffmpeg.input("req_video.mp4")
        stream = ffmpeg.output(stream, "video.gif")
        ffmpeg.run(stream)
    except Exception as ex:
        print(ex)

#Deleting video in mp4 format
def delete():
    try:
        os.remove("req_video.mp4")
        return "File removed successfully"
    except Exception as ex:
         print(ex)

#Path to gif video
def paths():
    try:
          p = os.path.abspath('req_video.gif')
          return p
    except Exception as ex:
         print(ex)

#Run functions
def main():
    print("Please input link")
    video = input()
    download(video)
    convert()
    delete()
    print(paths())

main()
