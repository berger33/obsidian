---
id: software.devops.tranche17.001655
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://raw.githubusercontent.com/superedge/superedge/main/README.md", "https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md", "https://github.com/superedge/superedge"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SuperEdge `ServiceGroup`: orquestração multi-região com `DeploymentGrid`, `StatefulSetGrid` e `ServiceGrid`

## Em uma frase
O `application-grid-controller` (parte do `ServiceGroup` na nuvem) e o `application-grid-wrapper` (na borda) gerenciam os CRDs `DeploymentGrid`, `StatefulSetGrid` e `ServiceGrid` para implantar microsserviços em múltiplas regiões de borda mantendo o tráfego de rede estritamente fechado dentro de cada região.

## Por que importa
Quando uma aplicação composta por `frontend` e `backend` é implantada em 50 regiões de borda (`NodeUnits`), cada região precisa de seu próprio conjunto de Pods e o `frontend` da Região 1 deve chamar exclusivamente o `backend` da Região 1 (sem atravessar a WAN para a Região 2).

## Como funciona
O usuário define uma chave de agrupamento (por exemplo o label `grid-selector` que identifica cada `NodeUnit`) em um `DeploymentGrid` e em um `ServiceGrid`. O `application-grid-controller` gera automaticamente um `Deployment` por região, enquanto o `application-grid-wrapper` no nó de borda intercepta a lista de `Endpoints`/`EndpointSlices` entregue ao `kube-proxy`, filtrando apenas os Pods que pertencem à mesma região (`grid`) daquele nó.

## Exemplo
```yaml
apiVersion: superedge.io/v1
kind: DeploymentGrid
metadata:
  name: edge-echo-grid
  namespace: default
spec:
  gridUniqKey: superedge.io/nodeunit
  defaultTemplate:
    replicas: 2
    selector:
      matchLabels:
        app: echo
    template:
      metadata:
        labels:
          app: echo
      spec:
        containers:
          - name: echo
            image: superedge/echoserver:2.2
```

## Limites e trade-offs
O `application-grid-wrapper` funciona como um proxy local entre o `kube-proxy` e o `lite-apiserver`: não é necessário modificar o binário do `kube-proxy` nem o plugin CNI para obter o isolamento de tráfego por `ServiceGrid`.

## Como verificar
Crie um `DeploymentGrid` e um `ServiceGrid` com a mesma `gridUniqKey` e confirme que chamadas ao `ClusterIP` do serviço em um nó de borda respondem apenas com IPs de Pods da mesma `NodeUnit`.

## Conexões
- [[superedge-edge-health-monitoramento-distribuido-consenso-admission]] — Veja também: SuperEdge `edge-health` e `edge-health-admission`: detecção distribuída de saúde na borda e proteção contra falsos positivos.
- [[superedge-tunnel-cloud-tunnel-edge-tcp-http-https-ssh-proxy]] — Veja também: SuperEdge `tunnel-cloud` e `tunnel-edge`: tunelamento reverso TCP, HTTP, HTTPS e SSH para manutenção na borda.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
