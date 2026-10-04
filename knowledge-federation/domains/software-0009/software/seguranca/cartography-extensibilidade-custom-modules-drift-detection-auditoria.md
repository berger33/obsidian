---
id: software.seguranca.tranche11.001010
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md", "https://docs.cartography.dev/usage/tutorial.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Extensibilidade do Cartography: Como Construir **Módulos Customizados (`IntelModule`)** para Ingerir Ativos Internos e CMDBs no Grafo de Segurança

## Em uma frase
Toda grande organização possui sistemas proprietários internos (como um CMDB corporativo, um catálogo de microsserviços no Backstage, um registro interno de donos de equipes ou firewalls on-premise) que não existem em nenhuma ferramenta pronta de mercado.

## Por que importa
Como destacou a documentação oficial (`Why Cartography?`), o Cartography foi desenhado desde o primeiro dia na Lyft para ser uma **Plataforma Extensível de Grafo**: adicionar uma nova fonte de dados requer apenas implementar o padrão **`get -> transform -> load -> cleanup`** usando o schema declarativo do Cartography (`CartographyNodeSchema` e `CartographyRelSchema`), que gera automaticamente as queries Cypher otimizadas com **`UNWIND $DictList`** e índices no Neo4j!

## Como funciona
Ao conectar o seu catálogo interno de **Equipes e Serviços (`Team -> OWNS -> Service -> DEPLOYED_ON -> AWSEC2Instance/KubernetesPod`)**, toda descoberta de caminho de ataque ou CVE já sai com o nome exato do time responsável pela correção!

## Exemplo
```cypher
// Exemplo de consulta Cypher unindo o catalogo de times (Team/Service) aos ativos AWS e vulnerabilidades CISA KEV no Cartography
MATCH (t:Team)-[:OWNS]->(s:Service)-[:DEPLOYED_ON]->(asset)-[:AFFECTED_BY]->(c:CVE {is_kev: true})
RETURN t.name AS equipe_responsavel,
       t.slack_channel AS canal_alerta,
       s.name AS servico,
       c.id AS cve_kev,
       coalesce(asset.instanceid, asset.name) AS recurso;
```

## Limites e trade-offs
Por que o Cartography utiliza sempre **`UNWIND $batch AS item MERGE (n:Node {id: item.id}) SET ...`** em vez de executar um `CREATE`/`MERGE` individual por ativo ao carregar dados em módulos customizados? Porque o `UNWIND` envia milhares de registros em uma única transação parametrizada pelo protocolo Bolt, sendo até **100x mais rápido** no Neo4j!

## Como verificar
Consulte o guia oficial `Writing Intel Modules` (`docs.cartography.dev/dev/`) para ver o template de `CartographyNodeSchema`.

## Conexões
- [[cartography-sincronizacao-multi-conta-update-tag-cleanup-staleness]] — Veja também: Operação em Produção do Cartography: Sincronização Multi-Conta AWS (`--aws-sync-all-profiles`), **`UPDATE_TAG`** e Limpeza de Nós Obsoletos (**`Cleanup Jobs`**).
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[cartography-gestao-vulnerabilidades-cves-epss-kev-crowdstrike-ecr]] — Referência cruzada direta com cartography-gestao-vulnerabilidades-cves-epss-kev-crowdstrike-ecr.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
