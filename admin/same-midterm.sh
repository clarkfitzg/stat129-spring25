# Run as sudo
# First, create users.txt containing all the users.

while read USER; do
    md5sum /home/fitzgerald/midterm-res/$USER/midterm/midterm.txt /home/$USER/midterm/midterm.txt
done < /home/fitzgerald/users.txt
