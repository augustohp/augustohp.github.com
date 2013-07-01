class jekyll::dependencies {
  package { "python-pygments":
    ensure => present,
    provider => apt
  }

  package { "build-essential":
    ensure => present,
    provider => apt
  }

  package { "RedCloth":
    ensure => present,
    provider => gem,
    require => [Package['build-essential']]
  }

  package { "jekyll":
    ensure => present,
    provider => gem,
    require => [Package["python-pygments"], Package["RedCloth"]]
  }
}