# Importing wave, struct, and sys from Python Standard Libraries
import wave
import struct
import sys

"""""
AudioParse.py
Version 1.0
Written By David Story

Description:
    AudioParse is a simple library that provides a function that can parse the data from the byte string returned from 
    the readframes(n)function for a wave-object. AudioParse takes input as a wave-object, and will return a list of 
    integers representing the audio points from the start of the audio file to the end of the audio file.

    For more information on the wave library and how the Python Standard Library functions work, visit the documentation
    here as follows:

    Python Standard Library: https://docs.python.org/3/library/index.html
    Wave documentation:      https://docs.python.org/3/library/wave.html

    For questions about this library you may email me at: storyd@sonoma.edu

"""""
# Licensing Information for this Library
""""
MIT License

Copyright (c) 2018 David Andrew Story

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


#########################################################################
#                             Start Code                                #
#########################################################################

def getAudioInfo(audio):
    """
    :param audio:
    :return none:

    Description: This function will take in an opened wave-object and print out information about the .wav
                 files characteristics.
    """
    print("Samples in the file: ", audio.getnframes())
    print("Sampling rate of the file: ", audio.getframerate())
    print("Sampling width of file (bits per file: output*8):", audio.getsamplewidth())
    length = round(int(audio.getnframes()) / int(audio.getframerate()), 3)
    print("Length in seconds of the file:", length, "seconds")


def parseFrames(audio):
    """
    :param audio:
    :return audioFrames:

    Description: This function will take in an opened wave-object, determine how many frames there are, then create
                 a list of integers that represent each sample of the audio. So if you were looking at the first
                 element in the returned list (audioFrames[0]), you would get a value between -32,768 to 32,767 since
                 each audio sample is a 16-bit sample. This function returns a list of nframe samples that are now
                 ints between -32,768 to 32,767 as stated before.
    """
    # Uses wave object function getnframes to get number of samples
    length = audio.getnframes()
    # List for final audio files
    audioFrames = []
    # For the number for audio samples
    for i in range(0, length):
        # Read first audio file sample
        frame = audio.readframes(1)
        # Unpack 2 bytes, since these WAV files are 16-bit
        data = struct.unpack("<h", frame)
        # Appends the data point to audio frame file
        audioFrames.append(data[0])
    # Clears variable memory
    del length
    # returns list of audio points
    return audioFrames


def writeNewWave(list, sr, name):
    """
    :param list sr name:
    :return newWave:

    Description: This function will take a list of integers that represent signed 16-bit wave samples, it will take
                 in a sampling rate as sr, and a name that for the .wav file. It will then open a .wav file, write
                 the frames from the list, and then close the file. The function will return newWAve, which is the
                 new wave-object of the written .wav file. The .wav file is written to the current directory.
    """
    # try-except is used here to catch any errors when creating the file
    # Probably most common error here is if user does not at .wav extension
    # to the name variable passed to function
    try:
        # Opens new wav file based on name
        newWave = wave.open(name, "w")
        # Sets channels to 1 (Mono)
        newWave.setnchannels(1)
        # Sets sample width to 2 (16-bit)
        newWave.setsampwidth(2)
        # Sets frame rate to that specified before
        newWave.setframerate(sr)
        # Sets number of frames to the length of the list you feed in
        newWave.setnframes(len(list))
        # For items in your list
        for items in list:
            # Makes item in list a 16-bit Byte
            byteType = struct.pack('<h', items)
            # Writes new byte as a frame in your new file
            newWave.writeframes(byteType)
        # Closes your wav file
        newWave.close()
        # Clears list and variable memory
        del list, sr, name
        # Returns new wav-object
        return newWave
    except:
        print("Error opening or naming file, check name and directory.")
        sys.exit(-1)

#########################################################################
#                              End Code                                 #
#########################################################################

