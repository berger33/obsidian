---
id: software.devops.tranche14.001316
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

# Submariner: Resolução DNS de Headless Services por Pod e cluster-id no ClusterSet

## Em uma frase
Para **Headless Services** (`clusterIP: None`, amplamente usados por bancos de dados distribuídos e StatefulSets como Kafka, Cassandra ou CockroachDB), o Lighthouse do Submariner permite endereçar cada Pod individualmente através do domínio `<pod-name>.<cluster-id>.<svc-name>.<ns>.svc.clusterset.local`.

## Por que importa
Diferente de um Service stateless com balanceamento round-robin, réplicas de um banco distribuído multi-região precisam se conectar diretamente ao registro DNS individual de cada peer em cada cluster.

## Como funciona
Ao exportar um Headless Service com `ServiceExport`, o Lighthouse publica registros DNS `A`/`AAAA` e `SRV` que incluem o `<cluster-id>` de cada cluster participante, exigindo que o `<cluster-id>` informado no `subctl join` seja um **DNS-1123 Label** válido (apenas letras minúsculas, dígitos e hífens).

## Exemplo
```bash
# Exemplo de consulta DNS para um Pod especifico de um StatefulSet em outro cluster:
nslookup db-0.cluster-east.cockroachdb.prod.svc.clusterset.local
```

## Limites e trade-offs
Definir um `cluster-id` contendo caracteres inválidos para DNS-1123 (como sublinhados `_` ou pontos `.`) quebra a resolução DNS de Pods individuais em Headless Services.

## Como verificar
Valide sempre que o `--clusterid` passado para `subctl join` obedeça estritamente à regra de DNS-1123 Label (`[a-z0-9-]`).

## Conexões
- [[submariner-lighthouse-service-discovery-serviceexport-clusterset-local]] — Veja também: Submariner: Descoberta de Serviços Multi-Cluster (Lighthouse, ServiceExport, ServiceImport e clusterset.local).
- [[submariner-globalnet-controller-overlapping-cidrs-nat]] — Veja também: Submariner: Interconexão de Clusters com CIDRs Sobrepostos usando Globalnet Controller.

## Fontes
- [Submariner Official Documentation — Architecture (Gateway Engine, Route Agent, Broker, Lighthouse Service Discovery & Globalnet)](https://submariner.io/getting-started/architecture/) — Documentação oficial de arquitetura do Submariner detalhando ClusterSet, ServiceExport, ServiceImport, domínio clusterset.local, Headless Services por cluster-id e Globalnet Controller; consultado em 2026-10-03.
- [Submariner GitHub — README.md (Network Path, vx-submariner VXLAN Tunnel, Operator, subctl & Helm Deployment)](https://raw.githubusercontent.com/submariner-io/submariner/devel/README.md) — README oficial do submariner-io/submariner descrevendo o caminho de pacotes entre worker nodes e nós Gateway eleitos, submariner-operator e comandos subctl; consultado em 2026-10-03.
- [Submariner — Official GitHub Repository](https://github.com/submariner-io/submariner) — Repositório oficial CNCF Sandbox do Submariner; consultado em 2026-10-03.
