import tensorflow as tf
import numpy as np

def analyze_content(video_frame):
    # Load pre-trained model
    model = tf.keras.models.load_model('path_to_your_model')
    
    # Preprocess the video frame
    frame = np.expand_dims(video_frame, axis=0)
    
    # Predict content analysis
    predictions = model.predict(frame)
    
    # Determine the effect based on predictions (custom logic here)
    if predictions[0] > 0.5:
        return 'happy'
    else:
        return 'neutral'
