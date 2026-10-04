---
id: software.seguranca.tranche03.000203
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
fontes: ["https://raw.githubusercontent.com/zeek/zeek/master/README.md", "https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst", "https://github.com/zeek/zeek"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Zeek Scripting Language: programação orientada a eventos com tipos nativos de rede (`addr`, `subnet`, `port`, `interval`, `set` e `table`)

## Em uma frase
Conforme destacado no README e em `doc/about/architecture.rst`, o diferencial central do Zeek é sua linguagem de script orientada a eventos (*Zeek Scripting Language*), que inclui tipos primitivos de primeira classe para engenharia de rede: **`addr`** (IPv4/IPv6), **`subnet`** (CIDR como `10.0.0.0/8`), **`port`** (`80/tcp`, `53/udp`), **`interval`** (`5mins`, `30secs`), **`time`** e estruturas **`table` / `set`** com expiração automática (`&create_expire`, `&read_expire`, `&write_expire`)!

## Por que importa
Escrever correlações temporais de rede em linguagens genéricas exige implementar manualmente parsers de CIDR, tabelas hash com coleta de lixo por TTL e máquinas de estado de conexão.

## Como funciona
Na linguagem do Zeek, você escreve handlers `event http_request(c: connection, method: string, original_URI: string, unescaped_URI: string, version: string)` ou `event dns_request(...)`, mantém contadores por IP de origem em uma `table[addr] of count &create_expire=1min` e dispara ações quando um limiar é atingido!

## Exemplo
```zeek
# Script detect-ssh-bruteforce-custom.zeek demonstrando tipos nativos addr, port e table com expiração:
module CustomSec;

global ssh_attempts: table[addr] of count &default=0 &create_expire=5mins;

event connection_state_remove(c: connection)
    {
    if ( c$id$resp_p == 22/tcp && c$conn?$conn_state && c$conn$conn_state == "S0" )
        {
        ssh_attempts[c$id$orig_h] += 1;
        if ( ssh_attempts[c$id$orig_h] == 20 )
            print fmt("Possível scan/força bruta SSH a partir de %s", c$id$orig_h);
        }
    }
```

## Limites e trade-offs
Sempre anote tabelas globais que acumulam IPs ou conexões da internet com atributos de expiração (**`&create_expire`**, **`&write_expire`** ou **`&read_expire`**); tabelas sem expiração em links de alto tráfego crescerão na memória RAM até esgotar o worker!

## Como verificar
Execute seu script localmente sobre um PCAP com `zeek -C -r sample.pcap ./detect-ssh-bruteforce-custom.zeek`.

## Conexões
- [[zeeknsm-logs-transacionais-conn-dns-http-ssl-files-x509-uid]] — Veja também: Zeek Logs Transacionais e Correlação por `uid` (`conn.log`, `dns.log`, `http.log`, `ssl.log`, `files.log`): pivotamento forense no SOC.
- [[zeeknsm-file-analysis-framework-faf-extracao-arquivos-hashing-mime]] — Veja também: Zeek File Analysis Framework (`FAF`): dissecção agnóstica de protocolo, detecção de MIME (`file_sniff`) e cálculo de hashes (`MD5`, `SHA1`, `SHA256`).

## Fontes
- [Zeek GitHub — README.md (Network Traffic Analysis & Security Monitoring Framework, Key Features, Scripting & Tooling)](https://raw.githubusercontent.com/zeek/zeek/master/README.md) — README oficial do zeek/zeek apresentando o framework de análise semântica de rede, estado de camada de aplicação e linguagem de scripts; consultado em 2026-10-03.
- [Zeek Official Documentation — Architecture (doc/about/architecture.rst: Event Engine, Packet/Session/File Analysis & Script Interpreter)](https://raw.githubusercontent.com/zeek/zeek/master/doc/about/architecture.rst) — Documentação oficial de arquitetura do Zeek detalhando a separação entre o Event Engine neutro de política e o Script Interpreter; consultado em 2026-10-03.
- [Zeek Network Security Monitor — Official GitHub Repository](https://github.com/zeek/zeek) — Repositório oficial BSD-3-Clause do Zeek; consultado em 2026-10-03.
