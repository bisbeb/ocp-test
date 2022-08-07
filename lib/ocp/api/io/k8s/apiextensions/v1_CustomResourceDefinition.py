from ocp.api.base import OcpBase

class v1_CustomResourceDefinition(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "apiextensions.k8s.io/v1", "CustomResourceDefinition")
    
