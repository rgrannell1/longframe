
FROM ubuntu:15.10

RUN apt-get update && apt-get install -y \
	libopencv-dev \
	python-opencv \




COPY . /src

WORKDIR /src

CMD ["python", "main.py"]
