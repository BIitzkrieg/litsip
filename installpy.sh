#!/usr/bin/bash

python3 --version 
export RC=$?
if [ "$RC" = "0" ]; then
	echo 'Python3 is already installed'



else
	echo ‘Downloading Python 3.5.3…
	wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tar.xz
	echo ‘Extracting…’
	xz -d Python-3.5.3.tar.xz
	tar -xvpf Python-3.5.3.tar
	cd Python-3.5.3/
	echo ‘Installing Python 3.5.3…’
	./configure --prefix=/usr/local
	make
	sudo make altinstall

	sudo ln -s /usr/local/bin/python3.5 /usr/bin/python3
	sudo ln -s /usr/local/bin/pip3.5 /usr/bin/pip3
	sudo ln -s /usr/local/bin/idle3.5 /usr/bin/idle3
    
fi
