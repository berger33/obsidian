---
id: software.devops.tranche08.000778
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

# Bytebase: detecção automática de desvio de esquema (Schema Drift Detection) e histórico unificado de revisões

## Em uma frase
O Bytebase monitora periodicamente o esquema real dos bancos de dados gerenciados, comparando-o com o último estado registrado pelas Issues do Bytebase para detectar e alertar automaticamente sobre **Schema Drift** (alterações feitas por fora da plataforma).

## Por que importa
Mesmo quando uma empresa adota uma plataforma de governança de banco de dados, durante um incidente de madrugada um administrador ainda pode conectar-se diretamente ao banco com uma conta de emergência e criar um índice ou alterar uma coluna sem registrar no pipeline; se esse desvio (`schema drift`) passar despercebido, a próxima migração planejada falhará. O motor de Change Management do Bytebase rastreia e detecta essas divergências.

## Como funciona
Sempre que o Bytebase aplica uma Issue de alteração de esquema (`DDL`), ele grava um snapshot estruturado da versão atual do esquema no histórico do banco de dados. Em segundo plano, um job periódico de sincronização inspeciona o catálogo real dos bancos de dados conectados e compara o esquema vivo com o último snapshot esperado: caso encontre qualquer tabela, coluna ou índice criado, modificado ou removido por fora do fluxo do Bytebase, a plataforma levanta um alerta de **Schema Drift**, exibindo o diff exato entre o esquema esperado e o esquema real para que a equipe reconcilie a linha de base (`baseline`).

## Exemplo
```sql
-- Exemplo: se alguém executar diretamente no psql fora do Bytebase:
ALTER TABLE orders ADD COLUMN manual_hotfix_flag BOOLEAN DEFAULT false;
-- O detector de Schema Drift do Bytebase sinaliza a divergência no painel do banco de dados orders.
```

## Limites e trade-offs
Para que a detecção de Schema Drift seja eficaz e raramente acionada, revogue permissões de `CREATE`/`ALTER`/`DROP` das contas pessoais de desenvolvedores e mantenha as credenciais de escrita de esquema restritas exclusivamente à conta de serviço do Bytebase (e a um procedimento formal de break-glass auditado).

## Como verificar
No painel de um banco de dados de homologação conectado ao Bytebase, acione `Sync Now` após realizar uma alteração manual externa de teste e verifique o alerta de drift com o diff SQL correspondente.

## Conexões
- [[bytebase-rollout-multi-ambiente-batch-change-multi-tenant]] — Veja também: Bytebase: pipelines de rollout multi-ambiente (Test, Staging, Prod) e mudanças em lote para bancos multi-tenant/sharded.
- [[bytebase-bancos-suportados-relacionais-nosql-analiticos]] — Veja também: Bytebase: governança unificada para bancos relacionais, NoSQL (MongoDB, Redis) e analíticos (Snowflake, ClickHouse, Spanner).
- [[bytebase-plataforma-governanca-banco-dados-humanos-ia]] — Referência cruzada direta com bytebase-plataforma-governanca-banco-dados-humanos-ia.
- [[bytebase-governanca-mudancas-gui-gitops-200-regras-sql-lint]] — Referência cruzada direta com bytebase-governanca-mudancas-gui-gitops-200-regras-sql-lint.
- [[atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd]] — Referência cruzada direta com atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd.

## Fontes
- [Bytebase GitHub — README.md (Change Management, 200+ SQL Lint Rules, RBAC/JIT/Masking, Compliance & AI MCP Server)](https://raw.githubusercontent.com/bytebase/bytebase/main/README.md) — README oficial do Bytebase detalhando plano de controle único entre humanos, agentes de IA e bancos de dados, mais de 200 regras de SQL lint, RBAC fino, acesso JIT, Dynamic Data Masking, Terraform Provider e MCP Server; consultado em 2026-10-03.
- [Bytebase Official Documentation — Self-host vs. Cloud & Deployment Architecture](https://docs.bytebase.com/get-started/self-host-vs-cloud) — Documentação oficial do Bytebase comparando opções de implantação Self-hosted (Docker e Kubernetes Helm) e Cloud; consultado em 2026-10-03.
- [Bytebase — Official GitHub Repository](https://github.com/bytebase/bytebase) — Repositório oficial do Bytebase; consultado em 2026-10-03.
