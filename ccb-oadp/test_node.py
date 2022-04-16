import pytest
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

def create_client():
  k8s_client = config.new_client_from_config()
  dyn_client = DynamicClient(k8s_client)
  return dyn_client

def get_node():
  dyn_client = create_client()
  nodes = dyn_client.resources.get(api_version='v1', kind='Node')
  node = nodes.get(label_selector='node-role.kubernetes.io/master=').items[0]
  return True

def test_node():
  assert get_node()
