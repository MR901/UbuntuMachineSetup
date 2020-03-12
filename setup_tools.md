

## Install Terminator  
[Reference](https://blog.arturofm.com/install-terminator-terminal-emulator-in-ubuntu/)
```
# Step 1 - Add Terminator Repository
sudo add-apt-repository ppa:gnome-terminator

# Step 2 - Update sources.list
sudo apt-get update

# Step 3 - Install Terminator
sudo apt-get install terminator
```

## Setup ZSH
[Reference(source)](https://github.com/ohmyzsh/ohmyzsh)
```
## Step 1 - Install
sudo apt install zsh

## Step 2 - Verify
zsh --version

## Step 3 - Default Shell
chsh -s $(which zsh)

## Restart Computer and Test
echo $SHELL
$SHELL --version
```


## Install GIT  
[Reference(DigitalOcean)](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-18-04-quickstart)
```
# Step 1 — Update Default Packages
sudo apt update

# Step 2 — Install Git
sudo apt install git

# Step 3 — Confirm Successful Installation
git --version

# Step 4 — Set Up Git
## user.name, user.email
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"

## edit these
nano ~/.gitconfig
```
  




