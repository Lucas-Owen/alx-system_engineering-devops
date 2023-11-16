# This manifest increases the limit of open files for holberton user
exec { 'change-os-config-for-holberton-user':
  command => '/bin/sed -i\
    -e \'/holberton.*hard.*nofile/c\holberton hard nofile 50000\'\
    -e \'/holberton.*soft.*nofile/c\holberton soft nofile 50000\'\
    /etc/security/limits.conf'
}
