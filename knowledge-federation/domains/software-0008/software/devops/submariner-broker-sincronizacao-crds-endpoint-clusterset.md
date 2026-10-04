---
id: software.devops.tranche14.001314
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://submariner.io/getting-started/architecture/", "https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md", "https://github.com/submariner-io/submariner"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Submariner: O Papel do Broker na Troca de Metadados (Endpoints e ServiceImports) entre Clusters

## Em uma frase
O **Broker** do Submariner é um conjunto de CRDs e permissões RBAC hospedado na API de um cluster Kubernetes (que pode ser um dos clusters conectados ou um cluster hub dedicado) onde todos os clusters participantes sincronizam seus objetos `Endpoint` e `ServiceImport`.

## Por que importa
Para que o Gateway do Cluster A saiba qual é o IP público, o subnet CIDR e a chave pública do Gateway do Cluster B sem configuração manual ponto-a-ponto em `N x N` clusters, é necessário um ponto de encontro declarativo.

## Como funciona
Ao executar `subctl deploy-broker`, é gerado um arquivo `broker-info.subm` contendo a URL da API e credenciais restritas ao namespace do Broker; cada cluster executado com `subctl join broker-info.subm` passa a publicar seus próprios metadados no Broker e observar os metadados dos demais clusters do `ClusterSet`.

## Exemplo
```bash
subctl deploy-broker --kubeconfig ~/.kube/config-hub
subctl join broker-info.subm --kubeconfig ~/.kube/config-cluster-a --clusterid cluster-a
subctl join broker-info.subm --kubeconfig ~/.kube/config-cluster-b --clusterid cluster-b
```

## Limites e trade-offs
Acreditar que o tráfego de dados dos Pods passa pelo Broker é um equívoco comum: o Broker troca exclusivamente metadados de controle via API Kubernetes, enquanto o plano de dados flui diretamente de Gateway para Gateway.

## Como verificar
Versione e proteja o arquivo `broker-info.subm` como um segredo sensível, pois ele concede permissão para registrar novos endpoints no `ClusterSet`.

## Conexões
- [[submariner-route-agent-vx-submariner-fluxo-pacotes-pod-service]] — Veja também: Submariner: Route Agent, Túnel Interno vx-submariner e Caminho de Rede entre Worker Nodes e Gateways.
- [[submariner-lighthouse-service-discovery-serviceexport-clusterset-local]] — Veja também: Submariner: Descoberta de Serviços Multi-Cluster (Lighthouse, ServiceExport, ServiceImport e clusterset.local).

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://submariner.io/getting-started/architecture/) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
