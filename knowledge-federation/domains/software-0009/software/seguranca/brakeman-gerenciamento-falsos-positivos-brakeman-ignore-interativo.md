---
id: software.seguranca.tranche04.000329
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

# Brakeman: Gestão Auditável de Falsos Positivos com `config/brakeman.ignore` (`-I` e `--show-ignored`)

## Em uma frase
O Brakeman gerencia exceções e falsos positivos através do arquivo estruturado `config/brakeman.ignore`, mantido pelo modo interativo (`brakeman -I`), onde cada alerta ignorado é vinculado a um `fingerprint` criptográfico e a uma nota justificativa (`note`).

## Por que importa
Diferente de comentários inline que silenciam uma linha inteira para qualquer tipo de problema futuro, o `fingerprint` do `brakeman.ignore` é específico para aquele tipo de alerta, arquivo e expressão AST, voltando a alertar se o código mudar de forma insegura.

## Como funciona
Ao executar `brakeman -I`, o engenheiro de segurança inspeciona cada alerta, escolhe ignorá-lo e registra a justificativa técnica obrigatória no JSON `config/brakeman.ignore`. Durante auditorias periódicas, `brakeman --show-ignored` lista todos os alertas suprimidos sem alterar o código de saída do pipeline.

## Exemplo
```json
{
  "ignored_warnings": [
    {
      "warning_type": "SQL Injection",
      "warning_code": 0,
      "fingerprint": "8c2f4b91e0a3d5f7123456789abcdef0123456789abcdef0123456789abcdef0",
      "check_name": "SQL",
      "message": "Possible SQL injection",
      "file": "app/models/report_query.rb",
      "line": 42,
      "note": "Coluna validada contra allowlist estática ALLOWED_COLUMNS na linha 38"
    }
  ]
}
```

## Limites e trade-offs
Aceitar entradas em `config/brakeman.ignore` com o campo `"note": ""` vazio em *pull requests* impede a rastreabilidade de auditoria; exija em CI que toda entrada de `ignored_warnings` possua uma justificativa não vazia.

## Como verificar
Execute `jq -e '.ignored_warnings | all(.note != null and (.note | length > 10))' config/brakeman.ignore` no pipeline de CI para garantir que toda supressão está documentada.

## Conexões
- [[brakeman-csrf-forgery-protection-sessoes-cookies-ssl-headers]] — Veja também: Brakeman: Auditoria de CSRF (`protect_from_forgery`), Sessões, Cookies, `force_ssl` e Regex (`\A...\z`).
- [[brakeman-integracao-ci-cd-sarif-compare-json-brakeman-yml]] — Veja também: Brakeman: Configuração Declarativa (`config/brakeman.yml`), Comparação Delta (`--compare`) e SARIF no CI/CD.
- [[brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching]] — Referência cruzada direta com brakeman-niveis-confianca-high-medium-weak-fluxo-dados-branching.
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
