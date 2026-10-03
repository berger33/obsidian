---
id: software.seguranca.tranche11.001001
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

# **CNCF Cartography (`cartography-cncf/cartography`)**: Arquitetura de Consolidação de Ativos de Infraestrutura, Nuvem, Kubernetes e Identidade em **Grafo Neo4j**

## Em uma frase
Criado originalmente na equipe de segurança da **Lyft** e hoje incubado como projeto oficial da **Cloud Native Computing Foundation (`cartography-cncf/cartography`, licença Apache 2.0)**, o **Cartography** é uma ferramenta em Python que extrai ativos e os relacionamentos implícitos entre eles a partir de **mais de 30 plataformas** (incluindo **AWS, GCP, Azure, Kubernetes, GitHub, Okta, Microsoft Entra ID, Keycloak, CrowdStrike Falcon, Cloudflare, Tailscale, OpenAI e Anthropic**) e os consolida em um banco de dados orientado a grafos **Neo4j**!

## Por que importa
Por que modelar a segurança de infraestrutura como um **Grafo de Propriedades (`Property Graph`) no Neo4j** em vez de apenas tabelas isoladas? Porque ataques reais atravessam fronteiras entre plataformas: um desenvolvedor autentica no **Okta/Entra ID**, assume via federação SAML/OIDC uma **IAM Role na AWS**, que tem permissão de administração sobre um cluster **EKS**, onde roda um Pod cuja imagem em **ECR** contém uma **CVE crítica explorada na CISA KEV**!

## Como funciona
No Cartography, cada etapa de sincronização executa quatro fases: **(1) Ingestão (`sync`)** dos nós e arestas via APIs oficiais; **(2) Enriquecimento (`analysis jobs`)** que calcula propriedades derivadas de risco (como `exposed_internet: true` e `anonymous_access: true`); **(3) Execução de `cartography-rules`**; e **(4) Limpeza (`cleanup`)** de nós obsoletos via `UPDATE_TAG`!

## Exemplo
```bash
# Instalar o Cartography com o codec Rust Bolt de alta performance e sincronizar modulos AWS, Kubernetes e GitHub no Neo4j
pip install "cartography[neo4j-rust]"
cartography \
  --neo4j-uri bolt://127.0.0.1:7687 \
  --neo4j-user neo4j \
  --neo4j-password-env-var NEO4J_PASSWORD \
  --selected-modules aws,kubernetes,github
```

## Limites e trade-offs
Dica de performance documentada no `README.md` oficial: instalar o extra **`cartography[neo4j-rust]`** substitui o codec Bolt padrão em Python pelo codec nativo em Rust do driver Neo4j, **reduzindo o tempo total de sincronização em 20% a 30%** em grandes ambientes multi-conta!

## Como verificar
Confirme que a interface web do Neo4j Browser (`http://localhost:7474`) ou o protocolo Bolt (`bolt://localhost:7687`) estão ativos antes de iniciar o `cartography`.

## Conexões
- [[cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3]] — Veja também: Cartography **Data Enrichment (`Analysis Jobs`)**: Como São Calculados os Atributos Derivados **`exposed_internet: true`** e **`anonymous_access: true`**.
- [[cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s]] — Referência cruzada direta com cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s.
- [[cloudquery-grafo-ativos-seguranca-neo4j-caminhos-ataque-iam-rede]] — Referência cruzada direta com cloudquery-grafo-ativos-seguranca-neo4j-caminhos-ataque-iam-rede.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
