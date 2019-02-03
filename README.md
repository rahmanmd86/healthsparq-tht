# Healthsparq
Includes take-home assignment for Healthsparq. This repo contains a script that takes in an `input.csv` file and sorts the contents to an `output.csv` file.
The script runs both locally and via Docker, Dockerfile is also provided.

# Directory Structure

```
hs-sorted/
    |--- data/
           |--- input.csv
           |--- output.csv (after the script runs)
    |--- sorted.py
    |--- Dockerfile
    |--- Readme.md
    |--- .gitignore
```

# Tools used

* python 3.6
* pip
* virtualenv
* numpy
* pandas

# Docker Setup (Via [Runnable](https://runnable.com/docker/))

[Install on Mac](https://runnable.com/docker/install-docker-on-macos)

[Install on Windows](https://runnable.com/docker/install-docker-on-windows-10)

[Install on Linux](https://runnable.com/docker/install-docker-on-linux)

# Running the script in Docker

-- Clone the repo

-- Make sure the Docker app is up and running

## Building the image
* Navigate to `hs-sorted` directory 
* Build Docker image 
    * `docker build -t hs-sorted:latest .`
* Ensure image is created: 
    * `docker image ls`

* Create a container
    * `docker create -ti --name <container-name> hs-sorted bash`
* Copy the output
    * `docker cp <container-name>:/app/data/output.csv ./data/`
* Remove the container
    * `docker rm -fv <container-name>`

# Running the script locally 

-- Clone the repo

-- Navigate to `hs-sorted` directory

-- Run below commands to setup the environment:

```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements
```
-- Specify `input.csv` in `data` directory

-- Run the script
    
    python sorted.py

