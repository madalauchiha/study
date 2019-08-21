#!/usr/bin/env bash

MPORT=192.168.100.99

# progress bar
ssh_host(){
    /usr/bin/expect <<-EOF
    set timeout 3
    spawn ssh worker@$1
    expect {
    "*password:" { send "uisee\r" }
    }
#    expect "*$"
#    interact
    expect eof
EOF
}

ssh_host ${MPORT}