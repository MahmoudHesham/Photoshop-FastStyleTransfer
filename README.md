# Photoshop Fast Style Transfer Using Machine Learning :art:
<p align="center"><b>A user-friendly tool to use fast-style-transfer for stylizing images directly inside ؛Photoshop.</b></p>

# Requirements
Based on the fast style transfer repository the machine learning solution requires tensorflow, Pillow, numpy and scipy to be installed on your python environment.

* Therefore there is "**requirements.txt**" that includes all the required libraries and can be installed simply by running this pip command
`pip install -r requirements.txt`
* Make sure to have **python.exe** and **scripts/pip.exe** is already in your system **PATH** environment variable.
* This solution is using **tensorflow-gpu** which requires by default to have a supporting **CUDA GPU** and **cuDNN** installed.
* If you are going to install the same **tensorflow-gpu** version that is mentioned in the requirement.txt file we recommend to use **CUDA v9.0** with the compatible version of **cuDNN**.
* In case of not having a supporting GPU, you can still use tensorflow the cpu version but the image processing time will be longer.

# Installation
![Photoshop Menu](Photoshop_menu.jpg?raw=true)
* After fulfilling the requirements all what you need is just to copy the **Presets** folder inside your photoshop root directory and accept the overwriting.
* Restart your photoshop if you have a running session already.
* Run the script from `File > Scripts > [3Deep] StyleTransfer`.
* Choose your favorite style from the avaliable styles.
* To expand your collections of styles please check the fast-style-transfer repoistory for how to train a new model instructions.

# Links
* cuDNN | https://developer.nvidia.com/cudnn
* CUDA | https://developer.nvidia.com/cuda-toolkit-archive

# Authors
* Photoshop tool (.jsx and .py) [3deep.org](https://www.3deep.org) | author [Mahmoud Hesham](https://github.com/MahmoudHesham).
* Super Resolution Repository ["Fast Style Transfer in TensorFlow"](https://github.com/lengstrom/fast-style-transfer) | author [lengstrom](https://github.com/lengstrom). 

# License
* All the scripts/tools/software-bridges developed by 3Deep are free for academic and non-commercial use only.
# The ML-solution license stated from the fast-style-transfer author:
> Copyright (c) 2016 Logan Engstrom. Contact me for commercial use (or rather any use that is not academic research) (email: engstrom at my university's domain dot edu). Free for research use, as long as proper attribution is given and this copyright notice is retained.