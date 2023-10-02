# This puppet manifest configures a new ubuntu nginx server that adds a custom header to the result

file{ '/etc/nginx/nginx.conf':
  ensure => file,
}
file_line { 'append':
  path => '/etc/nginx/nginx.conf',
  line => "add_header X-Served-By \"\$hostname\";",
}

sevice {'nginx':
}
