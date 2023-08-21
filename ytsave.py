import os
import sys
import subprocess
from components import *

def clear_console():
    os.system('cls||clear')

def install(package):
    print(f"Installing {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

clear_console()
logo("PixelPirate by Bhanuka Bandara", "2.0")

# Check and install required libraries
required_libraries = ["pytube", "mutagen", "tqdm"]

for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        print(f"⚠️ Required library {lib} is missing!")
        install(lib)

# Once all libraries are ensured to be installed, clear the console and re-display logo
clear_console()
logo("PixelPirate by Bhanuka Bandara", "2.0")

import time
from tqdm import tqdm
from pytube import YouTube
from mutagen.mp4 import MP4

def sanitize_filename(filename):
    """Sanitize the filename to avoid invalid characters."""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def progress_stream(stream, chunk, bytes_remaining):
    """Show progress bar during video download."""
    size = stream.filesize
    current_downloaded = size - bytes_remaining
    pbar.update(current_downloaded - pbar.n)  # Update with the difference between the previous and current download amounts

def download_video(url, destination, video_number, total_videos):
    """Download a video given its URL and a destination folder."""
    global pbar  # Make pbar a global variable
    try:
        yt = YouTube(url, on_progress_callback=progress_stream)
    except Exception as e:
        print(f"Error fetching video info for {url}: {e}")
        return

    # Extract video details
    channel_name = yt.author
    video_description = yt.description
    publish_date = yt.publish_date

    # Get the best video stream
    video_stream = (
        yt.streams
        .filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
    )

    if not video_stream:
        print(f"Error: No suitable video stream found for {url}")
        return

    # Sanitize the filename and append .mp4 extension
    safe_filename = sanitize_filename(yt.title + " - " + channel_name) + ".mp4"

    print(f"\nStarting download Video {video_number} of {total_videos}")
    print(f"Title: {yt.title}")
    print(f"Channel: {channel_name}")

    # Progress bar setup using tqdm
    with tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc="Downloading", colour="#2a9d8f") as pbar:
        video_stream.download(output_path=destination, filename=safe_filename)

    # Embed metadata into the video
    try:
        video = MP4(os.path.join(destination, safe_filename))
        video["\xa9nam"] = yt.title  # Title
        video["\xa9ART"] = channel_name  # Artist/Author
        video["\xa9day"] = str(publish_date)  # Publish date
        video.save()
    except Exception as e:
        print(f"Error embedding metadata: {e}")

    print(f"Completed: ✅")

def display_copyright():
    """Displays a simple copyright notice."""
    print("Always respect content creators' rights and permissions. Download videos for personal use only and ensure you have the right to access and store the content.\n")

def main():
    """Main function to execute the script."""
    os.system('cls||clear')

    # Call the logo function with your desired title and version number
    logo("PixelPirate by Bhanuka Bandara", "2.0")

    # Display copyright notice
    display_copyright()

    # Ask user for the destination folder and URLs
    destination = input("Enter destination folder:")
    urls = input("Enter YouTube video URLs separated by a comma:").split(',')

    total_videos = len(urls)
    for index, url in enumerate(urls, 1):
        download_video(url.strip(), destination, index, total_videos)

if __name__ == "__main__":
    main()
