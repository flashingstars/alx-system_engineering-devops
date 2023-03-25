# Puppet script to create ssh configuration file
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'user',
  group   => 'user',
  mode    => '0600',
  content => "Host myserver\n\
              HostName example.com\n\
              IdentityFile ~/.ssh/school\n\
              PasswordAuthentication no\n",
}
