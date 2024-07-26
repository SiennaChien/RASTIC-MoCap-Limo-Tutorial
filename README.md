# RASTIC - Motion Capture and AgileX Limo Tutorial
Welcome to Boston University's RASTIC Lab Space! This repository holds the scripts necessary to run the Motion Capture and AgileX Limos Tutorial (although not the ROS workspace or package). 


## Setup
line_follower.py and cav_for_line_follower.py are for coordination on the RASTIC Ubuntu Dell laptop, while limo_cmd_listener.py is for the listener node on the limo. For simplicity, the files are already downloaded and set up in the RASTIC Linux Dell laptop and Limo#780. Further instructions can be found in the Tutorial Documentation. vrpn_client_ros is a ros package for connecting to the Motion Capture Cameras, and is already built in the laptop as well. 

We do not currently have detailed documentation on how to run this tutorial on a personal device. 
If you had some experience in ROS and would like to run this tutorial on a personal device, download the three python files and build a workspace and package for them. Secure copy (scp) the workspace onto a Limo of your choice, and rebuild the workspace in the Limo. To connect to the Motion Capture Cameras, build the vrpn_client_ros package into the same workspace. 

## Before you start

Please talk to a RASTIC employee before starting this tutorial. To prevent any accidental injuries and damage to the Limos, we recommend you to do this tutorial in pairs, or to have a RASTIC employee assist you. 

The detailed documentation can be found in the RASTIC Google Drive, under "Manuals and Machine Instructions" -> "RASTIC Written Manuals" -> "Motion Capture & AgileX Limo Tutorial.pdf" or can be viewed [here](https://drive.google.com/file/d/1q9NDgcbJeZ9AusGzr6R6lM0c8bUHpnN8/view?usp=sharing  "here")
