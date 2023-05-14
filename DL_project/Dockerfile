FROM ubuntu:22.10
FROM python:3.8.16

# WORKDIR /FALdetector

COPY FALdetector .

RUN apt-get update && apt-get -y install cmake protobuf-compiler
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN python3.8 -m venv faldetector

RUN . faldetector/bin/activate && pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html && \
    pip install -r requirements.txt

COPY entrypoint.sh .
COPY test.py .

RUN chmod +x entrypoint.sh

ENTRYPOINT ./entrypoint.sh

