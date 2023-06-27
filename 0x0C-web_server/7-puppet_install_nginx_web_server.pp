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

exec { 'configure_nginx':
  command  => "echo 'server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://google.com;
    }
}' > /etc/nginx/sites-available/default",
  path     => '/bin:/usr/bin',
  creates  => '/etc/nginx/sites-available/default',
  require  => Package['nginx'],
  notify   => Service['nginx'],
}

exec {'run':
  command  => 'sudo service nginx restart',
  provider => shell,
}
