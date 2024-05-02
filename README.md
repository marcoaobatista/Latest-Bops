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

   ```plaintext
    SPOTIFY_LTBS_CLIENT_ID=your_client_id
    SPOTIFY_LTBS_CLIENT_SECRET=your_client_secret
    SPOTIFY_LTBS_REFRESH_TOKEN=your_refresh_token
    SPOTIFY_LTBS_SOURCE_ID=your_source_id
    SPOTIFY_LTBS_TARGET_ID=your_target_id
   ```

Once the environment variables are set up, you can run the script, and it will handle the rest automatically.

## Note

This script assumes that you have already created the source and target playlists on your Spotify account. Make sure the playlists exist and that you have the necessary permissions to modify them.

Please exercise caution when using this script, as it will delete all existing tracks from the target playlist before adding the latest tracks.

## Additional Notes
- Make sure to use a virtual environment when installing the dependencies and running the script
- Ensure that the environment variables in the `.env` file are kept private and not shared publicly.
- If you encounter any issues during setup or execution, refer to the project documentation or reach out to the project maintainers for assistance.