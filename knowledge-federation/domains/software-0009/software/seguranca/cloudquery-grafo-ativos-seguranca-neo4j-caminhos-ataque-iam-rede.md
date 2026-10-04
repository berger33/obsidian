---
id: software.seguranca.tranche10.000919
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md", "https://www.cloudquery.io/docs/cli/getting-started"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CloudQuery + **Neo4j (`cloudquery/neo4j`)**: Construção de **Grafos de Superfície de Ataque Cloud** (Rede -> Computação -> Identidade -> Dados)

## Em uma frase
Por que ferramentas líderes de CNAPP comercial representam a nuvem como um **Grafo**? Porque ataques reais em nuvem são **Caminhos em Grafo (*Attack Paths*)**: *Internet (`0.0.0.0/0`) -> LoadBalancer -> Pod Kubernetes -> Node IAM Role -> Permissão `s3:GetObject` -> Bucket S3 Confidencial*!

## Por que importa
Além de bancos relacionais SQL, o CloudQuery possui um plugin oficial de destino para o banco de grafos **Neo4j (`cloudquery/neo4j`)**!

## Como funciona
Ao sincronizar fontes como AWS, GCP, Azure e Kubernetes para o Neo4j (ou construir arestas de relacionamento sobre as chaves estrangeiras/ARNs), os ativos tornam-se **Nós (*Nodes*)** e os vínculos de rede, anexação de volumes e permissões IAM tornam-se **Arestas (*Relationships*)** consultáveis com a linguagem **Cypher** (a mesma usada pelo **BloodHound CE**)!

## Exemplo
```yaml
# aws-to-neo4j.yml — Sincronizando ativos de nuvem diretamente para um banco de grafos Neo4j para analise de Attack Paths
kind: destination
spec:
  name: neo4j
  path: cloudquery/neo4j
  registry: cloudquery
  version: "v5.0.0"
  write_mode: overwrite-delete-stale
  spec:
    connection_string: "bolt://127.0.0.1:7687"
    username: "neo4j"
    password: "${NEO4J_PASSWORD}"
```

## Limites e trade-offs
Unir os dados de Active Directory/Entra ID do **BloodHound CE** com os ativos de infraestrutura AWS/GCP/K8s sincronizados pelo **CloudQuery no Neo4j** permite mapear caminhos de ataque híbridos completos (de uma estação Windows on-premises até um bucket S3 na nuvem)!

## Como verificar
Consulte o grafo no Neo4j Browser para visualizar o raio de explosão (*blast radius*) de cada IAM Role.

## Conexões
- [[cloudquery-deteccao-drift-historico-temporal-snapshots-sql]] — Veja também: CloudQuery Forense: **Histórico Temporal (`write_mode: append`)** para Investigação de Incidentes ("O Que Mudou na Conta Antes do Ataque?").
- [[cloudquery-execucao-segura-containers-kubernetes-cronjob-telemetria]] — Veja também: CloudQuery em Produção: Implantação como **Kubernetes CronJob Hardened**, Logs Estruturados e Monitoramento de Métricas OpenTelemetry.
- [[cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm]] — Referência cruzada direta com cloudquery-arquitetura-elt-apache-arrow-inventario-ativos-cspm.

## Fontes
- [CloudQuery Official GitHub — High-Performance Open-Source Cloud Asset Inventory Powered by Apache Arrow](https://raw.githubusercontent.com/cloudquery/cloudquery/main/README.md) — repositório oficial do CloudQuery cobrindo arquitetura ELT em Go e Apache Arrow, casos de uso de inventário multi-cloud e CSPM; consultado em 2026-10-03.
- [CloudQuery Official CLI Documentation — Getting Started, Sync Modes & Integration Architecture](https://www.cloudquery.io/docs/cli/getting-started) — documentação oficial da CLI do CloudQuery cobrindo configuração de fontes/destinos, modos de sincronização e arquitetura de plugins; consultado em 2026-10-03.
