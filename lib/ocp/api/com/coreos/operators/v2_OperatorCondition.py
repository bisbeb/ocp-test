from ocp.api.base import OcpBase

class v2_OperatorCondition(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operators.coreos.com/v2", "OperatorCondition")
    
