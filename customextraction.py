import os
import librosa
import numpy as np
import soundfile as sf

def percussive_extraction_with_custom_parameters(audio_path, output_filename):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Short-Time Fourier Transform (STFT)
    stft = np.abs(librosa.stft(y))

    # Calculate amplitude envelope
    amplitude_envelope = np.mean(np.abs(librosa.stft(y)), axis=0)
    
    # Parameters based on provided information
    threshold_min = 1  # Minimum amplitude threshold
    threshold_max = 2  # Maximum amplitude threshold
    start_time = 23 * sr  # Time (in samples) of the first drum hit
    target_frequency = 64  # Target frequency around the drum hit

    # Apply thresholding based on amplitude range
    percussive_mask = (amplitude_envelope >= threshold_min) & (amplitude_envelope <= threshold_max)

    # Convert time-based start_time to frame index
    start_frame = librosa.time_to_frames(start_time, sr=sr, hop_length=512)  # Adjust hop_length as needed

    # Convert the target frequency to the closest bin index in the STFT
    freq_bin = np.argmin(np.abs(librosa.fft_frequencies(sr=sr) - target_frequency))

    # Apply masks for both amplitude and frequency
    percussive_mask[start_frame:, freq_bin:] &= True

    # Apply the mask to the original spectrogram
    percussive_stft = stft * percussive_mask[:, np.newaxis]

    # Inverse STFT to obtain the percussive component
    y_percussive = librosa.istft(percussive_stft)

    # Get the current working directory as the output directory
    output_directory = os.getcwd()

    # Save the extracted percussive audio as a WAV file in the current working directory
    output_path = os.path.join(output_directory, output_filename)
    sf.write(output_path, y_percussive, sr)

# Example usage
input_audio_path = 'guitardrums.wav'
output_filename = 'extracted_percussive_custom.wav'

percussive_extraction_with_custom_parameters(input_audio_path, output_filename)
