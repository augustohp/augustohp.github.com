class neat::dependencies {
  package { "sass":
    ensure => present,
    provider => gem
  }

  package { "bourbon":
    ensure => present,
    provider => gem,
    require => [Package['sass']]
  }

  package { "neat":
    ensure => present,
    provider => gem,
    require => [Package['bourbon']]
  }
}