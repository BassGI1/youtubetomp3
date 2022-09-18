from pytube import YouTube, Playlist
import os

videoArray = ['video', 'v', 'V', 'Video', 'VIDEO', 'Vid', 'vid', 'a video', 'a Video', 'A video', 'A Video']

if str(input("Am I downloading a single video or a playlist (public or unlisted)? ")) in videoArray:
    url = str(input('What is the url of the video? '))
    try:
        video = YouTube(url).streams.filter(only_audio=True).first()
        Desktop = os.environ["HOMEPATH"] + '\Desktop\\' + str(input("Where should I place the downloaded file? "))
        download = video.download(output_path=Desktop)
        name, extension = os.path.splitext(download)
        os.rename(download, f'{name}.mp3')
        input('I have successfully downloaded the video. Thank you.')
    except:
        input('That is not a valid url. Please try again.')

else:
    url = str(input('What is the url of the playlist? '))
    try:
        playlist = Playlist(url)
        Desktop = os.environ["HOMEPATH"] + '\Desktop\\' + str(input("Where should I place the downloaded files? "))
        for video_url in playlist:
            video = YouTube(video_url).streams.filter(only_audio=True).first()
            download = video.download(output_path=Desktop)
            name, extension = os.path.splitext(download)
            os.rename(download, f'{name}.mp3')
            print(f"Video '{video.title}' successfully downloaded!")
        input('Playlist successfully downloaded. Thank you.')
    except:
        input('That is not a valid url. Please try again.')