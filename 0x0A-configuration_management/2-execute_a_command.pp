#KIll a process using Puppet

exec { 'killmenow':
  command => 'pkill killmenow',
  provider => 'shell,
}

