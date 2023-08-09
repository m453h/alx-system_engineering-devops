# This puppet script fixes the bug for the web stack debugging #3 task
# It simply replaces phpp with php in the wp-settings.php file

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
