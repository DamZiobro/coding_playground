#!/bin/bash 


trap 'killall' INT

killall() {
    trap '' INT TERM     # ignore INT and TERM while shutting down
    echo "**** Shutting down... ****"     # added double quotes
    kill -TERM 0         # fixed order, send TERM not INT
    wait
    echo DONE
}

# render Dockerfile from templates
function renderDockerfiles() {
  echo "Rendering dockerfile templates into real Dockerfiles"

  dirs=$(ls -d dockerfiles/*/)
  for dir in $dirs; do

    #echo "Rendering files in dir: $dir"

    if [ ! -f $dir/DOCKERFILE.template -o ! -f VERSIONS ]; then
      echo -e "\n\n ERROR!!!! Cannot find file $dir/DOCKERFILE.template or VERSIONS !!!"
      return 1
    fi

    #remove old dockerfiles
    rm -rf $dir/Dockerfile*

    while read version; do 
      os=$(echo $version | cut -d: -f1)
      currdir=$(echo $dir | cut -d'/' -f2)
      #echo "os: $os; currdir: $currdir"
      if [ ${version:0:1} == "#" -o $os != $currdir ]; then
        continue
      fi
      echo "Rendering file in dir '$dir' for docker image version '$version'"  

      suffix=$(echo "$version" | tr '[A-Z]' '[a-z]' | tr '[:.]' '[\-\-]')
      version_nr=$(echo "$version" | cut -d: -f2)
      cp $dir/DOCKERFILE.template $dir/Dockerfile.$suffix

      sed -i "s/\%\%FROM_IMAGE\%\%/$version/g" $dir/Dockerfile.$suffix 
      sed -i "s/\%\%VERSION_NR\%\%/$version_nr/g" $dir/Dockerfile.$suffix 

    done < VERSIONS

  done

}
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# MAIN - SCRIPT ENTRY POINT
if [ -z $1 ]; then 
  echo  "\nERROR: wrong arguments\n"
  echo  "Usage: $(basename $0) imageName [Dockerfile suffix]"
  echo  "    ex1. $(basename $0) vim-install-test"
  echo  "    ex2. $(basename $0) vim-install-test ubuntu.16.04"
  exit 2
fi

renderDockerfiles || { echo -e "\n\nERROR in renderDockerfiles()\n\n"; exit -1; }

if [ ! -z $2 ]; then

    dockerfile=$(find . -name Dockerfile.$2 | head -n 1)
    echo "Building image for dockerfile: $dockerfile"

    if [ ! -f $dockerfile ]; then
      echo "ERROR: file $dockerfile does not exist - nothing to build"
      exit 3
    fi

    suffix=$(echo $(basename $dockerfile) | cut -d. -f2)
    docker build -t $1-$suffix -f $dockerfile . || { echo -e "\n\n ERROR: error while 'docker build'\n\n"; exit 3; }
else
  dockerfiles=$(find dockerfiles -name "Dockerfile.*")
  for file in $dockerfiles; do
    echo "Bulilding image for dockerfile: $file"
    suffix=$(echo $file | cut -d. -f2)
    #run building docker images in parallel
    {
      docker build -t $1-$suffix -f $file . || { echo -e "\n\n ERROR: error while 'docker build'\n\n"; exit 3; } 
    } &
  done

  echo -e "Waiting until all docker builds will finish. It may take long time (up to few hours). Please wait..."
  wait 

fi

echo "==================================================="
echo "                   DOCKER IMAGES"
echo "==================================================="
docker images
echo "==================================================="
echo "                   DOCKER CONTAINERS"
echo "==================================================="
docker ps -a

echo "====================================================================================================="
echo -e "SUCCESS - YOUR PUPPET MANIFESTS HAS BEEN SUCCESSFULL INSTALLED FOR MULTIPLE OPERATING SYSTEMS"
#use -priviledged option to be possible to run docker in docker containers
echo -e "You can run one of the images command like this one (for Ubuntu 16.04):"
echo -e "\ndocker run --rm=true --name test -i --privileged -t $1-ubuntu-16-04 /bin/bash\n"

echo "====================================================================================================="
