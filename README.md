# Sorting Hat

Talk to the Sorting Hat, answer his questions and get sorted into one of four Hogwarts houses - Gryffindor, Hufflepuff, Ravenclaw & Slytherin.

This project is an attempt to bring alive the character "Sorting Hat" from the Harry Potter series as a conversational agent. As part of the [Georgia Tech Technical Arts Practicum](https://dilac.iac.gatech.edu/node/27) and with guidance from Dr. Brian Magerko, Nicholas Davis and in collaboration with ADAM Lab (School of Interactive Computing), this project was demo-ed at the Eyedrum Gallery, Atlanta.
Implemented using python 2.7 and arduino to power the animatronic hat, a short video explaining this project can be found at: 

[Real Life Harry Potter Sorting Hat!](https://www.youtube.com/watch?v=wnRXR0BdQ-g)

### Dependencies/Modules
* Python 2.7 and modules:
- pygame
- serial
- speech_recognition

### Instructions to run

To start the program, run the command given below, in a Linux terminal (arguments are _optional_):
    python hat.py -p <arduino_port_num> -m <mic_index_num> -d <debug_flag>

eg. python hat.py -p 0 -m 0 -d True

arduino_port_num - this is the port number to which arduino controlling the hat movements is connected.
Not providing it runs only the conversational agent.

mic_index_num - this argument is the index of the preferred microphone(mic).
If not provided, program selects the default system mic.

debug_flag - set this as True if you want to turn on the debug information on console

Run "mics.py" to get a list of available microphones and their indices.