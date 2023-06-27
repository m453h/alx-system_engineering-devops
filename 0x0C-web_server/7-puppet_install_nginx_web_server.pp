# Installs Nginx web server using Puppet

package {'nginx':
  ensure => 'present',
}

exec {'install_nginx_web_server':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'set_hello_world_page':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}