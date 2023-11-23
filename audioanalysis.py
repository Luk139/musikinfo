import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

def analyze_audio(audio_path):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Calculate the Short-Time Fourier Transform (STFT) magnitude
    stft = np.abs(librosa.stft(y))

    # Calculate amplitude envelope over time
    amplitude_envelope = np.mean(np.abs(librosa.stft(y)), axis=0)

    # Plot the spectrogram
    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')

    # Plot amplitude envelope over time
    plt.subplot(3, 1, 2)
    plt.plot(librosa.times_like(amplitude_envelope, sr=sr), amplitude_envelope, label='Amplitude Envelope')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Amplitude Envelope')
    plt.legend()

    # Plot frequency distribution
    plt.subplot(3, 1, 3)
    librosa.display.specshow(stft, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f')
    plt.title('Frequency Distribution')

    plt.tight_layout()
    plt.show()

# Example usage: Provide the path to your audio file
input_audio_path = 'onlyguitar.wav'
analyze_audio(input_audio_path)
