---
id: software.seguranca.tranche14.001344
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

# A Nova Sintaxe de Regras do **Snort 3**: **Sticky Buffers (`http_uri`, `http_header`, `http_client_body`, `file_data`)**, Cabeçalhos de Serviço (`alert http`) e `snort2lua`

## Em uma frase
Quais foram as três grandes melhorias de engenharia de detecção na **Sintaxe de Regras do Snort 3** em comparação ao antigo Snort 2, e como converter automaticamente milhares de regras legadas do Snort 2 para o Snort 3?

## Por que importa
Primeira melhoria: **Cabeçalhos de Regra Baseados em Serviço (`alert http`, `alert ssl`, `alert dns`, `alert smb`)**! Em vez de escrever `alert tcp $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS` (que ficava cego se o servidor HTTP rodasse em outra porta!), no Snort 3 você escreve simplesmente **`alert http`** — e a regra é aplicada a qualquer fluxo identificado como HTTP pelo `wizard` em qualquer porta!

## Como funciona
Segunda melhoria: **Sticky Buffers (*Buffers Adesivos*)**! No Snort 2 antigo, modificadores como `http_uri;` ou `http_header;` vinham *depois* de cada `content:"..."`, tornando regras longas verbosas e propensas a erro. No Snort 3, o seletor de buffer (`http_uri;`, `http_raw_uri;`, `http_header;`, `http_client_body;`, `http_cookie;`, `file_data;`, `pkt_data;`) é um **Sticky Buffer colocado ANTES dos `content`**, e todas as cláusulas `content` e `pcre` seguintes inspecionam aquele buffer normalizado até que outro Sticky Buffer seja declarado! Terceira melhoria: sub-opções de `content` separadas por vírgula (**`content:"/admin/exec", nocase, fast_pattern;`**)!

## Exemplo
```text
# Regra nativa do Snort 3 usando cabecalho de servico 'alert http' (portless) e Sticky Buffers (http_method, http_uri e http_client_body)
alert http $EXTERNAL_NET any -> $HOME_NET any (
    msg:"SERVER-WEBAPP Tentativa de RCE Command Injection na rota /api/v1/diag";
    flow:to_server,established;
    http_method;
    content:"POST";
    http_uri;
    content:"/api/v1/diag", fast_pattern, nocase;
    http_client_body;
    content:"cmd=", nocase;
    pcre:"/cmd=[^&]*(\x3b|\x7c|\x60|\x24\x28)/i";
    sid:1000001;
    rev:1;
    classtype:web-application-attack;
)
```

## Limites e trade-offs
E se você tiver arquivos de regras ou configurações legadas do Snort 2.9? O Snort 3 inclui a ferramenta oficial **`snort2lua`** (`snort2lua -c snort.conf -o snort.lua` ou `snort2lua -c local.rules -r local_snort3.rules`), que converte automaticamente tanto o `snort.conf` quanto as regras Snort 2 para a nova sintaxe de *Sticky Buffers* do Snort 3!

## Como verificar
Sempre marque o `content` mais longo, único e específico da sua regra com a sub-opção **`fast_pattern`** para alimentar o motor **Intel Hyperscan** (MPSP — *Multi-Pattern Search Engine*) e garantir que a regra só seja avaliada quando aquele átomo exato aparecer no pacote!

## Conexões
- [[snort-inspetores-http-inspect-js-norm-dce-smb-scada-ics]] — Veja também: Inspetores Profundos de Protocolo (**Service Inspectors**) no Snort 3: **`http_inspect` / `http2_inspect`**, **`js_norm`**, **`dce_smb`** e Protocolos Industriais **OT/ICS (`modbus`, `dnp3`, `s7commplus`, `iec104`)**.
- [[snort-appid-openappid-visibilidade-camada-7-shadow-it-rna]] — Veja também: Descoberta de Aplicações Camada 7 (**OpenAppID / `appid`**) e Descoberta Passiva de Rede (**`rna` — *Real-time Network Awareness***) no Snort 3.
- [[snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan]] — Referência cruzada direta com snort-arquitetura-snort3-multithreaded-cpp17-luajit-libdaq-hyperscan.
- [[snort-configuracao-snort-lua-home-net-wizard-binder-portless]] — Referência cruzada direta com snort-configuracao-snort-lua-home-net-wizard-binder-portless.

## Fontes
- [Cisco Snort 3 (`Snort++`) Official GitHub Repository (`snort3/snort3`)](https://raw.githubusercontent.com/snort3/snort3/master/README.md) — repositório oficial do Cisco Snort 3 cobrindo arquitetura multithreaded, memória compartilhada de configuração, LuaJIT, `wizard`, sticky buffers, `libdaq` e Hyperscan; consultado em 2026-10-03.
- [Cisco Snort 3 Official Default Configuration (`lua/snort.lua`)](https://raw.githubusercontent.com/snort3/snort3/master/lua/snort.lua) — configuração oficial `snort.lua` detalhando `HOME_NET`, inspetores (`stream_tcp`, `http_inspect`, `js_norm`, `appid`, OT/ICS `modbus`/`dnp3`/`s7commplus`), `wizard`/`binder`, `profiler`, `latency`, `rate_filter` e `alert_json`; consultado em 2026-10-03.
