# PixelPirate

**PixelPirate** is your trusted matey in the digital seas, built to plunder the treasures of YouTube in the finest resolution. With enhanced features like automatic dependency installation and progress bars, setting its sights on high-quality content has never been easier. This downloader is engineered to quickly and efficiently capture videos for offline viewing, making your content consumption voyage smoother than ever.

## How It Works

Harnessing the power of popular libraries such as `pytube`, `mutagen`, and `tqdm`, PixelPirate follows these steps:

1. **URL Input:** The user provides a comma-separated list of YouTube video URLs.
2. **Resolution Selection:** The script automatically sails towards the highest available resolution for each video.
3. **Filename Sanitization:** To ensure your treasures are stored without any hiccups, PixelPirate sanitizes video titles, keeping them safe from potential filename conflicts.
4. **Download:** Videos are swiftly downloaded to the user-specified directory with an interactive progress bar.
5. **User Feedback:** Progress reports keep the user informed throughout the voyage.

## Function Breakdown

- **clear_console:** Clears the terminal screen.
- **install:** Installs the missing Python packages automatically.
- **sanitize_filename:** Ensures the filename doesn't contain characters that might cause issues.
- **progress_stream:** Updates the progress bar during the video download.
- **download_video:** Handles the main video downloading functionality, including metadata embedding.
- **display_copyright:** Shows a respectful copyright notice about video content.
- **main:** The main function that orchestrates the whole downloading process.

## Video Walkthrough

[Watch it on Youtube](https://youtu.be/gQpktXQwOyc)

## Setting Sail with PixelPirate

1. **Clone the Repository:** Begin by cloning the PixelPirate repository to your local machine.
2. **Install Dependencies:** PixelPirate now auto-installs any missing dependencies. Just run the script, and it'll take care of the rest!
3. **Specify Credentials:** Add your desired destination directory and YouTube URLs.
4. **Run the Script:** Navigate to your terminal or command prompt, and launch `ytsave.py`.
5. **Enjoy Your Treasures:** Once downloaded, navigate to your specified directory and enjoy the content offline.

## Customization

PixelPirate offers ample room for customization:

- **Video Resolution:** Though currently set to download the highest resolution, you can easily adjust preferences within the script.
- **Download Directory:** Choose any location on your machine to store your videos.
- **Additional Features:** Expand the script to include features like playlist downloads, audio extraction, or integration with other platforms.

## Credits

PixelPirate is the brainchild of [mrbhanukab](https://github.com/mrbhanukab). Feel free to dock at the GitHub repository to contribute, drop anchor on issues, or set forth suggestions.

Sail forth into the vast expanses of YouTube content with PixelPirate, ensuring you always have your favorite videos, no internet connection required.

[![github](https://img.shields.io/badge/Github-mrbhanukab-%23333?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/mrbhanukab)<br>
[![twitter](https://img.shields.io/badge/Twitter-mrbhanuka-%2300acee?style=for-the-badge&logo=Twitter&logoColor=white)](https://twitter.com/mrbhanuka)
