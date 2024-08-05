#! /bin/bash

docker build . -t cpython:3.13_gil_enabled --build-arg gil=enabled
docker run -it cpython:3.13_gil_enabled python free_threading.py
