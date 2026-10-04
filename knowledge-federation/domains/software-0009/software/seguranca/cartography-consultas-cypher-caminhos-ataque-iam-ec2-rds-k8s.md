---
id: software.seguranca.tranche11.001003
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

# Threat Hunting e Descoberta de **Caminhos de Ataque (*Attack Paths*)** no Cartography com Consultas **OpenCypher** Multi-Hop

## Em uma frase
Enquanto consultas SQL exigem saber de antemão quantos `JOIN`s existem entre uma origem e um destino, a linguagem **Cypher** do Neo4j permite buscar **caminhos de comprimento variável (`-[*1..6]->` e `shortestPath(...)`)** através de qualquer combinação de identidades, grupos, roles, instâncias e bancos de dados!

## Por que importa
No grafo do Cartography, isso permite responder em segundos à pergunta central de **Gestão de Exposição (CTEM) e Red/Purple Team**: *"Existe algum caminho pelo qual uma instância EC2 exposta à internet (`exposed_internet: true`) possa assumir um Instance Profile / IAM Role que tenha permissão para ler ou modificar um banco RDS de produção ou um bucket S3 confidencial?"*

## Como funciona
Da mesma forma, você pode explorar o esquema dinamicamente sem decorar todos os rótulos rodando **`MATCH (d:DNSRecord)--(n) RETURN DISTINCT labels(n)`** para descobrir quais tipos de ativos estão conectados aos seus registros DNS!

## Exemplo
```cypher
// Encontrar caminhos de ataque completos desde a Internet -> EC2 Exposta -> IAM Role -> Recurso Sensivel (S3 ou RDS sem criptografia)
MATCH path = (i:AWSEC2Instance {exposed_internet: true})-[*1..4]->(target)
WHERE (target:AWSS3Bucket) OR (target:AWSRDSInstance AND target.storage_encrypted = false)
RETURN i.instanceid AS ec2_origem,
       [n IN nodes(path) | coalesce(n.name, n.id, n.arn)] AS cadeia_ataque,
       labels(target) AS tipo_alvo;
```

## Limites e trade-offs
Compreenda o valor estratégico da query `MATCH path = (i:AWSEC2Instance {exposed_internet: true})-[*1..4]->(target)` acima: um scanner tradicional emitiria um alerta "Médio" para a porta aberta na EC2 e outro alerta "Baixo" para uma permissão S3 na IAM Role; já o grafo do Cartography mostra que **os dois juntos formam um caminho direto da internet pública até os dados críticos da empresa**!

## Como verificar
Use `RETURN *` no Neo4j Browser quando quiser visualizar os nós e arestas graficamente em vez de em formato tabular.

## Conexões
- [[cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3]] — Veja também: Cartography **Data Enrichment (`Analysis Jobs`)**: Como São Calculados os Atributos Derivados **`exposed_internet: true`** e **`anonymous_access: true`**.
- [[cartography-identidade-federada-okta-entra-aws-github-keycloak]] — Veja também: Grafo de Identidade Cross-Platform no Cartography: Correlacionando **Okta, Microsoft Entra ID, Keycloak, Google Workspace, GitHub e AWS IAM**.
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
