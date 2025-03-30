## Log into git on machine
git config --global user.name "Julian Johnson"

git config --global user.email "julian.johnson.10@outlook.com"

## Perform zone transfer (only works over port 53/tcp)
dig axfr @$ip $domain 2>&1 | tee "tcp_53_dns_dig.txt"

dig @192.0.2.1 example.com axfr