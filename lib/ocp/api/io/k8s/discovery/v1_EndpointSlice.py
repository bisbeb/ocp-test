from ocp.api.base import OcpBase

class v1_EndpointSlice(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "discovery.k8s.io/v1", "EndpointSlice")
    
