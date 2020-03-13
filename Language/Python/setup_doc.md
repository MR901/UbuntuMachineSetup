---  
  
## Install pip3  

```
# Step 1 — Update Default Packages
sudo apt update

# Step 2 — Install pip for python3
sudo apt install python3-pip

# Step 3 — Confirm Successful Installation
pip3 --version

# Step 4 - install packages
pip3 install -r requirements.txt
pip3 install package_name==version

# Step 5 - upgrade a package
pip3 install --upgrade package_name

# Listing Installed Packages
pip3 list

# Uninstalling Packages With Pip
pip3 uninstall package_name
```
  
## Install Virtualenv  
```
# Step 1 - Install Virtualenv
sudo apt-get update
sudo apt-get install python-virtualenv

# Step 2 - Create a Virtual Environment & Install Python 3
virtualenv -p python3 $(pwd)/Documents/VirtualEnv/PersonalEnv
or
virtualenv -p /usr/bin/python3 

# Step 3 - Activate Virtual Env
source virtualenvironment/project_1/bin/activate

# Step 4 - Deactivate Env
deactivate
```
  
---  
  
## Install Jupyter Notebook  
```
# Step 1 - Install Noebook
pip3 install notebook

# Step 2 - Opening
jupyter notebook
or incase zsh
~/.local/bin/jupyter-notebook 
or
run using bash
SHELL := /bin/bash


# Opening a Specific Notebook
jupyter notebook notebook.ipynb

# Start notebook using custom IP or Port
jupyter notebook --port 9999

# Starting a Notebook without opening a browser
jupyter notebook --no-browser

# jupyter Help
jupyter notebook --help
```
  
---  

## Install Ipykernel  
```
# Step 1 - Installing Package  
pip3 install ipykernel

# Step 2 - Adding Virtual env to jupyter   
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"

# checking kernel json
cat /home/user/.local/share/jupyter/kernels/<myenv>/kernel.json

# Check Available kernel
jupyter kernelspec list

# uninstall env
jupyter kernelspec uninstall myenv

```
  
---  

## Install Docker  

## Install MongoDB  

## Install Redis  

#



