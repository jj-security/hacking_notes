### Target: 10.10.11.48

I started off with an nmap scan of all tcp ports. Got too focused on the empty apache default webpage. I ended up running another with all udp ports. Found a service called daloradius, which i am unfamiliar with.

Google searches provided me with default login creds:
administrator
radius


#### Nmap with UDP results
```
└─$ sudo nmap -Pn -sU -sV -p 161 --script="banner,(snmp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "udp_161_snmp-nmap.txt" 10.10.11.48
[sudo] password for kali: 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-03-23 02:26 EDT
Nmap scan report for 10.10.11.48
Host is up (0.11s latency).

PORT    STATE SERVICE VERSION
161/udp open  snmp    SNMPv1 server; net-snmp SNMPv3 server (public)
| snmp-info: 
|   enterprise: net-snmp
|   engineIDFormat: unknown
|   engineIDData: c7ad5c4856d1cf6600000000
|   snmpEngineBoots: 31
|_  snmpEngineTime: 1d12h04m47s
| snmp-sysdescr: Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64
|_  System uptime: 1d12h04m46.94s (12988694 timeticks)
Service Info: Host: UnDerPass.htb is the only daloradius server in the basin!

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.30 seconds
```

#### snmp-check results let me know its a daloradius server
```
─$ sudo snmp-check 10.10.11.48 -c public
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 10.10.11.48:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 10.10.11.48
  Hostname                      : UnDerPass.htb is the only daloradius server in the basin!
  Description                   : Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64
  Contact                       : steve@underpass.htb
  Location                      : Nevada, U.S.A. but not Vegas
  Uptime snmp                   : 1 day, 12:06:34.66
  Uptime system                 : 1 day, 12:06:24.11
  System date                   : 2025-3-23 06:28:16.0
```

```                                                                                                   
┌──(kali㉿kali)-[~]
└─$ snmpwalk -c public -v1 -t 10 10.10.11.48
iso.3.6.1.2.1.1.1.0 = STRING: "Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (13032418) 1 day, 12:12:04.18
iso.3.6.1.2.1.1.4.0 = STRING: "steve@underpass.htb"
iso.3.6.1.2.1.1.5.0 = STRING: "UnDerPass.htb is the only daloradius server in the basin!"
iso.3.6.1.2.1.1.6.0 = STRING: "Nevada, U.S.A. but not Vegas"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (2) 0:00:00.02
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (1) 0:00:00.01
iso.3.6.1.2.1.1.9.1.4.9 = Timeticks: (2) 0:00:00.02
iso.3.6.1.2.1.1.9.1.4.10 = Timeticks: (2) 0:00:00.02
iso.3.6.1.2.1.25.1.1.0 = Timeticks: (13034009) 1 day, 12:12:20.09
iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 E9 03 17 06 22 02 00 2B 00 00 
iso.3.6.1.2.1.25.1.3.0 = INTEGER: 393216
iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/vmlinuz-5.15.0-126-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro net.ifnames=0 biosdevname=0
"
iso.3.6.1.2.1.25.1.5.0 = Gauge32: 0
iso.3.6.1.2.1.25.1.6.0 = Gauge32: 225
iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
End of MIB
```

