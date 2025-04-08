# Run as sudo
# First, create users.txt containing all the users.

while read USER; do
    mkdir $USER
    cp -r /home/$USER/midterm/ $USER
done < /home/fitzgerald/users.txt
