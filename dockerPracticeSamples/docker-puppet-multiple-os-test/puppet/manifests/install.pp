#===========================================================
# make sure that this puppet script is run as sudo
if $id != "root" {
  fail("ERROR: you need to run this puppet script as 'root'. Use 'sudo' tool...")
} 
notice("SUCCESS: You runned tool as root")

#===========================================================
# global puppet commands configurations 
Exec { 
   path      => $path,
   logoutput => on_failure,
} 

$vim_package = $::operatingsystem ? {
  'Fedora' => "vim-enhanced",
  'CentOS' => "vim-enhanced",
  default => "vim",
}

class system_packages_install {
    notice ("Installing vim package...")

    $packages = [
      "$vim_package",
    ]

    package { $packages: 
      ensure  => installed, 
    }

}
include system_packages_install

