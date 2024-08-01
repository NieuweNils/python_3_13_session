#! /bin/bash

docker build . -t cpython:3.13_gil_disabled --build-arg gil=gil_disabled
docker run -it cpython:3.13_gil_disabled bash
