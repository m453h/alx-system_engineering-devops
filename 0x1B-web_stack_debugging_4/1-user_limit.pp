# Fixes maximum file limit issue for Holberton user

exec { 'increase-hard-limit':
  command => 'sed -i "/holberton hard/s/5/5024/" /etc/security/limits.conf',
  path    => ['/bin','/usr/bin']
}

-> exec { 'increase-soft-limit':
  command => 'sed -i "/holberton soft/s/4/10048/" /etc/security/limits.conf',
  path    => ['/bin','/usr/bin']
}
