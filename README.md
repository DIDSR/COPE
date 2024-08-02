# WebXR-contrast-sensitivity-tool
The contrast sensitivity tool evaluates the monocular and/or binocular contrast perception on head-mounted display (HMD). Contrast sensitivity response (CSR), as the reciprocol of the threshold (minimum) contrast of the human participant, is measured at various spatial frequencies. This is achieved using a 2D sinusoidal pattern with predefined contrast and spatial frequency, known as a Gabor target. The Gabor target can be rendered at a single or multiple locations across the display field of view (FOV). The tool ensures that the sinusoidal contrast pattern remains circular (or perpendicular to the radial direction) relative to the target location, as this orientation effectively captures contrast degradation caused by optical aberrations.

In the experiment, the location, size, spatial frequency range, and background noise of the Gabor target can be adjusted during initial setup. The depth of the target is fixed at a long distance of 150 m. During the perceptual experiments, the target's contrast can be incremented or decremented by adjusting the display gray level using a headset controller or Bluetooth keyboard until reaching the threshold contrast of each trial. At the end of the experiment, all trial data is saved as a JSON file. Statistical analysis of the results measured on mulitple human participants is applied to obtain the CSR of users within a group (e.g., similar interpuillary distance settings, age, or visual acuity etc).

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
