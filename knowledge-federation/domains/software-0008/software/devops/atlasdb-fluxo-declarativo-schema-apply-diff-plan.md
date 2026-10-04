---
id: software.devops.tranche08.000763
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

# Ariga Atlas: fluxo declarativo (atlas schema diff e atlas schema apply) com dev-url para normalização

## Em uma frase
No fluxo declarativo do Atlas, `atlas schema diff` compara dois estados de esquema (banco ativo, arquivo `.hcl`/`.sql` ou ORM) e `atlas schema apply` calcula o diff, exibe o SQL planejado e aplica as mudanças após confirmação ou `--auto-approve`.

## Por que importa
Durante o desenvolvimento ou ao gerenciar esquemas declarativos como infraestrutura como código, escrever scripts `ALTER TABLE` manualmente para adicionar cada coluna ou índice é repetitivo e propenso a erros de dialeto SQL. A seção `Declarative Workflow` do README oficial e o guia `Getting Started` (`atlasgo.io/getting-started`) mostram como o Atlas automatiza esse cálculo usando um `dev-url` para normalização.

## Como funciona
Para comparar o estado desejado (ex.: `file://schema.sql` ou `file://schema.hcl`) com o banco alvo (`-u`), o Atlas utiliza um **Dev Database** (`--dev-url "docker://postgres/15/dev"` ou `"docker://mysql/8/dev"`): o Atlas sobe temporariamente um container limpo do motor exato do banco, aplica o esquema desejado nele para que o próprio SGBD normalize tipos, defaults e expressões (ex.: `INT` -> `int(11)` ou `SERIAL` -> `integer` + `sequence`), inspeciona ambos os lados e calcula o plano SQL exato de transição. Com `atlas schema diff --from ... --to ...`, o operador apenas visualiza as diferenças; com `atlas schema apply -u ... --to ...`, o Atlas exibe o plano SQL (`-- Plan:`) e aguarda aprovação interativa (`Apply` / `Abort`) ou aplica diretamente com `--auto-approve`.

## Exemplo
```bash
# Comparar e aplicar declarativamente um arquivo schema.sql contra um banco MySQL usando um container Docker efêmero como dev-url
atlas schema diff \
  --from "mysql://root:pass@localhost:3306/example" \
  --to "file://schema.sql" \
  --dev-url "docker://mysql/8/dev"

atlas schema apply \
  -u "mysql://root:pass@localhost:3306/example" \
  --to "file://schema.sql" \
  --dev-url "docker://mysql/8/dev"
```

## Limites e trade-offs
O parâmetro `--dev-url` precisa apontar para um banco de dados temporário vazio (preferencialmente usando o driver `docker://...` que cria e destrói um container efêmero automaticamente), pois o Atlas limpa e recria objetos dentro do `dev-url` durante o processo de normalização; **jamais** passe a URL de um banco de produção ou homologação compartilhada como `--dev-url`.

## Como verificar
Após aplicar as mudanças com `atlas schema apply`, execute o mesmo comando uma segunda vez e confirme que o Atlas reporta `Schema isSynced: no changes to be made` (idempotência).

## Conexões
- [[atlasdb-inspecao-esquema-hcl-sql-json-mermaid-erd]] — Veja também: Ariga Atlas: inspeção de esquemas (atlas schema inspect) em HCL, SQL dividido por arquivo, JSON e diagramas ERD Mermaid.
- [[atlasdb-fluxo-versionado-migrate-diff-lint-apply]] — Veja também: Ariga Atlas: fluxo versionado com geração automática de migrações (atlas migrate diff, lint e apply).
- [[atlasdb-schema-as-code-declarativo-versionado-multibanco]] — Referência cruzada direta com atlasdb-schema-as-code-declarativo-versionado-multibanco.

## Fontes
- [Ariga Atlas GitHub — README.md (Declarative & Versioned Workflows, 50+ Lint Analyzers, 16 ORMs, Schema Test & Security-as-Code)](https://raw.githubusercontent.com/ariga/atlas/master/README.md) — README oficial do Ariga Atlas documentando schema inspect (HCL, SQL, JSON, Mermaid ERD), schema apply/diff, migrate diff/lint/apply, 16 ORMs, testes unitários .test.hcl, Security-as-Code (RLS/RBAC), Terraform Provider e Kubernetes Operator; consultado em 2026-10-03.
- [Ariga Atlas Official Documentation — Getting Started with Atlas](https://atlasgo.io/getting-started) — Guia oficial do Atlas (atlasgo.io) sobre uso de dev-url, inspeção e migrações declarativas e versionadas; consultado em 2026-10-03.
- [Ariga Atlas — Official GitHub Repository](https://github.com/ariga/atlas) — Repositório oficial do Ariga Atlas; consultado em 2026-10-03.
