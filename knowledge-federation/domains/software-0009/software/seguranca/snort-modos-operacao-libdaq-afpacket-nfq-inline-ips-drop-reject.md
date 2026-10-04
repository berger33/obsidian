---
id: software.seguranca.tranche14.001346
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/snort3/snort3/master/README.md", "https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Operação Inline (**IPS Ativo: `drop`, `sdrop`, `reject`**) vs. Passivo (**IDS / TAP**) no Snort 3 com **`libdaq` (`afpacket`, `nfq`, `pcap`, `dpdk`)**

## Em uma frase
Como colocar o **Snort 3** em modo **IPS Inline (Prevenção de Intrusão Ativa)** no Linux para que pacotes maliciosos que disparam regras críticas sejam **descartados em tempo real (`drop` / `block`)** antes de chegarem ao servidor alvo, em vez de apenas gerar um alerta passivo?

## Por que importa
O Snort 3 utiliza a camada modular **`libdaq` (*Data Acquisition Library*)** configurada na seção `daq = { ... }` do `snort.lua` ou na linha de comando (`--daq <modulo> -Q`): **(1) Modo Passivo (IDS via SPAN/Mirror Port)**: usa `--daq pcap` ou `--daq afpacket` sobre uma interface de escuta passiva (`-i eth1`); **(2) Modo Inline Layer-2 Bridge (`--daq afpacket -Q -i eth1:eth2`)**: une duas placas de rede em um par *Zero-Copy Memory-Mapped Ring* (`AF_PACKET v3`) onde todo pacote que entra em `eth1` só sai em `eth2` se o Snort 3 aprová-lo!; e **(3) Modo Inline Integrado ao Firewall Linux `nftables` (`--daq nfq -Q`)**: o `nftables` envia pacotes selecionados para uma fila `nfqueue` em espaço de usuário e o Snort 3 dá o veredito `NF_ACCEPT` ou `NF_DROP`!

## Como funciona
No bloco **`ips = { mode = 'inline', ... }`** do `snort.lua`, as regras com ação **`drop`** (descarta o pacote/fluxo e gera log), **`sdrop`** (descarta silenciosamente) ou **`reject`** (descarta e envia TCP `RST` / ICMP Unreachable via `reject = { reset = 'both' }`) passam a bloquear ataques instantaneamente!

## Exemplo
```bash
# Executar o Snort 3 em modo IPS Inline (-Q) usando o modulo DAQ afpacket em bridge entre duas interfaces (eth1:eth2) com 4 threads
snort -c /etc/snort/snort.lua -Q --daq afpacket -i eth1:eth2 \
  --daq-var buffer_size_mb=512 --max-packet-threads 4 -A alert_json
```

## Limites e trade-offs
Atenção obrigatória ao usar **`afpacket`** ou **`pcap`** em interfaces de rede modernas no Linux: **desative os *Offloads de Reassemblagem de Placa de Rede* (`GRO` — *Generic Receive Offload* e `LRO` — *Large Receive Offload*) com `ethtool -K eth1 gro off lro off`**! Se `GRO`/`LRO` ficarem ligados, a placa de rede junta vários pacotes TCP em "super-pacotes" de 64 KB antes de entregá-los ao Snort, distorcendo a inspeção de tamanho de pacote e causando descartes em modo inline!

## Como verificar
Use **`ips = { mode = 'tap' }`** inicialmente para validar novas regras e mude para **`mode = 'inline'`** após confirmar ausência de falsos positivos.

## Conexões
- [[snort-appid-openappid-visibilidade-camada-7-shadow-it-rna]] — Veja também: Descoberta de Aplicações Camada 7 (**OpenAppID / `appid`**) e Descoberta Passiva de Rede (**`rna` — *Real-time Network Awareness***) no Snort 3.
- [[snort-reputacao-ip-suppress-event-filter-rate-filter-anti-dos]] — Veja também: Controle de Ruído, **IP Reputation (`reputation`)**, **`suppress`**, **`event_filter`** e **`rate_filter`** no Snort 3: Prevenindo Alert Fatigue e Floods.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
