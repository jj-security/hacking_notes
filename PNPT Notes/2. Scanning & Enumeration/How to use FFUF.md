# How to use FFUF

## 1. **What is FFUF?**
FFUF (Fast Web Fuzzer) is a powerful and fast fuzzing tool used for discovering virtual hosts, directories, and subdomains.

## 2. **Finding Virtual Hosts**
Virtual hosts (VHosts) are domain names that resolve to the same IP address but serve different content.

### **Basic VHost Enumeration**
Use FFUF to fuzz for potential virtual hosts on a target server:
```sh
ffuf -w wordlist.txt -H "Host: FUZZ.target.com" -u http://target.com -mc 200
```

### **Explanation:**
- `-w wordlist.txt`: Specifies the wordlist for fuzzing.
- `-H "Host: FUZZ.target.com"`: Injects words into the `Host` header.
- `-u http://target.com`: URL of the target.
- `-mc 200`: Filters results by HTTP status code 200 (OK).

## 3. **Enumerating with IP Address Instead of Domain**
If DNS resolution is not available, target the raw IP address:
```sh
ffuf -w wordlist.txt -H "Host: FUZZ" -u http://192.168.1.100 -mc 200
```

## 4. **Using SecLists for Better Wordlists**
SecLists provides high-quality wordlists for virtual host fuzzing:
```sh
ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.target.com" -u http://target.com -mc 200
```

## 5. **Saving Output for Analysis**
To store results in a JSON or CSV file:
```sh
ffuf -w wordlist.txt -H "Host: FUZZ.target.com" -u http://target.com -mc 200 -o results.json -of json
```
- `-o results.json`: Saves output to a file.
- `-of json`: Specifies JSON format (can also use CSV, HTML, MD, etc.).

## 6. **Advanced Filtering Options**
Filter results based on response size or status codes:
```sh
ffuf -w wordlist.txt -H "Host: FUZZ.target.com" -u http://target.com -mc 200,302 -fs 0
```
- `-mc 200,302`: Show only responses with status 200 or 302.
- `-fs 0`: Filter out responses with size 0.

## 7. **Bypassing WAFs & Rate Limiting**
Some techniques to evade security measures:
- Randomize user agents:
  ```sh
  ffuf -w wordlist.txt -H "Host: FUZZ.target.com" -H "User-Agent: $(shuf -n1 user-agents.txt)" -u http://target.com -mc 200
  ```
- Use delay (`-p 0.5` for 500ms delay between requests):
  ```sh
  ffuf -w wordlist.txt -H "Host: FUZZ.target.com" -u http://target.com -mc 200 -p 0.5
  ```

## 7. **Basic Directory Scan**
```sh
ffuf -u http://TARGET/FUZZ -w /usr/share/wordlists/dirb/common.txt
```

## 8. Add common web extensions (good for files + dirs)
```sh
ffuf -u http://TARGET/FUZZ -w /usr/share/wordlists/dirb/common.txt -e .php,.html,.txt,.bak,.zip,.tar.gz
```

## 9. Filter out noise (most sites return tons of 403/404)
```sh
ffuf -u http://TARGET/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,204,301,302,307,401,403,405,500
```

