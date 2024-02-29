import os
import librosa
import soundfile as sf

def separate_percussive_and_harmonic(audio_path, percussive_output, harmonic_output):
    # Load audio file
    y, sr = librosa.load(audio_path)
    
    # Apply Harmonic-Percussive Source Separation (HPSS)
    y_harmonic, y_percussive = librosa.effects.hpss(y)

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
input_audio_path = 'onlyguitar.wav'  # Replace with your audio file path
percussive_output_filename = 'extracted_percussive.wav'
harmonic_output_filename = 'extracted_harmonic.wav'

separate_percussive_and_harmonic(input_audio_path, percussive_output_filename, harmonic_output_filename)
