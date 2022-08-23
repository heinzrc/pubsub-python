# pubsub-python
Pubsub written in python to change apex config specifically 

# Installation
Download the latest version of python from here: https://www.python.org/downloads/

During the install, ensure both the pip and path options are checked

Install websockets module:
```
pip3 install websockets
```
To make use of the rest of the script some autoexec files will need to be set up in your games local files

Config files should be located in the cfg folder of your installation (This will be the same for Origin as well)
```
C:\Steam\steamapps\common\Apex Legends\cfg
```
This is where we will place our autoexecs

autoexec1.cfg:
Config to constantly execute the config that contains the variable sensitivity

autoexec2.cfg:
This file contains the senstivity that will be changed via channel points redemptions

autoexec3.cfg:
Config that disables variable sensitivities

After all three files are copied to the correct location, add the following to your games launch options
```
+exec autoexec1
```

# Running the code
Before you run the code you will have to change a few lines of code

The first two are: <CLIENT_ID> and <USER_AUTH_TOKEN>

![image](https://user-images.githubusercontent.com/65210276/186210676-fbcdb4a7-ca54-42b8-bb0d-bd1a1404442f.png)

To find both of these you can go to https://06k.org/pubsub/generate.html 

Once you login with twich there will be 3 buttons

![image](https://user-images.githubusercontent.com/65210276/186206068-ae2b9c81-ef8f-4482-8420-702d886673e6.png)

Clicking them will copy their contents to your clipboard

The third button contains your auth token

![image](https://user-images.githubusercontent.com/65210276/186205736-6fd8d7a6-35d0-4956-9a66-ae7d893b4420.png)

After that you will need to paste the file path of your autoexec2.cfg in the following line

![image](https://user-images.githubusercontent.com/65210276/186211970-9578f87c-4d9f-452d-98e3-bcd474b0a9ad.png)

To run the code, go to wherever you downloaded the code to

Type 'cmd' into the filepath bar

![image](https://user-images.githubusercontent.com/65210276/186215114-0690de25-5e98-4aa7-91f6-e37490fbc335.png)

In the resulting command prompt type the following:

```
python3 main.py
```

# Channel Points Setup

In order to utilize the now running script you will need to setup channel points rewards with titles that correspond to the following list:

![image](https://user-images.githubusercontent.com/65210276/186217771-c2c8dc3f-fa51-4152-b1fa-3745d046cf98.png)

Your rewards should look like the following to correspond with the code 

![image](https://user-images.githubusercontent.com/65210276/186218214-e5be518b-eb7a-4727-b50c-8c6d5e2f2df7.png)

Note that only the title matters. Things like cost have no effect on the performance of this program (in it's current state)

# Customization

Within webSocketClient.py you will find the list of titles and corresponding in game sensitvities. You can change all of these values to just about any number as long as the titles correspond with a reward.

# Credits

Python Twitch API integration template written by https://github.com/SlackingVeteran/
