Vagrant.configure("2") do |config|

  config.vm.box = "precise64"
  config.vm.hostname = "blog.localhost"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.network :forwarded_port, guest: 4000, host: 8081, auto_correct: true
  config.vm.synced_folder ".", "/var/www"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "./.puppet/manifests"
    puppet.manifest_file = "blog.pp"
    puppet.module_path = "./.puppet/modules"
  end

end