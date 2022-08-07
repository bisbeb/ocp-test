from ocp.api.base import OcpBase

class v1_Job(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "batch/v1", "Job")
    
