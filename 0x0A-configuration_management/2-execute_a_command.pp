#Puppet manifest to kill a process named killmenow

exec {'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
