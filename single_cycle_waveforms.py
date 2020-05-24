"""
Python script for creating Single Cycle Waveforms from Wav files.

Originally for hardware such as the Elektron Monomachine / Octatrack. 

Dependencies
osc_gen https://github.com/harveyormston/osc_gen

Original code by Harvey Ormston.

Edited by Chris Speed and Jérémie C. Wenger 2020.

Added the feature to loop over file directories and slice them into a batch of new single cycle waveforms.

Please keep the audio file sizes as small as possible!
"""

import wavetable
import dsp
import os

FOLDER_PATH = r'C:\\Users\\Chris Speed\\Music\\Wavetables' #add your file directory here

def list_dir(my_dir):
    file_names = os.listdir(my_dir)
    for file_name in file_names:
        source = os.path.join(my_dir, file_name)
        # slice
        try:
            wt = wavetable.WaveTable(16, wave_len=128).from_wav(source, resynthesize=False)
            # Write the resulting oscillator to a wav file.
            new_name = os.path.splitext(file_name)[0] + '-new.wav'
            wt.to_wav(os.path.join(my_dir, new_name))
            print("processed:", source)
        except Exception as e:
            print("oops, didn't work for:", source)
            print(e)

if __name__ == '__main__':
    list_dir(FOLDER_PATH) 
