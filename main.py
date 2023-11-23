from percussive_extraction import percussive_extraction
from harmonic_extraction import harmonic_extraction

def main():
    percussive_input_audio = 'audios\onlydrums.wav'  # Replace with your audio file name for percussive extraction
    percussive_output_filename = 'extracted_percussive.wav'

    harmonic_input_audio = 'audios\onlyguitar.wav'  # Replace with your audio file name for harmonic extraction
    harmonic_output_filename = 'extracted_harmonic_guitar.wav'

    percussive_extraction(percussive_input_audio, percussive_output_filename)
    harmonic_extraction(harmonic_input_audio, harmonic_output_filename)

if __name__ == "__main__":
    main()
