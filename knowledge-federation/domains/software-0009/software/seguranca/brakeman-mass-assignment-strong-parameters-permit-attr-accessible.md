---
id: software.seguranca.tranche04.000325
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

# Brakeman: Detecção de Mass Assignment e Abuso de Strong Parameters (`permit!` e Chaves Sensíveis)

## Em uma frase
As verificações `CheckMassAssignment` e `CheckPermitAttributes` do Brakeman auditam o uso de *Strong Parameters* (`params.require(...).permit(...)`) nos controllers Rails para impedir atribuição em massa de colunas privilegiadas.

## Por que importa
Chamar `params.permit!` libera recursivamente todos os parâmetros enviados pelo cliente para `User.new()` ou `user.update()`, permitindo que um atacante sobrescreva campos como `admin: true`, `role_id` ou `account_balance`.

## Como funciona
Além de sinalizar qualquer uso de `.permit!` (confiança `High`), o `CheckPermitAttributes` inspeciona os símbolos passados para `.permit(:name, :email, :role, :is_admin)` e emite alertas sempre que atributos sensíveis de controle de acesso ou chaves estrangeiras de ownership (`:account_id`, `:admin`, `:role`) são expostos à edição pelo usuário.

## Exemplo
```ruby
# INSEGURO — Aciona CheckMassAssignment (High) e CheckPermitAttributes:
def update
  @user.update(params.require(:user).permit!)
end

# SEGURO — Allowlist explícita restrita apenas a campos editáveis pelo próprio usuário:
def user_params
  params.require(:user).permit(:display_name, :time_zone)
end
```

## Limites e trade-offs
Mesmo usando `.permit(:role)` explicitamente sem `.permit!`, permitir atributos de autorização em endpoints compartilhados entre usuários comuns e administradores cria escalação vertical de privilégio.

## Como verificar
Execute `brakeman -t MassAssignment,PermitAttributes` e confirme que nenhuma action utiliza `permit!` nem inclui atributos de privilégio nas listas `.permit(...)` públicas.

## Conexões
- [[brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to]] — Veja também: Brakeman: Detecção de Cross-Site Scripting (`CheckCrossSiteScripting`, `raw`, `html_safe` e `link_to`).
- [[brakeman-command-injection-ssrf-open-redirect-dynamic-render]] — Veja também: Brakeman: Command Injection (`CheckExecute`), SSRF, Path Traversal (`CheckSendFile`) e Dynamic Render.
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Referência cruzada direta com brakeman-prevencao-sql-injection-activerecord-interpolacao-arel.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
