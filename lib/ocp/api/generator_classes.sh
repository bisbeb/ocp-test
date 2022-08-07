#!/bin/bash

# generate input file use the following command:
# oc get $(oc api-resources --namespaced=false --verbs=list -o name | awk '{printf "%s%s",sep,$0;sep=","}') --no-headers  --ignore-not-found --all-namespaces -o=custom-columns=KIND:.kind,APIVETSION:.apiVersion --sort-by='kind' | sort -u | awk '{printf("%s;%s\n",$1,$2)}' > resources.txt

# oc get $(oc api-resources --namespaced=true --verbs=list -o name | awk '{printf "%s%s",sep,$0;sep=","}') --no-headers  --ignore-not-found --all-namespaces -o=custom-columns=KIND:.kind,APIVETSION:.apiVersion --sort-by='kind' | sort -u | awk '{printf("%s;%s\n",$1,$2)}' > resources_namespaced.txt
# the file needs some manuel adjust, so remove Kinds not needed manually

echo "# cluster-wide resources"
echo "# ======================"
for l in $(cat resources.txt | sort); do
  kind=$(cut -d\; -f1 <<< $l)
  apiVersion=$(cut -d\; -f2 <<< $l)
  version=$(basename $apiVersion)
  package=$(dirname $apiVersion | sed 's/\(.*\)\.\(.*\)\.\(.*\)/\3\.\2\.\1/' | sed 's/\./\//g')
  #rm -rf $package
  if [ "$apiVersion" != "v1" ]; then
    mkdir -p $package
    echo """from ocp.api.base import OcpBase

class ${version}_${kind}(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, \"${apiVersion}\", \"${kind}\")
    """ >> $package/${version}_${kind}.py
  else
    echo """from ocp.api.base import OcpBase

class ${version}_${kind}(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, \"${apiVersion}\", \"${kind}\")
    """ >> ./${version}_${kind}.py
  fi
done

echo "# namespaced resources"
echo "# ======================"
for l in $(cat resources_namespaced.txt | sort); do
  kind=$(cut -d\; -f1 <<< $l)
  apiVersion=$(cut -d\; -f2 <<< $l)
  version=$(basename $apiVersion)
  package=$(dirname $apiVersion | sed 's/\(.*\)\.\(.*\)\.\(.*\)/\3\.\2\.\1/' | sed 's/\./\//g')
  #rm -rf $package
  if [ "$apiVersion" != "v1" ]; then
    mkdir -p $package
    echo """from ocp.api.base import OcpBase

class ${version}_${kind}(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, \"${apiVersion}\", \"${kind}\")
    """ >> $package/${version}_${kind}.py
  else
    echo """from ocp.api.base import OcpBase

class ${version}_${kind}(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, \"${apiVersion}\", \"${kind}\")
    """ >> ./${version}_${kind}.py
  fi
done

echo "# touch __init__.py"
echo "# ======================"
find . -type d | grep -v __py |  xargs -I {} touch {}/__init__.py
