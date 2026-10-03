---
id: software.seguranca.tranche05.000412
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

# Dalfox: Fase de Discovery — Parameter Mining (`--mining-dict`, `--mining-dom`), Análise de Contexto e BAV

## Em uma frase
Antes de injetar payloads de XSS, a fase de *Discovery* do Dalfox descobre parâmetros ocultos usando dicionários integrados/customizados (`--mining-dict`, `--mining-dict-word`) e extração do próprio DOM/JavaScript da página (`--mining-dom`), além de testar *Basic Another Vulnerability* (BAV: SQLi, SSTI, Open Redirect, CRLF).

## Por que importa
Muitas vulnerabilidades de XSS residem em parâmetros não listados na URL visível (ex.: `?debug=`, `?callback=`, `?redirect_uri=`, `?template=`) que o código JavaScript ou HTML da página lê silenciosamente.

## Como funciona
Durante o *Discovery*, o Dalfox envia sondas de reflexão para identificar em qual ponto da árvore HTML o valor cai (dentro de comentário `<!-- -->`, atributo `href="..."`, evento `onload="..."`, bloco `<script>` ou texto puro) e quais caracteres especiais (`<`, `>`, `"`, `'`, crase, `(`, `)`) sobrevivem sem HTML-encoding.

## Exemplo
```bash
# Executar descoberta de parâmetros ocultos no DOM e via wordlist customizada antes da varredura XSS
dalfox scan "https://app.staging.corp/profile" \
  --mining-dom \
  --mining-dict-word /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
  --format jsonl --output /tmp/dalfox-discovery.jsonl
```

## Limites e trade-offs
Se o objetivo for apenas mapear quais parâmetros refletem entradas sem enviar nenhum payload de ataque XSS para o servidor, utilize `--only-discovery` ou `--dry-run`.

## Como verificar
Inspecione `jq -c 'select(.type == "R" or .type == "V")' /tmp/dalfox-discovery.jsonl` para revisar os parâmetros descobertos e seus contextos de reflexão.

## Conexões
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Veja também: Dalfox: Arquitetura de Análise de Parâmetros e Varredura de XSS (`dalfox scan`, Tiers `V`/`R`/`A`/`I`).
- [[dalfox-alvos-multi-localizacao-param-json-graphql-xml-inject-marker]] — Veja também: Dalfox: Modelagem de Alvos (`--param name:location`, `--inject-marker FUZZ`, `raw-http` e `har`).
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Referência cruzada direta com katana-extracao-campos-field-extraction-custom-regex-jsonl.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
