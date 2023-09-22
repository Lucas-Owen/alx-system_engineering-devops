# This manifest runs a command that kills a process named killmenow
exec { 'pkill killmenow':
  path => ['/usr/bin', '/usr/sbin', '/bin']
}
