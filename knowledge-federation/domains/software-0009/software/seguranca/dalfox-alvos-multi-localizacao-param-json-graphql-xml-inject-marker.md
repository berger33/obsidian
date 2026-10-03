---
id: software.seguranca.tranche05.000413
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

# Dalfox: Modelagem de Alvos (`--param name:location`, `--inject-marker FUZZ`, `raw-http` e `har`)

## Em uma frase
O Dalfox permite direcionar a análise para parâmetros específicos por localização (`--param name:location`, suportando `query`, `body`, `json`, `multipart`, `cookie`, `header`, `graphql` e `xml`), marcadores de posição arbitrários (`--inject-marker FUZZ`) e capturas completas `--input-type raw-http` ou `har`.

## Por que importa
Aplicações modernas frequentemente refletem dados enviados em cabeçalhos HTTP (`X-Search`, `Referer`), campos de objetos JSON ou variáveis de queries GraphQL em vez de query strings tradicionais.

## Como funciona
Ao usar `--inject-marker FUZZ`, o analista pode posicionar o marcador em segmentos de caminho REST (`/users/FUZZ/bio`), cabeçalhos (`-H "X-Forwarded-Host: FUZZ"`) ou corpos complexos. Já `--input-type har` (HTTP Archive exportado do DevTools do navegador) analisa todas as requisições capturadas durante a navegação real do usuário, deduplicando URLs equivalentes com `--dedup-urls signature`.

## Exemplo
```bash
# Testar injeção XSS em cabeçalho customizado e em campo JSON específico usando marcadores e localizações
dalfox scan "https://app.staging.corp/api/v1/preview" \
  -X POST -H "Content-Type: application/json" \
  -H "X-Client-Locale: FUZZ" \
  -d '{"title":"Relatorio","subtitle":"teste"}' \
  --param subtitle:json \
  --inject-marker FUZZ
```

## Limites e trade-offs
Ao usar `--cookie-from-raw request.http`, o Dalfox encerra imediatamente com código de saída `2` se o arquivo não contiver um cabeçalho `Cookie:`, impedindo que o scan prossiga deslogado e reporte falsamente `0 XSS`.

## Como verificar
Execute com `--dry-run` primeiro para confirmar no plano de execução que tanto o marcador `FUZZ` quanto o parâmetro `subtitle:json` foram selecionados para teste.

## Conexões
- [[dalfox-descoberta-mining-parametros-dom-dict-bav-static-analysis]] — Veja também: Dalfox: Fase de Discovery — Parameter Mining (`--mining-dict`, `--mining-dom`), Análise de Contexto e BAV.
- [[dalfox-verificacao-dom-ast-headless-blind-xss-callback]] — Veja também: Dalfox: Verificação DOM/AST, Stored XSS (`SXSS`) e Blind XSS com Callback (`-b` / `--blind`).
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Referência cruzada direta com dalfox-arquitetura-scanner-xss-analise-parametros-rust-go.
- [[dalfox-monitoramento-sessao-autenticada-session-check-abort]] — Referência cruzada direta com dalfox-monitoramento-sessao-autenticada-session-check-abort.
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — Referência cruzada direta com ffuf-fuzzing-parametros-get-post-json-headers-raw-request.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
