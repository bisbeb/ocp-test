from ocp.api.base import OcpBase

class v1_PodDisruptionBudget(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "policy/v1", "PodDisruptionBudget")
    
