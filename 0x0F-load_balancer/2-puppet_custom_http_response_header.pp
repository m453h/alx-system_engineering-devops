# Installs Nginx web server using Puppet
$my_host = $facts['networking']['hostname']
package {'nginx':
  ensure => 'present',
}
->exec {'redirect_page':
  command  => "sudo sed -i \"12i add_header X-Served-By ${my_host};\" /etc/nginx/nginx.conf",
  provider => shell,
}
->exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
