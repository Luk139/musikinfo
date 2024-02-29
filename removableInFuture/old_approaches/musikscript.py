if __name__ == '__main__':
    import librosa
    import soundfile as sf
    import numpy as np
    import datetime
    import librosa.display
    import matplotlib.pyplot as plt
    import IPython
    from scipy.ndimage import median_filter


def advanced_percussive_extraction(audio_path):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Short-Time Fourier Transform (STFT)
    stft = np.abs(librosa.stft(y))

    # Perform median filtering along the frequency axis to emphasize percussive elements
    # Adjust the filter size according to the characteristics of the audio
    filtered_stft = median_filter(stft, size=(1, 25))  # Example filter size
    
    # Apply thresholding to discriminate between percussive and non-percussive components
    threshold = 0.4 * np.max(filtered_stft)  # Adjust threshold according to the audio
    percussive_mask = filtered_stft > threshold

    # Apply the mask to the original spectrogram
    percussive_stft = stft * percussive_mask

    # Inverse STFT to obtain the percussive component
    y_percussive = librosa.istft(percussive_stft)

    return y_percussive

    # Load the original audio file
    y_original, sr = librosa.load(input_audio_file)

    # Modify parameters for STFT computation
    n_fft = 2048  # Increase window size
    hop_length = 512  # Decrease hop length

    # Perform STFT with adjusted parameters
    stft_harmonic = librosa.stft(y_original, n_fft=n_fft, hop_length=hop_length)

    # Apply HPSS for separation
    y_harmonic, y_percussive = librosa.decompose.hpss(stft_harmonic)

    # Convert the separated components to time domain
    y_harmonic_time = librosa.istft(y_harmonic, hop_length=hop_length)
    y_percussive_time = librosa.istft(y_percussive, hop_length=hop_length)

    # Save the separated components as WAV files
    sf.write('harmonic.wav', y_harmonic_time, sr)
    sf.write('percussive.wav', y_percussive_time, sr)
    output_percussive_path ='advperc.wav'
    advanced_percussive_extraction_and_save(input_audio_path, output_percussive_path)
   

