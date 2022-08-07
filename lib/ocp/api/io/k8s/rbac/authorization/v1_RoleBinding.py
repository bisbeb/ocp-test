from ocp.api.base import OcpBase

class v1_RoleBinding(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "rbac.authorization.k8s.io/v1", "RoleBinding")
    
