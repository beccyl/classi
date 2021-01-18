FROM ubuntu:18.04

LABEL description="Exact and Approximate k-mer Counting System" \
    container="squeakr" \
    about.summary="Exact and Approximate k-mer Counting System" \
    about.home="https://github.com/splatlab/squeakr" \
    software.version="0.7" \
    version="1" \
    about.copyright="" \
    about.license="BSD-3-Clause" \
    about.license_file="https://github.com/splatlab/squeakr/blob/master/LICENSE" \
    extra.binaries="" \
    about.tags="field::biology, field::biology:bioinformatics, implemented-in::c++,:commandline,:text-mode, role::program,:utility"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
    && apt-get install -y \
        bc \
        cmake \
        #git-all \
        g++ \
        libboost-all-dev \
        libbz2-dev \
        libssl-dev \
        wget \
        zlib1g-dev \
    && apt-get clean \
    && apt-get purge \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/splatlab/squeakr.git
#RUN cd squeakr && make squeakr && mv squeakr /usr/local/bin/
#RUN rm -rf squeakr
#RUN groupadd -r myuser && useradd -r -g myuser myuser
#USER myuser
RUN wget https://github.com/splatlab/squeakr/archive/V0.7.tar.gz -O - | tar -xz
RUN cd squeakr-0.7 && make squeakr && mv squeakr /usr/local/bin/
RUN rm -rf squeakr-0.7
COPY lognumslots.sh /usr/local/bin
RUN chmod 755 /usr/local/bin/lognumslots.sh
