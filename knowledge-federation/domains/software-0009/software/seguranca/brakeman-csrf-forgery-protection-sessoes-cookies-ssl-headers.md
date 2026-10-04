---
id: software.seguranca.tranche04.000328
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

# Brakeman: Auditoria de CSRF (`protect_from_forgery`), Sessões, Cookies, `force_ssl` e Regex (`\A...\z`)

## Em uma frase
O Brakeman audita as configurações globais de segurança do Rails em `ApplicationController` e `config/environments/production.rb`, incluindo proteção CSRF (`CheckForgerySetting`), `force_ssl` (`CheckForceSSL`), segredos de sessão (`CheckSessionSettings`) e âncoras de regex (`CheckValidationRegex`).

## Por que importa
Em Ruby, expressões regulares de validação de modelo que usam `^...$` em vez de `\A...\z` validam apenas uma linha individual da string, permitindo que um atacante injete payloads maliciosos após uma quebra de linha (`\n`).

## Como funciona
O `CheckValidationRegex` inspeciona todas as chamadas `validates_format_of` / `validates ..., format: { with: /.../ }` nos models ActiveRecord e alerta sempre que `^` ou `$` são usados no lugar de `\A` e `\z`. Paralelamente, `CheckForgerySetting` verifica se `protect_from_forgery with: :exception` está presente e se `skip_before_action :verify_authenticity_token` foi aplicado indevidamente em controllers baseados em sessão.

## Exemplo
```ruby
# INSEGURO — Permite bypass via newline ("user@corp.com\n<script>...") — CheckValidationRegex:
validates :email, format: { with: /^[a-z0-9._%+-]+@corp\.com$/i }

# SEGURO — Valida o início e o fim absolutos da string inteira com \A e \z:
validates :email, format: { with: /\A[a-z0-9._%+-]+@corp\.com\z/i }
```

## Limites e trade-offs
Desativar `verify_authenticity_token` em um controller que aceita tanto tokens Bearer quanto cookies de sessão expõe os usuários autenticados via navegador a ataques de Cross-Site Request Forgery (CSRF).

## Como verificar
Execute `brakeman -t ForgerySetting,SessionSettings,ForceSSL,ValidationRegex` e valide que todas as regexes de modelo usam `\A...\z` e que `config.force_ssl = true` está ativo em produção.

## Conexões
- [[brakeman-desserializacao-insegura-yaml-marshal-oj-eval-send]] — Veja também: Brakeman: Desserialização Insegura (`YAML.load`, `Marshal.load`, `CSV`), `eval` e `send` Dinâmico.
- [[brakeman-gerenciamento-falsos-positivos-brakeman-ignore-interativo]] — Veja também: Brakeman: Gestão Auditável de Falsos Positivos com `config/brakeman.ignore` (`-I` e `--show-ignored`).
- [[brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to]] — Referência cruzada direta com brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to.
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
