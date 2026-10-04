---
id: software.seguranca.tranche14.001343
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

# Inspetores Profundos de Protocolo (**Service Inspectors**) no Snort 3: **`http_inspect` / `http2_inspect`**, **`js_norm`**, **`dce_smb`** e Protocolos Industriais **OT/ICS (`modbus`, `dnp3`, `s7commplus`, `iec104`)**

## Em uma frase
O que acontece se um atacante dividir um payload de exploit HTTP em dezenas de pacotes TCP fora de ordem (*TCP Segmentation Overlapping*), comprimir a resposta em `gzip`/`deflate`/`brotli`, usar codificação chunked ou ofuscar um script JavaScript malicioso com múltiplos espaços e codificações hexadecimais?

## Por que importa
Antes que qualquer regra de assinatura seja avaliada, o pacote passa pela cadeia de **Inspectors** configurada na seção `2. configure inspection` do `snort.lua`: **(1) `stream` e `stream_tcp`** — remontam fluxos TCP com consciência do sistema operacional alvo (`policy = 'linux'` / `'windows'`) para impedir evasão por fragmentação/overlap TCP!; **(2) `http_inspect` e `http2_inspect`** — descompactam payloads HTTP/1.1 e HTTP/2 (`HPACK`), decodificam URLs, normalizam caminhos (`/a/b/../c` -> `/a/c`) e separam cada parte da requisição em *Sticky Buffers* limpos!; e **(3) `js_norm` (*Enhanced JavaScript Normalizer*)** — um parser sintático Flex que normaliza código JavaScript inline em tempo real para derrotar ofuscação de exploits client-side!

## Como funciona
Além de TI tradicional (`dce_smb`, `dce_rpc`, `dns`, `ssl`, `ssh`), o Snort 3 já traz **Inspetores Nativos para Redes Industriais OT / SCADA / ICS**: **`modbus`**, **`dnp3`**, **`iec104`**, **`mms`**, **`opcua`**, **`cip` (Ethernet/IP)** e **`s7commplus` (Siemens S7)**!

## Exemplo
```bash
# Inspecionar todas as opcoes de normalizacao e descompressao suportadas pelos inspetores http_inspect e js_norm no Snort 3
snort --help-module http_inspect
snort --help-module js_norm
```

## Limites e trade-offs
Habilitar **`file_inspect = { rules_file = 'file_magic.rules' }`** e **`file_policy = { }`** no `snort.lua` também permite ao Snort 3 identificar o tipo real de arquivos (`PDF`, `EXE`, `ELF`, `ZIP`) pelo *File Magic* (independentemente da extensão do nome do arquivo!), calcular o hash `SHA-256` em trânsito e capturar o arquivo suspeito!

## Como verificar
Em redes industriais OT/SCADA, ative exclusivamente os inspetores dos protocolos usados pelos seus CLPs/RTUs (`modbus`, `s7commplus`, `opcua`) para alertar sobre comandos de escrita de registradores não autorizados.

## Conexões
- [[snort-configuracao-snort-lua-home-net-wizard-binder-portless]] — Veja também: Configuração de **`snort.lua`** e Detecção de Protocolos Independente de Porta (**Portless Inspection**): Como o **`wizard`** e o **`binder`** Derrotam Evasões de Porta!.
- [[snort-sintaxe-regras-snort3-sticky-buffers-http-inspect-file-data]] — Veja também: A Nova Sintaxe de Regras do **Snort 3**: **Sticky Buffers (`http_uri`, `http_header`, `http_client_body`, `file_data`)**, Cabeçalhos de Serviço (`alert http`) e `snort2lua`.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
