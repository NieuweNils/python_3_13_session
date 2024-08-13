# this needs to be set to either enabled or disabled
ARG gil

FROM ubuntu:24.04 AS base

# fetch ubuntu sources
RUN sed -i 's/Types: deb/Types: deb deb-src/g' /etc/apt/sources.list.d/ubuntu.sources
RUN apt update -y
RUN apt upgrade -y

# get minimal requirements for python build
RUN apt-get build-dep python3 -y
RUN apt install pkg-config -y

# get requirements for fully functional python
RUN apt install build-essential -y     \
    && apt install gdb -y     \
    && apt install libbz2-dev -y     \
    && apt install libffi-dev -y     \
    && apt install libgdbm-dev -y     \
    && apt install libgdbm-compat-dev -y     \
    && apt install liblzma-dev -y     \
    && apt install libncurses5-dev -y     \
    && apt install libreadline6-dev -y     \
    && apt install libsqlite3-dev -y     \
    && apt install libssl-dev -y     \
    && apt install lzma -y     \
    && apt install lzma-dev -y     \
    && apt install tk-dev -y     \
    && apt install uuid-dev -y     \
    && apt install zlib1g-dev -y

# sudo is nice
RUN apt install sudo -y

# get CPython
RUN apt install git -y
RUN git clone https://github.com/python/cpython.git
WORKDIR /cpython
RUN git checkout 3.13

FROM base AS python_3_13_gil_enabled
# build & install python with GIL enabled
RUN ./configure
RUN make
RUN make install

FROM base AS python_3_13_gil_disabled
# build & install python with GIL disabled
RUN ./configure --disable-gil
RUN make
RUN make install

FROM python_3_13_gil_${gil} AS final
# make python3 our default python
RUN ln -s $(which python3) /usr/bin/python

# add demo code
COPY data/ data/
COPY 9_free_threading.py free_threading.py
