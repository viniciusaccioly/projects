# Samba 4 no Debian 11
# Link Juliano Ramos 
# https://www.youtube.com/watch?v=E_GGg7Brx8Q


vim /etc/network/interface

# Adicionar repositorio non free
deb http://ftp.deian.org/debian/ name-distro main contrib non-free

apt install samba smbclient krb5-user dnsutils winbind

# "na instalçao do kerberos informar o dominio"
exemplo.com
# "servidor kerberos"
localhost
# "servidor administrativo kerberos "
localhost

cp /etc/samba/smb.conf /etc/samba/smb.conf.bkp
rm /etc/samba/smb.conf

cat /etc/krb5.conf
# "verificar no inicio 'realm' está aparecendo o dominio configurado

# apos executar o comando abaixo, digitar o dominio, trocar apenas o dns externo, e senha de Adminitrador
samba-tool domain provision
    exemplo.com
    
reboot

smbclient -L localhost -U Adminitrator

vim /etc/resolv.conf
    nameserver 127.0.0.1

dig -t srv _ldap.tcp.exemplo.com
dig -t srv _kerberos.tcp.exemplo.com
dig -t a servidor.exemplo.com

vim /usr/share/samba/setup/krb5.conf
    "default_realm = EXEMPLO.COM"

cp /usr/share/samba/setup/krb5.conf /etc/

kinit Adminitrator


# Criação dos usuarios
samba-tool user list
samba-tool user create financeiro
#password IFalunos;

# expirar senha com 7 dias
samba-tool user setexpiry financeiro --days=7


# Ativando recurso RSAT no windows 
https://www.minitool.com/news/install-rsat-windows-11-10.html

# Adicionando unidade organizacional e vinculando usuario
samba-tool group add "nome do grupo" "user"
samba-tool group list
samba-tool group listmembusers "Domain Users" 



# Configurando no Home PROFILES /etc/samba/smb.conf
[profiles]
    comment = Pasta dos Perfis dos Usuários
    path = /arquivos/empresa/usuarios/profiles
    read only = No
    store dos attibutes = Yes
    create mask = 0600
    directory mask = 0700
    profiles acl = Yes
    csc policy = disable

smbcontroll all reload-config
chmod 1770 /arquivos/empresa/usuarios/profiles
chgrp "Domain Users" /arquivos/empresa/usuarios/profiles




# no windows rsat
Perfil do usuario
\\servidor\profiles\%USERNAME%
H: \\servidor\home\financeiro