---
id: software.seguranca.tranche14.001342
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

# Configuração de **`snort.lua`** e Detecção de Protocolos Independente de Porta (**Portless Inspection**): Como o **`wizard`** e o **`binder`** Derrotam Evasões de Porta!

## Em uma frase
Em sistemas de detecção antigos, se um servidor HTTP ou SSH rodasse em uma porta não-padrão (por exemplo, um painel web malicioso ou C2 HTTP na porta TCP `8443` ou `4444` em vez da porta `80`), o inspetor HTTP nem sequer era acionado se a porta não estivesse listada manualmente em `HTTP_PORTS`!

## Por que importa
No **Snort 3 (`snort.lua`)**, esse ponto cego foi eliminado pela dupla **`wizard` + `binder` (*Portless Service Autodetection*)**!

## Como funciona
Como funciona a seção `3. configure bindings` do `snort.lua`? Quando uma nova conexão TCP/UDP começa, se ela não bater em um binding estático específico, ela cai na regra final **`{ use = { type = 'wizard' } }`**: o inspetor **`wizard`** analisa os primeiros bytes reais do fluxo (*spells* e *hexes*, como `GET / HTTP/1.`, `\x16\x03` do TLS ou `SSH-2.0-`), descobre dinamicamente qual protocolo de aplicação está rodando naquela porta arbitrária e aciona o **`binder`** (`{ when = { service = 'http' }, use = { type = 'http_inspect' } }`) para **plugar automaticamente o inspetor correto (`http_inspect`, `http2_inspect`, `ssl`, `ssh`, `smb`, `dns`) em qualquer porta TCP/UDP**!

## Exemplo
```lua
-- Trecho essencial de /etc/snort/snort.lua definindo HOME_NET, EXTERNAL_NET e ativando deteccao automatica de protocolos via wizard + binder
HOME_NET = '10.0.0.0/8 172.16.0.0/12 192.168.0.0/16'
EXTERNAL_NET = '!$HOME_NET'

include 'snort_defaults.lua'

stream = { }
stream_tcp = { }
http_inspect = { }
http2_inspect = { }
ssl = { }
dns = { }
wizard = default_wizard
```

## Limites e trade-offs
Repare na definição clássica de **`EXTERNAL_NET = '!$HOME_NET'`** (todo IP que não pertence à sua rede interna `HOME_NET`) no topo do `snort.lua`: configurar `HOME_NET` com as sub-redes CIDR exatas da sua organização é o passo número 1 para eliminar falsos positivos e focar as regras `$EXTERNAL_NET -> $HOME_NET`!

## Como verificar
Você também pode sobrescrever qualquer variável ou tabela Lua diretamente na linha de comando sem editar o arquivo usando a flag **`--lua`** (ex.: `--lua "HOME_NET = '192.168.1.0/24'"`).

## Conexões
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Veja também: Arquitetura do **Cisco Snort 3 (`snort3/snort3` — Snort++)**: Motor NIDS/NIPS **Multithreaded em C++17**, Configuração **LuaJIT (`snort.lua`)** e **Hyperscan**.
- [[snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics]] — Veja também: Inspetores Profundos de Protocolo (**Service Inspectors**) no Snort 3: **`http_inspect` / `http2_inspect`**, **`js_norm`**, **`dce_smb`** e Protocolos Industriais **OT/ICS (`modbus`, `dnp3`, `s7commplus`, `iec104`)**.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
