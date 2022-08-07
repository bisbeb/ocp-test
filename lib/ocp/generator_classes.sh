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
  apiVersion_nromalized=$(cut -d\; -f2 <<< $l | sed 's/\//_/g' | sed 's/\./_/g')
  echo """class ${apiVersion_nromalized}${kind}(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, \"${apiVersion}\", \"${kind}\")
  """
done

echo "# namespaced resources"
echo "# ===================="
for l in $(cat resources_namespaced.txt); do
  kind=$(cut -d\; -f1 <<< $l)
  apiVersion=$(cut -d\; -f2 <<< $l)
  apiVersion_nromalized=$(cut -d\; -f2 <<< $l | sed 's/\//_/g' | sed 's/\./_/g')
  echo """class ${apiVersion_nromalized}${kind}(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, \"${apiVersion}\", \"${kind}\")
  """
done
