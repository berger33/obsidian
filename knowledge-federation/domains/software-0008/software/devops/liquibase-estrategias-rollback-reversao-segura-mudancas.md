---
id: software.devops.tranche08.000748
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
fontes: ["https://raw.githubusercontent.com/liquibase/liquibase/master/README.md", "https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md", "https://github.com/liquibase/liquibase"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Liquibase: estratégias de reversão de esquema (rollback por tag, contagem ou data) e validação prévia

## Em uma frase
O Liquibase permite reverter alterações de banco de dados de forma controlada (`rollback`, `rollback-count`, `rollback-to-date`) utilizando instruções de rollback auto-geradas (em changelogs XML/YAML/JSON) ou blocos `--rollback` explícitos (em changelogs SQL).

## Por que importa
Quando o deploy de uma nova versão de aplicação apresenta falhas críticas em produção e precisa ser revertido, reverter apenas a imagem do container no Kubernetes pode não ser suficiente se a migração de banco de dados alterou estruturas ou constraints incompatíveis com a versão anterior do código. Segundo o README oficial do Liquibase, facilitar o rollback de mudanças é um dos pilares centrais da ferramenta.

## Como funciona
Para changesets declarativos (XML, YAML, JSON) que contêm apenas operações reversíveis puras (como `createTable`, `addColumn` ou `createIndex`), o Liquibase consegue deduzir automaticamente a instrução inversa (`DROP TABLE`, `DROP COLUMN`, `DROP INDEX`). Já para changesets escritos em SQL formatado (`--liquibase formatted sql`) ou para operações destrutivas/complexas, o autor declara explicitamente a cláusula `--rollback <SQL>` (ou `<rollback>` no XML/YAML). Ao executar um rollback apontando para uma tag criada previamente (`liquibase tag v1.4.0` -> `liquibase rollback v1.4.0`) ou um número de changesets (`liquibase rollback-count 1`), o Liquibase executa os scripts inversos em ordem reversa e remove as linhas correspondentes da tabela `DATABASECHANGELOG`.

## Exemplo
```bash
# Marcar o estado atual do banco com uma tag de versão, aplicar update e simular o SQL de rollback (future-rollback-sql)
liquibase tag release-2026-10
liquibase update
liquibase future-rollback-sql
```

## Limites e trade-offs
Reverter um `createTable` executando `DROP TABLE` apaga permanentemente quaisquer linhas que tenham sido inseridas naquela tabela durante os minutos em que a versão nova esteve no ar; por isso, em sistemas críticos 24x7, prefira o padrão **expand-and-contract** (migrações retrocompatíveis onde a versão `N` adiciona colunas opcionais sem quebrar a versão `N-1`) e valide sempre os scripts de reversão antes do deploy usando `liquibase future-rollback-sql`.

## Como verificar
Inclua `liquibase future-rollback-sql` no seu pipeline de CI/CD para garantir que nenhum changeset novo seja mesclado sem possuir um caminho de rollback válido definido.

## Conexões
- [[liquibase-formatos-changelog-sql-xml-yaml-json-changesets]] — Veja também: Liquibase: formatos de Changelog (SQL, XML, YAML, JSON), ordenação de Changesets e Checksums.
- [[liquibase-migracao-4-x-para-5-0-checklist-producao]] — Veja também: Liquibase: guia prático de atualização do Liquibase 4.x para 5.0+ em pipelines e produção.
- [[liquibase-gerenciamento-mudancas-esquema-banco-dados]] — Referência cruzada direta com liquibase-gerenciamento-mudancas-esquema-banco-dados.
- [[atlasdb-linting-migracoes-50-analisadores-seguranca]] — Referência cruzada direta com atlasdb-linting-migracoes-50-analisadores-seguranca.

## Fontes
- [Liquibase GitHub — README.md (Database Schema Change Management, Quarterly Releases & CI/CD Integrations)](https://raw.githubusercontent.com/liquibase/liquibase/master/README.md) — README oficial do Liquibase cobrindo rastreamento e rollback de mudanças de banco de dados, fluxo com H2, cadência de releases trimestrais/nightly e gate de aprovação Sonatype; consultado em 2026-10-03.
- [Liquibase Docker Documentation — docker/README.md (Liquibase 5.0 FSL vs Secure, LPM Drivers & Migration Guide)](https://raw.githubusercontent.com/liquibase/liquibase/main/docker/README.md) — Documentação oficial de imagens Docker do Liquibase detalhando o licenciamento 5.0+ (Community FSL vs Secure), remoção de drivers embutidos por padrão, uso do Liquibase Package Manager (lpm add --global) e roteiro de migração de 6 etapas; consultado em 2026-10-03.
- [Liquibase — Official GitHub Repository](https://github.com/liquibase/liquibase) — Repositório oficial do Liquibase; consultado em 2026-10-03.
