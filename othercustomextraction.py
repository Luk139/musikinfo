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
    threshold_min = 0.6  # Minimum amplitude threshold (considering ~0dB)
    threshold_max = 2.0  # Maximum amplitude threshold (considering ~0dB)
    start_time = 23.0  # Time (in seconds) of the first drum hit
    target_frequency_min = 64  # Lower bound of target frequency around the drum hit
    target_frequency_max = 128  # Upper bound of target frequency around the drum hit
    db_threshold = 80  # Threshold for frequency distribution in dB

    percussive_mask = (amplitude_envelope >= threshold_min) & (amplitude_envelope <= threshold_max)

    # Convert time-based start_time to frame index
    start_frame = int(librosa.time_to_frames(start_time, sr=sr, hop_length=512))

    print("Shape of percussive_mask:", percussive_mask.shape)
    print("Start frame:", start_frame)

    # Convert the target frequency range to the closest bin indices in the STFT
    freq_bin_min = np.argmin(np.abs(librosa.fft_frequencies(sr=sr) - target_frequency_min))
    freq_bin_max = np.argmin(np.abs(librosa.fft_frequencies(sr=sr) - target_frequency_max))

    # Apply masks for both amplitude and frequency
    if start_frame < percussive_mask.shape[0]:
        percussive_mask = np.tile(percussive_mask, (stft.shape[0], 1))
        percussive_mask[:, start_frame:] = True
        if freq_bin_min < percussive_mask.shape[0] and freq_bin_max < percussive_mask.shape[0]:
            percussive_mask[freq_bin_min:freq_bin_max, start_frame:] = True

    print("After applying masks, new shape of percussive_mask:", percussive_mask.shape)

    # Rest of the code remains the same...
    # ...

# Example usage
input_audio_path = 'guitardrums.wav'  # Replace with your audio file path
output_filename = 'extracted_percussive_custom.wav'

percussive_extraction_with_custom_parameters(input_audio_path, output_filename)
