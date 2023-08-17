# Fixes limit issue in Nginx

exec {'fix-nginx-limit':
  command => "sed -i 's/15/4096/g' /etc/default/nginx",
  path    => ['/bin','/usr/bin']
}

-> exec {'restart-nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin','/usr/bin']
}
