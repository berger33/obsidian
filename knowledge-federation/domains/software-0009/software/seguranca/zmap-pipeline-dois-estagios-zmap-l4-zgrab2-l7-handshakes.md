---
id: software.seguranca.tranche08.000796
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
fontes: ["https://raw.githubusercontent.com/zmap/zmap/main/README.md", "https://raw.githubusercontent.com/zmap/zgrab2/master/README.md", "https://github.com/zmap/zmap/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura **ZMap (L4) + ZGrab 2.0 (L7)**: Pipeline de Sondagem em Escala de Camada de Transporte para Transcrição Completa de Handshakes de Aplicação

## Em uma frase
Como o ZMap é propositalmente um scanner *stateless* de pacote único (ele envia `SYN`, recebe `SYN-ACK` e o kernel envia `RST`), o ZMap sozinho não completa handshakes TCP nem fala protocolos de aplicação (TLS, HTTP, SSH, SMTP, Modbus).

## Por que importa
Conforme documentado no `README.md` oficial do **ZGrab 2.0 (`zmap/zgrab2`)**, o projeto ZMap foi desenhado para operar em dupla com o **ZGrab 2.0** em um pipeline Unix nativo (**`zmap -p 443 | zgrab2 tls`**): o **ZMap** descobre em alta velocidade quais IPs têm a porta L4 aberta e alimenta em streaming via `stdin` o **ZGrab 2.0** (escrito em Go), que realiza o handshake completo de Camada 7 e grava a transcrição estruturada em JSON!

## Como funciona
O ZGrab 2.0 inclui **30 módulos nativos de protocolo L7**: `amqp`, `bacnet`, `banner`, `dnp3`, `fox`, `ftp`, `http`, `imap`, `ipp`, `jarm`, `managesieve`, `memcached`, `modbus`, `mongodb`, `mqtt`, `mssql`, `mysql`, `ntp`, `oracle`, `pop3`, `postgres`, `pptp`, `redis`, `siemens`, `smb`, `smtp`, `socks5`, `ssh`, `telnet` e `tls`!

## Exemplo
```bash
# Pipeline classico ZMap (L4 stateless) -> ZGrab 2.0 (L7 stateful) para auditar certificados e cifras TLS na porta 443
sudo zmap -p 443 -B 10M -q \
  -b /cases/easm/internal_blocklist.conf \
  10.20.0.0/16 \
  | zgrab2 tls --port 443 --output-file=/cases/easm/zgrab2_tls_443.jsonl
```

## Limites e trade-offs
Conforme destaca a nota de **Ethical Scanning** no `README.md` oficial do ZGrab 2.0: o ZGrab coleta exclusivamente informações de handshake disponíveis antes da autenticação (banners, certificados X.509, versões de protocolo, algoritmos SSH KEX/HostKey) e **aborta a conexão antes de qualquer tentativa de login**, garantindo segurança operacional total em auditorias de inventário.

## Como verificar
Inspecione os certificados X.509 e versões TLS negociadas no arquivo JSONL com `jq '.data.tls.result.handshake_log.server_certificates.certificate.parsed.subject' /cases/easm/zgrab2_tls_443.jsonl`.

## Conexões
- [[zmap-modulos-saida-output-modules-campos-output-filter-json-csv]] — Veja também: ZMap **Output Modules (`-O`)**, Seleção de Campos (**`-f` / `--output-fields`**) e Expressões Booleanas **`--output-filter`**.
- [[zmap-zgrab2-configuracao-multiplos-modulos-multiple-ini-triggers]] — Veja também: **ZGrab 2.0 (`zgrab2 multiple -c config.ini`)**: Orquestração de Múltiplos Protocolos L7, Formato CSV (`IP, DOMAIN, TAG, PORT`) e **`--trigger`**.
- [[zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless]] — Referência cruzada direta com zmap-arquitetura-varredura-internet-grupos-ciclicos-multiplicativos-stateless.

## Fontes
- [ZMap Official GitHub — Fast Single-Packet Network Scanner Architecture](https://raw.githubusercontent.com/zmap/zmap/main/README.md) — documentação oficial do ZMap cobrindo permutação por grupos cíclicos multiplicativos, módulos de sondagem/saída e controle de banda; consultado em 2026-10-03.
- [ZGrab 2.0 Official GitHub — Modular Application-Layer (L7) Network Scanner](https://raw.githubusercontent.com/zmap/zgrab2/master/README.md) — documentação oficial do ZGrab 2.0 cobrindo os 30 módulos de protocolo de camada 7, encadeamento com o ZMap e modo multiple.ini; consultado em 2026-10-03.
- [ZMap Official Wiki — Probe Modules, Output Filters, Blocklists & Ethical Scanning](https://github.com/zmap/zmap/wiki) — wiki técnica oficial do ZMap sobre listas de bloqueio RFC 1918, filtros de saída, sharding determinístico e boas práticas de varredura ética; consultado em 2026-10-03.
