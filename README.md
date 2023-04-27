# Get Images From YouTube App

The Get Images From YouTube App is a web application built using Django that enables users to download YouTube videos by providing the URL, and transcribe the video. The web page will display the YouTube video's title, description, and transcript. Users can retrieve K most related images to a keyword, a key image, or both, by entering or uploading relevant information.

## Model

The app uses the OpenAI CLIP model to extract images and the OpenAI Whisper model to transcribe the audio of the video.
The Python model available at https://colab.research.google.com/drive/1E3Q5FQGVizitBojWL2sY9syR55yqMwhY?usp=sharing, which has been evaluated to perform best when taking both keywords and key images as parameters.


## Note

Please note that the app may not work due to inconsistencies with the Pytube library. There have been recent bugs reported with this library that may affect the app's functionality.

## Installation

To run the app locally, follow these steps:

1. Clone the repository.
2. Install the required packages. A document requirements.txt would be uploaded in the future.
3. Start the Django server by running `python manage.py runserver`.
4. Open the app in your browser at `http://localhost:8000/`.

## Usage

To use the app, follow these steps:

1. Enter the YouTube video URL on the homepage.
2. Choose whether to extract images based on a keyword, a key image, or both.
3. Enter the relevant information for the chosen extraction method.
4. Submit the form to retrieve the K most related images.

## Credits

This app was developed by Anson Lai.
