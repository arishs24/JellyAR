import cv2
import ffmpeg
from content_analysis import analyze_content
from ar_effects import apply_ar_effects

def process_video(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Analyze content of the frame
        analysis_result = analyze_content(frame)
        
        # Apply AR effects based on analysis
        frame_with_effects = apply_ar_effects(frame, analysis_result)
        
        # Write the frame with effects
        out.write(frame_with_effects)

    cap.release()
    out.release()

def encode_video(input_frames_path, output_video_path):
    (
        ffmpeg
        .input(input_frames_path)
        .output(output_video_path)
        .run()
    )
