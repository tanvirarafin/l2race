# Learning to Race (l2race)
 
Simulation of racecar from eye of god view. User code must drive the car as quickly as possible around the track.

## Requirements


 - anaconda or miniconda https://www.anaconda.com/products/individual
 - Use Python 3.7.x (for pygame 2.0, using prebuilt python wheel archive)

Conda is your best friend! Make a new environment to work in l2race.
You can install the requirements in this environment using its own pip.

Make a new environment (see https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)
```shell script
(l2race) F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race>conda create --name l2race
WARNING: A conda environment already exists at 'C:\Users\tobid\anaconda3\envs\l2race'
Remove existing environment (y/[n])? n


CondaSystemExit: Exiting.

```

Make sure you are using the conda pip in your conda environment:
```shell script
Microsoft Windows [Version 10.0.19041.388]
(c) 2020 Microsoft Corporation. All rights reserved.
(l2race) F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race>where pip
C:\Users\tobid\anaconda3\envs\l2race\Scripts\pip.exe
```
Install the requiremepnts:

```shell script
(l2race) F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race>pip install -r requirements.txt
Requirement already satisfied: svgpathtools in c:\users\tobid\anaconda3\envs\l2race\lib\site-packages (from -r requirements.
txt (line 2)) (1.3.3)
Requirement already satisfied: pygame==2.0.0.dev10 in c:\users\tobid\anaconda3\envs\l2race\lib\site-packages (from -r requir
ements.txt (line 3)) (2.0.0.dev10)
......
``` 
### pygame
For pygame 2.0-dev10 (needed for python 3.7), see wheels at https://www.piwheels.org/project/pygame/ or https://github.com/pygame/pygame/releases . Then use pip install wheel-file. Download the wheel for pygame 2.0 for python 3.7 and your OS.


requirements.txt was built automatically using https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt
```shell script
pip install pipreqs
pipreqs --force .
```
You can build the conda env l2race using
```shell script
conda env create -f environment.yml
```

# Running l2race

l2race uses client-server. 

The client draws the racetrack and car and accepts input from keyboard or xbox joystick controller or your software agent.

The server computes the car dynamics model in response to your command input and returns the car state to the client.

From root of l2race, start the server and client from separate terminals (or from pycharm; see below).

### start client
```shell script
(l2race) F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race>python -m server
pygame 2.0.0.dev10 (SDL 2.0.12, python 3.7.7)
Hello from the pygame community. https://www.pygame.org/contribute.html
WARNING:commonroad.vehicleDynamics_MB:check_cython: F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race\commonroad\vehicleDynamics_MB.py is still just a slowly interpreted script.
WARNING:__main__:Gooey GUI builder not available, will use command line arguments.
Install with "pip install Gooey". See README
WARNING:__main__:Gooey GUI not available, using command line arguments.
You can try to install with "pip install Gooey"
INFO:__main__:waiting on <socket.socket fd=1512, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('0.0.0.0', 50000)>
```

Start the server:

```shell script
(l2race) F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race>python -m server
pygame 2.0.0.dev10 (SDL 2.0.12, python 3.7.7)
Hello from the pygame community. https://www.pygame.org/contribute.html
WARNING:commonroad.vehicleDynamics_MB:check_cython: F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race\commonroad\vehicleDynamics_MB.py is still just a slowly interpreted script.
WARNING:__main__:Gooey GUI builder not available, will use command line arguments.
Install with "pip install Gooey". See README
WARNING:__main__:Gooey GUI not available, using command line arguments.
You can try to install with "pip install Gooey"
```

Don't worry about missing Gooey; install it if you want to have a GUI pop up to launch the client and server.

It should not start running the client and you should see this:

![screenshot](media/oval_track_screenshot.png)

## client options
````shell script
(l2race) F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race>python -m client -h
pygame 2.0.0.dev10 (SDL 2.0.12, python 3.7.7)
Hello from the pygame community. https://www.pygame.org/contribute.html
WARNING:commonroad.vehicleDynamics_MB:check_cython: F:\tobi\Dropbox (Personal)\GitHub\neuromorphs\l2race\commonroad\vehicleDynamics_MB.py is still just a slowly interpreted script.
WARNING:__main__:Gooey GUI builder not available, will use command line arguments.
Install with "pip install Gooey". See README
WARNING:__main__:Gooey GUI not available, using command line arguments.
You can try to install with "pip install Gooey".
Ignore this warning if you do not want a GUI.
usage: client.py [-h] [--host HOST] [--port PORT] [--fps FPS]
                 [--joystick JOYSTICK] [--record] [--car_name CAR_NAME]
                 [--track_name TRACK_NAME] [--multi] [--timeout_s TIMEOUT_S]

l2race client: run this if you are a racer.

optional arguments:
  -h, --help            show this help message and exit

Client arguments::
  --host HOST           IP address or DNS name of model server. (default:
                        localhost)
  --port PORT           Server port address for initiating connections.
                        (default: 50000)
  --fps FPS             Frame rate on client side (server always sets time to
                        real time). (default: 30)
  --joystick JOYSTICK   Desired joystick number, starting with 0. (default: 0)
  --record              record data to date-stamped filename, e.g. --record
                        will write datestamped files named 'l2race-XXX.csv' in
                        folder 'data, where XXX is a date/timestamp'.
                        (default: False)
  --car_name CAR_NAME   Name of this car. (default: l2racer)
  --track_name TRACK_NAME
                        Name of track. Available tracks are in the
                        'media/tracks' folder. Available tracks are ['oval',
                        'Sebri', 'track_1', 'track_2', 'track_3', 'track_4',
                        'track_5', 'track_6'] (default: oval)
  --multi               Activate multi-car mode, where all cars run on same
                        track. Default is solo mode where each car gets own
                        track. (default: False)
  --timeout_s TIMEOUT_S
                        Socket timeout in seconds for communication with model
                        server. (default: 0.2)

Run with no arguments to open dialog for server IP

````

### joystick and keyboard
 - Help for each device is printed on startup. For keyboard, you can type h anytime to see the keys help in console.
 - You need to focus on the pygame window for either input to work.

# Development

## pycharm

l2race includes pycharm _.idea_ files that have many useful run configurations already set up.

## Recording data

The _--record_ option automatically records a .csv file to the _data_ folder. This file has the time, commnands, and car state.
