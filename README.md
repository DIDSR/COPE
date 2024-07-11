# WebXR-contrast-sensitivity-tool
 
The Contrast Sensitivity Dectection Tool measures the miniumum threshold contrast sensitivity of human subjects at various positions across the display FOV. Using a 2D sinusoidal pattern with predefined contrast and spatial frequency as a Gabor target, we determine the contrast sensitivity as the reciprocal of threshold contrast per position. The Gabor target can be rendered at the center, left (for nasal rotation, 𝛼 = -9°), and right (for temporal rotation, 𝛼 = 9°) locations within the display FOV if the 9 location checkbox is selected. At maxmimum, the target can be shown at 9 locations. The tool is set to display the orientation of the target such that the sinusoidal contrast pattern is always circular (or perpendicular to the radial direction) with respect to the target location because it has been shown that the circular orientation of the pattern is suitable to capture the contrast degradation by optical aberration.

In the experiment, the location, dimension, and spatial frequency range of the Gabor target can be adjusted when set up. However, the depth of the target is predefined to be at 150 meters. The target modulation (contrast) can be increased or decreased with a step of one display gray level using a headset controller or a Bluetooth keyboard. Participant can also press B on the keyboard or controller to indicate that they couldn't see the gabor at full contrast in a certain size, standard deviation, frequency, and position.  At the end, all the trial data is saved into json file. This provides an easy way to display scenes on multiple headsets so that users can assess and compare image quality. 

Overall, the tool consists of a user interface built using A-Frame, Three.js, and WebXR for the easy creation of image quality test patterns. It is housed on a website that can be accessed on any WebXR-compatible device with internet access. Results of the tool will be downloaded as a JSON file at the end of the experiement. This feature enables users to easily test and save results.

The tool is available here: [Contrast Sensitivity Dectection Tool](https://khushibhansali.github.io/WebXR-contrast-sensitivity-tool/tool/)

Documentation for the tool is available here: [Contrast Sensitivity Dectection Tool](https://khushibhansali.github.io/WebXR-contrast-sensitivity-tool/tool/)


## Contrast Sensitivity Dectection Tool

![plot](Image/exp1.PNG)

## Download the repositiory following these steps:
1. Click on the green code button between add file button and about section. 
2. Download the repositiory as a zip file or use the command line, navigate to destination folder (cd command), and type ```git clone https://github.com/Khushibhansali/WebXR-tools.git```
3. Open the index.html to modify the contents of the webpage. 
4. Open scripts.js to change any logic from the experiments.

Note: The lib folder is nessecary for Aframe dependencies.
