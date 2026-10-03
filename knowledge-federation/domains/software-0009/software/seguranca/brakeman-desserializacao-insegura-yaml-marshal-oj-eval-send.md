---
id: software.seguranca.tranche04.000327
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

# Brakeman: Desserialização Insegura (`YAML.load`, `Marshal.load`, `CSV`), `eval` e `send` Dinâmico

## Em uma frase
As verificações `CheckDeserialize`, `CheckYAML`, `CheckEvaluation` e `CheckSend` do Brakeman detectam execução remota de código (RCE) via desserialização de objetos Ruby arbitrários, avaliação de código dinâmico e invocação reflexiva de métodos.

## Por que importa
Em Ruby, `Marshal.load`, `YAML.load` (em versões do Psych anteriores ao Psych 4 onde equivalia a `unsafe_load`) e `Oj.load` (no modo `:object` padrão) instanciam *gadgets* arbitrários na memória que executam comandos do sistema operacional durante a desserialização ou coleta de lixo.

## Como funciona
O Brakeman verifica chamadas a `Marshal.load`, `YAML.unsafe_load`, `YAML.load` com entrada externa, `eval`/`instance_eval`/`class_eval`/`module_eval`, `constantize` (`params[:klass].constantize`) e `public_send`/`send(params[:action])`, alertando sempre que o nome da classe, método ou payload serializado puder ser influenciado pelo cliente.

## Exemplo
```ruby
# INSEGURO — RCE por desserialização e reflexão dinâmica:
data = Marshal.load(Base64.decode64(cookies[:state]))
target = params[:handler].constantize.new
target.send(params[:operation], data)

# SEGURO — YAML.safe_load com classes restritas e despacho por mapa fixo:
data = YAML.safe_load(payload, permitted_classes: [Date, Symbol])
```

## Limites e trade-offs
Chamar `public_send(params[:method])` achando que é seguro contra métodos privados ainda permite ao atacante invocar métodos públicos destrutivos herdados de `Object` ou `ActiveRecord::Base` (como `destroy` ou `exit`).

## Como verificar
Execute `brakeman -t Deserialize,YAML,Evaluation,Send,UnsafeReflection` e confirme `0` ocorrências no código de aplicação.

## Conexões
- [[brakeman-command-injection-ssrf-open-redirect-dynamic-render]] — Veja também: Brakeman: Command Injection (`CheckExecute`), SSRF, Path Traversal (`CheckSendFile`) e Dynamic Render.
- [[brakeman-csrf-forgery-protection-sessoes-cookies-ssl-headers]] — Veja também: Brakeman: Auditoria de CSRF (`protect_from_forgery`), Sessões, Cookies, `force_ssl` e Regex (`\A...\z`).
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
