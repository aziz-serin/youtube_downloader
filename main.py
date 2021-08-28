from pytube import YouTube
from pytube.exceptions import *
import sys
import os


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


def download_media(media):
    stream = media.streams.first()
    print('\n{fn} | {fs} bytes'.format(
        fn=stream.default_filename,
        fs=stream.filesize,
    ))
    try:
        stream.download("./Downloads")
        sys.stdout.write('\n')
    except KeyboardInterrupt:
        quit()


def run_app():
    media_link = input("Welcome to Youtube Downloader! Please enter the link you want to download or press(q) to exit: ")
    if media_link == 'q':
        quit()
    try:
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


def main():
    while True:
        run_app()


if __name__ == "__main__":
    main()