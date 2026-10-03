---
id: software.seguranca.tranche08.000747
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

# mitmproxy: **Client-Side Replay (`-C`)** e **Server-Side Replay (`-S`)** para Testes de Regressão de Autorização (**IDOR / BOLA**) e Simulação Offline

## Em uma frase
O `mitmproxy` grava cada fluxo (`HTTPFlow`) em um formato serializado completo que permite dois tipos opostos de reprodução determinística: **Client-Side Replay (`--client-replay` / `-C`)** e **Server-Side Replay (`--server-replay` / `-S`)**.

## Por que importa
No **Client-Side Replay (`-C`)**, o `mitmdump` atua como o cliente HTTP e reenvia todas as requisições contidas no arquivo `.mitm` contra o servidor ao vivo — combinando `-C fluxos_usuario_a.mitm` com `--modify-headers "/~q/Authorization/Bearer <TOKEN_USUARIO_B>"` e um addon de comparação, você testa instantaneamente **IDOR / BOLA (*Broken Object Level Authorization*, OWASP API1:2023)** em centenas de endpoints!

## Como funciona
Já no **Server-Side Replay (`-S`)**, o `mitmdump` atua como um servidor simulado que responde às requisições do cliente usando as respostas gravadas anteriormente no arquivo `.mitm`, permitindo analisar um aplicativo mobile ou malware mesmo depois que o servidor de comando e controle (C2) original saiu do ar!

## Exemplo
```bash
# Reproduzir todas as requisicoes gravadas do Usuario A trocando o token pelo do Usuario B para auditar BOLA/IDOR
mitmdump -nc /cases/pentest/user_a_flows.mitm \
  --modify-headers "/~q/Authorization/Bearer TOKEN_DE_BAIXO_PRIVILEGIO_USER_B" \
  -w /cases/pentest/bola_replay_results.mitm
```

## Limites e trade-offs
Na comando acima, a flag **`-n` (`--no-server`)** instrui o `mitmdump` a não abrir a porta de proxy `8080`, executando apenas o replay das requisições de `-C` (`-c`) e encerrando assim que todas as respostas forem recebidas e gravadas em `-w`.

## Como verificar
Compare os códigos de status HTTP e tamanhos de resposta entre `user_a_flows.mitm` e `bola_replay_results.mitm` com um script Python usando `mitmproxy.io.FlowReader` para detectar endpoints que continuaram retornando `200 OK` para o Usuário B.

## Conexões
- [[mitmproxy-modificacao-trafego-modify-body-modify-headers-map-local]] — Veja também: mitmproxy: Reescrita Declarativa sem Código (`--modify-headers`, `--modify-body`, `--map-local` e `--map-remote`).
- [[mitmproxy-leitura-programatica-arquivos-fluxo-flowreader-har-export]] — Veja também: mitmproxy (`mitmproxy.io.FlowReader` & `save_har`): Análise Forense Offline de Arquivos `.mitm`, Extração de Segredos e Exportação **HAR / cURL / OpenAPI**.
- [[mitmproxy-automacao-addons-python-request-response-websocket-hooks]] — Referência cruzada direta com mitmproxy-automacao-addons-python-request-response-websocket-hooks.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
