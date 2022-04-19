from setuptools import setup

setup(name='kp2d',
      version="1.0",
      packages=['kp2d'],
      install_requires=[
          'awscli',
          'boto3',
          'h5py',
          'jupyter',
          'keras',
          'matplotlib',
          'numpy',
          'opencv-python-headless',
          'pandas',
          'path.py',
          'pillow',
          'pycuda',
          'tensorboardx',
          'termcolor',
          'tqdm',
          'wandb',
          'yacs'],
      )
