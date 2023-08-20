from pytube import YouTube
import os
from components import *
import time

def sanitize_filename(filename):
    """Sanitize the filename to avoid invalid characters."""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def download_video(url, destination, video_number, total_videos):
    """Download a video given its URL and a destination folder."""
    yt = YouTube(url)
    
    # Get the best video stream
    video_stream = (
        yt.streams
        .filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
    )
    
    # Sanitize the filename and append .mp4 extension
    safe_filename = sanitize_filename(yt.title) + ".mp4"
    
    print(f"\nStarting download Video {video_number} of {total_videos}")
    print(f"Title: {yt.title}")
    print(f"Size: {round(video_stream.filesize / (1024 * 1024), 2)} MB")
    start_time = time.time()
    
    # Download video
    video_stream.download(output_path=destination, filename=safe_filename)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {round(elapsed_time, 2)} seconds")
    print(f"Completed: ✅")

def main():
    """Main function to execute the script."""
    os.system('cls||clear')
    
    # Call the logo function with your desired title and version number
    logo("PixelPirate by Bhanuka Bandara", "2.0")
    
    # Ask user for the destination folder and URLs
    destination = input("Enter destination folder:")
    urls = input("Enter YouTube video URLs separated by a comma:").split(',')
    
    print("\n")
    total_videos = len(urls)
    for index, url in enumerate(urls, 1):
        download_video(url.strip(), destination, index, total_videos)

if __name__ == "__main__":
    main()
