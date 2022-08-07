from ocp.api.base import OcpBase

class v1alpha1_StorageVersionMigration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "migration.k8s.io/v1alpha1", "StorageVersionMigration")
    