```
┌──(kali㉿kali)-[~]
└─$ sudo feroxbuster --url http://10.10.11.48:80/daloradius/                                          
[sudo] password for kali: 
                                                                                                                  
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://10.10.11.48:80/daloradius/
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
404      GET        9l       31w      273c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
403      GET        9l       28w      276c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
301      GET        9l       28w      319c http://10.10.11.48/daloradius/app => http://10.10.11.48/daloradius/app/
301      GET        9l       28w      323c http://10.10.11.48/daloradius/library => http://10.10.11.48/daloradius/library/
301      GET        9l       28w      319c http://10.10.11.48/daloradius/doc => http://10.10.11.48/daloradius/doc/
301      GET        9l       28w      323c http://10.10.11.48/daloradius/contrib => http://10.10.11.48/daloradius/contrib/
301      GET        9l       28w      321c http://10.10.11.48/daloradius/setup => http://10.10.11.48/daloradius/setup/
301      GET        9l       28w      325c http://10.10.11.48/daloradius/app/users => http://10.10.11.48/daloradius/app/users/
301      GET        9l       28w      331c http://10.10.11.48/daloradius/contrib/scripts => http://10.10.11.48/daloradius/contrib/scripts/
301      GET        9l       28w      326c http://10.10.11.48/daloradius/contrib/db => http://10.10.11.48/daloradius/contrib/db/
301      GET        9l       28w      327c http://10.10.11.48/daloradius/doc/install => http://10.10.11.48/daloradius/doc/install/
301      GET        9l       28w      326c http://10.10.11.48/daloradius/app/common => http://10.10.11.48/daloradius/app/common/
301      GET        9l       28w      334c http://10.10.11.48/daloradius/app/common/library => http://10.10.11.48/daloradius/app/common/library/
301      GET        9l       28w      343c http://10.10.11.48/daloradius/contrib/scripts/maintenance => http://10.10.11.48/daloradius/contrib/scripts/maintenance/
301      GET        9l       28w      335c http://10.10.11.48/daloradius/app/common/includes => http://10.10.11.48/daloradius/app/common/includes/
301      GET        9l       28w      336c http://10.10.11.48/daloradius/app/common/templates => http://10.10.11.48/daloradius/app/common/templates/
301      GET        9l       28w      333c http://10.10.11.48/daloradius/app/common/static => http://10.10.11.48/daloradius/app/common/static/
301      GET        9l       28w      330c http://10.10.11.48/daloradius/app/users/lang => http://10.10.11.48/daloradius/app/users/lang/
301      GET        9l       28w      333c http://10.10.11.48/daloradius/app/users/library => http://10.10.11.48/daloradius/app/users/library/
301      GET        9l       28w      332c http://10.10.11.48/daloradius/app/users/static => http://10.10.11.48/daloradius/app/users/static/
200      GET      340l     2968w    18011c http://10.10.11.48/daloradius/LICENSE
200      GET      247l     1010w     7814c http://10.10.11.48/daloradius/doc/install/INSTALL
301      GET        9l       28w      339c http://10.10.11.48/daloradius/app/users/notifications => http://10.10.11.48/daloradius/app/users/notifications/
301      GET        9l       28w      329c http://10.10.11.48/daloradius/app/operators => http://10.10.11.48/daloradius/app/operators/
301      GET        9l       28w      337c http://10.10.11.48/daloradius/app/operators/library => http://10.10.11.48/daloradius/app/operators/library/
301      GET        9l       28w      336c http://10.10.11.48/daloradius/app/operators/static => http://10.10.11.48/daloradius/app/operators/static/
301      GET        9l       28w      334c http://10.10.11.48/daloradius/app/operators/lang => http://10.10.11.48/daloradius/app/operators/lang/
301      GET        9l       28w      343c http://10.10.11.48/daloradius/app/operators/notifications => http://10.10.11.48/daloradius/app/operators/notifications/
[############>-------] - 3m    234240/390072  2m      found:26      errors:8297   
[############>-------] - 3m    235890/390072  2m      found:26      errors:8305   
🚨 Caught ctrl+c 🚨 saving scan state to ferox-http_10_10_11_48:80_daloradius_-1742712153.state ...
[############>-------] - 3m    235899/390072  2m      found:26      errors:8305   
[##############>-----] - 3m     21887/30000   129/s   http://10.10.11.48:80/daloradius/ 
[#############>------] - 3m     19530/30000   116/s   http://10.10.11.48/daloradius/ 
[#############>------] - 3m     20579/30000   123/s   http://10.10.11.48/daloradius/app/ 
[#############>------] - 3m     20874/30000   127/s   http://10.10.11.48/daloradius/library/ 
[#############>------] - 3m     19796/30000   120/s   http://10.10.11.48/daloradius/doc/ 
[##############>-----] - 3m     21162/30000   129/s   http://10.10.11.48/daloradius/contrib/ 
[############>-------] - 3m     18655/30000   114/s   http://10.10.11.48/daloradius/contrib/db/ 
[############>-------] - 3m     19170/30000   118/s   http://10.10.11.48/daloradius/setup/ 
[##########>---------] - 3m     16262/30000   101/s   http://10.10.11.48/daloradius/doc/install/ 
[###########>--------] - 3m     17591/30000   109/s   http://10.10.11.48/daloradius/app/common/ 
[##########>---------] - 3m     16157/30000   100/s   http://10.10.11.48/daloradius/app/users/ 
[#############>------] - 3m     19823/30000   123/s   http://10.10.11.48/daloradius/contrib/scripts/ 
[##>-----------------] - 52s     4250/30000   83/s    http://10.10.11.48/daloradius/app/operators/ 
```

```http://10.10.11.48/daloradius/app/operators/``` takes me to a login page.


