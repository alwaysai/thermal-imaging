# thermal-imaging-repo
This repo contains applications that demostarte how to use FLiR Lepton thermal camera.  The FLiR sensor uses microbolometer array that changes resistance as its heated up.  By measuring resistance the sensor can determine the tempature of detected objects.  The sensor's firmware creates a colored image that encodes that resistance data into heat map.  The image can be processed using the same techniques as visible light.

To use the applications in this repo you will need a FLir Lepton camera module, information on where to purchase one can be found here https://lepton.flir.com/

To get USB connectivity you will need a PureThermal board, information on where to purchase one can be found here https://www.digikey.com/en/product-highlight/g/groupgets/purethermal-boards?utm_adgroup=xGeneral&utm_source=google&utm_medium=cpc&utm_campaign=Dynamic%20Search&utm_term=&utm_content=xGeneral&gclid=Cj0KCQjw28T8BRDbARIsAEOMBcx4dKdKK7L4yeLrnVBfl1GyPnaFo-tPLi55sXJyuX3zQA7RwKLBvyIaAqy4EALw_wcB  


Applications for themal camera:
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
FLiR Lepton Camera needs to be connected to PureThermal board that provides USB connectivity to use the applications in this repo 

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
