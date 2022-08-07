from ocp.api.base import OcpBase

class v1_OLMConfig(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v1", "OLMConfig")
    
