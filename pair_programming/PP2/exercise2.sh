# i/bin/bash
# coder: Jiahui Tang
# share/listener: N/A
# we only managed to finish e1 during pp2
# I am working on e2 on my own

for files in $(find -maxdepth 1 -type f -perm -u+x)
do
	echo "$files"
done

