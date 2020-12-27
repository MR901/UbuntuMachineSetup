#!/bin/bash

curl https://filedn.com/lvAAVme905izr39uF7ae8PH/amleet_lib/cv_src/model.zip --output model.zip
#wget -r --no-parent --reject "index.html*" https://filedn.com/lvAAVme905izr39uF7ae8PH/amleet_lib/cv_src/model.zip -O model.zip


echo 'Files that will be extracted includes the following'
echo

unzip -l model.zip

unzip model.zip -d ..

rm model.zip


