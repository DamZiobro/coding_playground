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

class system_packages_install {
    notice ("Installing GStreamer dependencies...")

    $general_packages = [
      "libtool",
      "autotools-dev", 
      "pkg-config", 
      "gtk-doc-tools", 
      "libglib2.0-0", 
      "libglib2.0-dev", 
      "autopoint", 
      "autoconf", 
      "libbison-dev", 
      "flex", 
      "x264", 
      "libx264-dev", 
      "build-essential", 
      "freeglut3", 
      "freeglut3-dev", 
      "libgles2-mesa-dev", 
      "liborc-0.4.0", 
      "liborc-0.4-dev", 
      "libav-tools", 
      "yasm", 
      "git", 
    ]

    $additional_packages = $::operatingsystem ? {
      'Ubuntu' => 
        $::lsbdistcodename ? {
          "xenial"  => [
            "faac", 
            "librtmp1", 
            "librtmp-dev", 
            "libfaac-dev",
          ],
          "trusty" => [
            "librtmp0", 
            "librtmp-dev", 
          ],
          default  => [],
        },
      'Debian' => 
        $::lsbdistcodename ? {
          "wheezy" => [
            "librtmp0", 
            "librtmp-dev", 
          ],
          default  => [],
        },
      default => [],
    }

    package { $general_packages: 
      ensure  => installed, 
    }

    package { $additional_packages: 
      ensure  => installed, 
      require => [
        Package[$general_packages],
      ]
    }

}
include system_packages_install

class gstreamer_install($gstreamer_version = "1.12.2", $install_dir="/tmp/gstreamerInstall") {

  notice ("Installing gstreamer from sources")

  file { $install_dir: 
    ensure  => directory, 
    require => [
      Class['system_packages_install'] ,
    ],
  }

  define install_from_source ($package_name, $url, $target="/tmp/$package_name", $build_command = "make -j`nproc` && sudo make -j`nproc` install", $revision = master, $unless_cmd = "ls /tmp/XXXXXX &> /dev/null"){ 

    notice ("Installing $package_name")

    file { $target: 
      ensure  => directory, 
    }

    exec { "git_clone_$package_name":
      cwd     => $target,
      command => "git clone $url --branch $revision $package_name-$revision",
      timeout => 1000,
      require => [
        File[$target], 
      ]
    }

    if $build_command != "" {
      notice("Building $package_name from source using command: $build_command. Target: $target; package_name: $package_name; revision: $revision")
      exec { "make_$package_name":
        path    => [ $path, "$target/$package_name-$revision" ],
        cwd     => "$target/$package_name-$revision",
        command => $build_command,
        timeout => 1000,
        #unless  => $unless_cmd,
        require => [ 
            Exec["git_clone_$package_name"], 
        ]
      }
    }
  }

  define install_gstreamer_subpackage ($package_name, $install_dir, $gstreamer_version) {
    install_from_source { "${package_name}_install":
      package_name  => "$package_name",
      url           => "git://anongit.freedesktop.org/gstreamer/$package_name",
      revision      => "$gstreamer_version",
      target        => "$install_dir/$package_name-$gstreamer_version",
      build_command => "./autogen.sh --prefix=/usr/local --disable-gtk-doc && make -j`nproc` && sudo make -j`nproc` install",
      unless_cmd    => "gst-inspect-1.0 --version | grep $gstreamer_version",
      require       => [ 
          Class['system_packages_install'] ,
          File[$install_dir] ,
      ],
    }
  }


  #TODO - compress below functions to avoid copying them (class template? other solution?)
  install_gstreamer_subpackage { "install_gstreamer_invoke": 
      package_name      => "gstreamer" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
  }
  install_gstreamer_subpackage { "install_gst-plugins-base_invoke": 
      package_name      => "gst-plugins-base" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
      require           => [
          Gstreamer_install::Install_gstreamer_subpackage["install_gstreamer_invoke"] ,
      ]
  }
  install_gstreamer_subpackage { "install_gst-plugins-good_invoke": 
      package_name      => "gst-plugins-good" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
      require           => [
          Gstreamer_install::Install_gstreamer_subpackage["install_gstreamer_invoke"] ,
          Gstreamer_install::Install_gstreamer_subpackage["install_gst-plugins-base_invoke"] ,
      ]
  }
  install_gstreamer_subpackage { "install_gst-plugins-bad_invoke": 
      package_name      => "gst-plugins-bad" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
      require           => [
          Gstreamer_install::Install_gstreamer_subpackage["install_gstreamer_invoke"] ,
          Gstreamer_install::Install_gstreamer_subpackage["install_gst-plugins-base_invoke"] ,
      ]
  }
  install_gstreamer_subpackage { "install_gst-plugins-ugly_invoke": 
      package_name      => "gst-plugins-ugly" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
      require           => [
          Gstreamer_install::Install_gstreamer_subpackage["install_gstreamer_invoke"] ,
          Gstreamer_install::Install_gstreamer_subpackage["install_gst-plugins-base_invoke"] ,
      ]
  }
  install_gstreamer_subpackage { "install_gst-rtsp-server_invoke": 
      package_name      => "gst-rtsp-server" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
      require           => [
          Gstreamer_install::Install_gstreamer_subpackage["install_gstreamer_invoke"] ,
          Gstreamer_install::Install_gstreamer_subpackage["install_gst-plugins-base_invoke"] ,
      ]
  }
  install_gstreamer_subpackage { "install_gst-libav_invoke": 
      package_name      => "gst-libav" ,
      install_dir       => $install_dir,
      gstreamer_version => $gstreamer_version,
      require           => [
          Gstreamer_install::Install_gstreamer_subpackage["install_gstreamer_invoke"] ,
          Gstreamer_install::Install_gstreamer_subpackage["install_gst-plugins-base_invoke"] ,
      ]
  }
  #ldconfig 
  exec { 'gstreamer_ldconfig':
    command => "ldconfig",
    require => [
      Gstreamer_install::Install_gstreamer_subpackage['install_gstreamer_invoke'] ,
      Gstreamer_install::Install_gstreamer_subpackage['install_gst-plugins-base_invoke'] ,
      Gstreamer_install::Install_gstreamer_subpackage['install_gst-plugins-good_invoke'] ,
      Gstreamer_install::Install_gstreamer_subpackage['install_gst-plugins-bad_invoke'] ,
      Gstreamer_install::Install_gstreamer_subpackage['install_gst-plugins-ugly_invoke'] ,
      Gstreamer_install::Install_gstreamer_subpackage['install_gst-rtsp-server_invoke'] ,
      Gstreamer_install::Install_gstreamer_subpackage['install_gst-libav_invoke'] ,
    ]
  }

}
include gstreamer_install
