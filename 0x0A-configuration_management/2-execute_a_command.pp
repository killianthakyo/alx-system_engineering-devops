# Create a manifest in puppet that kills a process named killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
