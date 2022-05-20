# SERVIDOR Samba 4 no Debian 11
# Link Juliano Ramos 
# https://www.youtube.com/watch?v=E_GGg7Brx8Q
# clona git com scripts do vaamonde  https://github.com/vaamonde/samba4-l2.git


# vim /etc/network/interface

# sudo vim /etc/hosts

    127.0.0.1       localhost
    127.0.1.1       servidorSmb.empresa.local           servidorSmb
    192.168.0.100   servidorSmb.empresa.local           servidorSmb

# sudo vim /etc/hostname
    servidorSmb

# vim /etc/resolv.conf
    nameserver 127.0.0.1

# Adicionar repositorio contrib e non-free /etc/apt/source.list
    deb http... main contrib non-free

# Instalação dos pacotes 
    apt install samba smbclient krb5-user dnsutils winbind

# "na instalçao do kerberos informar o dominio" 
####    obs: usando como novo dominio titech.intra
    empresa.local
# "servidor kerberos"
    servidorSmb.empresa.local
# "servidor administrativo kerberos "
    servidorSmb.empresa.local

# mv /etc/samba/smb.conf /etc/samba/smb.conf.bkp

# apos executar o comando abaixo, digitar o dominio, trocar apenas o dns externo, e senha de Adminitrador 

# samba-tool domain provision
    exemplo.com

    
reboot

cp /var/lib/samba/private/krb5.conf /etc/


# sudo systemctl stop smbd nmbd winbind
# sudo systemctl disable smbd nmbd winbind

# systemctl unmask samba-ad-dc.service
# systemctl start samba-ad-dc.service
# systemctl enable samba-ad-dc.service


# "verificar no inicio 'realm' está aparecendo o dominio configurado
    cat /etc/krb5.conf

smbclient -L localhost -U Adminitrator

"""
dig -t srv _ldap.tcp.exemplo.com
dig -t srv _kerberos.tcp.exemplo.com
dig -t a servidor.exemplo.com

vim /usr/share/samba/setup/krb5.conf
    "default_realm = EXEMPLO.COM"

cp /usr/share/samba/setup/krb5.conf /etc/

kinit Adminitrator"""


# Criação dos usuarios
samba-tool user list
samba-tool user create financeiro
#password IFalunos;

# expirar senha com 7 dias
samba-tool user setexpiry financeiro --days=7

# Criação grupos
samba-tool group listmembers "Domain Users"
samba-tool group add financeiro
samba-tool group addmembers financeiro vinicius

# Adicionando unidade organizacional e vinculando usuario
samba-tool group add "nome do grupo" "user"
samba-tool group list
samba-tool group listmembusers "Domain Users" 



# Configurando no Home PROFILES /etc/samba/smb.conf
[profiles]
    comment = Pasta dos Perfis dos Usuários
    path = /arquivos/empresa/usuarios/profiles
    read only = No
    store dos attributes = Yes
    create mask = 0600
    directory mask = 0700
    profile acls = Yes
    csc policy = disable

smbcontroll all reload-config
chmod 1770 /arquivos/empresa/usuarios/profiles
chgrp "Domain Users" /arquivos/empresa/usuarios/profiles


___________________________________________________________________________________
# CLIENTE WINDOWS
# Ativando recurso RSAT no windows cliente
https://www.minitool.com/news/install-rsat-windows-11-10.html

# no windows rsat
Perfil do usuario
\\servidor\profiles\%USERNAME%
H: \\servidor\home\financeiro