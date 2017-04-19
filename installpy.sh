python3 --version 
export RC=$?
if [ "$RC" = "0" ]; then
	echo 'Python3 is already installed'



else
	echo ‘Download Python 3.5.1…’
	wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
	echo ‘Extracting…’
	xz -d Python-3.5.1.tar.xz
	tar -xvpf Python-3.5.1.tar
	cd Python-3.5.1/
	echo ‘Installing Python 3.5.1…’
	./configure --prefix=/usr/bin
	make
	sudo make altinstall

	sudo ln -s /usr/local/bin/python3.5 /usr/bin/python3
	sudo ln -s /usr/local/bin/pip3.5 /usr/bin/pip3
	sudo ln -s /usr/local/bin/idle3.5 /usr/bin/idle3
    
fi
