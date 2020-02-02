from shutil import copyfile
import scipy.io.wavfile
def yes (path, name="a.wav"):
    # copyfile(path, "userobjects/"+name)
    binary_file_data = path
    
    binary_file_path = "userobjects/a.wav"
    with open(binary_file_path, 'w') as f:
        f.write(binary_file_data)

    # Download the sound file from gcp
    sound_file = scipy.io.wavfile.read(binary_file_path)
if __name__ == "__main__":
    yes("r.m4a")