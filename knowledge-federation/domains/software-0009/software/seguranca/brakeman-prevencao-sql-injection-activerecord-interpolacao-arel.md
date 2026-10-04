---
id: software.seguranca.tranche04.000323
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

# Brakeman: Detecção de SQL Injection (`CheckSQL`) em ActiveRecord, Interpolação de Strings e Arel

## Em uma frase
A verificação `CheckSQL` do Brakeman detecta injeção de SQL em métodos do ActiveRecord (`where`, `find_by_sql`, `order`, `group`, `having`, `pluck`, `joins`, `lock`) e em chamadas `Arel.sql()` quando strings interpoladas incorporam parâmetros não parametrizados.

## Por que importa
No Rails, passar um Hash (`User.where(email: params[:email])`) ou placeholders (`where("email = ?", params[:email])`) é seguro, mas interpolar Ruby (`where("email = '#{params[:email]}'")`) ou passar `params[:sort]` diretamente em `order()` permite injeção de SQL.

## Como funciona
O Brakeman inspeciona a árvore sintática de todas as chamadas a escopos e métodos de consulta do ActiveRecord, diferenciando strings literais estáticas e placeholders `?`/`:named` de interpolações `#{...}` ou concatenações `+` envolvendo `params`, `cookies` ou chamadas encadeadas.

## Exemplo
```ruby
# INSEGURO — Aciona alerta Brakeman CheckSQL (High Confidence):
User.where("role = '#{params[:role]}' AND active = 1")

# SEGURO — Consulta parametrizada com Hash ou bind parameters:
User.where(role: params[:role], active: true)
```

## Limites e trade-offs
Envolver uma string interpolada em `Arel.sql("direction #{params[:dir]}")` apenas silencia o `ActiveRecord::UnknownAttributeReference` do Rails em tempo de execução, mas continua vulnerável a SQL Injection e é corretamente sinalizado pelo Brakeman.

## Como verificar
Execute `brakeman -t SQL` no repositório e confirme `0` alertas de SQL Injection, usando `--sql-safe-methods` apenas para wrappers formalmente auditados que validam contra *allowlists* estritas.

## Conexões
- [[brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching]] — Veja também: Brakeman: Níveis de Confiança (`High`, `Medium`, `Weak`) e Sensibilidade de Fluxo (`--branch-limit`).
- [[brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to]] — Veja também: Brakeman: Detecção de Cross-Site Scripting (`CheckCrossSiteScripting`, `raw`, `html_safe` e `link_to`).
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.
- [[brakeman-mass-assignment-strong-parameters-permit-attr-accessible]] — Referência cruzada direta com brakeman-mass-assignment-strong-parameters-permit-attr-accessible.
- [[brakeman-command-injection-ssrf-open-redirect-dynamic-render]] — Referência cruzada direta com brakeman-command-injection-ssrf-open-redirect-dynamic-render.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
