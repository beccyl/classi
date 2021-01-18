FROM ubuntu:18.04

LABEL description="ntCard: a streaming algorithm for cardinality estimation in genomics data" \
    container="ntcard" \
    maintainer="Rebecca Evans <rebecca.louise.evans@gmail.com>" \
    about.summary="ntCard: a streaming algorithm for cardinality estimation in genomics data" \
    about.home="https://www.bcgsc.ca/resources/software/ntcard" \
    software.version="1.2.2" \
    version="1" \
    about.copyright="" \
    about.license="MIT License" \
    about.license_file="https://github.com/bcgsc/ntCard/blob/master/LICENSE" \
    extra.binaries="" \
    about.tags=""

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y \
    && apt-get install -y \
        autoconf \
        autotools-dev \
        binutils-common \
        git-all \
        g++ \
        libbz2-dev \
        libcurl4-openssl-dev \
        libcrypto++-dev \
        liblzma-dev \
        libncurses5-dev \
        libssl-dev \
        libz-dev \
        make \
        wget \
        zlib1g-dev \
    && apt-get clean \
    && apt-get purge \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && rm -rf /var/lib/apt/lists/*


ENV SAMTOOLS_VERSION 1.9

# Set Standard settings
ENV PATH /usr/bin:/bin:/usr/local/bin

# install samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && tar -xjf samtools-${SAMTOOLS_VERSION}.tar.bz2 \
    && rm -rf samtools-${SAMTOOLS_VERSION}.tar.bz2  \
    && cd samtools-${SAMTOOLS_VERSION}/ \
    && ./configure && make && make install

ENV PATH "/usr/local/samtools-${SAMTOOLS_VERSION}/:${PATH}"

# install htslib
RUN wget https://github.com/samtools/htslib/releases/download/${SAMTOOLS_VERSION}/htslib-${SAMTOOLS_VERSION}.tar.bz2 \
    && tar -xjf htslib-${SAMTOOLS_VERSION}.tar.bz2 \
    && rm -rf htslib-${SAMTOOLS_VERSION}.tar.bz2  \
    && cd htslib-${SAMTOOLS_VERSION}/ \
    && ./configure && make && make install

ENV PATH "/usr/local/htslib-${SAMTOOLS_VERSION}/:${PATH}"

# link libraries
RUN /sbin/ldconfig

#RUN git clone https://github.com/bcgsc/ntCard.git
RUN wget https://github.com/bcgsc/ntCard/archive/1.2.2.tar.gz -O - | tar -xz
RUN ls
RUN cd ntCard-1.2.2 && ./autogen.sh && ./configure CFLAGS='-g -O3' CXXFLAGS='-g -O3' && make && make install
