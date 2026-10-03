---
id: software.devops.tranche08.000780
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/bytebase/bytebase/main/README.md", "https://docs.bytebase.com/get-started/self-host-vs-cloud", "https://github.com/bytebase/bytebase"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Bytebase: modelo open-source e diferenças entre as edições Community, Pro e Enterprise

## Em uma frase
O Bytebase é desenvolvido abertamente no repositório `bytebase/bytebase` e distribuído em uma única imagem/binário que opera por padrão na edição gratuita **Community** e desbloqueia recursos avançados nas edições **Pro** e **Enterprise** mediante licença.

## Por que importa
Ao planejar a adoção do Bytebase como plano de controle de banco de dados, arquitetos e gestores precisam saber quais funcionalidades estão disponíveis gratuitamente na edição Community auto-hospedada e quais recursos corporativos (como SSO empresarial avançado, fluxos de aprovação customizados multi-nível, Dynamic Data Masking avançado e JIT access em larga escala) pertencem aos planos Pro e Enterprise. A documentação oficial `Self-host vs. Cloud` e `Pricing` detalha esse modelo.

## Como funciona
Diferentemente de produtos que exigem reinstalar outra imagem de container para mudar de edição, o Bytebase empacota todas as capacidades na mesma imagem oficial `bytebase/bytebase:latest`. Sem chave de licença, a instância roda na edição **Community**, oferecendo gerenciamento de mudanças GUI/GitOps, SQL Review com regras de lint, SQL Editor e suporte aos bancos de dados suportados. Para equipes maiores que necessitam de fluxos de rollout e aprovação customizados (**Pro**) ou organizações com requisitos estritos de segurança como SSO/SCIM, RBAC granular, Dynamic Data Masking, Just-in-Time Access, Audit Log estendido e SLA dedicado (**Enterprise**), basta carregar a chave de licença no painel administrativo da própria instância.

## Exemplo
```bash
# Inspecionar a imagem oficial única bytebase/bytebase que atende às edições Community, Pro e Enterprise
docker image inspect bytebase/bytebase:latest --format '{{.Config.ExposedPorts}} {{.Config.Entrypoint}}'
```

## Limites e trade-offs
O repositório `bytebase/bytebase` utiliza um modelo open-core (onde o núcleo do produto está sob licença aberta Apache-2.0 e o diretório de extensões proprietárias Enterprise reside na árvore com licença comercial específica); portanto, se uma equipe decidir redistribuir versões modificadas do Bytebase comercialmente, deve observar os arquivos `LICENSE` de cada diretório do repositório.

## Como verificar
Acesse `Settings -> Subscription` no console do Bytebase auto-hospedado para verificar o plano ativo da instância (`Community`, `Pro` ou `Enterprise`) e os limites aplicáveis.

## Conexões
- [[bytebase-bancos-suportados-relacionais-nosql-analiticos]] — Veja também: Bytebase: governança unificada para bancos relacionais, NoSQL (MongoDB, Redis) e analíticos (Snowflake, ClickHouse, Spanner).
- [[bytebase-plataforma-governanca-banco-dados-humanos-ia]] — Referência cruzada direta com bytebase-plataforma-governanca-banco-dados-humanos-ia.
- [[bytebase-arquitetura-implantacao-self-hosted-vs-cloud-postgres]] — Referência cruzada direta com bytebase-arquitetura-implantacao-self-hosted-vs-cloud-postgres.
- [[liquibase-mudancas-versao-5-0-licenca-fsl-community-secure]] — Referência cruzada direta com liquibase-mudancas-versao-5-0-licenca-fsl-community-secure.

## Fontes
- [Bytebase GitHub — README.md (Change Management, 200+ SQL Lint Rules, RBAC/JIT/Masking, Compliance & AI MCP Server)](https://raw.githubusercontent.com/bytebase/bytebase/main/README.md) — README oficial do Bytebase detalhando plano de controle único entre humanos, agentes de IA e bancos de dados, mais de 200 regras de SQL lint, RBAC fino, acesso JIT, Dynamic Data Masking, Terraform Provider e MCP Server; consultado em 2026-10-03.
- [Bytebase Official Documentation — Self-host vs. Cloud & Deployment Architecture](https://docs.bytebase.com/get-started/self-host-vs-cloud) — Documentação oficial do Bytebase comparando opções de implantação Self-hosted (Docker e Kubernetes Helm) e Cloud; consultado em 2026-10-03.
- [Bytebase — Official GitHub Repository](https://github.com/bytebase/bytebase) — Repositório oficial do Bytebase; consultado em 2026-10-03.
