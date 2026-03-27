### 5 Stages of ethical hacking

**Reconnaissance/Information Gathering:**

The reconnaissance stage involves gathering information about the target system or network. It includes passive information gathering techniques such as searching publicly available information, browsing websites, and examining DNS records. The goal is to collect as much information as possible to understand the target and identify potential entry points.

**Scanning & Enumeration:**

In the scanning stage, the ethical hacker actively probes the target system or network to discover open ports, services, and vulnerabilities. Various tools and techniques are employed, such as port scanning, network mapping, and vulnerability scanning. This stage helps identify potential weaknesses that can be exploited.

**Gaining Access/Exploitation:**

In this stage, the ethical hacker attempts to gain unauthorized access to the target system or network. The focus is on exploiting vulnerabilities discovered during the scanning stage. Techniques such as password cracking, social engineering, and exploiting software vulnerabilities may be employed to gain access to the target system.

**Maintaining Access/Persistence:**

Once access is gained, the ethical hacker aims to maintain access to the compromised system or network. This stage involves bypassing security mechanisms, setting up backdoors or remote access tools, and establishing persistent access. The objective is to mimic the actions of a real attacker and assess the potential impact of a successful compromise.

**Covering Tracks/Clean-up:**

In the final stage, the ethical hacker removes any traces of their activities from the target system or network. This includes deleting logs, modifying or removing files, and restoring the system to its original state. The goal is to ensure that the ethical hacking activity remains undetected, leaving no evidence of the penetration testing activity behind.

It's important to note that ethical hacking should always be performed with proper authorization and within the bounds of the law. Ethical hackers are responsible for following strict ethical guidelines, maintaining confidentiality, and obtaining necessary permissions from the system or network owners before conducting any penetration testing activities.

## 1. Reconnaissance
	- Location information
		- Drone recon
		- Building layout (badge readers, break areas, security, fencing)
	- Job information
		- Employee info
		- Pictures
	- Web & Host Assessment:
		- Target Validation
			- WHOIS, nslookup, dnsrecon
		- Finding subdomains
			- Google Fu, dig, nmap, sublist3r, Bluto, crt.sh, etc.
		- Fingerprinting
			- Nmap
			- Wappalyzer
			- WhatWeb, BuiltWith
			- Netcat
		- Data Breaches
			- HaveIBeenPwned, Breach-Parse, WeLeakInfo
		- 

![Cyber Kill Chain](<images/PNPT Notes/image.png>)