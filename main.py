import streamlit as st
from pytube import YouTube
from io import BytesIO

def download_video(url):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Display video details
        st.write("Video Details:")
        st.write(f"Title: {yt.title}")
        st.write(f"Duration: {yt.length} seconds")
        st.write(f"Author: {yt.author}")

        # Prompt user to choose a stream if enabled
        
            # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to BytesIO buffer
        buffer = BytesIO()
        video_stream.stream_to_buffer(buffer)
        #fname = f"{yt.title}.mp4",
        # Display download button
        st.download_button(
            label="Download Video",
            data=buffer.getvalue(),  # Use the BytesIO buffer directly
            file_name=f"{yt.title}.mp4",
            help="Click to download the video."
        )

        st.success(f"\nDownload complete: {yt.title}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube video URL
    video_url = st.text_input("Enter the YouTube video URL:")

    # Checkbox for choosing a specific stream
   # choose_stream = st.checkbox("Choose a specific stream")

    # Button to trigger the download
    if st.button("Let's go"):
        download_video(video_url)

if __name__ == "__main__":
    main()
