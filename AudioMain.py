import wave
import sys
import AudioParse
import AudioSteganography

"""
AudioMain.py
Written by: Your Name Here
EE Python Workshop 2019

"""
"""
Description: This is the main file which you use to run your audio steganography program. What this program will do
             is, based on user inputs, be able to either:
                1) decode a secret message that is hidden inside of a 16-bit .WAV file and then print or store that
                   message in a .txt file. 
                   
                2) Take a text file and the name of an 16-bit .WAV file, embed the ASCII character bytes and an end
                   character into the audio,and return the altered audio. 
                   
             Inputs for the decode program, in a terminal should look like the following:
             
                >>python AudioMain.py DECODE filename.wav secretmessage.txt
                
             * The above decode input assumes you are saving your text file to your current directory, you can 
             add a 4th argument if you would like to specify which directory you save to *
                
             Inputs for the encode program, in a terminal should look like the following:
             
                >>python AudioMain.py ENCODE yourmessage.txt soundtohidein.wav
                
             * The above encode input assumes you are saving your final audio file to your current directory, you can 
             add a 4th argument if you would like to specify which directory you save to *
"""
"""
Standard Python Libraries Used:
    Wave.py
    Sys.py
    
Dependencies (Provided):
    AudioParse.py
    AudioSteganography.py
    
    AudioParse.py: 
    
        Provides a Class and class functions to aid you in turning your 16-bit .WAV file into a list of samples that you
        can easily manipulate and work with. Read the file and functions for a better understanding of how the class 
        works. Ambitious or skeptical students may choose to disregard this file and create their own parsing scheme, 
        that is fine and encouraged; however, in lieu of time this file is here to avoid getting stuck on nitty-gritty
        problems.
    
    AudioSteganography.py:
    
        This is where you will write the functions for Encode and Decode that you will call in this file, AudioMain.py,
        to perform all the logic for decoding and encoding the audio samples.
"""
"""
More info on libraries and instructions:
    Project Instructions: http://meadowviewlab.com/_pages/python-instructions/
    sys.py documentation: https://docs.python.org/3/library/sys.html
    wave.py documentation: https://docs.python.org/3/library/wave.html
    
Project files at:
    https://github.com/david-story/Audio-Steganography
"""

def main():
    """
    This will be your main function, here you want to:
        1) Parse the inputs for the argument and check for valid inputs and which mode you want to enter.

        2) For decode, you want to use the class and functions from AudioParse to handle the nitty-gritty of parsing the
           .WAV file for you. From here you must use the instructions and your intuition to create a
           strategy for decoding the samples, implement that logic in AudioSteganography.py, and then call the functions
           to run the decoding here.

        OR

        3) For encode, you will again need to use the AudioParse class and functions to parse the .WAV file, from there
           you will then implement the logic in AudioSteganography.py that will do the encoding process outlined in the
           instructions and based on the strategy that you come up with.

    Below I will provide an example of you can use the Python Library Sys.py to get user inputs. You need to call
    AudioMain.py in a terminal (terminal on OS/Linux, CMD on Windows) to have this work.

    Run this line in your terminal to test out this file:

        >>python AudioMain.py this 1 3 true file.wav test.txt

    If you are ready, begin coding.
    """

    # This will print that you are beginning the program
    print("Beginning Program!")

    # Using sys.py to get arguments passed in the terminal, This prints a list of line arguments passed.
    print(sys.argv)

    # This prints the total number of arguments
    print(len(sys.argv))

    # Check for more than 0 arguments, prints the first
    if len(sys.argv) > 0:
        print(sys.argv[0])

    # Begin coding!

main()