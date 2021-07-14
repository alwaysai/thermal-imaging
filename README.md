# Thermal Imaging
This repo contains applications that demonstrate how to use FLiR Lepton thermal camera.  The FLiR sensor uses microbolometer array that changes resistance as its heated up.  By measuring resistance the sensor can determine the temperature of detected objects.  The sensor's firmware creates a colored image that encodes that resistance data into heat map.  The image can be processed using the same techniques as visible light.

![Lepton](https://user-images.githubusercontent.com/21957723/96892827-e22c1600-143e-11eb-983a-9d2316730169.jpg)

To use the applications in this repo you will need a FLir Lepton camera module, information on where to purchase one can be found [here](https://lepton.flir.com/)

![14670-PureThermal_2-_FLiR_Lepton_Dev_Board-01](https://user-images.githubusercontent.com/21957723/96893184-4bac2480-143f-11eb-869d-b9ff4f29169b.jpg)

To get USB connectivity you will need a PureThermal board, information on where to purchase one can be found [here](https://www.digikey.com/en/product-highlight/g/groupgets/purethermal-boards?utm_adgroup=xGeneral&utm_source=google&utm_medium=cpc&utm_campaign=Dynamic%20Search&utm_term=&utm_content=xGeneral&gclid=Cj0KCQjw28T8BRDbARIsAEOMBcx4dKdKK7L4yeLrnVBfl1GyPnaFo-tPLi55sXJyuX3zQA7RwKLBvyIaAqy4EALw_wcB)


Applications for thermal cameras:
1. Night Vision - Detect objects in thermal spectrum at night
2. Medical diagnosis - Temperature taking
3. Building inspection - Detect insulation leaks
4. Automotive - Monitor cooling performance
5. Tracking - Infrared radiation based centroid tracking

## Requirements
* [alwaysAI account](https://alwaysai.co/auth?register=true)
* [alwaysAI Development Tools](https://alwaysai.co/docs/get_started/development_computer_setup.html)

## Repo Programs
| Folder                     	| Description                                                                                              	|
|----------------------------	|----------------------------------------------------------------------------------------------------------	|
| verify-thermal-camera       | Application checks that FLiR Lepton and TrueThermal board are working on the alwaysAI platform  	|
| hsv 	                      | Application visualizes HSV Value Channel in thermal spectrum|
| thermal-edges  	            | Application use Canny edge detector to find edges of objects detected by thermal camera|
| thermal-stream-save         | Application saves a thermal video stream from a FLiR Lepton camera mounted on TrueThermal board|
| thermal-detector            | Application detects objects in the thermal spectrum and bounds the edges of the detected objects|

## Usage
FLiR Lepton Camera needs to be connected to PureThermal board that provides USB connectivity to use the applications in this repo.

Once the alwaysAI tools are installed on your development machine (or edge device if developing directly on it) you can install and run the app with the following CLI commands:

To perform initial configuration of the app:
```
aai app configure
```

To prepare the runtime environment and install app dependencies:
```
aai app install
```

To start the app:
```
aai app start
```

## Support
* [Documentation](https://alwaysai.co/docs/)
* [Community Discord](https://discord.gg/z3t9pea)
* Email: support@alwaysai.co
