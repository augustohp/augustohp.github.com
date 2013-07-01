class jekyll {
  include jekyll::dependencies

  exec { "jekyll-build":
    command => "jekyll build --trace",
	cwd => "/var/www",
    path => "/opt/vagrant_ruby/bin",
    group => "vagrant",
    logoutput => true,
    require => [Class["jekyll::dependencies"], Package['jekyll']]
  }

  notify { "run-watch":
  	message => "Site built. You should run `cd /var/www && jekyll serve` inside the VM and acess http://127.0.0.1:8081 to see your blog.",
  	subscribe => Exec['jekyll-build'],
  }
}