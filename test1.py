vrf definition <VRF name user input>
 rd <as-number>:<loopback0 ip address>
 route-target export <from user input>
 route-target import <from user input>
 !
 address-family ipv4
 exit-address-family

interface <neo4j which interface connected to CE router>
  ip address <ip-address of pe router interface>
  vrf forwarding <VRF name user input> 

router bgp <neo4j as-number on pe side>  
!
 address-family ipv4 vrf <VRF name user input>
  neighbour <on the ce router, the interface ip> remote-as <neo4j as-number on ce side>  
  neighbour <on the ce router, the interface ip> activate  
 exit-address-family 
end