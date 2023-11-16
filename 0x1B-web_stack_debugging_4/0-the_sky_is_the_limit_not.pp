# This manifest fixes the number of open files limits in nginx configuration

exec { 'fix-for-nginx':
  command => '/bin/sed -i "s/15/5000/" /etc/default/nginx ;
    sudo service nginx restart'
}
