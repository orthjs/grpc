# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM grpcweb/prereqs

ARG MAKEFLAGS=-j8

RUN apt-get -qq update && apt-get -qq install -y \
  autoconf \
  automake \
  build-essential \
  curl \
  git \
  libtool \
  libssl-dev \
  make \
  zip

WORKDIR /github/grpc-web

RUN cd ./third_party/protobuf && \
  ./autogen.sh && \
  ./configure && \
  make && \
  make install && \
  ldconfig

RUN cd ./javascript/net/grpc/web/generator && \
  make protoc-gen-grpc-web
