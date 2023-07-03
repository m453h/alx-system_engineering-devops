# Installs Nginx web server using Puppet

package {'nginx':
  ensure => 'present',
}

exec {'allow_nginx_through_firewall':
  command  => 'ufw allow \'nginx http\' ; ufw reload',
  provider => shell,
}

exec {'set_var_www_html_permissions':
  command  => 'chmod 755 -R /var/www/html',
  provider => shell,
}

exec {'set_hello_world_page':
  command  => 'echo "Hello World!" | tee /var/www/html/index.html',
  provider => shell,
}

exec {'set_404_page':
  command  => 'echo "Ceci n\'est pas une page" | tee /var/www/html/404.html',
  provider => shell,
}

exec {'start_nginx':
  command  => 'service nginx start',
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
