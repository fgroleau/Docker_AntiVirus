FROM ubuntu
RUN apt update && apt upgrade -y
RUN DEBIAN_FRONTEND="noninteractive" apt -y install tzdata 
RUN mkdir /Scan /ToScan
RUN apt install -y clamav-daemon clamav-freshclam clamav-unofficial-sigs python3 python3-pip
RUN mkdir /var/run/clamav && chown clamav:clamav /var/run/clamav && chmod 750 /var/run/clamav
RUN service clamav-daemon start && service clamav-freshclam restart
RUN freshclam && clamscan
COPY requirement.txt .
RUN pip3 install -r requirement.txt
COPY main.py .
CMD python3 /main.py