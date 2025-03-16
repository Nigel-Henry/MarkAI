from moviepy.editor import VideoFileClip

def edit_video(video_path, operations):
    """
    Edit a video based on the specified operations.

    Parameters:
    video_path (str): The path to the video file.
    operations (list): A list of operations to perform on the video. 
                       Supported operations are 'trim' and 'resize'.

    Returns:
    str: The path to the edited video file.
    """
    try:
        clip = VideoFileClip(video_path)
        for operation in operations:
            if operation == 'trim':
                # Trim the video to the first 10 seconds
                clip = clip.subclip(10, 20)
            elif operation == 'resize':
                # Resize the video to a height of 360 pixels
                clip = clip.resize(height=360)
        # Write the edited video back to the same path
        clip.write_videofile(video_path)
    except Exception as e:
        print(f"An error occurred while editing the video: {e}")
        return None

    return video_path