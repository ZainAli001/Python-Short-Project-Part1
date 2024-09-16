from pytube import YouTube, Playlist
from prettytable import PrettyTable

x = PrettyTable(padding_width=5)
y = PrettyTable(padding_width=5)


def choice1():
    global vid, videos
    yout = YouTube(link)
    videos = yout.streams.filter(only_video=True)
    vid = list(enumerate(videos))


def choice2():
    global audios, vid
    yout = YouTube(link)
    audios = yout.streams.filter(only_audio=True)
    vid = list(enumerate(audios))


def choice3():
    global audios, vid
    yout = Playlist(link)
    for video in yout.videos:
        video.streams.first().download()
    print("Success")


try:
    y.field_names = ["YOUTUBE DOWNLOADER"]
    y.add_rows(
        [
            ["Press 1 for Youtube Video downlaod"],
            ["Press 2 for Youtube audio downlaod"],
            ["Press 3 for Youtube Playlist downlaod"],

        ]
    )
    print(y)
    choice = input("Enter choice : ")

    if "1" in choice:
        link = input("Enter the link :")
        choice1()

        x.field_names = ['Index', "Streams"]
        for i in vid:
            x.add_rows([[i[0], i[1]]])

        print(x)
        userInput = int(input("Enter index : "))

        videos[userInput].download()
        print("Success")
    elif "2" in choice:
        link = input("Enter the link :")
        choice2()

        x.field_names = ['Index', "Streams"]
        for i in vid:
            x.add_rows([[i[0], i[1]]])

        print(x)
        userInput = int(input("Enter index : "))

        audios[userInput].download()
        print("Success")
    elif "3" in choice:
        link = input("Enter the link :")
        choice3()
    else:
        print("Invalid Choice")
except Exception as e:
    print(e)


# link = 'https://www.youtube.com/watch?v=yQJOd8Iow2o&list=RDMMyQJOd8Iow2o&start_radio=1'
# yout = YouTube(link)
# videos = yout.streams.filter(only_audio=True)

# vid = list(enumerate(videos))

# print(yout.title)
# print(yout.thumbnail_url)

# videos = yout.streams.all()
# videos = yout.streams.filter(only_video=True)
