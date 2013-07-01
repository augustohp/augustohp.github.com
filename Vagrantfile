Vagrant.configure("1") do |config|

  config.vm.box = "precise64"
  config.vm.host_name = "blog.localhost"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.forward_port 4000, 8081
  config.vm.share_folder('var-www', '/var/www', './')

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "./.puppet/manifests"
    puppet.manifest_file = "blog.pp"
    puppet.module_path = "./.puppet/modules"
  end

end