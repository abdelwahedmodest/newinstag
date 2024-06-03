COMMANDS
General dependencies

$ sudo apt-get update
$ sudo apt-get -yr upgrade
$ sudo apt-get -y install unzip python3-pip python3-dev build-essential libssl-dev libffi-dev xvfb
$ sudo pip3 install -upgrade pip
$ export LANGUAGE=en_US.UTF-8
$ export LANG=en_US.UTF-8
$ export LC_ALL=en_US.UTF-8
$ locale-gen en_US.UTF-8
$ sudo dpkg-reconfigure locales
$ pip3 install -- upgrade pip

Chrome-stable

$ cd ~
$ wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ sudo apt-get install -y -f
$ sudo rm google-chrome-stable_current_amd64.deb

Firefox-stable

$ sudo apt-get install firefox

last  command  

pip  install   instapy