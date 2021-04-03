# Resource to execute a command:
exec { 'killer':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}