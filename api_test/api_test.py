import pytest
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient
from openshift.helper.userpassauth import OCPLoginConfiguration
from ocp.api.v1_Node import *
from ocp.api.v1_Secret import *
from ocp.api.v1_Namespace import *
from ocp.api.io.openshift.oauth.v1_OAuthClient import *

def create_client():
  apihost = 'https://api.crc.testing:6443'
  token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkpsbjZodkZsMUlpUlRMU2ZKRnd2S240c1dZTWhBeFhMT2ZGT1ZSeS1PYk0ifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJ0ZXN0Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImFkbWluLXRva2VuLXB0NHFnIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiZjc3OWExZjAtNWNmZi00NDE4LThhYzAtZDNlMWNjYmFhNmYwIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OnRlc3Q6YWRtaW4ifQ.3DAjvSDzW2y7wd2rxIW_V3C7JDAsDNvZlm2B6M7dXcbwrLOZNr2p5kn7XfpUt5zVOxbb9Zp3rUrEglmawNnvzV69mfpSBFSwMn-GZcW5fXdLLZSIEuWP60erskF2BRkZIA_Yte05sXOXj0GOa1GgdIJVSCKyj79Ij5FMvk6yegUcg5mAu5Cu-kh0EW_T91e4m9HHMVDTUb0fmFO_QcJFOTsQpGyLRTE4SAf78L1mWTH5HXLLodAY-MbZe_RtUl9lbJpr0BywLu-PB8JtuS1tqfHZdUcWI3hLZcIX_btCXxz6_KIjKfu7RfgXLBo8qblXgjX5qaLlmT809ldFlSOL8kjpcoql6r56rjL3gF6tclRC-9l9dcCV_8qY4kSoCgNPFnNIuLLesCl-iPeLuSGq7WkA-zhrD3P4cs1lU-6Q1pbNSjDrJgEhk4zF0klzud56ByVUVb6cJKgA1A571dg4nepIVWCTShhtspnfZ5Bbj5E2IB6t2elfcGmZRLTfV-IElhS8OhunmI2aqtidf2jTUyW8oSINvEFaNMFe6om9Y_UbaF2zADjtY_wISlFJiuL0l64YRKJNwCFSHnFLfxkpydXKooi3qfk5P4hl9Qjo0sW9lUqzx3Y_y3ZJ0rT6PK2b1V9IwDRSKgX4Yrym_r4wbMHmPO-iJKGawf4-MZ4sFf4'
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
  v1_nodes = v1_Node(dyn_client)
  nodes = v1_nodes.get()
  print(nodes[0].status.conditions[3].status)
  v1_secrets = v1_Secret(dyn_client)
  secrets = v1_secrets.get(namespace="test", name="admin-dockercfg-gjf79")
  print(secrets)
  v1_namespace = v1_Namespace(dyn_client)
  for ns in v1_namespace.get():
    print(ns.metadata.name)
  v1_oauthclients = v1_OAuthClient(dyn_client)
  oauthclients = v1_oauthclients.get()
  return True

def test_node():
  assert get_node()
