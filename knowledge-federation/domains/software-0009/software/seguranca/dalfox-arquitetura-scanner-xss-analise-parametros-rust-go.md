---
id: software.seguranca.tranche05.000411
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/hahwul/dalfox/main/README.md", "https://dalfox.hahwul.com/reference/cli/", "https://github.com/hahwul/dalfox/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dalfox: Arquitetura de Análise de Parâmetros e Varredura de XSS (`dalfox scan`, Tiers `V`/`R`/`A`/`I`)

## Em uma frase
**Dalfox** (`hahwul/dalfox`, MIT — reescrito em Rust na v3 preservando a série Go v2) é um scanner especializado em descoberta de vulnerabilidades Cross-Site Scripting (Reflected, Stored e DOM-based) e análise estática/dinâmica de parâmetros HTTP.

## Por que importa
Diferente de scanners que apenas testam uma lista cega de payloads `<script>alert(1)</script>`, o Dalfox analisa primeiro em qual contexto sintático do HTML/DOM/JavaScript o parâmetro é refletido e adapta os payloads exatamente para fechar as tags ou atributos daquele contexto.

## Como funciona
Os achados são classificados em quatro níveis (*tiers*): **`V`** (*Verified* — execução de XSS confirmada via verificação DOM/AST ou Headless), **`R`** (*Reflected* — caracteres especiais perigosos refletidos sem codificação no contexto), **`A`** (*AST* — sumidouro DOM/JavaScript estático identificado) e **`I`** (*Informational* — cabeçalhos/BAV), retornando exit code `0` (limpo), `1` (achados encontrados) ou `2` (erro de configuração/sessão perdida).

## Exemplo
```bash
# Escanear uma URL filtrando apenas achados verificados (tier V) e falhando com exit code 1 se houver XSS
dalfox scan "https://app.staging.corp/search?q=notebook&category=all" \
  --only-poc v \
  --poc-type curl \
  --format json --output /tmp/dalfox-verified.json
```

## Limites e trade-offs
A forma abreviada `dalfox <URL>` sem o subcomando explícito `scan` aceita apenas flags globais; passe sempre `dalfox scan <TARGET> [FLAGS]` ao usar opções avançadas de workers, sessão ou formato.

## Como verificar
Execute `dalfox --version` e valide o relatório gerado com `jq '. | length' /tmp/dalfox-verified.json`.

## Conexões
- [[dalfox-descoberta-mining-parametros-dom-dict-bav-static-analysis]] — Veja também: Dalfox: Fase de Discovery — Parameter Mining (`--mining-dict`, `--mining-dom`), Análise de Contexto e BAV.
- [[dalfox-verificacao-dom-ast-headless-blind-xss-callback]] — Referência cruzada direta com dalfox-verificacao-dom-ast-headless-blind-xss-callback.
- [[dalfox-comparacao-baseline-sarif-state-file-ci-cd]] — Referência cruzada direta com dalfox-comparacao-baseline-sarif-state-file-ci-cd.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
