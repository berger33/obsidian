---
id: software.seguranca.tranche04.000330
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md", "https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md", "https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Brakeman: Configuração Declarativa (`config/brakeman.yml`), Comparação Delta (`--compare`) e SARIF no CI/CD

## Em uma frase
O Brakeman suporta configuração declarativa versionada em `config/brakeman.yml`, comparação diferencial entre scans (`--compare baseline.json`) e exportação nativa em formato SARIF (`-f sarif`) para integração com GitHub Code Scanning.

## Por que importa
Em monorepos Rails legados com dezenas de alertas antigos, o modo `--compare` permite bloquear *pull requests* que introduzam qualquer alerta novo (`new` warnings > 0) enquanto a dívida técnica anterior é reduzida gradualmente.

## Como funciona
O comando `brakeman -C` exporta as flags de linha de comando para `config/brakeman.yml`. No pipeline de CI, o Brakeman gera `brakeman.sarif` para anotações inline no GitHub Pull Request ou executa `brakeman --compare main-report.json -o diff.json`, que separa os achados em duas listas: `fixed` (corrigidos) e `new` (introduzidos no branch).

## Exemplo
```yaml
# config/brakeman.yml versionado no repositório Rails
---
:run_all_checks: true
:confidence_level: 2
:exit_on_warn: true
:exit_on_error: true
:ignore_file: config/brakeman.ignore
:output_files:
  - tmp/brakeman.sarif
  - tmp/brakeman.json
```

## Limites e trade-offs
Se o pipeline de CI for executado com `--no-exit-on-warn` para apenas fazer upload do arquivo SARIF e o GitHub Advanced Security não estiver configurado como *required status check*, alertas críticos passarão no merge sem bloqueio.

## Como verificar
Execute `brakeman -c config/brakeman.yml` no CI e valide que o processo retorna exit code `0` e gera `tmp/brakeman.sarif` com `runs[0].results` vazio para alertas ativos.

## Conexões
- [[brakeman-gerenciamento-falsos-positivos-brakeman-ignore-interativo]] — Veja também: Brakeman: Gestão Auditável de Falsos Positivos com `config/brakeman.ignore` (`-I` e `--show-ignored`).
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.
- [[brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching]] — Referência cruzada direta com brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
