# https://github.com/thoughtbot/neat
class neat {
  include neat::dependencies

  exec { "bourbon-install":
    command => "bourbon install",
	cwd => "/var/www/res/style",
    path => "/opt/vagrant_ruby/bin",
    group => "vagrant",
    logoutput => true,
    require => [Class["jekyll::dependencies"], Package['bourbon']]
  }

  exec { "neat-install":
    command => "neat install",
	cwd => "/var/www/res/style",
    path => "/opt/vagrant_ruby/bin",
    group => "vagrant",
    logoutput => true,
    require => [Class["jekyll::dependencies"], Package['neat'], Exec['bourbon-install']]
  }

  notify { "run-neat-update":
  	message => "Neat installed. Run `cd /var/www/res/style && neat update` inside the VM to generate CSS.",
  	subscribe => Exec['neat-install'],
  }
}