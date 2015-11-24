# Install all the necessary packages on Master

# Install OS level packages
yum install -y tmux
yum install -y pssh
yum install -y python27 python27-devel
yum install -y freetype-devel libpng-devel
wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python27

# Install Python Packages
easy_install-2.7 pip
easy_install py4j
pip2.7 install ipython==2.0.0
pip2.7 install pyzmq==14.6.0
pip2.7 install jinja2==2.7.3
pip2.7 install tornado==4.2
pip2.7 install numpy
pip2.7 install matplotlib
pip2.7 install nltk
