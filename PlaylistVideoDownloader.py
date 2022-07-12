    
from pytube import *
import re
from pytube.cli import on_progress  #this module contains the built in progress bar. 


DOWNLOAD_DIR = '/home/thoraiia/Videos/Debug'

playlistUrl = input("Enter Playlist Url \n")

playlist = Playlist(playlistUrl)

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))


for i in range(len(playlist.video_urls)):
    url = playlist.video_urls[i]
    video = YouTube(url, on_progress_callback=on_progress)
    print("\n*** Video ",(i+1))
    print(video.title)
    try:
        video.streams.get_by_itag(22).download(output_path=DOWNLOAD_DIR)
    except AttributeError:
        print("720 Quality is not Available \n")
        video.streams.get_by_itag(18).download(output_path=DOWNLOAD_DIR)
    except:
        print("Something went wrong \n")


print("****** Download Is Complete ******")