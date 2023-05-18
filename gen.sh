> image.txt
image_dirs=$(find / -name "*.jpg")
for image in $image_dirs
do
  echo $image >> image.txt
done