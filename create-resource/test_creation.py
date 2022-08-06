import pytest
import yaml, time
from kubernetes import client, config
from openshift.dynamic import DynamicClient

def setup_ns():
  with open("resources/ns.yaml") as f:
    data = yaml.safe_load(f)
  return data

def setup_svc():
  with open("resources/svc.yaml") as f:
    data = yaml.safe_load(f)
  return data

def create_client():
  k8s_client = config.new_client_from_config()
  dyn_client = DynamicClient(k8s_client)
  return dyn_client

def test_service_creation():
  dyn_client = create_client()
  namespaces = dyn_client.resources.get(api_version='v1', kind='Namespace')
  ns_resp = namespaces.create(body=setup_ns())
  assert ns_resp.metadata.name == "test-ns"
  services = dyn_client.resources.get(api_version='v1', kind='Service') 
  svc_resp = services.create(body=setup_svc(), namespace="test-ns")
  assert svc_resp.metadata.name == "my-service"
  namespaces.delete(name="test-ns")
  time.sleep(10)
  assert len(namespaces.get(field_selector="metadata.name=test-ns").items) == 0

