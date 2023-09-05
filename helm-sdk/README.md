## Configuration

The following table lists the configurable parameters of the laura-care-duvidas-generalista-actions chart and their default values.
## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | pod affinity |
| deploymentAnnotations | object | `{}` | annotations applied to the server deployment |
| extraEnv | list | `[]` | extra environment variables to set on the server container |
| fullnameOverride | string | `""` | override the chart fullname |
| image.pullPolicy | string | `"IfNotPresent"` | image pullPolicy to use |
| image.registry | string | `"docker.io"` | registry where the HAPI FHIR server image is hosted |
| image.repository | string | `"hapiproject/hapi"` | the path inside the repository |
| image.tag | string | `"v6.2.1@sha256:8d1b4c1c8abd613f685267a3dda494d87aba4cff449eed39902a6ece2c086f3c"` | the image tag. As of v5.7.0, this is the `distroless` flavor by default, add `-tomcat` to use the Tomcat-based image. |
| imagePullSecrets | list | `[]` | image pull secrets to use when pulling the image |
| ingress.annotations | object | `{}` | provide any additional annotations which may be required. Evaluated as a template. |
| ingress.enabled | bool | `false` | whether to create an Ingress to expose the FHIR server HTTP endpoint |
| ingress.hosts[0].host | string | `"fhir-server.127.0.0.1.nip.io"` |  |
| ingress.hosts[0].pathType | string | `"ImplementationSpecific"` |  |
| ingress.hosts[0].paths[0] | string | `"/"` |  |
| ingress.tls | list | `[]` | ingress TLS config |
| livenessProbe.failureThreshold | int | `5` |  |
| livenessProbe.initialDelaySeconds | int | `30` |  |
| livenessProbe.periodSeconds | int | `20` |  |
| livenessProbe.successThreshold | int | `1` |  |
| livenessProbe.timeoutSeconds | int | `30` |  |
| nameOverride | string | `""` | override the chart name |
| nodeSelector | object | `{}` | node selector for the pod |
| podAnnotations | object | `{}` | annotations applied to the server pod |
| podDisruptionBudget.enabled | bool | `false` | Enable PodDisruptionBudget for the server pods. uses policy/v1/PodDisruptionBudget thus requiring k8s 1.21+ |
| podDisruptionBudget.maxUnavailable | string | `""` | maximum unavailable instances |
| podDisruptionBudget.minAvailable | int | `1` | minimum available instances |
| podSecurityContext | object | `{}` | pod security context |
| readinessProbe.failureThreshold | int | `5` |  |
| readinessProbe.initialDelaySeconds | int | `30` |  |
| readinessProbe.periodSeconds | int | `20` |  |
| readinessProbe.successThreshold | int | `1` |  |
| readinessProbe.timeoutSeconds | int | `20` |  |
| replicaCount | int | `1` | number of replicas to deploy |
| resources | object | `{}` | configure the FHIR server's resource requests and limits |
| securityContext.allowPrivilegeEscalation | bool | `false` |  |
| securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| securityContext.privileged | bool | `false` |  |
| securityContext.readOnlyRootFilesystem | bool | `true` |  |
| securityContext.runAsGroup | int | `65532` |  |
| securityContext.runAsNonRoot | bool | `true` |  |
| securityContext.runAsUser | int | `65532` |  |
| securityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| service.port | int | `8080` | port where the server will be exposed at |
| service.type | string | `"ClusterIP"` | service type |
| startupProbe.failureThreshold | int | `10` |  |
| startupProbe.initialDelaySeconds | int | `30` |  |
| startupProbe.periodSeconds | int | `30` |  |
| startupProbe.successThreshold | int | `1` |  |
| startupProbe.timeoutSeconds | int | `30` |  |
| tolerations | list | `[]` | pod tolerations |
| topologySpreadConstraints | list | `[]` | pod topology spread configuration see: https://kubernetes.io/docs/concepts/workloads/pods/pod-topology-spread-constraints/#api |