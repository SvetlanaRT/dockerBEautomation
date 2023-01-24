#!/bin/bash

echo "creating dirs"
mkdir -p /home/seluser/.pki/nssdb

echo "cret util -N"
certutil -d /home/seluser/.pki/nssdb -N -f empty_pass.txt

echo "cret util -L"
certutil -d sql:/home/seluser/.pki/nssdb -L -f empty_pass.txt

echo "importing pfx"
pk12util -d sql:/home/seluser/.pki/nssdb -i /home/seluser/client.core.coregcp.kaymera.com.pfx -w ca_pass.txt

echo "cret util -L after importing"
certutil -d sql:/home/seluser/.pki/nssdb -L -f empty_pass.txt