# WebXR-contrast-sensitivity-tool
The Contrast Sensitivity Detection Tool measures the minimum threshold contrast sensitivity of human subjects at various positions across the display field of view (FOV). This is achieved using a 2D sinusoidal pattern with predefined contrast and spatial frequency, known as a Gabor target. The tool calculates contrast sensitivity as the reciprocal of the threshold contrast at each position. The Gabor target can be rendered at the center, left (nasal rotation, 𝛼 = -9°), and right (temporal rotation, 𝛼 = 9°) locations within the display FOV. When the 9-location checkbox is selected, the target can be shown at a maximum of nine locations. The tool ensures that the sinusoidal contrast pattern remains circular (or perpendicular to the radial direction) relative to the target location, as this orientation effectively captures contrast degradation caused by optical aberrations.

In the experiment, the location, size, and spatial frequency of the Gabor target can be adjusted during setup. The depth of the target is fixed at 150 meters. The target's contrast can be incremented or decremented by one display gray level using a headset controller or Bluetooth keyboard. Participants can press 'B' on the keyboard or controller if they cannot see the Gabor target at full contrast in a specific size, standard deviation, frequency, and position. At the end of the experiment, all trial data is saved as a JSON file, allowing for easy display and comparison of image quality across multiple headsets.

The tool features a user interface built with A-Frame, Three.js, and WebXR, facilitating the creation of image quality test patterns. It is accessible via any WebXR-compatible device with internet access, and the results are downloadable as a JSON file at the conclusion of the experiment, making it simple for users to test and save results.

The tool is available here: [Contrast Sensitivity Detection Tool](https://khushibhansali.github.io/WebXR-contrast-sensitivity-tool/tool/)

Documentation for the tool is available here: [Documentation](https://khushibhansali.github.io/WebXR-contrast-sensitivity-tool/documentation/)


## Contrast Sensitivity Dectection Tool

![plot](Image/exp1.PNG)

## Download the repositiory following these steps:
1. Click on the green code button between add file button and about section. 
2. Download the repositiory as a zip file or use the command line, navigate to destination folder (cd command), and type ```git clone https://github.com/Khushibhansali/WebXR-tools.git```
3. Open the index.html to modify the contents of the webpage. 
4. Open scripts.js to change any logic from the experiments.

Note: The lib folder is nessecary for Aframe dependencies.
