---
id: software.seguranca.tranche14.001345
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

# Descoberta de Aplicações Camada 7 (**OpenAppID / `appid`**) e Descoberta Passiva de Rede (**`rna` — *Real-time Network Awareness***) no Snort 3

## Em uma frase
Um NIDS/NIPS moderno não deve apenas procurar exploits conhecidos: ele também precisa responder à equipe de Segurança: **"Quais aplicações de Camada 7 (ex.: Tor, BitTorrent, Telegram, AnyDesk, TeamViewer, Ngrok, OpenAI API, Dropbox) estão rodando na rede corporativa (*Shadow IT*) e quais novos hosts/sistemas operacionais apareceram na VLAN sem autorização?"**

## Por que importa
O Snort 3 possui dois inspetores dedicados para essa visibilidade total: **(1) `appid` (*OpenAppID*)** — carrega mais de 4.000 detectores Lua abertos (`app_detector_dir = '/usr/local/lib/odp'`) que identificam aplicações, clientes, serviços e payloads web em tempo real, permitindo escrever regras IPS que filtram diretamente pelo nome da aplicação (**`appids:"tor, ngrok, teamviewer";`**)!; e **(2) `rna` (*Real-time Network Awareness*)**!

## Como funciona
O inspetor **`rna`** analisa passivamente os pacotes que passam pela rede (fingerprints TCP/IP SYN, DHCP, MAC OUI, banners HTTP/SSH/SMB) para **construir automaticamente o inventário vivo de todos os hosts, sistemas operacionais, portas abertas e serviços descobertos na rede sem enviar um único pacote ativo de scan**!

## Exemplo
```lua
-- Habilitar no snort.lua o OpenAppID (appid) com log de estatisticas de aplicacoes e usar 'appids' dentro de regras do Snort 3
appid =
{
    app_detector_dir = '/usr/local/lib/odp',
    log_stats = true,
    app_stats_period = 300,
}
```

## Limites e trade-offs
Olhe como é simples criar uma regra de política corporativa usando **`appids`** no Snort 3 depois de ativar o `appid`: **`alert tcp $HOME_NET any -> $EXTERNAL_NET any ( msg:"POLICY-SHADOW-IT Uso de tunel reverso Ngrok ou Tor detectado"; flow:to_server,established; appids:"ngrok,tor"; sid:1000020; rev:1; )`**!

## Como verificar
Combine os eventos gerados pelo **`rna`** e pelo **`appid`** com o SIEM para detectar em segundos qualquer dispositivo não gerenciado (*Rogue Device*) conectado na rede interna.

## Conexões
- [[snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data]] — Veja também: A Nova Sintaxe de Regras do **Snort 3**: **Sticky Buffers (`http_uri`, `http_header`, `http_client_body`, `file_data`)**, Cabeçalhos de Serviço (`alert http`) e `snort2lua`.
- [[snort-modos-operacao-libdaq-afpacket-nfq-inline-ips-drop-reject]] — Veja também: Operação Inline (**IPS Ativo: `drop`, `sdrop`, `reject`**) vs. Passivo (**IDS / TAP**) no Snort 3 com **`libdaq` (`afpacket`, `nfq`, `pcap`, `dpdk`)**.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.
- [[snort-configuracao-snort-lua-home-net-wizard-binder-portless]] — Referência cruzada direta com snort-configuracao-snort-lua-home-net-wizard-binder-portless.
- [[arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi]] — Referência cruzada direta com arkime-arquitetura-full-packet-capture-capture-viewer-opensearch-spi.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
