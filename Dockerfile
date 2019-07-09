FROM ubuntu:18.04

# Update docker machine with software tools.
RUN apt-get update -q && apt-get install -y -q \
    sudo \
    build-essential \
    g++ \
    libssl-dev \
    curl \
    wget \
    vim \
    git \
    ssh \
    bash-completion

# Do the updates
RUN apt-get update


# Do the clean-up
RUN apt-get clean && apt-get autoclean

# Do the updates
RUN apt-get update

# Python
RUN apt-get install -y --no-install-recommends software-properties-common

RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt-get update -q && apt-get install -y -q \
    python3.6 \
    python-setuptools \
    python3-pip \
    python3.6-dev

# Install tesseract
RUN apt-get install -y tesseract-ocr


COPY requirements.txt ./requirements/requirements.txt

WORKDIR /

# Upgrade pip
RUN python3.6 -m pip install --upgrade pip
# Install python requirements
RUN python3.6 -m pip install -r /requirements/requirements.txt

# Install tesseract geo language
RUN apt-get install -y tesseract-ocr-kat

# For opencv
RUN apt update && apt install -y libsm6 libxext6


ENV DEBIAN_FRONTEND=noninteractive

# For matplotlib
RUN apt-get install -y python3-tk

# Bundle app source
COPY . .

# Show
RUN ls -l

# Set Default Encoding
ENV PYTHONIOENCODING=utf-8



# Set Encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Expose port
EXPOSE 8080

# Run App
RUN chmod +x runner.sh
CMD ./runner.sh
