from ocp.api.base import OcpBase

class v1_RangeAllocation(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "security.internal.openshift.io/v1", "RangeAllocation")
    
