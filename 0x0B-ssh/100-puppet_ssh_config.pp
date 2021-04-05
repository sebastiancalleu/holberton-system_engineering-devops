# puppet script to modify the configuration file.
# modify password authentication and identityfile.

file_line { 'indentityfile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^IdentityFile',
  line   => 'IdentityFile ~/.ssh/holberton',
  }

file_line { 'passwordauthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => '^PasswordAuthentication',
  line   => 'PasswordAuthentication no',
  }