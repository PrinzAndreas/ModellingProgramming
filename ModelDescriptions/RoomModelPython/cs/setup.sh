apt update 
apt install -y python3.6 python3.6-dev python3-pip gnuplot 
update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1


# INSTALL REQUIREMENTS
pip install -r cs/requirements.txt

# # REMOVE EXCESS PYTHON INTERPRETERS 
# rm -rf $(find /usr/bin -type f -name python*)
