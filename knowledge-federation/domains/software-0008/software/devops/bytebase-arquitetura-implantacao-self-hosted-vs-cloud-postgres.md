---
id: software.devops.tranche08.000776
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

# Bytebase: opções de implantação (Self-hosted via Docker/Kubernetes vs Bytebase Cloud) e banco de metadados PostgreSQL

## Em uma frase
O Bytebase pode ser consumido como serviço gerenciado (**Bytebase Cloud**) ou auto-hospedado (**Self-hosted** via Docker ou Helm chart no Kubernetes), suportando armazenamento de metadados em PostgreSQL embutido no container ou em instância PostgreSQL externa (`--pg`).

## Por que importa
Equipes de plataforma precisam escolher entre a agilidade de não gerenciar infraestrutura (Bytebase Cloud) ou manter todo o tráfego de banco de dados dentro da VPC privada corporativa (Self-hosted), além de configurar alta disponibilidade para o banco de metadados do próprio Bytebase. A página oficial `Self-host vs. Cloud` (`docs.bytebase.com/get-started/self-host-vs-cloud`) compara ambos os modelos.

## Como funciona
(1) **Bytebase Cloud**: hospedado e atualizado pela equipe do Bytebase, permitindo provisionar uma instância em segundos para avaliar ou gerenciar bancos acessíveis; (2) **Self-hosted**: implantado dentro da rede privada da organização via imagem Docker `bytebase/bytebase` ou Helm chart `bytebase/bytebase` no Kubernetes. No modo self-hosted, por padrão o container inicializa um PostgreSQL embutido gravando no diretório `/var/opt/bytebase`; para ambientes de produção críticos, o operador passa a flag `--pg="postgresql://user:pwd@host:5432/bytebase"` (ou variável `PG_URL`) para que o Bytebase armazene seu estado em um cluster PostgreSQL externo gerenciado (como AWS RDS, Cloud SQL ou CloudNativePG) com backups e réplicas.

## Exemplo
```bash
# Iniciar o Bytebase em produção apontando para um banco PostgreSQL externo de metadados via --pg
docker run --init \
  --name bytebase-prod \
  --publish 8080:8080 \
  --volume ~/.bytebase/data:/var/opt/bytebase \
  bytebase/bytebase:latest \
  --pg "postgresql://bytebase:secret@pg-meta.internal:5432/bytebase"
```

## Limites e trade-offs
Ao usar o Bytebase Cloud para gerenciar bancos de dados que residem em sub-redes privadas de nuvem (AWS VPC, GCP VPC, Azure VNet), é necessário configurar conectividade segura (peering/bastion/whitelist de IP); já o modo Self-hosted roda dentro da própria VPC ao lado dos bancos de dados privados sem expor portas de banco para a internet.

## Como verificar
Nos logs de inicialização do container `bytebase`, confirme a conexão bem-sucedida ao banco de metadados PostgreSQL externo configurado em `--pg` e verifique o endpoint `/healthz`.

## Conexões
- [[bytebase-integracao-ia-mcp-server-text-to-sql-page-agent]] — Veja também: Bytebase: governança para agentes de IA com MCP Server, Text-to-SQL no SQL Editor e Page Agent.
- [[bytebase-rollout-multi-ambiente-batch-change-multi-tenant]] — Veja também: Bytebase: pipelines de rollout multi-ambiente (Test, Staging, Prod) e mudanças em lote para bancos multi-tenant/sharded.
- [[bytebase-plataforma-governanca-banco-dados-humanos-ia]] — Referência cruzada direta com bytebase-plataforma-governanca-banco-dados-humanos-ia.
- [[bytebase-governanca-mudancas-gui-gitops-200-regras-sql-lint]] — Referência cruzada direta com bytebase-governanca-mudancas-gui-gitops-200-regras-sql-lint.
- [[bytebase-edicoes-community-pro-enterprise-licenciamento]] — Referência cruzada direta com bytebase-edicoes-community-pro-enterprise-licenciamento.

## Fontes
- [Bytebase GitHub — README.md (Change Management, 200+ SQL Lint Rules, RBAC/JIT/Masking, Compliance & AI MCP Server)](https://raw.githubusercontent.com/bytebase/bytebase/main/README.md) — README oficial do Bytebase detalhando plano de controle único entre humanos, agentes de IA e bancos de dados, mais de 200 regras de SQL lint, RBAC fino, acesso JIT, Dynamic Data Masking, Terraform Provider e MCP Server; consultado em 2026-10-03.
- [Bytebase Official Documentation — Self-host vs. Cloud & Deployment Architecture](https://docs.bytebase.com/get-started/self-host-vs-cloud) — Documentação oficial do Bytebase comparando opções de implantação Self-hosted (Docker e Kubernetes Helm) e Cloud; consultado em 2026-10-03.
- [Bytebase — Official GitHub Repository](https://github.com/bytebase/bytebase) — Repositório oficial do Bytebase; consultado em 2026-10-03.
