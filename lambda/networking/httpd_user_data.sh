#!/bin/bash

yum update -y
yum install -y httpd
systemctl start httpd
echo $(hostname) > /var/www/html/index.html
