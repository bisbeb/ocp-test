from ocp.api.base import OcpBase

class v1_APIService(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apiregistration.k8s.io/v1", "APIService")
    
