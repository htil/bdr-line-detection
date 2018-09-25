# Brain-Drone Race Line Detection

The Brain-Drone Race is a competition featuring users' cognitive ability and mental endurance. During this event competitors are required to out-focus opponents in a drone drag race influenced by electrical signals emitted from the brain.

This python class is designed to facilitate the detection of the line which the drones will follow. It allows for the analysis of an image, returning an error to represent the drone's deviation from the line. This system uses methodologies such as Gaussian Blur, Color-Based Filtering, Canny Edge Detection, and Hough Line Transform.

This BDR Line Detection class is developed by the Human Technology Interaction Lab at the University of Alabama.

### Methodology
The following image will be used as a sample test image to illustrate the workflow of the algorithm.

<img src="https://github.com/htil/bdr-line-detection/blob/master/images/straight_center.jpg" width="200">

**1. Gaussian Blur**

Since edge detection results are easily affected by image noise, it is essential to filter out image noise to prevent false edge detection. To smooth the image, a Gaussian filter is applied to the image, which slightly smooths the image to reduce the effects of obvious noise on the edge detector.

<img src="https://github.com/htil/bdr-line-detection/blob/master/images/sample_workflow/blur.jpg" width="200">

**2. HLS Conversion**

The line for the Brain-Drone Race is red. In order to isolate this line, it is necessary to choose the most suitable color space that clearly highlights the line. This allows the image to retain as much of the red line as possible while blacking out other noise in the image.

HSL is an alternative color space representation to the RGB color space. Based on testing of various color spaces, the HSL representation produced the clearest red line of all color spaces. 

<img src="https://github.com/htil/bdr-line-detection/blob/master/images/sample_workflow/hls.jpg" width="200">

**3. Color-Based Filtering**

Once the image has been converted to HSL, a mask is then applied to the image that filters based on a range of HSL values. The values for this mask were selected heuristically based on the general HSL range of red. When this mask is applied to the blurred image, the result is an image that consists of the isolated red line.

<img src="https://github.com/htil/bdr-line-detection/blob/master/images/sample_workflow/mask.jpg" width="200">

**4. Canny Edge Detection**

The Canny Edge Detection algorithm detects a wide range of edges in images by measuring the intensity gradients of each pixel. Following this process, an image is produced in which each side of the red line is clearly marked as an edge.

<img src="https://github.com/htil/bdr-line-detection/blob/master/images/sample_workflow/edges.jpg" width="200">

**5. Hough Line Transform**

The Hough Transform is a technique which can be used to isolate features of a particular shape within an image. It is used here to detect the edges of the red line in the image. These lines can then be visualized by overlaying them on the original image.

<img src="https://github.com/htil/bdr-line-detection/blob/master/images/sample_workflow/result.jpg" width="200">

**6. Error Calculation**

//TODO: add description
