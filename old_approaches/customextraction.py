import os
import librosa
import numpy as np
import soundfile as sf

def percussive_extraction_with_custom_parameters(audio_path, output_filename):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Decompose the audio into harmonic and percussive components
    harmonic, percussive = librosa.effects.hpss(y)
    
    # Get the percussive onset envelope
    onset_env = librosa.onset.onset_strength(y=percussive, sr=sr)
    
    # Calculate the percussive events
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)

    # Create a mask for the percussive events
    percussive_mask = np.zeros_like(y, dtype=bool)
    for onset in onset_frames:
        start = librosa.frames_to_samples(onset, hop_length=512)
        end = start + 512  # Adjust the window length as needed
        percussive_mask[start:end] = True

    # Apply the percussive mask to the original signal
    y_percussive = y * percussive_mask
    
    # Get the current working directory as the output directory
    output_directory = os.getcwd()

    # Save the extracted percussive audio as a WAV file in the current working directory
    output_path = os.path.join(output_directory, output_filename)
    sf.write(output_path, y_percussive, sr)

# Example usage
input_audio_path = 'guitardrums.wav'
output_filename = 'extracted_percussive_custom.wav'

percussive_extraction_with_custom_parameters(input_audio_path, output_filename)
