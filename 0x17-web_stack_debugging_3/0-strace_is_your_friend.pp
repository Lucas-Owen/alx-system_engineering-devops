# This puppet manifest renames a file

Exec {'rename':
  command => '/usr/bin/mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp'
}
