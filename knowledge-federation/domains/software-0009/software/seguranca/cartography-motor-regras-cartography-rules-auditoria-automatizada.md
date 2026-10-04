---
id: software.seguranca.tranche11.001005
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

# Execução Automatizada de Regras de Segurança no Grafo com **`cartography-rules`** (`list`, `run`, `object_storage_public` e Frameworks)

## Em uma frase
Além da exploração visual no Neo4j Browser, o Cartography inclui a ferramenta de linha de comando **`cartography-rules`**, que executa **Regras de Segurança e Conformidade baseadas em Grafo** diretamente contra a base Neo4j populada pelo `cartography`!

## Por que importa
Por que validar regras de segurança sobre o grafo com `cartography-rules`? Porque uma regra no Cartography não verifica apenas um atributo isolado de um único recurso: ela pode expressar condições topológicas complexas em Cypher (como almacenamiento de objetos público, bancos de dados sem criptografia acessíveis por workloads expostos, ou identidades sem MFA com caminhos para dados críticos)!

## Como funciona
O uso no terminal ou em pipelines de CI/CD é direto: **`cartography-rules list`** exibe os pacotes de regras disponíveis, **`cartography-rules list <regra>`** detalha os requisitos de uma regra específica (ex.: `object_storage_public`), e **`cartography-rules run <regra|all>`** executa as consultas contra o Neo4j e retorna os ativos violadores!

## Exemplo
```bash
# Listar todas as regras de seguranca embutidas no Cartography e executar a verificacao de buckets/storage publicos
export NEO4J_PASSWORD="senha-segura-neo4j-prod"
cartography-rules list
cartography-rules list object_storage_public
cartography-rules run object_storage_public --uri bolt://127.0.0.1:7687 --user neo4j
```

## Limites e trade-offs
Integre a execução de **`cartography-rules run`** logo após o término do job diário de sincronização do `cartography`, enviando qualquer retorno não-vazio diretamente para o seu **SIEM**, **DefectDojo** ou canal de engenharia de segurança.

## Como verificar
Use sempre a variável de ambiente `NEO4J_PASSWORD` (ou `--neo4j-password-env-var`) para nunca expor a senha do banco Neo4j na linha de comando (`ps aux`).

## Conexões
- [[cartography-identidade-federada-okta-entra-aws-github-keycloak]] — Veja também: Grafo de Identidade Cross-Platform no Cartography: Correlacionando **Okta, Microsoft Entra ID, Keycloak, Google Workspace, GitHub e AWS IAM**.
- [[cartography-gestao-vulnerabilidades-cves-epss-kev-crowdstrike-ecr]] — Veja também: Priorização de Vulnerabilidades Baseada em Contexto no Cartography: Cruzando **CrowdStrike Spotlight, AWS ECR/Inspector, EPSS e CISA KEV**.
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3]] — Referência cruzada direta com cartography-enriquecimento-dados-analysis-jobs-exposed-internet-s3.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
