---
id: software.seguranca.tranche04.000322
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

# Brakeman: Níveis de Confiança (`High`, `Medium`, `Weak`) e Sensibilidade de Fluxo (`--branch-limit`)

## Em uma frase
O Brakeman classifica cada alerta em três níveis de confiança (`High`, `Medium` e `Weak`) com base na certeza de que um dado controlado pelo usuário (`params`, `cookies`, `request.env`) atinge diretamente uma operação insegura.

## Por que importa
Permite bloquear *pull requests* imediatamente em alertas `High` (`-w3`) sem paralisar a engenharia com alertas especulativos onde uma variável intermediária pode ou não conter entrada não confiável.

## Como funciona
Um alerta recebe confiança **High** (`-w3`) quando `params[:id]` é interpolado diretamente em um sink perigoso ou quando uma configuração booleana crítica está desativada; **Medium** (`-w2`) quando uma variável local/instância é usada de modo inseguro sem certeza absoluta de origem externa; e **Weak** (`-w1`) quando a entrada do usuário passa por transformações indiretas ou atributos de banco. O motor rastreia ramificações condicionais (`if`/`case`) até `--branch-limit 5` por padrão.

## Exemplo
```bash
# Falhar o pipeline apenas para alertas de confiança High (-w3) mantendo análise completa de branches
brakeman -w3 --branch-limit 10 --no-pager
```

## Limites e trade-offs
Usar `--faster` (equivalente a `--skip-libs --no-branching`) acelera a execução em monorepos gigantes, mas desativa a sensibilidade de fluxo em expressões `if/else` e ignora código em `lib/`, podendo ocultar vulnerabilidades reais.

## Como verificar
Execute `brakeman -w2 -f json | jq '.warnings | group_by(.confidence) | map({confidence: .[0].confidence, total: length})'` para auditar a distribuição de alertas por nível de confiança.

## Conexões
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Veja também: Brakeman: Arquitetura de Análise Estática *Whole-Program* para Aplicações Ruby on Rails.
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Veja também: Brakeman: Detecção de SQL Injection (`CheckSQL`) em ActiveRecord, Interpolação de Strings e Arel.
- [[brakeman-gerenciamento-falsos-positivos-brakeman-ignore-interativo]] — Referência cruzada direta com brakeman-gerenciamento-falsos-positivos-brakeman-ignore-interativo.
- [[brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml]] — Referência cruzada direta com brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
