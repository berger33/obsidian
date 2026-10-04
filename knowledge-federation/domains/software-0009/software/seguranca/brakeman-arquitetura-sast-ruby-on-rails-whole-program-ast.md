---
id: software.seguranca.tranche04.000321
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

# Brakeman: Arquitetura de Análise Estática *Whole-Program* para Aplicações Ruby on Rails

## Em uma frase
Brakeman é o analisador estático de segurança (SAST) especializado em aplicações Ruby on Rails (versões 2.3.x a 8.x), realizando análise de programa inteiro (*whole-program analysis*) sem necessidade de executar o servidor ou carregar o banco de dados.

## Por que importa
Diferente de linters genéricos de Ruby que olham arquivo por arquivo isoladamente, o Brakeman correlaciona `config/routes.rb`, inicializadores, `Gemfile.lock`, *models* ActiveRecord, *controllers* e *templates* ERB/Haml/Slim para rastrear entradas do usuário até sinks perigosos.

## Como funciona
O scanner converte o código Ruby em S-expressions (via `ruby_parser` / `prism`), resolve heranças de classes, propaga constantes e variáveis de instância (`@record`) entre ações de controllers e views, e executa dezenas de verificações (`Checks`) em paralelo usando threads dedicadas.

## Exemplo
```bash
# Executar todas as verificações (incluindo checks opcionais) com relatório JSON e console colorido
brakeman -A --color -o /dev/stdout -o brakeman-report.json /srv/rails-app
```

## Limites e trade-offs
Usar `--only-files` ou excluir diretórios inteiros de `app/models` ou `app/controllers` com `--skip-files` degrada a análise *whole-program* porque variáveis de instância populadas nos controllers deixarão de ser rastreadas nas views.

## Como verificar
Execute `brakeman -q -f json` na raiz do projeto Rails e inspecione a chave `scan_info` para confirmar o número de controllers, models e templates analisados com `errors: []`.

## Conexões
- [[brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching]] — Veja também: Brakeman: Níveis de Confiança (`High`, `Medium`, `Weak`) e Sensibilidade de Fluxo (`--branch-limit`).
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Referência cruzada direta com brakeman-prevencao-sql-injection-activerecord-interpolacao-arel.
- [[brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml]] — Referência cruzada direta com brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
