---
id: software.seguranca.tranche11.001002
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

# Cartography **Data Enrichment (`Analysis Jobs`)**: Como São Calculados os Atributos Derivados **`exposed_internet: true`** e **`anonymous_access: true`**

## Em uma frase
Quando você consulta a API oficial `DescribeInstances` da AWS EC2 ou `GetBucketPolicy` do Amazon S3, a AWS **não retorna um campo booleano simples dizendo `exposed_internet: true` ou `anonymous_access: true`**: descobrir se uma instância EC2 está realmente acessível a partir da internet exige correlacionar o `NetworkInterface`, os `EC2SecurityGroup`s, as regras `IpPermissionsInbound` (`0.0.0.0/0` ou `::/0`), Load Balancers (`ELBv2`), Subnets e Route Tables!

## Por que importa
Conforme destaca o tutorial oficial do Cartography (`docs.cartography.dev/usage/tutorial.html`), esse é um dos maiores diferenciais da ferramenta: após ingerir os objetos brutos da nuvem, o Cartography executa **Jobs de Análise e Enriquecimento de Grafo (*Data Enrichment / Analysis Jobs*)** em Cypher que percorrem a topologia de rede e as políticas IAM e gravam diretamente nos nós finais propriedades prontas para auditoria!

## Como funciona
Graças a esse enriquecimento automático, qualquer analista do SOC ou engenheiro pode consultar em 1 linha Cypher todas as instâncias EC2 expostas à internet (`MATCH (i:AWSEC2Instance{exposed_internet: true})`) ou todos os buckets S3 que permitem acesso anônimo (`MATCH (s:AWSS3Bucket{anonymous_access: true})`)!

## Exemplo
```cypher
// Consultas Cypher no Neo4j aproveitando os atributos enriquecidos pelo Cartography (exposed_internet e anonymous_access)
MATCH (a:AWSAccount)-[:RESOURCE]->(i:AWSEC2Instance {exposed_internet: true})
RETURN a.name AS conta_aws, i.instanceid AS ec2_id, i.publicdnsname AS dns_publico, i.privateipaddress AS ip_privado;

MATCH (a:AWSAccount)-[:RESOURCE]->(b:AWSS3Bucket {anonymous_access: true})
RETURN a.name AS conta_aws, b.name AS bucket_publico, b.region AS regiao;
```

## Limites e trade-offs
Você também pode escrever seus próprios **Analysis Jobs** customizados em JSON/Cypher e passá-los para o Cartography via `--analysis-job-directory`, marcando automaticamente ativos que violam políticas internas da sua empresa (por exemplo, `missing_edr_agent: true` quando um nó `AWSEC2Instance` não possui relação com um nó `CrowdstrikeHost`!).

## Como verificar
Inspecione no repositório oficial a pasta `cartography/data/jobs/analysis/` para ver todas as queries Cypher de enriquecimento nativas.

## Conexões
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Veja também: **CNCF Cartography (`cartography-cncf/cartography`)**: Arquitetura de Consolidação de Ativos de Infraestrutura, Nuvem, Kubernetes e Identidade em **Grafo Neo4j**.
- [[cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s]] — Veja também: Threat Hunting e Descoberta de **Caminhos de Ataque (*Attack Paths*)** no Cartography com Consultas **OpenCypher** Multi-Hop.
- [[cartography-motor-regras-cartography-rules-auditoria-automatizada]] — Referência cruzada direta com cartography-motor-regras-cartography-rules-auditoria-automatizada.
- [[steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud]] — Referência cruzada direta com steampipe-arquitetura-zero-etl-postgres-fdw-plugins-sql-cloud.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
