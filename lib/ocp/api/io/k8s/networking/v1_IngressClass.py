from ocp.api.base import OcpBase

class v1_IngressClass(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "networking.k8s.io/v1", "IngressClass")
    
