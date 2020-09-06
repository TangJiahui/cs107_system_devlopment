for files in $(find -maxdepth 1 -type f)
do
echo ${files:2} $(wc -l < $files)
done