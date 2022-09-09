# easy-use-stable-diffusion-
A easy python script to use stable diffusion from stability.ai with docker.



## Requirements

1. Nvidia Docker

   test with Nvidia Docker 2.11.0.

   please refer to https://github.com/NVIDIA/nvidia-docker to install.

2. Python package

   ```bash
   pip install pynvml
   ```

3. GPU Memory

   a 512*512 images need a GPU memory larger than 10G, a RTX3090 can not generate a image larger than $1280\times 640$ pixels.



## Usage

Firstly install Nvidia Docker and pynvml, then it is easy to use!

```bash
git clone git@github.com:riverback/easy-use-stable-diffusion.git
```

```bash
cd ./easyeasy-use-stable-diffusion.git
```

```bash
python3 docker_stable_diffusion.py
```

wait and find your images in the `easy-use-stable-diffusion/images` folder!



## Arguments

**Required**

1. cuda_idx
2. image_info:
   1. prompt
   2. height
   3. width

**Optional**

1. image_info:
   1. guidance_scale
   2. seed
   3. num_images



You can find some awesome works from https://lexica.art/ and try their prompts.

