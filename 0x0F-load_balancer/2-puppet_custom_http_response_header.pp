# Installs Nginx web server using Puppet

package {'nginx':
  ensure => 'present',
}
->exec {'redirect_page':
  command  => 'sudo sed -i "12i add_header X-Served-By \"${hostname}\";" /etc/nginx/sites-available/default',
  provider => shell,
}
->exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
