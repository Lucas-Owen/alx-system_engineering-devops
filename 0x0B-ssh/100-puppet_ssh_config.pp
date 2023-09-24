#!/usr/bin/env bash
# This puppet file configures the client ssh to connect to a server without typing a password
file_line { 'Private Key File':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => 'IdentityFile ~/.ssh/school',
}

file_line { 'Disable Password Authentication':
  path   => '/etc/ssh/ssh_config',
  ensure => 'present',
  line   => 'PasswordAuthentication no',
}
