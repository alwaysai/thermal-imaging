# thermal-imaging-repo

Use cases for a depth cameras are:
1. Night Vision - Detect objects in thermal spectrum at night
2. Medical diagnosis - Temapature taking
3. Building inspection - Detect insulation leaks
4. Automotive - Monitor cooling performance
5. Tracking - Infrared radiation based centriod tracking


## Repo Programs
| Folder                     	| Description                                                                                              	|
|----------------------------	|----------------------------------------------------------------------------------------------------------	|
| verify-thermal-camera       | Application checks that FLiR Lepton and TrueThermal board are working on the alwaysAI platform  	|
| hsv 	                      | Application visualizes HSV Value Channel in thermal spectrum|
| thermal-edges  	            | Application use Canny edge detector to find edges of objects detected by thermal camera|
| thermal-detector            | Application detects objects in the thermal spectrum and bounds the edges of the detected objects|

## Running
Realsense Camera needs to be connected to USB 3.x hub for applications to work

Use the alwaysAI CLI to build and start these apps on Linux PCs and Devices:

Configure (once): `aai app configure`

Build: `aai app deploy`

Run: `aai app start`

If you are using a Mac or Windows 10 PC do the following:

Configure (once): `aai app configure`

Build: `aai app install`

Run: `aai app start`


## Support
Docs: https://dashboard.alwaysai.co/docs/getting_started/introduction.html

Realsense API Docs: https://alwaysai.co/docs/edgeiq_api/real_sense.html

Community Discord: https://discord.gg/R2uM36U

Email: contact@alwaysai.co
