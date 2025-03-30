# Port Redirection & Tunneling Notes

## 1. **Local Port Forwarding (L-Tunneling)**

Local port forwarding allows forwarding traffic from a local machine to a remote service via SSH.

### **Example:** Forward local port 80 to a remote machine on port 80

```sh
ssh -N -L 80:127.0.0.1:80 student@192.168.149.52 -p 2222
```

**Explanation:**

- `-N`: No remote command execution, only forwarding.
- `-L`: Local forwarding.
- `80:127.0.0.1:80`: Forward local port 80 to the remote machine's port 80.
- `-p 2222`: Use SSH on port 2222.

## 2. **Remote Port Forwarding (R-Tunneling)**

Remote port forwarding allows forwarding traffic from a remote machine to a local service.

### **Example:** Forward remote port 5555 to local port 5555

```sh
ssh -R 5555:127.0.0.1:5555 student@192.168.149.52 -p 2222
```

To catch the shell on the remote machine:

```sh
nc -lvnp 5555
```

**Use case:**

- Useful when bypassing NAT or firewalls by allowing remote systems to access a local service.

## 3. **Dynamic Port Forwarding (SOCKS Proxy)**

This sets up a SOCKS proxy to route traffic through an SSH tunnel.

### **Example:** Start a SOCKS proxy on local port 9050

```sh
ssh -N -D 127.0.0.1:9050 -p 2222 student@192.168.149.52
```

**Explanation:**

- `-D`: Dynamic port forwarding, creating a SOCKS proxy.
- Traffic from applications (like browsers) can be routed through this proxy.

## 4. **Proxychains for Routing Traffic Through a Proxy**

Proxychains allows redirecting traffic through a proxy like TOR or an SSH SOCKS proxy.

### **Example:** Checking the proxychains configuration

```sh
cat /etc/proxychains4.conf
```

### **Example:** Routing a Netcat connection through proxychains

```sh
proxychains nc localhost 34024
```

## 5. **SSHuttle: VPN-Like Network Pivoting**

SSHuttle provides a way to tunnel traffic through an SSH connection, like a VPN.

### **Example:** Route traffic through an edge device to access an internal network

```sh
sshuttle -r student@192.168.149.52 192.168.10.0/24 -p 2222
```

**Use case:**

- Useful when pivoting into an internal network.
- No need for root access on the remote machine.

## 6. **Chaining Tunnels for Complex Scenarios**

Tunneling can be nested for advanced network pivoting.

### **Example:** Double SSH tunnel to reach an internal network

```sh
ssh -L 8888:127.0.0.1:9999 student@192.168.149.52 -p 2222
ssh -L 9999:127.0.0.1:80 admin@10.10.10.5 -p 22
```

This setup forwards port `80` from `10.10.10.5` through `192.168.149.52` to `localhost:8888`.

## 7. **Reverse Shells Using SSH Tunneling**

A reverse shell can be tunneled using SSH for stealth and bypassing firewalls.

### **Example:** Listener on Attacker Machine

```sh
nc -lvnp 4444
```

### **Example:** Reverse Shell Execution on Target

```sh
ssh -R 4444:127.0.0.1:4444 student@192.168.149.52 -p 2222
```

**Use case:**

- The shell connects back through an SSH tunnel, evading firewalls and NAT.

---

These techniques are crucial for pentesting and lateral movement within a network. Let me know if you need more details or practical scenarios!

