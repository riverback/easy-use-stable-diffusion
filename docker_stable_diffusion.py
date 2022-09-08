"""
Enjoy Stable Diffusion from stability.ai here!

Args:
    Required:
        cuda_idx
        image info
            --prompt
            --height
            --width
    Optional:
        image info
            --guidance_scale
            --seed
            --num_images

You can find some awesome works from https://lexica.art/ and try their prompts.
"""

import os
import pynvml as nv
from getpass import getuser

### set gpu idx
cuda_idx = 6


### set image info
"""
Args:
    prompt: str, A description of required images
    height: int, height must be divided by 8
    width: int, width must be divided by 8
    guidance_scale: int, higher guidance_scale may lead to more closely matched images, but at the expense of image quality 
    seed: int
    num_images: int, generate `num_images` images for the same prompt
"""
prompt = "symmetry!! lord of the rings the shire scenery landscape, highly detailed, perfect lighting, perfect composition, 4 k, artgerm, derek zabrocki, greg rutkowski "
height = 1024
width = 512
guidance_scale = 7
seed = 3338472344
num_images = 5
img_size = height * width # img_size should be samller than 1280*640 pixles if you are using RTX3090


### check gpu status
GPU_MEMORY_512x512 = 10000 # M

nv.nvmlInit()
handle = nv.nvmlDeviceGetHandleByIndex(cuda_idx)
info = nv.nvmlDeviceGetMemoryInfo(handle)
gpu_total = info.total / 1024**2
gpu_free = info.free / 1024**2
gpu_used = info.used / 1024**2


if img_size / 512**2 * GPU_MEMORY_512x512 > gpu_free or img_size > 1208*640:
    print("gpu memory total: {:d}M".format(int(gpu_total)))
    print("gpu memory free: {:d}M".format(int(gpu_free)))
    print("gpu memory used: {:d}M".format(int(gpu_used)))
    raise ValueError("the free gpu memory cannot handle the required image size")



### run stable-diffusion docker application
image_name = 'zhuangpku/sd:latest'
container_name = '{}-stable_diffusion'.format(getuser())
pwd = os.getcwd()
image_folder = os.path.join(pwd, 'images')
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

command_line = f'docker run -ti --gpus "device={cuda_idx}" \
-v {image_folder}:/mydir/images \
--name {container_name} {image_name} \
python3 /mydir/generate.py \
--prompt "{prompt}" \
--height {height} \
--width {width} \
--guidance_scale {guidance_scale} \
--seed {seed} \
--num_images {num_images} '

print(command_line)

os.system(command_line)
os.system(f"docker rm {container_name}")
