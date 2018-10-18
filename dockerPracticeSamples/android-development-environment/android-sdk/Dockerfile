FROM ubuntu:18.04

#disable y/n question prompts
ENV DEBIAN_FRONTEND noninteractive

# install dependencies
RUN apt-get update && \
    apt-get -y install \
      wget \
      unzip \
      openjdk-8-jdk \
      gradle \
      openssh-client \
      sudo \
      vim \
      git \
      patchutils \
      wget

ENV ANDROID_HOME=/opt/android-sdk-linux \
    ANDROID_SDK_VERSION=25.2.3 \
    ANDROID_BUILD_TOOLS_VERSION=27.0.3 \
    ANDROID_BUILD_TOOLS_VERSION_MAJOR=27

#download Android SDK
RUN mkdir -p $ANDROID_HOME /usr/lib/sysusers.d/ && \
    cd $ANDROID_HOME && \
    wget https://dl.google.com/android/repository/tools_r$ANDROID_SDK_VERSION-linux.zip && \
    unzip tools_r$ANDROID_SDK_VERSION-linux.zip

#install Android SDK
RUN echo y | ${ANDROID_HOME}/tools/android update sdk --no-ui --all --filter "platform-tools,build-tools-$ANDROID_BUILD_TOOLS_VERSION,android-$ANDROID_BUILD_TOOLS_VERSION_MAJOR,extra-android-support"

ENV PATH $PATH:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools:$ANDROID_HOME/build-tools/$ANDROID_SDK_VERSION/

