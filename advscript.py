import os
import librosa
import numpy as np
from scipy.ndimage import median_filter
import soundfile as sf

def advanced_percussive_extraction_and_save(audio_path, output_filename):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Short-Time Fourier Transform (STFT)
    stft = np.abs(librosa.stft(y))

    # Perform median filtering along the frequency axis to emphasize percussive elements
    # Adjust the filter size according to the characteristics of the audio
    filtered_stft = median_filter(stft, size=(1, 5))  # Emphasize shorter transient elements
    
    # Apply thresholding to discriminate between percussive and non-percussive components
    threshold = 0.1 * np.max(filtered_stft)  # Adjust threshold according to the audio
    percussive_mask = filtered_stft > threshold

    # Apply the mask to the original spectrogram
    percussive_stft = stft * percussive_mask

    # Inverse STFT to obtain the percussive component
    y_percussive = librosa.istft(percussive_stft)
    
    # Get the current working directory as the output directory
    output_directory = os.getcwd()
    
    # Save the extracted percussive audio as a WAV file in the current working directory
    output_path = os.path.join(output_directory, output_filename)
    sf.write(output_path, y_percussive, sr)

# Example usage
input_audio_path = 'guitardrums.wav'
output_filename = 'extracted_percussive.wav'

advanced_percussive_extraction_and_save(input_audio_path, output_filename)
