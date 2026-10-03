---
id: software.seguranca.tranche05.000415
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

# Dalfox: Monitoramento Contínuo de Sessão Autenticada (`--session-check`, `--session-check-url` e `--on-session-loss`)

## Em uma frase
O Dalfox ativa automaticamente o monitoramento de sessão sempre que credenciais são fornecidas (`--cookies`, `--cookie-from-raw` ou cabeçalhos `Cookie`/`Authorization`) ou quando `--session-check` e `--session-check-url` são configurados.

## Por que importa
Previne a falha silenciosa mais perigosa em scans autenticados de DAST: quando a sessão expira no meio da varredura, o servidor passa a responder com a tela de login para todos os payloads e a ferramenta reportaria falsamente que a aplicação está `100% limpa` (`exit 0`).

## Como funciona
O operador define uma expressão regular que deve permanecer presente nas respostas autenticadas (`--session-check "Bem-vindo, Auditor"`) e opcionalmente um endpoint leve de verificação (`--session-check-url "https://app.staging.corp/api/me"`). Se a sessão cair e `--on-session-loss abort` (padrão) estiver ativo, o Dalfox interrompe o alvo, marca o relatório como `incomplete` / `SESSION_LOST` (nunca `clean`) e retorna exit code `2`.

## Exemplo
```bash
# Executar scan autenticado com verificação autoritativa de sessão ativa e aborto imediato em queda de login
dalfox scan "https://app.staging.corp/settings/profile?tab=general" \
  --cookies "session_id=${STAGING_SESSION}" \
  --session-check '"authenticated":true' \
  --session-check-url "https://app.staging.corp/api/v1/session/status" \
  --on-session-loss abort
```

## Limites e trade-offs
Combinar scans autenticados com crawlers sem excluir caminhos de logout (`--exclude-url "logout|signout"`) derrubará a própria sessão durante a varredura.

## Como verificar
Simule um cookie inválido/expirado e confirme que o Dalfox detecta `SESSION_LOST` e encerra com código de saída `2` em vez de `0`.

## Conexões
- [[dalfox-verificacao-dom-ast-headless-blind-xss-callback]] — Veja também: Dalfox: Verificação DOM/AST, Stored XSS (`SXSS`) e Blind XSS com Callback (`-b` / `--blind`).
- [[dalfox-controle-escopo-out-of-scope-include-exclude-url]] — Veja também: Dalfox: Governança de Escopo (`--out-of-scope`, `--out-of-scope-file`, `--include-url`, `--exclude-url` e `--ignore-param`).
- [[dalfox-alvos-multi-localizacao-param-json-graphql-xml-inject-marker]] — Referência cruzada direta com dalfox-alvos-multi-localizacao-param-json-graphql-xml-inject-marker.
- [[katana-crawling-autenticado-headers-cookies-chrome-ws-url]] — Referência cruzada direta com katana-crawling-autenticado-headers-cookies-chrome-ws-url.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
