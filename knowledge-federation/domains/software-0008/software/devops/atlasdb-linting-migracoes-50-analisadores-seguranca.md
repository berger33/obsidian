---
id: software.devops.tranche08.000765
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
fontes: ["https://raw.githubusercontent.com/ariga/atlas/master/README.md", "https://atlasgo.io/versioned/lint", "https://github.com/ariga/atlas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ariga Atlas: análise estática e linting de migrações (atlas migrate lint) com mais de 50 analisadores de risco

## Em uma frase
O comando `atlas migrate lint` analisa arquivos de migração SQL usando mais de 50 analisadores especializados para detectar alterações destrutivas (`DROP TABLE`/`DROP COLUMN`), mudanças dependentes de dados (adição de índice único ou coluna `NOT NULL` sem default), locks de tabela e regressões de performance.

## Por que importa
Uma migração SQL sintaticamente válida que passa nos testes unitários com 10 linhas de dados pode causar horas de indisponibilidade em produção se tentar adicionar uma coluna `NOT NULL` sem valor padrão, criar um índice único sobre dados duplicados existentes ou adquirir um lock exclusivo em uma tabela de 100 milhões de linhas. A seção `Versioned Workflow` e `What is Atlas?` do README oficial destacam os 50+ analisadores do `atlas migrate lint`.

## Como funciona
Ao executar `atlas migrate lint --dir "file://migrations" --dev-url "docker://mysql/8/dev" --latest 1` (ou comparando com a branch base no Git via `--git-base`), o Atlas simula a aplicação das migrações anteriores e da migração nova no `--dev-url`, inspeciona a árvore sintática (AST) de cada instrução SQL e a evolução do catálogo do SGBD, e executa mais de 50 verificadores específicos do dialeto do banco (MySQL, Postgres, SQL Server, etc.). Caso detecte uma operação destrutiva (ex.: `Dropping non-virtual column "name"`) ou perigosa, o comando imprime diagnósticos detalhados com códigos de referência (ex.: `DS103`, `MF101`) e retorna código de saída diferente de zero para bloquear o Pull Request no CI.

## Exemplo
```bash
# Analisar a última migração criada no diretório migrations/ em busca de mudanças destrutivas ou locks perigosos
atlas migrate lint \
  --dir "file://migrations" \
  --dev-url "docker://postgres/15/dev" \
  --latest 1
```

## Limites e trade-offs
Quando uma remoção de coluna (`DROP COLUMN`) ou tabela (`DROP TABLE`) é intencional e faz parte da fase final de limpeza (contract) de uma migração em duas etapas já validada pela equipe, o `atlas migrate lint` bloqueará o PR por padrão sob a política de `destructive changes`; nesses casos, o autor deve adicionar a diretiva de comentário explícita (`-- atlas:nolint DS103`) no topo do arquivo SQL daquela migração para documentar e autorizar a exceção de forma auditável.

## Como verificar
Adicione temporariamente uma instrução `ALTER TABLE users DROP COLUMN email;` em uma migração de teste e execute `atlas migrate lint --latest 1` para confirmar que o analisador detecta e bloqueia a mudança destrutiva.

## Conexões
- [[atlasdb-fluxo-versionado-migrate-diff-lint-apply]] — Veja também: Ariga Atlas: fluxo versionado com geração automática de migrações (atlas migrate diff, lint e apply).
- [[atlasdb-integracao-16-orms-go-ts-python-java-dotnet-php]] — Veja também: Ariga Atlas: carregamento automático de esquema a partir de 16 ORMs em Go, TypeScript, Python, Java, C#/.NET e PHP.
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[bytebase-governanca-mudancas-gui-gitops-200-regras-sql-lint]] — Referência cruzada direta com bytebase-governanca-mudancas-gui-gitops-200-regras-sql-lint.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/versioned/lint) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
