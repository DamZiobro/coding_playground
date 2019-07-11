

$user="damian"
$home="/home/$user"
$source_dir="$home/projects/gstreamerCSharp"
$install_prefix="/usr"

#===========================================================
# make sure that this puppet script is run as sudo
if $id != "root" {
  fail("ERROR: you need to run this puppet script as 'root'. Use 'sudo' tool...")
}

#===========================================================
# template class for installation from git repository
define install_from_source ($package_name, $url, $target="/usr/src/$package_name", $build_command = "make -j`nproc` && sudo make -j`nproc` install", $revision = master, $provider = "git", $unless_cmd = "ls /tmp/XXXXXX &> /dev/null", $user = $user){ 

  notice ("Installing $package_name")

  vcsrepo { $target:
    ensure   => present, 
    provider => $provider, 
    source   => $url,
    revision => $revision,
    user     => $user,
  }

  if $build_command != "" {
    exec { "make_$package_name":
      user    => $user,
      path    => [ $path, $target ],
      cwd     => $target,
      command => $build_command,
      timeout => 1000,
      unless  => $unless_cmd,
      logoutput => true,
      require => [ 
          Vcsrepo["$target"], 
          Package['make'], 
      ]
    }
  }
}

#===========================================================
# install required packages
class system_packages_install {
    notice ("Installing system repository packages...")
    $packages = [ 
		  'make', 
    ]

    package { $packages: 
         ensure  => installed, 
    }
}

#===========================================================
# install gtk_sharp from tarball 
class gtk_sharp_install_from_source {
  notice ("Installing gtk_sharp from sources")
  $gtk_sharp_deps = [
    'libgtk-3-dev',
  ]
  package { $gtk_sharp_deps: ensure => installed, }

  install_from_source { 'gtk_sharp_install':
    package_name  => "gtk_sharp",
    url           => "https://github.com/mono/gtk-sharp",
    target        => "$source_dir/gtk-sharp",
    build_command => "./autogen.sh --prefix=$install_prefix && ./configure && make -j`nproc` && sudo make -j`nproc` install",
    provider      => "git",
    user          => "root",
    require       => [ 
        Package[$gtk_sharp_deps] , 
    ],
  }
}

#===========================================================
# TODO - install gstreamer-sharp

#===========================================================
# install gstreamer_sharp from tarball 
class gstreamer_sharp_install_from_source {
  notice ("Installing gstreamer_sharp from sources")
  $gstreamer_sharp_deps = [
    #'libgtk-3-dev',
  ]
  package { $gstreamer_sharp_deps: ensure => installed, }

  install_from_source { 'gstreamer_sharp_install':
    package_name  => "gstreamer_sharp",
    url           => "https://github.com/gstreamer-sharp/gstreamer-sharp",
    target        => "$source_dir/gstreamer-sharp",
    build_command => "./autogen.sh --prefix=$install_prefix && make -j`nproc` install",
    provider      => "git",
    user          => "root",
    require       => [ 
        Package[$gstreamer_sharp_deps] , 
        Class["gtk_sharp_install_from_source"],
    ],
  }
}

#===========================================================
# include all classes 
include system_packages_install
include gtk_sharp_install_from_source
include gstreamer_sharp_install_from_source
