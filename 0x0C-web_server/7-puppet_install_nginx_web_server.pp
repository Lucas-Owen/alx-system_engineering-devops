# This manifest sets up a configuration for an ngix server on a linux machine
package {'nginx':
  ensure => installed,
  notify => Exec['setup ufw', 'setup redirect', 'setup 404']
}

exec {'setup 404':
  command     => "/usr/bin/sed -i \'51 a \\\terror_page 404 \\/404.html;\\n\' /etc/nginx/sites-available/default",
  refreshonly => true
}

exec {'setup redirect':
  command     => "/usr/bin/sed -i \'47 a \\\tlocation \\/redirect_me \\{\\n\t\treturn 301 https:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4;\\n\t\\}\\n\' /etc/nginx/sites-available/default",
  refreshonly => true
}

exec {'setup ufw':
  command     => 'ufw allow \'Nginx HTTP\'',
  refreshonly => true
}

file {'/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  notify  => Service['nginx']
}

file {'/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  notify  => Service['nginx']
}

service {'nginx':
  ensure => 'running',
}
