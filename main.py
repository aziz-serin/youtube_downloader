from pytube import YouTube
from pytube.exceptions import *
from pytube import Search
import sys
import os
from os import system, name


def format_sec(time):
    secs = time%60
    mins = int((time-secs)/60)
    rep = f'{mins}mins{secs}secs'
    return rep


def display_info(media):
    print("\nTitle: ", media.title.upper())
    print("Author: ", media.author)
    print("Length: ", format_sec(media.length))
    print("Views: ", f'{media.views:,}')
    print("Published", media.publish_date, '\n')


def display_search():
    keyword = input("Enter the keyword: ")
    results = Search(keyword).results
    dictionary = {}

    for index, result in enumerate(results):
        dictionary[index] = result
    print("\n|-------------------Results--------------------------|")

    for i in range(0, len(dictionary)):
        print(i, dictionary[i].title)

    print("|----------------------------------------------------|\n")

    print("If you found the video you are looking for, enter the index of it")
    choice = int(input("or, enter something else to go back: "))

    while True:
        if(choice >= 0 and choice <= len(dictionary)):
            what_to_do = input("If you want to view info of the media, press v"
                               ", to download press d, to go back press q: ")
            if(what_to_do == 'v'):
                display_info(dictionary[choice])
                continue
            elif(what_to_do == 'd'):
                download_media(dictionary[choice])
                break
            elif(what_to_do == 'q'):
                break
            else:
                continue
        else:
            return




def download_media(media):
    media.register_on_progress_callback(show_progress_bar)
    stream = media.streams.get_audio_only()
    if stream != None:
        try:
            stream.download("./Downloads")
        except KeyboardInterrupt:
            quit()
    else:
        print("Audio is not available for this media.")

def show_progress_bar(stream, _chunk, bytes_remaining):
  current = ((stream.filesize - bytes_remaining)/stream.filesize)
  percent = ('{0:.1f}').format(current*100)
  progress = int(50*current)
  status = '#' * progress + '-' * (50 - progress)
  sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
  file_size = '{0:.3g}'.format(stream.filesize/1024/1024)
  print(file_size, "/", file_size, "MB")
  print('\n')
  sys.stdout.flush()

def run_app():
    choice = str(input("\nPress 1 to enter an url, or 2 to use the search function: "))

    if(choice == '1'):
        media_link = input("Please enter the link you want to download or press(q) to exit: ")
        if media_link == 'q':
            quit()
        try:
            global media
            media = YouTube(media_link)
        except (VideoUnavailable, RegexMatchError):
            print(f'Video {media_link} is unavailable, going back to main menu...\n')
            return
        while True:
            response = input("Is this the video you were looking for: {} (y/n)? ".format(media.title))
            if response == 'y':
                break
            elif response == 'n':
                return
            else:
                continue
        while True:
            print("Tell me what to do with this video: ")
            print("Download(d)")
            print("View info(v)")
            print("I am done with this video(q)")
            choice = input("?")
            if choice == 'd':
                download_media(media)
            elif choice == 'v':
                display_info(media)
            elif choice == 'q':
                break
            else:
                continue

    elif(choice == '2'):
        display_search()
    else:
        pass

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    clear()
    print("----------------------Welcome to Youtube Downloader!------------------------")
    while True:
        run_app()
        quit = input("Press q to quit or something else to continue: ")
        if (quit == 'q'):
            sys.exit()

if __name__ == "__main__":
    main()