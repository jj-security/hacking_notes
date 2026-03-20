### Target: 10.10.10.245 - Cap
### Special Notes:
N/A

#### Start off with an nmap scan of tcp and udp:
`sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target`

`sudo nmap -sU $target --defeat-icmp-ratelimit -p- -oN $target.nmap -vvv --min-rate 1000 -T5`


#### Nmap TCP Results
```
└─# sudo nmap -sS -sV -Pn -p- -T4 -oN backfire_tcp.nmap -vvv --min-rate 1000 10.10.11.49
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-28 02:48 EDT
NSE: Loaded 47 scripts for scanning.
Initiating Parallel DNS resolution of 1 host. at 02:48
Completed Parallel DNS resolution of 1 host. at 02:48, 0.00s elapsed
DNS resolution of 1 IPs took 0.00s. Mode: Async [#: 1, OK: 0, NX: 1, DR: 0, SF: 0, TR: 1, CN: 0]
Initiating SYN Stealth Scan at 02:48
Scanning 10.10.11.49 [65535 ports]
Discovered open port 22/tcp on 10.10.11.49
Discovered open port 443/tcp on 10.10.11.49
SYN Stealth Scan Timing: About 44.97% done; ETC: 02:49 (0:00:38 remaining)
Discovered open port 8000/tcp on 10.10.11.49
Completed SYN Stealth Scan at 02:49, 67.48s elapsed (65535 total ports)
Initiating Service scan at 02:49
Scanning 3 services on 10.10.11.49
Completed Service scan at 02:49, 13.08s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.11.49.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 02:49
Completed NSE at 02:49, 1.55s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 02:49
Completed NSE at 02:49, 2.07s elapsed
Nmap scan report for 10.10.11.49
Host is up, received user-set (0.25s latency).
Scanned at 2025-03-28 02:48:32 EDT for 85s
Not shown: 65530 closed tcp ports (reset)
PORT     STATE    SERVICE  REASON              VERSION
22/tcp   open     ssh      syn-ack ttl 63      OpenSSH 9.2p1 Debian 2+deb12u4 (protocol 2.0)
443/tcp  open     ssl/http syn-ack ttl 63      nginx 1.22.1
5000/tcp filtered upnp     port-unreach ttl 63
7096/tcp filtered unknown  port-unreach ttl 63
8000/tcp open     http     syn-ack ttl 63      nginx 1.22.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

#### Nmap UDP Results
```

```

#### Notes

## 22/tcp

## 8000/tcp

Found a file:

```
Operators {
    user "ilya" {
        Password = "CobaltStr1keSuckz!"
    }

    user "sergej" {
        Password = "1w4nt2sw1tch2h4rdh4tc2"
    }
}

```