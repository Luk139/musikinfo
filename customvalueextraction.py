import os
import librosa
import numpy as np
import soundfile as sf

def percussive_extraction(audio_path, output_filename):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Short-Time Fourier Transform (STFT)
    stft = np.abs(librosa.stft(y))

    # Calculate amplitude envelope
    amplitude_envelope = np.mean(np.abs(librosa.stft(y)), axis=0)
    
    # Parameters for separation
    threshold_min = 1.1  # Minimum amplitude threshold
    threshold_max = 2  # Maximum amplitude threshold
    start_time = 00.0  # Time (in seconds) of the first drum hit
    target_frequency_min = 64  # Lower bound of target frequency
    target_frequency_max = 128  # Upper bound of target frequency
    db_threshold = 100  # Threshold for frequency distribution in dB

    # Create a mask to separate percussive component
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

    # Get the current working directory
    current_dir = os.getcwd()

    # Define input and output paths
    input_audio_path = os.path.join(current_dir, 'audios', audio_path)
    output_directory = os.path.join(current_dir, 'extractedfiles')
    output_path = os.path.join(output_directory, output_filename)

    # Check if the output directory exists, if not create it
    os.makedirs(output_directory, exist_ok=True)

    # Save the extracted percussive audio as a WAV file
    sf.write(output_path, y_percussive, sr)
    print("Percussive component saved to:", output_path)

# Example usage
if __name__ == "__main__":
    input_audio_filename = 'audios\LukTrack.wav'  # Replace with your audio file name
    output_filename = 'extracted_percussive.wav'
    percussive_extraction(input_audio_filename, output_filename)
