This image scan every file put in the ToScan folder and if the file is secure it will move it to the Scanned folder

You can use the dockerhub version with :

docker pull felixg9/antivirus

For the image to work you need to use like this :

docker run -d --restart always --name antivirus \
-v <Path to the file TO scan folder> :/ToScan \
-v <Path to the file that where scan and safe>:/Scanned \
felixg9/antivirus