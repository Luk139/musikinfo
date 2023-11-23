import os
import librosa
import numpy as np
import soundfile as sf

def separate_percussive_and_harmonic(audio_path, percussive_output, harmonic_output):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Short-Time Fourier Transform (STFT)
    stft = np.abs(librosa.stft(y))

    # Calculate amplitude envelope
    amplitude_envelope = np.mean(np.abs(librosa.stft(y)), axis=0)
    
    # Parameters for separation
    threshold_min = 1.1  # Minimum amplitude threshold (considering ~0dB)
    threshold_max = 2.0  # Maximum amplitude threshold (considering ~0dB)
    start_time = 0.0  # Time (in seconds) of the first drum hit
    target_frequency_min = 0  # Lower bound of target frequency around the drum hit
    target_frequency_max = 64  # Upper bound of target frequency around the drum hit

    # Create a mask to separate percussive and harmonic components
    percussive_mask = (amplitude_envelope >= threshold_min) & (amplitude_envelope <= threshold_max)

    # Convert time-based start_time to frame index
    start_frame = int(librosa.time_to_frames(start_time, sr=sr, hop_length=512))

    # Convert the target frequency range to the closest bin indices in the STFT
    freq_bin_min = np.argmin(np.abs(librosa.fft_frequencies(sr=sr) - target_frequency_min))
    freq_bin_max = np.argmin(np.abs(librosa.fft_frequencies(sr=sr) - target_frequency_max))

    # Apply masks for both amplitude and frequency
    if start_frame < percussive_mask.shape[0]:
        percussive_mask = np.tile(percussive_mask, (stft.shape[0], 1))
        percussive_mask[:, start_frame:] = True
        if freq_bin_min < percussive_mask.shape[0] and freq_bin_max < percussive_mask.shape[0]:
            percussive_mask[freq_bin_min:freq_bin_max, start_frame:] = True

    # Apply the mask to the original spectrogram to separate percussive component
    percussive_stft = stft * percussive_mask
    # Inverse STFT to obtain the percussive component
    y_percussive = librosa.istft(percussive_stft)

    # Invert the percussive mask to extract harmonic component
    harmonic_mask = np.logical_not(percussive_mask)
    # Apply the mask to the original spectrogram to separate harmonic component
    harmonic_stft = stft * harmonic_mask
    # Inverse STFT to obtain the harmonic component
    y_harmonic = librosa.istft(harmonic_stft)

    # Get the current working directory as the output directory
    output_directory = os.getcwd()

    # Save the extracted percussive audio as a WAV file
    percussive_output_path = os.path.join(output_directory, percussive_output)
    sf.write(percussive_output_path, y_percussive, sr)
    print("Percussive component saved to:", percussive_output_path)

    # Save the extracted harmonic audio as a WAV file
    harmonic_output_path = os.path.join(output_directory, harmonic_output)
    sf.write(harmonic_output_path, y_harmonic, sr)
    print("Harmonic component saved to:", harmonic_output_path)

# Example usage
input_audio_path = 'guitardrums.wav'  # Replace with your audio file path
percussive_output_filename = 'extracted_percussive.wav'
harmonic_output_filename = 'extracted_harmonic.wav'

separate_percussive_and_harmonic(input_audio_path, percussive_output_filename, harmonic_output_filename)
