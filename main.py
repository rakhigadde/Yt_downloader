import streamlit as st
from pytube import YouTube

def download_video(url, output_path='.', choose_stream=False):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Display video details
        st.write("Video Details:")
        st.write(f"Title: {yt.title}")
        st.write(f"Duration: {yt.length} seconds")
        st.write(f"Author: {yt.author}")

        # Prompt user to choose a stream if enabled
        if choose_stream:
            st.write("\nAvailable Streams:")
            for i, stream in enumerate(yt.streams.filter(file_extension="mp4")):
                st.write(f"{i + 1}. {stream.resolution} - {stream.mime_type}")

            choice = st.number_input("Enter the stream number to download:", min_value=1, max_value=len(yt.streams.filter(file_extension="mp4")))
            video_stream = yt.streams.filter(file_extension="mp4")[int(choice) - 1]
        else:
            # Get the highest resolution stream
            video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)

        st.success(f"\nDownload complete: {yt.title}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube video URL
    video_url = st.text_input("Enter the YouTube video URL:")

    # Input field for download path
    download_path = st.text_input("Enter the download path (default is current directory):", '.')

    # Checkbox for choosing a specific stream
    choose_stream = st.checkbox("Choose a specific stream")

    # Button to trigger the download
    if st.button("Download Video"):
        download_video(video_url, download_path, choose_stream)

if __name__ == "__main__":
    main()
