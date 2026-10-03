---
id: software.seguranca.tranche08.000746
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://docs.mitmproxy.org/stable/concepts/modes/", "https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md", "https://docs.mitmproxy.org/stable/addons-overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# mitmproxy: Reescrita Declarativa sem Código (`--modify-headers`, `--modify-body`, `--map-local` e `--map-remote`)

## Em uma frase
Para muitas tarefas de pentest e depuração de segurança (como injetar um cabeçalho de autorização, substituir um bundle JavaScript minificado de produção por uma cópia desofuscada local ou alterar `"isAdmin":false` para `"isAdmin":true` no JSON de resposta), não é necessário nem escrever um script Python: o `mitmproxy` inclui quatro addons nativos de linha de comando.

## Por que importa
Essas opções usam uma sintaxe uniforme de separador arbitrário (ex.: `/filtro/alvo/substituto`): **(1) `--modify-headers` (`-H`)** adiciona, altera ou remove cabeçalhos HTTP; **(2) `--modify-body` (`-B`)** aplica substituição regex no corpo de requisições ou respostas; **(3) `--map-local` (`-M`)** serve um arquivo ou diretório do seu disco local no lugar da resposta do servidor remoto (sem sequer tocar no servidor remoto!); e **(4) `--map-remote`** redireciona transparentemente uma URL para outro backend.

## Como funciona
Usar **`--map-local`** durante a análise de um frontend Single-Page Application (React/Angular/Vue) permite baixar o arquivo `app.bundle.js`, embelezá-lo (`prettier`), adicionar `console.log`/`debugger` e servi-lo localmente para todas as recargas do navegador.

## Exemplo
```bash
# Injetar cabecalho em requisicoes (~q), modificar JSON nas respostas (~s) e servir um bundle JS local via --map-local
mitmdump \
  --modify-headers "/~q/X-Pentest-ID/SecOps-2026" \
  --modify-body '/~s & ~d api\.internal\.corp/"role":"viewer"/"role":"admin"/' \
  --map-local '|https://app.internal.corp/static/js/main.min.js|/cases/pentest/main.beautified.js'
```

## Limites e trade-offs
Note na sintaxe `/~q/...` vs `/~s/...`: o filtro **`~q`** restringe a modificação apenas às **requisições** (client -> server), enquanto **`~s`** restringe apenas às **respostas** (server -> client); se você omitir o filtro, a substituição será aplicada em ambas as direções.

## Como verificar
Verifique no painel de detalhes do `mitmproxy` que fluxos servidos por `--map-local` são concluídos instantaneamente sem conexão de saída.

## Conexões
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Veja também: mitmproxy: Desenvolvimento de **Addons em Python (`-s script.py`)** — Hooks de Ciclo de Vida (`request`, `response`, `websocket_message`, `tcp_message`, `dns_request`).
- [[mitmproxy-replay-cliente-servidor-testes-regressao-idor-bola]] — Veja também: mitmproxy: **Client-Side Replay (`-C`)** e **Server-Side Replay (`-S`)** para Testes de Regressão de Autorização (**IDOR / BOLA**) e Simulação Offline.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[mitmproxy-expressoes-filtro-flow-filters-interceptacao-seletiva]] — Referência cruzada direta com mitmproxy-expressoes-filtro-flow-filters-interceptacao-seletiva.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
