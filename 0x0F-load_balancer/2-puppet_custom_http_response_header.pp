# Installs Nginx web server using Puppet

package {'nginx':
  ensure => 'present',
}

exec {'install_nginx_web_server':
  command  => 'apt-get update ; apt-get -y install nginx',
  provider => shell,
}

exec { 'ufw-allow-http':
  command => '/usr/sbin/ufw allow "nginx http"',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Package['nginx'],
}

exec { 'ufw-reload':
  command => '/usr/sbin/ufw reload',
  path    => '/usr/bin:/usr/sbin:/bin',
  require => Exec['ufw-allow-http'],
}

file { '/var/www/html':
  ensure => 'directory',
  mode   => '0755',
  recurse => true,
}

exec {'set_hello_world_page':
  command  => 'echo "Hello World!" | tee /var/www/html/index.html',
  provider => shell,
}

exec {'set_404_page':
  command  => 'echo "Ceci n\'est pas une page" | tee /var/www/html/404.html',
  provider => shell,
}

$my_host = $facts['networking']['hostname']

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      root /var/www/html;
      index index.html index.htm index.nginx-debian.html;

      server_name _;
      
      add_header X-Served-By ${my_host};

      location / {
        try_files \$uri \$uri/ =404;
      }

      location /redirect_me {
        return 301 https://google.com;
      }

      error_page 404 /404.html;
      location  /404.html {
        internal;
      }
    }
  ",
}

exec {'run':
  command  => 'service nginx restart',
  provider => shell,
}
