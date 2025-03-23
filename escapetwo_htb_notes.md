### Target: 10.10.11.51 - EscapeTwo

#### Start off with an nmap scan of tcp and udp:
```sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target```

```sudo nmap -sU $target --defeat-icmp-ratelimit -p- -oN $target.nmap -vvv --min-rate 1000 -T5```


#### Nmap TCP Results
```
└─$ sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-23 12:59 EDT
NSE: Loaded 47 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 12:59
Completed Parallel DNS resolution of 1 host. at 12:59, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 12:59
Scanning 10.10.11.51 [65535 ports]
Discovered open port 139/tcp on 10.10.11.51
Discovered open port 135/tcp on 10.10.11.51
Discovered open port 445/tcp on 10.10.11.51
Discovered open port 53/tcp on 10.10.11.51
Discovered open port 5985/tcp on 10.10.11.51
Discovered open port 389/tcp on 10.10.11.51
SYN Stealth Scan Timing: About 23.61% done; ETC: 13:02 (0:01:40 remaining)
Discovered open port 49810/tcp on 10.10.11.51
Discovered open port 636/tcp on 10.10.11.51
Discovered open port 49722/tcp on 10.10.11.51
Discovered open port 88/tcp on 10.10.11.51
Discovered open port 1433/tcp on 10.10.11.51
Discovered open port 593/tcp on 10.10.11.51
SYN Stealth Scan Timing: About 46.49% done; ETC: 13:02 (0:01:10 remaining)
Discovered open port 464/tcp on 10.10.11.51
Discovered open port 49692/tcp on 10.10.11.51
Discovered open port 47001/tcp on 10.10.11.51
Discovered open port 9389/tcp on 10.10.11.51
Discovered open port 49691/tcp on 10.10.11.51
Discovered open port 49700/tcp on 10.10.11.51
Discovered open port 49665/tcp on 10.10.11.51
Discovered open port 49664/tcp on 10.10.11.51
SYN Stealth Scan Timing: About 69.37% done; ETC: 13:02 (0:00:40 remaining)
Discovered open port 3268/tcp on 10.10.11.51
Discovered open port 3269/tcp on 10.10.11.51
Discovered open port 49667/tcp on 10.10.11.51
Discovered open port 49743/tcp on 10.10.11.51
Discovered open port 49695/tcp on 10.10.11.51
Discovered open port 49668/tcp on 10.10.11.51
Discovered open port 49668/tcp on 10.10.11.51
SYN Stealth Scan Timing: About 63.10% done; ETC: 13:03 (0:01:13 remaining)
SYN Stealth Scan Timing: About 78.35% done; ETC: 13:03 (0:00:43 remaining)
Completed SYN Stealth Scan at 13:03, 195.71s elapsed (65535 total ports)
Initiating Service scan at 13:03
Scanning 26 services on 10.10.11.51
Service scan Timing: About 61.54% done; ETC: 13:04 (0:00:35 remaining)
Completed Service scan at 13:04, 65.03s elapsed (26 services on 1 host)
NSE: Script scanning 10.10.11.51.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 13:04
Completed NSE at 13:04, 4.28s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 13:04
Completed NSE at 13:04, 3.51s elapsed
Nmap scan report for 10.10.11.51
Host is up, received user-set (0.12s latency).
Scanned at 2025-03-23 12:59:58 EDT for 268s
Not shown: 65509 filtered tcp ports (no-response)
PORT      STATE SERVICE       REASON          VERSION
53/tcp    open  domain        syn-ack ttl 127 Simple DNS Plus
88/tcp    open  kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2025-03-23 17:03:23Z)
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack ttl 127
464/tcp   open  kpasswd5?     syn-ack ttl 127
593/tcp   open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ssl/ldap      syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
1433/tcp  open  ms-sql-s      syn-ack ttl 127 Microsoft SQL Server 2019 15.00.2000
3268/tcp  open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
3269/tcp  open  ssl/ldap      syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: sequel.htb0., Site: Default-First-Site-Name)
5985/tcp  open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
9389/tcp  open  mc-nmf        syn-ack ttl 127 .NET Message Framing
47001/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49664/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49668/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49691/tcp open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49692/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49695/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49700/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49722/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49743/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49810/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 268.80 seconds
           Raw packets sent: 196684 (8.654MB) | Rcvd: 157 (6.908KB)

```

#### Nmap UDP Results
```
└─$ sudo nmap -sU 10.10.11.51 --defeat-icmp-ratelimit -p- -oN 10.10.11.51_udp.nmap -vvv --min-rate 1000 -T5
[sudo] password for kali: 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-23 14:36 EDT
Initiating Ping Scan at 14:36
Scanning 10.10.11.51 [4 ports]
Completed Ping Scan at 14:36, 0.12s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:36
Completed Parallel DNS resolution of 1 host. at 14:36, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating UDP Scan at 14:36
Scanning 10.10.11.51 [65535 ports]
UDP Scan Timing: About 23.05% done; ETC: 14:38 (0:01:44 remaining)
UDP Scan Timing: About 45.91% done; ETC: 14:38 (0:01:12 remaining)
Discovered open port 389/udp on 10.10.11.51
Discovered open port 123/udp on 10.10.11.51
UDP Scan Timing: About 68.77% done; ETC: 14:38 (0:00:41 remaining)
Discovered open port 53/udp on 10.10.11.51
Discovered open port 88/udp on 10.10.11.51
Discovered open port 88/udp on 10.10.11.51
UDP Scan Timing: About 61.08% done; ETC: 14:39 (0:01:17 remaining)
UDP Scan Timing: About 76.32% done; ETC: 14:39 (0:00:47 remaining)
Completed UDP Scan at 14:39, 197.40s elapsed (65535 total ports)
Nmap scan report for 10.10.11.51
Host is up, received echo-reply ttl 127 (0.19s latency).
Scanned at 2025-03-23 14:36:22 EDT for 198s
Not shown: 65531 closed|filtered udp ports (no-response)
PORT    STATE SERVICE      REASON
53/udp  open  domain       udp-response ttl 127
88/udp  open  kerberos-sec udp-response ttl 127
123/udp open  ntp          udp-response ttl 127
389/udp open  ldap         udp-response ttl 127

Read data files from: /usr/share/nmap
WARNING: Some ports marked closed|filtered may actually be open. For more accurate results, do not use --defeat-icmp-ratelimit .
Nmap done: 1 IP address (1 host up) scanned in 197.63 seconds
           Raw packets sent: 196969 (9.517MB) | Rcvd: 98 (23.248KB)

```

