---
id: software.devops.tranche17.001657
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

# SuperEdge `site-manager`: modelagem topológica de sites com `NodeUnit` e `NodeGroup`

## Em uma frase
O controlador `site-manager` introduz os CRDs `NodeUnit` (representando uma unidade física/site de borda na mesma LAN) e `NodeGroup` (agrupando múltiplas `NodeUnits` para distribuição de cargas de trabalho).

## Por que importa
Em frotas reais de borda, um único grupo de aplicação (como "Região Sul") é formado por dezenas de pequenos sites físicos independentes (lojas, subestações ou pedágios), onde cada site possui de 1 a 5 servidores conectados na mesma switch local.

## Como funciona
O administrador agrupa os servidores do mesmo local físico em uma `NodeUnit` (que serve de fronteira para o consenso do `edge-health`, para o fechamento de tráfego do `ServiceGrid` e para o cluster K3s local do `Kins`) e agrupa várias `NodeUnits` em um `NodeGroup` para orquestrar `DeploymentGrids` em larga escala.

## Exemplo
```yaml
apiVersion: site.superedge.io/v1alpha1
kind: NodeUnit
metadata:
  name: toll-station-01
spec:
  type: edge
  nodes:
    - edge-node-01
    - edge-node-02
```

## Limites e trade-offs
Quando um nó é adicionado a `spec.nodes` de uma `NodeUnit`, o `site-manager` aplica automaticamente no objeto `Node` o label identificador daquela unidade (`superedge.io/nodeunit: toll-station-01`).

## Como verificar
Crie uma `NodeUnit` listando dois nós de borda e verifique com `kubectl get nodes --show-labels` a injeção automática do label da unidade.

## Conexões
- [[superedge-tunnel-cloud-tunnel-edge-tcp-http-https-ssh-proxy]] — Veja também: SuperEdge `tunnel-cloud` e `tunnel-edge`: tunelamento reverso TCP, HTTP, HTTPS e SSH para manutenção na borda.
- [[superedge-lite-apiserver-autenticacao-mtls-rotacao-certificados-x509]] — Veja também: SuperEdge `lite-apiserver`: autenticação multi-cliente (X.509 mTLS, Bearer Token) e suporte a rotação de certificados.

## Fontes
- [SuperEdge GitHub — README.md (Kubernetes-Native Edge Container Management System, Kins L4/L5 Autonomy, ServiceGroup & Edge-Health)](https://raw.githubusercontent.com/superedge/superedge/main/README.md) — README oficial do superedge/superedge detalhando componentes de nuvem e borda, níveis de autonomia L3/L4/L5 (Kins), DeploymentGrid/ServiceGrid, tunnel e edgeadm; consultado em 2026-10-03.
- [SuperEdge Official Documentation — Components: lite-apiserver (TLS CN Reverse Proxy, Bolt/Badger/File Cache & Certificate Rotation)](https://raw.githubusercontent.com/superedge/superedge/main/docs/components/lite-apiserver.md) — Documentação técnica oficial do componente lite-apiserver no SuperEdge cobrindo proxy por Common Name X.509, motores de cache local e autonomia L3; consultado em 2026-10-03.
- [SuperEdge — Official GitHub Repository](https://github.com/superedge/superedge) — Repositório oficial Apache-2.0 do SuperEdge; consultado em 2026-10-03.
