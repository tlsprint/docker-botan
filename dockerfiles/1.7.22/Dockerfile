# This file is automatically generated with Dockerfile.j2 as a template. Do not
# edit by hand, since your changes will be lost!
FROM buildpack-deps AS builder

# Create a shallow clone of the implementation repository in the work directory,
# containing only the code of the specified version/tag.
WORKDIR /botan
RUN git clone --branch 1.7.22 --depth 1 https://github.com/randombit/botan.git .

# Build
# Some versions incorrectly guess the CPU as i686, while the images are build
# on x86_64. This is solved by passing a flag to the configure script.
RUN ./configure.pl --cpu=x86_64
RUN make