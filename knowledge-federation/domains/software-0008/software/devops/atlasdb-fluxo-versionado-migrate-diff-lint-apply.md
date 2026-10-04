---
id: software.devops.tranche08.000764
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
fontes: ["https://raw.githubusercontent.com/ariga/atlas/master/README.md", "https://atlasgo.io/getting-started", "https://github.com/ariga/atlas"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ariga Atlas: fluxo versionado com geração automática de migrações (atlas migrate diff, lint e apply)

## Em uma frase
No fluxo versionado do Atlas, `atlas migrate diff` gera automaticamente os arquivos de migração SQL no diretório `migrations/` (junto ao arquivo de integridade `atlas.sum`) comparando o diretório de migrações existentes com o estado desejado, seguidos por `atlas migrate lint` e `atlas migrate apply`.

## Por que importa
Equipes que exigem controle estrito de cada script SQL versionado no Git não precisam abrir mão da produtividade declarativa: em vez de escrever o arquivo `20261003_add_users.sql` à mão, o desenvolvedor edita o esquema desejado (no seu ORM, SQL ou HCL) e deixa o Atlas calcular e gerar o script versionado automaticamente. A seção `Versioned Workflow` do README oficial do Atlas detalha esse ciclo.

## Como funciona
(1) **Planejamento (`atlas migrate diff`)**: o comando lê todas as migrações já existentes em `--dir "file://migrations"`, aplica-as no `--dev-url` para descobrir o estado atual das migrações, compara com o estado desejado em `--to "file://schema.hcl"` (ou ORM) e grava um novo arquivo `<timestamp>_<name>.sql` contendo apenas o delta necessário, atualizando os hashes criptográficos no arquivo `atlas.sum`; (2) **Verificação (`atlas migrate lint`)**: analisa as novas migrações em busca de mudanças destrutivas ou perigosas; e (3) **Execução (`atlas migrate apply`)**: conecta-se ao banco de destino (`-u`) e aplica em ordem as migrações pendentes do diretório `--dir "file://migrations"`, registrando o progresso na tabela de revisões `atlas_schema_revisions`.

## Exemplo
```bash
# Gerar automaticamente uma nova migração versionada a partir do schema.hcl e aplicá-la no banco alvo
atlas migrate diff create_users \
  --dir "file://migrations" \
  --to "file://schema.hcl" \
  --dev-url "docker://mysql/8/dev"

atlas migrate apply \
  --dir "file://migrations" \
  -u "mysql://root:pass@localhost:3306/example"
```

## Limites e trade-offs
Se um desenvolvedor editar manualmente um arquivo `.sql` dentro do diretório `migrations/` (por exemplo, para adicionar um `UPDATE` de backfilling de dados logo após o `atlas migrate diff`), o hash daquele arquivo deixará de bater com o registrado no `atlas.sum` e o Atlas recusará a execução até que o desenvolvedor execute `atlas migrate hash` para recalcular e assinar o `atlas.sum` atualizado.

## Como verificar
Inspecione o arquivo `migrations/atlas.sum` gerado pelo `atlas migrate diff` e execute `atlas migrate validate --dir "file://migrations"` para confirmar a integridade da cadeia de migrações.

## Conexões
- [[atlasdb-fluxo-declarativo-schema-apply-diff-plan]] — Veja também: Ariga Atlas: fluxo declarativo (atlas schema diff e atlas schema apply) com dev-url para normalização.
- [[atlasdb-linting-migracoes-50-analisadores-seguranca]] — Veja também: Ariga Atlas: análise estática e linting de migrações (atlas migrate lint) com mais de 50 analisadores de risco.
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.
- [[atlasdb-integracao-16-orms-go-ts-python-java-dotnet-php]] — Referência cruzada direta com atlasdb-integracao-16-orms-go-ts-python-java-dotnet-php.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
