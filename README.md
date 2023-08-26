# PixelPirate

PixelPirate is your ultimate YouTube video downloader, ensuring high-quality content even offline! [Click image to watch the video]

[![Watch the video](https://img.youtube.com/vi/T9dFwPH7DAA/maxresdefault.jpg)](https://www.youtube.com/watch?v=T9dFwPH7DAA&list=PLFSdcwZzq5YG-boHtXGR1Akypl3BYXtMY&index=1)


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Supported operating systems](#supported-operating-systems)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Optimizations](#optimizations)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Credits](#credits)

## Introduction

PixelPirate is engineered to swiftly capture videos from YouTube for offline consumption. Designed for those who wish to have their favorite videos accessible without the need for an internet connection, it brings efficiency and reliability to your content consumption voyage.

## Features

- **High-Quality Downloads:** Always fetches the best available resolution.
- **Automatic Dependency Handling:** No more manual library installation; PixelPirate has got you covered.
- **Interactive UI:** An intuitive progress bar that keeps you updated.
- **Metadata Embedding:** Enriches your downloaded videos with essential metadata.
- **Filename Sanitization:** Ensures safe and conflict-free storage.

## Technologies Used

- **Python:** For back-end logic and the main scripting language.
- **pytube:** To interface with YouTube and handle video downloads.
- **mutagen:** To embed metadata into downloaded videos.
- **tqdm:** To showcase the interactive download progress bar.

## Supported operating systems
![Windows](	https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Mac](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Setup & Installation

### Prerequisites

- Python installed on your system.
- pip, the Python package manager.

### Steps

1. Clone the PixelPirate repository to your local machine.
2. Navigate to the cloned repository.
3. Run the `ytsave.py` script. The script will handle any missing dependencies.
4. Specify the desired destination directory and YouTube URLs.

## Usage

Upon running the script, the console will prompt you for:

1. Your desired destination directory.
2. The YouTube URLs you wish to download (comma-separated).

The videos will then be downloaded to your specified directory.

```bash
# Example
Enter destination folder: /path/to/your/folder
Enter YouTube video URLs separated by a comma: https://youtube.com/video1, https://youtube.com/video2
```

## Optimizations

Performance improvements were made to ensure quick downloads. Filename sanitization ensures a hiccup-free storage experience, and automatic dependency installation reduces user intervention.

## Contribution Guidelines

PixelPirate welcomes contributions. Fork the repository, make your changes in a new branch, and submit a pull request. Detailed guidelines can be found in the repository.

## License

This project is licensed under the terms of the MIT License. You can check out the full license [here](https://github.com/mrbhanukab/PixelPirate/blob/main/LICENSE). **Also Make sure to always respect the copyrights of video content creators.**

## Credits

PixelPirate is the brainchild of [mrbhanukab](https://github.com/mrbhanukab). For contributions, issues, or suggestions, visit the GitHub repository.

[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mrbhanukab)
[![twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/mrbhanuka)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bhanuka-bandara-8a209420a)
[![kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/bhanukabandara)
