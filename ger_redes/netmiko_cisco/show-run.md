R1#sh run
Building configuration...
  
Current configuration : 4012 bytes
!
! Last configuration change at 23:11:28 UTC Sun May 22 2022 by cisco
!
version 15.6
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname R1
!
boot-start-marker
boot-end-marker
!
!
!
no aaa new-model
ethernet lmi ce
!
!
!
mmi polling-interval 60
no mmi auto-configure
no mmi pvc
mmi snmp-timeout 180
!         
!         
!         
!         
!         
!         
!         
!         
ip dhcp excluded-address 192.168.122.100 192.168.122.110
!         
ip dhcp pool LAN
 network 192.168.122.0 255.255.255.0
 default-router 192.168.122.100 
 domain-name example.netacad.com
!         
!         
!         
no ip domain lookup
ip domain name example.netacad.com
ip cef    
no ipv6 cef
!         
multilink bundle-name authenticated
!         
!         
!         
!         
username cisco privilege 15 password 0 cisco123!
!         
redundancy
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
!         
interface Loopback1
 description [Vinicius Accioly]'s loopback
 ip address 10.1.1.1 255.255.255.0
!         
interface Loopback2
 description [Vinicius Accioly]'s loopback
 no ip address
!         
interface Loopback10
 description [Vinicius Accioly]'s loopback
 ip address 10.10.1.1 255.255.255.0
!         
interface Loopback12
 description [Vinicius Accioly]'s loopback
 ip address 10.12.1.1 255.255.255.0
!         
interface Loopback14
 description [Vinicius Accioly]'s loopback
 ip address 10.14.1.1 255.255.255.0
!         
interface Loopback16
 description [Vinicius Accioly]'s loopback
 ip address 10.16.1.1 255.255.255.0
!         
interface GigabitEthernet0/0
 description Link to PC
 ip address 192.168.122.100 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!         
interface GigabitEthernet0/1
 no ip address
 shutdown 
 duplex auto
 speed auto
 media-type rj45
!         
interface GigabitEthernet0/2
 no ip address
 shutdown 
 duplex auto
 speed auto
 media-type rj45
!         
interface GigabitEthernet0/3
 no ip address
 shutdown 
 duplex auto
 speed auto
 media-type rj45
!         
ip forward-protocol nd
!         
!         
no ip http server
no ip http secure-server
!         
!         
!         
!         
control-plane
!         
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!         
line con 0
 exec-timeout 0 0
 logging synchronous
line aux 0
line vty 0 4
 exec-timeout 0 0
 logging synchronous
 login local
 transport input ssh
line vty 5 15
 exec-timeout 0 0
 logging synchronous
 login local
 transport input ssh
!         
no scheduler allocate
!         
end       
          
