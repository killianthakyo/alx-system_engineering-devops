#KIll a process using Puppet

exec { 'killmenow':
  command => 'pkill -f killmenow',
  provider => 'shell,
}

