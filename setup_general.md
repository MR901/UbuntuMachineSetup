

Setup 
htop
opencv - source



---  

## Install Git  
[Reference](https://linuxize.com/post/how-to-install-git-on-ubuntu-18-04/)
```
# Step 1 - Updating the package index
sudo apt update

# Step 2 - Install
sudo apt install git

# Step 3 - Check
git --version

# Step 4 - Configuration
git config --global user.name "Your Name"
git config --global user.email "youremail@yourdomain.com"
#nano ~/.gitconfig

# Step 5 - Check 
git config --list

```

---  

## Install Terminator  
[Reference](https://blog.arturofm.com/install-terminator-terminal-emulator-in-ubuntu/)
```
# Step 1 - Add Terminator Repository
sudo add-apt-repository ppa:gnome-terminator

# Step 2 - Update sources.list
sudo apt-get update

# Step 3 - Install Terminator
sudo apt-get install terminator

# Step 4 - customize the layouts

```

---  

## Setup ZSH
[Reference(source)](https://github.com/ohmyzsh/ohmyzsh)
```
## Step 1 - Install
sudo apt install zsh

## Step 2 - Verify
zsh --version

## Step 3 - Default Shell
chsh -s $(which zsh)

## Step 4 - Restart Computer and Test
echo $SHELL
$SHELL --version
```



---  

## Install Nano
[Reference](https://www.hostinger.in/tutorials/how-to-install-and-use-nano-text-editor)
```
# Step 1 - Check If Present or not
nano --version

# Step 2 - Install
sudo apt-get install nano

# Step 3 - Opening and Closing File
nano filename
```

Configure Nano Editor
[Reference](https://www.agnosticdev.com/content/configure-nano-command-line-development)
```
# Step 1 - Open up the global configuration file for nano, with nano ;-)
sudo nano /etc/nanorc

# Enable Mouse Control
set mouse

# Don't wrap text at all.
set nowrap

# Use smooth scrolling as the default.
set smooth

# See linenumbers
set linenumbers

# configure a color for comments
syntax "comments" ".*"
color blue "^#.*"

```
  
To enable text highlighting, make sure the following include statements are not commented out
```
## Nanorc files
include "/usr/share/nano/nanorc.nanorc"
 
## C/C++
include "/usr/share/nano/c.nanorc"
 
## Makefiles
include "/usr/share/nano/makefile.nanorc"
 
## Cascading Style Sheets
include "/usr/share/nano/css.nanorc"
 
## Debian files
include "/usr/share/nano/debian.nanorc"
 
## Gentoo files
include "/usr/share/nano/gentoo.nanorc"
 
## HTML
include "/usr/share/nano/html.nanorc"
 
## PHP
include "/usr/share/nano/php.nanorc"
 
## TCL
include "/usr/share/nano/tcl.nanorc"
 
## TeX
include "/usr/share/nano/tex.nanorc"
 
## Quoted emails (under e.g. mutt)
# include "/usr/share/nano/mutt.nanorc"
 
## Patch files
include "/usr/share/nano/patch.nanorc"
 
## Manpages
include "/usr/share/nano/man.nanorc"
 
## Groff
include "/usr/share/nano/groff.nanorc"
 
## Perl
include "/usr/share/nano/perl.nanorc"
 
## Python
include "/usr/share/nano/python.nanorc"
 
## Ruby
include "/usr/share/nano/ruby.nanorc"
 
## Java
include "/usr/share/nano/java.nanorc"
 
## Fortran
include "/usr/share/nano/fortran.nanorc"
 
## Objective-C
include "/usr/share/nano/objc.nanorc"
 
## OCaml
include "/usr/share/nano/ocaml.nanorc"
 
## AWK
include "/usr/share/nano/awk.nanorc"
 
## Assembler
include "/usr/share/nano/asm.nanorc"
 
## Bourne shell scripts
include "/usr/share/nano/sh.nanorc"
 
## POV-Ray
include "/usr/share/nano/pov.nanorc"
 
## XML-type files
include "/usr/share/nano/xml.nanorc"
```




---  
  

---  



