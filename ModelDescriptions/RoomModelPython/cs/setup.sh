export DEBIAN_FRONTEND=noninteractive

# Backup current sources.list
cp /etc/apt/sources.list /etc/apt/sources.list.backup

# Update sources.list to use archive.debian.org for old releases
sed -i 's/deb.debian.org/archive.debian.org/g' /etc/apt/sources.list
sed -i 's|security.debian.org|archive.debian.org/debian-security|g' /etc/apt/sources.list
sed -i '/buster-updates/d' /etc/apt/sources.list
sed -i 's|archive.debian.org/debian-security/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list

# Update package lists
apt update 
apt install -y gnuplot 

# INSTALL REQUIREMENTS
pip install -r cs/requirements.txt

# # REMOVE EXCESS PYTHON INTERPRETERS 
rm -rf $(find /usr/bin -type f -name python*)
