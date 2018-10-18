FROM xmementoit/android-sdk

ENV ANDROID_STUDIO_DIR=/opt/android-studio

RUN wget https://dl.google.com/dl/android/studio/ide-zips/3.1.4.0/android-studio-ide-173.4907809-linux.zip -O /tmp/android-studio.zip && \
    unzip /tmp/android-studio.zip -d /opt && rm /tmp/android-studio.zip 

RUN useradd -u 1000 -d /home/android -s /sbin/nologin -m android
VOLUME /home/android

ENV PATH $PATH:${ANDROID_STUDIO_DIR}/bin

#install android devices rules
RUN apt-get -y install systemd udev
COPY android_rules/51-android.rules /etc/udev/rules.d/51-android.rules
COPY android_rules/android-udev.conf /usr/lib/sysusers.d/android-udev.conf

USER android 
WORKDIR /home/android
#ENTRYPOINT studio.sh 
  
