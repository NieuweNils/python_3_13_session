#! /bin/bash

docker build ../ -f Dockerfile -t cpython:3.13_gil_disabled --build-arg gil=disabled
docker run -it cpython:3.13_gil_disabled python free_threading.py