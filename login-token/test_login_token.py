import pytest
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient
from openshift.helper.userpassauth import OCPLoginConfiguration

def create_client():
  apihost = 'https://api.crc.testing:6443'
  token = '<sa-token>'
  kubeConfig = OCPLoginConfiguration()
  kubeConfig.debug = False
  kubeConfig.host = apihost
  kubeConfig.verify_ssl = False
  kubeConfig.api_key = {"authorization":"Bearer " + token}
  k8s_client = client.ApiClient(kubeConfig)
  dyn_client = DynamicClient(k8s_client)
  return dyn_client

def get_node():
  dyn_client = create_client()
  nodes = dyn_client.resources.get(api_version='v1', kind='Node')
  node = nodes.get().items[0]
  print(node)
  return True

def test_node():
  assert get_node()
