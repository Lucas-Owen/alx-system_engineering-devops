# Web Infrastructure Design;
Most common web infrastructure design is the LAMP stack.  
Linux - OS  
Apache - HTTP Server  
MySQL - RDBMS  
PHP, Perl or Python - Programming Language  
These components are generic and largely interchangeable now.
## IP Address
A unique identifier of a computer in a network. Could be IPv4 or IPv6
### Reserved IP addresses
0.0.0.0 - The default network
255.255.255.255: Broadcast address
127.0.0.1: Loopback address
169.254.0.1-169.254.255.254: Automatic Private IP addressing range assigned automatically when a computer is unsuccessful in getting an address from a DHCP server
### Classes of IPv4 addresses
1.0.0.0 - 127.0.0.0: Class A
128.0.0 - 191.255.0.0: Class B
192.0.0.0 - 223.255.255.0: Class C
224.0.0.0 - 239.255.255.255: Class D
240.0.0.0 - 254.255.255.254: Class E
### Subnet classes of IPv4 addresses
10.0.0.0 - 10.255.255.255: Class A
172.16.0.0 - 172.31.255.255: Class B
192.168.0.0 - 192.168.255.255: Class C
224.0.0.0 - 239.255.255.255: Class D
240.0.0.0 - 254.255.255.254: Class E
## Domain Name System
Basic functionality is to translate domain names to ip addresses
### Searching stages
Browser cache
OS cache
ISP
Root server
TLD server (Top Level Domain) e.g .COM, .NET, .ORG - Coordinated by ICANN
Authoritative name servers

## Record Types
### A (Address) Record
Maps a domain name to the IPv4 address of the computer hosting the domain
```
api.dnsimple.com.	59	IN	A	208.93.64.253
```
### AAAA Record
Maps a domain name to the IPv6 address of the computer hosting the domain
```
example.com.	59	IN	AAAA	3001:0db7:3c5d:0024:0000:0000:1a2f:3c1b
```
### CNAME (Canonical name) Record
Maps one domain name (alias) to another domain name (canonical)
```
NAME                    TYPE   VALUE
--------------------------------------------------
bar.example.com.        CNAME  foo.example.com.
foo.example.com.        A      192.0.2.23
```
### MX (Mail Exchanger) Record
Specifies the mail server responsible for accepting email messages on behalf of a domain name
```
Domain			TTL   Class    Type  Priority      Host
example.com.		1936	IN	MX	10         onemail.example.com.
example.com.		1936	IN	MX	10         twomail.example.com.
```
### TXT (Text) Record
Provides the ability to associate arbitrary text with a host or other name
```
example.com.   IN   TXT   "This domain name is reserved for use in documentation"
```
### NS (Name Server) Record
Delegates a subdomain to a set of name servers. It specifies the authoritative DNS server for a domain.
e.g
```
dnsimple.com. 172800 IN NS ns1.dnsimple.com.
dnsimple.com. 172800 IN NS ns2.dnsimple.com.
dnsimple.com. 172800 IN NS ns3.dnsimple.com.
dnsimple.com. 172800 IN NS ns4.dnsimple.com.
```
### SOA (Start of Authority) Record
Stores admin information about a domain

## Monitoring
Watching computer metrics, recording them, and alerting something is unusual

### Application monitoring
Monitoring running software
### Server monitoring
CPU, memory, disk or network

### Some famous monitoring tools
NewRelic, DataDog, Uptime Robot, Nagios, WaveFront

## Server
Computer hardware or software that provides functionality for other programs or devices (clients).
### Web Server
A software that delivers web pages. Handles HTTP requests from client and sends back a response.
### Application Server
A software that exposes business logic to client applications through various protocols.  
request -> web server -> application server -> web server -> response
## Protocol
A set of established rules that specify how to format, send and receive data to enable communication between computer network endpoints.  
### TCP/IP model
This is a protocol suite used in client-server models. 
#### Application Layer
Provides users with access to network resources. Examples of protocols used here include HTTP, SMTP, FTP
#### Transport Layer
Ensures layers are transmitted correctly. Ensures that link between source and destination is established. Examples of protocols used here include UDP, TCP
#### Internet/Network Layer
Receives and sends packets for the network (IP Addresses). Examples of protocols here - ARP, ICMP
#### Network Access Layer
Comprise of the physical and data link layers (Physical connections and MAC addresses).

### Types of network protocols
#### Communication Protocols
Describe the format how data is exchanged between networks.
E.g UDP, TCP, HTTP
#### Management Protocols
Specify the policies and processes needed to monitor administer and maintain a computer network.
E.g SNMP, ICMP
#### Security Protocols
Ensure that the data in transit over the network connection is kept safe and secure.
E.g SSH, HTTPS

## Port Number
They allow different applications on the same computer to share network resources simultaneously. Open ports have an associated application that listens for new connection requests and closed ports do not.

## Load Balancer
Distributing requests across multiple servers.
### Software Load Balancers
They use scheduling algoriths such as Weighted Scheduling Algorithm, Round Robin Scheduling, Least Connection First Scheduling  
Examples include HAProxy, NGINX, mod_athena, Varnish, Balance, LVS  
### Hardware Load Balancers
These are specialized routers or switches deployed between the servers and the client. They are implemented on Layer 4 (Transport Layer) and Layer 7 (Application Layer) of OSI model.

## SPOF (Single Point of Failure)
A flaw in the design, configuration, or implementation of a system, circuit, or component that poses a potential risk because it could lead to a situation in which just one malfunction or fault causes the whole system to stop working. 

## Firewall
They analyze data packets that request entry to the network and allow, limit, or block network traffic based on preconfigured rules in the hardware or software.
