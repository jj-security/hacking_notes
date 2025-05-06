# Target: <ip-address>

#### Start off with an nmap scan of tcp and udp:

```bash
sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target
```

```bash
sudo nmap -sU $target --defeat-icmp-ratelimit -p- -oN $target.nmap -vvv --min-rate 1000 -T5
```


#### Nmap TCP Results

```

```

#### Nmap UDP Results

```

```

#### Notes

## 22/tcp

## 80/tcp
