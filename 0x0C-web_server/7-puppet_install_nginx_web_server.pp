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

exec {'redirect_page':
  command => 'sudo sed -i "47i rewrite ^/redirect_me https://google.com permanent;" /etc/nginx/sites-available/default',
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
