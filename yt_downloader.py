import yt_dlp


def download_video(url: str, cookies_file: str, save_path: str = "./videos") -> str:
    """Download a YouTube video using yt-dlp with cookies."""
    try:
        ydl_opts = {
            'outtmpl': f"{save_path}/%(title)s.%(ext)s",  # Output template
            'cookiefile': cookies_file,  # Path to cookies file
            'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',  # Video + audio at 1080p
            'merge_output_format': 'mp4',  # Ensure output is merged into MP4
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)

            file_name = ydl.prepare_filename(result)
            return file_name
    except Exception as e:
        print(f"An error occurred: {e}")
