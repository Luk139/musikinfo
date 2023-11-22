if __name__ == '__main__':
    import librosa
    import soundfile as sf
    import numpy as np
    import datetime
    import librosa.display
    import matplotlib.pyplot as plt
    import IPython
    #Replace 'input_audio_file' with your input audio file path
    input_audio_file = 'guitardrums.wav'

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
