# Spotify Playlist Manager

This Python script is designed to manage Spotify playlists by creating a smaller playlist containing the latest tracks from a larger playlist. The purpose of this script is to optimize storage space on a user's device by maintaining a smaller playlist with the most recent tracks.

## Functionality

The script performs the following tasks:

1. **Authentication**: It authenticates with the Spotify API using client credentials and a refresh token.

2. **Retrieve Latest Tracks**: It retrieves the latest tracks from a specified source playlist on Spotify. By default, it retrieves the last 15 tracks added to the playlist.

3. **Update Target Playlist**: It updates a target playlist on Spotify by deleting all existing tracks and adding the latest tracks retrieved from the source playlist. This ensures that the target playlist always contains the most recent tracks.

## Dependencies

The script utilizes the following Python libraries:

- `requests`: Used for making HTTP requests to the Spotify API.
- `base64`: Used for encoding client credentials for authentication.
- `json`: Used for parsing JSON responses from the Spotify API.
- `os.environ`: Used for accessing environment variables for configuration.
- `dotenv`: Used for loading environment variables from a `.env` file.

## Usage

Before running the script, ensure you have set up the required environment variables in a `.env` file with the following keys:

- `SPOTIFY_LTBS_CLIENT_ID`: Your Spotify client ID.
- `SPOTIFY_LTBS_CLIENT_SECRET`: Your Spotify client secret.
- `SPOTIFY_LTBS_REFRESH_TOKEN`: Your Spotify refresh token.
- `SPOTIFY_LTBS_SOURCE_ID`: The ID of the source playlist containing the latest tracks.
- `SPOTIFY_LTBS_TARGET_ID`: The ID of the target playlist to update with the latest tracks.

Once the environment variables are set up, you can run the script, and it will handle the rest automatically.

## Note

This script assumes that you have already created the source and target playlists on your Spotify account. Make sure the playlists exist and that you have the necessary permissions to modify them.

Please exercise caution when using this script, as it will delete all existing tracks from the target playlist before adding the latest tracks.

# Project Setup Guide

This guide will walk you through setting up the project and configuring the necessary environment variables to run it successfully.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- Pip (Python package installer)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/marcoaobatista/Latest-Bops.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Latest-Bops
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the project directory:

    ```bash
    touch .env
    ```

2. Open the `.env` file in a text editor and add the following environment variables:

    ```plaintext
    SPOTIFY_LTBS_CLIENT_ID=your_client_id
    SPOTIFY_LTBS_CLIENT_SECRET=your_client_secret
    SPOTIFY_LTBS_REFRESH_TOKEN=your_refresh_token
    SPOTIFY_LTBS_SOURCE_ID=your_source_id
    SPOTIFY_LTBS_TARGET_ID=your_target_id
    ```

    Replace `your_client_id`, `your_client_secret`, `your_refresh_token`, `your_source_id`, and `your_target_id` with your actual values obtained from Spotify.

3. Save and close the `.env` file.

## Usage

You can now run the project using the provided Python scripts. Here's an example of how to use them:

```bash
python main.py
```

This will execute the main script and perform the desired actions based on the configuration provided in the `.env` file.

## Additional Notes

- Ensure that the environment variables in the `.env` file are kept private and not shared publicly.
- If you encounter any issues during setup or execution, refer to the project documentation or reach out to the project maintainers for assistance.