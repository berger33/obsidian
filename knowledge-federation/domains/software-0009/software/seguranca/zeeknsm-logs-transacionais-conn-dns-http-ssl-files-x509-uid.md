---
id: software.seguranca.tranche03.000202
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek Logs Transacionais e Correlação por `uid` (`conn.log`, `dns.log`, `http.log`, `ssl.log`, `files.log`): pivotamento forense no SOC

## Em uma frase
Toda a telemetria gerada pelos scripts padrão do Zeek é organizada em arquivos de log tabulares ou JSON (`conn.log`, `dns.log`, `http.log`, `ssl.log`, `x509.log`, `files.log`, `pe.log`, `smb_files.log`, `kerberos.log`, `ssh.log`, `notice.log`) interligados por identificadores únicos determinísticos: **`uid`** (Connection UID, ex.: `C5bLoe2M0t3...`) e **`fuid`** (File UID, ex.: `F9aK1p3...`).

## Por que importa
Quando um analista de resposta a incidentes investiga uma conexão suspeita no firewall, logs comuns não vinculam diretamente a sessão TCP de camada 4 aos múltiplos certificados TLS ou aos arquivos binários transferidos dentro daquela sessão.

## Como funciona
No Zeek, toda conexão em `conn.log` recebe um **`uid`** único que é repetido em `http.log`, `dns.log`, `ssl.log` e `ssh.log`; quando um arquivo ou certificado trafega nessa conexão, o Zeek gera um **`fuid`** em `files.log` que referencia o `uid` da conexão e aponta para os metadados detalhados em `x509.log` ou `pe.log`!

## Exemplo
```bash
#habilitando saída nativa em JSON em todos os logs do Zeek e filtrando uma sessão específica pelo uid:
zeek -C -r tráfego.pcap LogAscii::use_json=T
jq 'select(.uid == "CHhAvVGS1DHFjwGM9")' conn.log http.log ssl.log files.log
```

## Limites e trade-offs
Além do `uid` interno do Zeek, carregue o script `policy/protocols/conn/community-id-logging` para incluir a coluna `community_id` (hash SHA-1 padrão de 5-tupla) em `conn.log`, permitindo pivotar instantaneamente entre eventos do **Zeek** e alertas do **Suricata**!

## Como verificar
Verifique os campos de `conn.log` (`id.orig_h`, `id.resp_h`, `proto`, `service`, `duration`, `orig_bytes`, `resp_bytes`, `conn_state`) com `jq . conn.log | head -n 20`.

## Conexões
- [[zeeknsm-arquitetura-event-engine-script-interpreter-nsm]] — Veja também: Zeek Network Security Monitor: arquitetura em duas camadas (*Event Engine* e *Script Interpreter*) para análise semântica de rede.
- [[zeeknsm-linguagem-scripts-eventos-tipos-nativos-addr-subnet-port-table]] — Veja também: Zeek Scripting Language: programação orientada a eventos com tipos nativos de rede (`addr`, `subnet`, `port`, `interval`, `set` e `table`).

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
