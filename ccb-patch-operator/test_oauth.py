import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

def create_client():
  k8s_client = config.new_client_from_config()
  dyn_client = DynamicClient(k8s_client)
  return dyn_client

def get_oauth():
  dyn_client = create_client()
  oauths = dyn_client.resources.get(api_version='config.openshift.io/v1', kind='OAuth')
  oauth = oauths.get(field_selector='metadata.name=cluster').items[0]
  return oauth["metadata"]["name"]

def test_proxy():
  assert get_oauth() == 'cluster'
