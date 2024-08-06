# Heif2jpg_dockerized

This project provides python script for converting HEIF files to JPG format.

## Features
* Recursively converts HEIF files to JPG.
* Creates a new directory named `ConvertedFiles` to store the converted images.
* Dockerized for ~~easy setup and deployment~~ learning purpose.

## Installation
### Clone the Repository
```
git clone git@github.com:ysh1th/Heif2jpg_dockerized.git
cd Heif2jpg_dockerized
```

### Docker Installation
Ensure that Docker is installed on your machine. If not, you can download and install Docker from [Docker's official website](https://docs.docker.com/get-docker/).

### Building the Docker Image
Build the Docker Image using the provided `Dockerfile`:
```
docker build -t heif2jpg .
```

## Usage
### 1. Prepare Your Files
Place your HEIF files in a directory on your local machine (anywhere)

### 2. Run the Docker Container
Use the following command to run the Docker container, replacing `/path/to/your/heic/files` with the path to your directory containing HEIF files:
```
docker run -it --rm -v /path/to/your/heic/files:/app/heic_files heif2jpg /app/heic_files
```
* `-it`: Runs the container in interactive mode.
* `--rm`: Automatically removes the container after it exits.
* `-v` /path/to/your/heic/files:/app/heic_files: Mounts the local directory to the container.
* `heif2jpg`: The name of the Docker image.
* `/app/heic_files`: The directory inside the container where HEIF files are located.

## Troubleshooting
* Permission Denied: [click here](https://phoenixnap.com/kb/docker-permission-denied)