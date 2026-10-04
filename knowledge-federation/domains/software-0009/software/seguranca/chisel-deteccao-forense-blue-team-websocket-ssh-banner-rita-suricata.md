---
id: software.seguranca.tranche16.001560
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/jpillora/chisel/master/README.md", "https://raw.githubusercontent.com/jpillora/chisel/master/main.go"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Engenharia de Detecção (**Blue Team / SOC / NIDS**) Contra Túneis **Chisel**: Handshake **WebSocket (`Sec-WebSocket-Protocol: chisel-v3`)**, Banner SSH Interno e **Long Connections**

## Em uma frase
Como um engenheiro de detecção (**Suricata / Cisco Snort 3 / Zeek / RITA / Arkime**) identifica que um atacante ou insider abriu um túnel reverso com o **Chisel (`jpillora/chisel`)** na rede corporativa?

## Por que importa
Existem **3 indicadores técnicos de altíssima fidelidade** em diferentes camadas: **(Indicador 1 — Cabeçalho HTTP de Upgrade WebSocket em Texto Claro ou no Proxy SSL)**: durante o handshake WebSocket (`GET / HTTP/1.1` com `Upgrade: websocket`), o cliente Chisel envia por padrão o cabeçalho **`Sec-WebSocket-Protocol: chisel-v3`** (e logo após o `101 Switching Protocols`, trafega o banner **`SSH-2.0-Go`** da biblioteca `crypto/ssh` se o túnel estiver sobre HTTP sem TLS!).

## Como funciona
**(Indicador 2 — Persistência e Volume Simétrico no RITA / Zeek)**: mesmo quando criptografado em HTTPS (`wss://`), um túnel Chisel mantém uma **Long Connection** (frequentemente com pings de `--keepalive 25s` exatos!) para um destino de baixa prevalência (`Prevalence = 1`); e **(Indicador 3 — Telemetria de Endpoint / EDR)**: argumentos de linha de comando contendo `R:socks`, `--fingerprint` ou binários Go carregando símbolos `github.com/jpillora/chisel`!

## Exemplo
```bash
# Inspecionar um binario suspeito com strings/FLOSS procurando assinaturas internas dos pacotes Go do Chisel e regras de protocolo
strings -a /tmp/binario_suspeito | grep -E "(jpillora/chisel|chisel-v3|chserver|chclient)"
```

## Limites e trade-offs
Veja na linha acima por que mesmo que um atacante renomeie o executável `chisel` para `nginx-worker` ou `systemd-helper`, uma simples busca por **`jpillora/chisel`** ou **`chisel-v3`** nas strings do binário (ou uma regra **YARA** no **Velociraptor**) identifica a ferramenta instantaneamente se o binário não foi recompilado com ofuscação!

## Como verificar
E nas suas regras de **Suricata / Snort 3**, crie um alerta para qualquer requisição HTTP de saída que contenha o cabeçalho `Sec-WebSocket-Protocol: chisel` ou `SSH-2.0-Go` logo após `101 Switching Protocols`!

## Conexões
- [[chisel-tunelamento-udp-dns-snmp-wireguard-over-chisel-tcp]] — Veja também: Tunelamento de Protocolos **UDP (`<remote>/udp`)** no Chisel: Encapsulando Consultas **DNS (`53/udp`)**, **SNMP (`161/udp`)** ou **WireGuard** sobre HTTP/WebSockets.
- [[chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang]] — Referência cruzada direta com chisel-arquitetura-tunel-tcp-udp-http-websocket-ssh-crypto-golang.

## Fontes
- [Chisel Official GitHub Repository (`jpillora/chisel`)](https://raw.githubusercontent.com/jpillora/chisel/master/README.md) — repositório oficial do túnel TCP/UDP sobre HTTP/SSH Chisel em Go cobrindo `--keygen`/`--keyfile`, `--authfile`, `--reverse`, `--socks5` e `--backend`; consultado em 2026-10-03.
- [Chisel Official CLI & Remotes Specification (`main.go`)](https://raw.githubusercontent.com/jpillora/chisel/master/main.go) — código-fonte e especificação oficial do CLI do Chisel detalhando a gramática de `<remote>`, modo `stdio:%h:%p`, sufixo `/udp` e sinais Unix (`SIGUSR2`, `SIGHUP`); consultado em 2026-10-03.
