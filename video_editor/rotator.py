from moviepy.video.fx.all import rotate

def rotate_video(video, angle):
  new_clip = rotate(video, angle, unit='deg', resample='bicubic', expand=True)
  cv2.VideoWriter('videos/video_resized.mp4', -1)
  return "Video rotated successfully!"

