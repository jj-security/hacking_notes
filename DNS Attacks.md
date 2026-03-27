## DNS Zone Transfer

### What it is?
A zone transfer (DNS AXFR) is a DNS mechanism used to replicate all records from a primary DNS server to a secondary DNS server.
- It uses DNS query type: `AXFR` full transfer or `IXFR` (incremental)
- Normally allowed only between trusted DNS servers.
- Returns the entire DNS zone file
- Can dump:
	- All subdomains (dev.example.com, vpn.example.com)
	- internal hostnames (dc01, jira, test01)
	- IP mappings (A/AAAA records)
	- Mail records (MX)
	- Name servers (NS)
	- TXT records (creds, tokens, SPF configs)
- If allowed publicly, it is free recon.
- Full attack surface mapping

## Perform zone transfer (only works over port 53/tcp)

```
dig axfr @$ip $domain 2>&1 | tee "tcp_53_dns_dig.txt"
```

```
dig @192.0.2.1 example.com axfr
```

- If vulnerable, will return a full zone dump

### What a hacker could gain from this info?

- List of all subdomains, no need to brute force them
- Internal network insight (sometimes RFC1918 IPs)
- Priority targets (mail, VPN, admin portals)
- Better wordlists for further attacks

## DNS Cache Poisoning (DNS Spoofing)
Injecting fake DNS entries into the resolver cache
- To redirect users to an attacker controlled IP
- MITM, phishing

## Subdomain Takeover
A dangling DNS record pointing to an unused service, that an attacker claims

## DNS Tunneling
Data exfil/C2 over DNS queries
Bypass firewalls (DNS usually allowed)

