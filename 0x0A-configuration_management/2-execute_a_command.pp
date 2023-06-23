# Kills proces named killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
