import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path)
    
    stft = np.abs(librosa.stft(y))

    amplitude_envelope = np.mean(np.abs(librosa.stft(y)), axis=0)

    plt.figure(figsize=(12, 6))
    plt.subplot(3, 1, 1)
    librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')

    plt.subplot(3, 1, 2)
    plt.plot(librosa.times_like(amplitude_envelope, sr=sr), amplitude_envelope, label='Amplitude Envelope')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Amplitude Envelope')
    plt.legend()

    plt.subplot(3, 1, 3)
    librosa.display.specshow(stft, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f')
    plt.title('Frequency Distribution')

    plt.tight_layout()
    plt.show()

input_audio_path = 'audios/guitardrums.wav'
analyze_audio(input_audio_path)
