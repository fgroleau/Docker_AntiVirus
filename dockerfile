FROM python:3.9.0-buster
RUN apt update && apt upgrade -y
RUN mkdir /Scan /ToScan
RUN apt install -y clamav-daemon clamav-freshclam clamav-unofficial-sigs 
RUN freshclam && clamscan
COPY requirement.txt .
RUN pip3 install -r requirement.txt
COPY main.py .
CMD python3 /main.py