from ocp.api.base import OcpBase

class v1_PrometheusRule(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "monitoring.coreos.com/v1", "PrometheusRule")
    
