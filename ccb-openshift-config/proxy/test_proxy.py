import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

def create_client():
  k8s_client = config.new_client_from_config()
  dyn_client = DynamicClient(k8s_client)
  return dyn_client

def get_proxy():
  dyn_client = create_client()
  proxies = dyn_client.resources.get(api_version='config.openshift.io/v1', kind='Proxy')
  proxy = proxies.get(field_selector='metadata.name=cluster').items[0]
  return proxy["metadata"]["name"]

def test_proxy():
  assert get_proxy() == 'cluster'
