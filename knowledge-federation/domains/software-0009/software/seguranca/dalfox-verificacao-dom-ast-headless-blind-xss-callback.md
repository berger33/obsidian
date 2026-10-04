---
id: software.seguranca.tranche05.000414
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

# Dalfox: Verificação DOM/AST, Stored XSS (`SXSS`) e Blind XSS com Callback (`-b` / `--blind`)

## Em uma frase
O Dalfox combina análise sintática DOM/AST e verificação em navegador Headless para confirmar a execução real de JavaScript (tier `V`), além de suportar fluxos de **Stored XSS** (onde a injeção ocorre em uma rota de escrita e o gatilho é verificado em uma rota de leitura) e **Blind XSS** (`-b` / `--blind`).

## Por que importa
Vulnerabilidades de *Blind XSS* ocorrem quando o payload enviado em um formulário público (ex.: ticket de suporte, log de erro ou cabeçalho `User-Agent`) só é renderizado horas depois no painel administrativo interno de um operador.

## Como funciona
Ao passar `-b https://xss-collector.secops.corp`, o Dalfox anexa payloads de *callback* assíncronos que carregam um script externo caso o HTML seja interpretado sem escape em qualquer sistema de retaguarda. Para *Stored XSS* imediato, o modo sequencial envia o payload na requisição `POST` e consulta a URL de visualização (`--trigger`) para verificar a persistência no DOM.

## Exemplo
```bash
# Escanear formulário de feedback injetando payloads de Blind XSS apontando para coletor OAST autorizado
dalfox scan "https://portal.staging.corp/support/ticket" \
  -X POST -d "subject=Erro&message=teste" \
  -p subject -p message \
  -b "https://oast-callback.secops.internal.corp/bxss" \
  --format json --output /tmp/dalfox-bxss.json
```

## Limites e trade-offs
Nunca utilize domínios de callback de terceiros públicos não controlados pela sua organização em `-b` durante testes corporativos, pois o callback de Blind XSS pode transmitir o DOM e cookies de painéis internos para fora da empresa.

## Como verificar
Verifique nos logs do servidor coletor interno (`oast-callback.secops.internal.corp`) o recebimento das sondas de callback quando o painel administrativo de teste renderizar o ticket.

## Conexões
- [[dalfox-alvos-multi-localizacao-param-json-graphql-xml-inject-marker]] — Veja também: Dalfox: Modelagem de Alvos (`--param name:location`, `--inject-marker FUZZ`, `raw-http` e `har`).
- [[dalfox-monitoramento-sessao-autenticada-session-check-abort]] — Veja também: Dalfox: Monitoramento Contínuo de Sessão Autenticada (`--session-check`, `--session-check-url` e `--on-session-loss`).
- [[dalfox-arquitetura-scanner-xss-analise-parametros-rust-go]] — Referência cruzada direta com dalfox-arquitetura-scanner-xss-analise-parametros-rust-go.
- [[dalfox-waf-fingerprinting-evasao-custom-payloads-encoders]] — Referência cruzada direta com dalfox-waf-fingerprinting-evasao-custom-payloads-encoders.
- [[brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to]] — Referência cruzada direta com brakeman-deteccao-xss-templates-erb-raw-html-safe-link-to.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
