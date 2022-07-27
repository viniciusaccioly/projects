#!/bin/bash

# Pos instalação Fedora
echo -e "fastestmirror=true\ndeltarpm=true\nmax_parallel_downloads=20" | tee -a /etc/dnf/dnf.conf

sudo dnf update

# Adicionando repositorios
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf config-manager --set-enable google-chrome

# Programas de acesso remoto

anydesk
teamviewer

# Programas em geral

sudo dnf install google-chrome-stable vim terminator telegram-desktop obs-studio
vscode

discord



# Virtualização https://fedorabr.org/discussion/414/tutorial-instalando-e-configurando-virtualbox-no-fedora-31-pelo-rpmfusion

sudo dnf install kernel-devel-$(uname -r) akmod-VirtualBox
sudo dnf install VirtualBox.x86_64
sudo akmods
sudo systemctl restart vboxdrv
lsmod  | grep -i vbox



VMware-workstation
