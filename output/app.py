from flask import Flask, request, send_file, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video_route():
    video_file = request.files['video']
    input_video_path = 'input_video.mp4'
    output_video_path = 'output/processed_video.mp4'
    
    # Save the uploaded video
    video_file.save(input_video_path)
    
    # Process the video
    process_video(input_video_path, output_video_path)
    
    # Send the processed video back to the user
    return send_file(output_video_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
