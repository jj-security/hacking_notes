
### Target: 10.10.10.245 - Cap
### Special Notes:
N/A

#### Start off with an nmap scan of tcp and udp:
```sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target```

```sudo nmap -sU $target --defeat-icmp-ratelimit -p- -oN $target.nmap -vvv --min-rate 1000 -T5```


#### Nmap TCP Results
```

```

#### Nmap UDP Results
```

```

#### Notes

## 22/tcp

## 80/tcp
found email address: support@dog.htb. going to try and log into it.

![alt text](image.png)