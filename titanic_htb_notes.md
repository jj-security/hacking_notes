### Target: 10.10.11.51 - EscapeTwo
### Special Notes:


#### Start off with an nmap scan of tcp and udp:
```sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target```

```sudo nmap -sU $target --defeat-icmp-ratelimit -p- -oN $target.nmap -vvv --min-rate 1000 -T5```


#### Nmap TCP Results
```bash
┌──(kali㉿kali)-[~/targets/titanic]
└─$ sudo nmap -sS -sV -Pn -p- -T4 -oN 10.10.11.55_tcp.nmap -vvv --min-rate 1000 10.10.11.55
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-23 18:14 EDT
NSE: Loaded 47 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 18:14
Completed Parallel DNS resolution of 1 host. at 18:14, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 18:14
Scanning 10.10.11.55 [65535 ports]
Discovered open port 80/tcp on 10.10.11.55
Discovered open port 22/tcp on 10.10.11.55
SYN Stealth Scan Timing: About 45.53% done; ETC: 18:15 (0:00:37 remaining)
Increasing send delay for 10.10.11.55 from 0 to 5 due to max_successful_tryno increase to 5
Increasing send delay for 10.10.11.55 from 5 to 10 due to 193 out of 481 dropped probes since last increase.
Completed SYN Stealth Scan at 18:15, 68.96s elapsed (65535 total ports)
Initiating Service scan at 18:15
Scanning 2 services on 10.10.11.55
Completed Service scan at 18:15, 6.30s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.55.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.62s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.66s elapsed
Nmap scan report for 10.10.11.55
Host is up, received user-set (0.12s latency).
Scanned at 2025-03-23 18:14:06 EDT for 77s
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.52
Service Info: Host: titanic.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 76.74 seconds
           Raw packets sent: 68735 (3.024MB) | Rcvd: 68813 (2.755MB)

```

#### Nmap UDP Results
```bash
┌──(kali㉿kali)-[~/targets/escapetwo]
└─$ sudo nmap -sU 10.10.11.55 --defeat-icmp-ratelimit -p- -oN 10.10.11.55_udp.nmap -vvv --min-rate 1000 -T5
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-23 18:14 EDT
Initiating Ping Scan at 18:14
Scanning 10.10.11.55 [4 ports]
Completed Ping Scan at 18:14, 0.11s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:14
Completed Parallel DNS resolution of 1 host. at 18:14, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating UDP Scan at 18:14
Scanning 10.10.11.55 [65535 ports]
UDP Scan Timing: About 23.42% done; ETC: 18:16 (0:01:41 remaining)
UDP Scan Timing: About 46.30% done; ETC: 18:16 (0:01:11 remaining)
UDP Scan Timing: About 69.19% done; ETC: 18:16 (0:00:41 remaining)
Completed UDP Scan at 18:16, 131.40s elapsed (65535 total ports)
Nmap scan report for 10.10.11.55
Host is up, received reset ttl 63 (0.11s latency).
Scanned at 2025-03-23 18:14:14 EDT for 131s
All 65535 scanned ports on 10.10.11.55 are in ignored states.
Not shown: 65401 closed|filtered udp ports (no-response), 134 closed udp ports (port-unreach)

Read data files from: /usr/share/nmap
WARNING: Some ports marked closed|filtered may actually be open. For more accurate results, do not use --defeat-icmp-ratelimit .
Nmap done: 1 IP address (1 host up) scanned in 131.65 seconds
           Raw packets sent: 131204 (6.338MB) | Rcvd: 61437 (2.465MB)

```


╔══════════╣ PATH
╚ https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/index.html#writable-path-abuses
/home/developer/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
