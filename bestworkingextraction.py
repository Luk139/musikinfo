import os
import librosa
import soundfile as sf
import numpy as np

def harmonic_extraction(audio_path, output_filename):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Harmonic-Percussive Source Separation (HPSS)
    y_harmonic, y_percussive = librosa.effects.hpss(y)

    # Get the current working directory
    current_dir = os.getcwd()

    # Define input and output paths+
    input_audio_path = os.path.join(current_dir, 'audios', audio_path)
    output_directory = os.path.join(current_dir, 'extractedfiles')
    output_path_harmonic = os.path.join(output_directory, output_filename)
    output_path_percussive = os.path.join(output_directory, 'extracted_percussive.wav')

    # Check if the output directory exists, if not create it
    os.makedirs(output_directory, exist_ok=True)

    # Save the extracted harmonic audio as a WAV file
    sf.write(output_path_harmonic, y_harmonic, sr)
    print("Harmonic component saved to:", output_path_harmonic)

    # Subtract the harmonic component from the original audio to get the percussive component
    y_percussive_only = y - y_harmonic

    # Save the extracted percussive audio as a WAV file
    sf.write(output_path_percussive, y_percussive_only, sr)
    print("Percussive component saved to:", output_path_percussive)

# Example usage
if __name__ == "__main__":
    input_audio_filename = 'audios/LukTrack.wav'  # Replace with your audio file name
    output_filename = 'extracted_harmonic_guitar.wav'
    harmonic_extraction(input_audio_filename, output_filename)
