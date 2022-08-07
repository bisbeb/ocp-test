from ocp.api.base import OcpBase

class v1_APIRequestCount(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apiserver.openshift.io/v1", "APIRequestCount")
    
