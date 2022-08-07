from ocp.api.base import OcpBase

class v1beta1_HelmChartRepository(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "helm.openshift.io/v1beta1", "HelmChartRepository")
    
