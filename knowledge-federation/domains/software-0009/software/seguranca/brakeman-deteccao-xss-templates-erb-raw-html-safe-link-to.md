---
id: software.seguranca.tranche04.000324
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

# Brakeman: Detecção de Cross-Site Scripting (`CheckCrossSiteScripting`, `raw`, `html_safe` e `link_to`)

## Em uma frase
As verificações de XSS do Brakeman (`CheckCrossSiteScripting`, `CheckLinkTo`, `CheckLinkToHref`, `CheckContentTag` e `CheckJSONEncoding`) identificam pontos onde o escape automático de HTML do Rails é contornado ou insuficiente.

## Por que importa
Embora o Rails escape `<%= ... %>` por padrão desde a versão 3, o uso de `raw()`, `.html_safe`, `<%== ... %>` ou `link_to "Perfil", params[:website]` (que permite URIs `javascript:`) reintroduz XSS refletido e armazenado.

## Como funciona
O Brakeman rastreia dados de `params`, `cookies` e atributos de modelos (`@user.bio`) até os templates de visualização. Se um valor não sanitizado recebe `.html_safe` ou `raw`, ou se `link_to` recebe uma URL dinâmica sem validação de protocolo HTTP/HTTPS, o scanner emite alerta detalhando o caminho do controller até a linha exata da view.

## Exemplo
```erb
<%# INSEGURO — XSS via html_safe e URI javascript: em link_to %>
<div class="bio"><%= @user.bio.html_safe %></div>
<%= link_to "Site externo", params[:return_url] %>

<%# SEGURO — Escape padrão do ERB e sanitização com allowlist de protocolo %>
<div class="bio"><%= sanitize(@user.bio, tags: %w[b i p]) %></div>
```

## Limites e trade-offs
Passar a flag `--ignore-model-output` suprime alertas de XSS originados de atributos do banco de dados (`@user.bio`), o que oculta vulnerabilidades de *Stored XSS* caso os dados do modelo provenham de formulários públicos.

## Como verificar
Execute `brakeman -t CrossSiteScripting,LinkTo,ContentTag` sem `--ignore-model-output` e valide que nenhum atributo de usuário usa `.html_safe` ou `raw` sem sanitizador explícito.

## Conexões
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Veja também: Brakeman: Detecção de SQL Injection (`CheckSQL`) em ActiveRecord, Interpolação de Strings e Arel.
- [[brakeman-mass-assignment-strong-parameters-permit-attr-accessible]] — Veja também: Brakeman: Detecção de Mass Assignment e Abuso de Strong Parameters (`permit!` e Chaves Sensíveis).
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.
- [[brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching]] — Referência cruzada direta com brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching.
- [[brakeman-csrf-forgery-protection-sessoes-cookies-ssl-headers]] — Referência cruzada direta com brakeman-csrf-forgery-protection-sessoes-cookies-ssl-headers.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
