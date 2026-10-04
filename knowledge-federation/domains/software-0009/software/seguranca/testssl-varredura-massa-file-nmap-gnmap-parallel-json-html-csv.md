---
id: software.seguranca.tranche07.000609
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://testssl.sh/doc/testssl.1.md", "https://github.com/drwetter/testssl.sh", "https://github.com/testssl/testssl.sh"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `testssl.sh`: Varredura em Massa (`--file` / `-iL`, Entrada Nmap `-oG`), Execução Paralela (`--parallel`) e Relatórios Estruturados (`--jsonfile`, `--csvfile`, `--htmlfile`)

## Em uma frase
Para auditar centenas de endpoints TLS em pipelines de conformidade contínua, o `testssl.sh` aceita um arquivo de lote via **`--file <arquivo>`** (ou `-iL <arquivo>`), que pode conter tanto linhas de comando individuais do `testssl.sh` quanto diretamente um arquivo de saída **Nmap Greppable (`nmap -oG`)**.

## Por que importa
Combinado com **`--mode parallel`** (ou `--parallel`) e as opções de exportação estruturada (**`--jsonfile-pretty`**, **`--csvfile`**, **`--htmlfile`** e **`--logfile`**), o `testssl.sh` audita frotas inteiras de microsserviços em paralelo e gera artefatos JSON/CSV prontos para ingestão no DefectDojo ou SIEM.

## Como funciona
Durante varreduras em lote com `--file`, o `testssl.sh` ativa implicitamente `--warnings batch` (abortando alvos irresponsivos sem aguardar confirmação de teclado) e valida se o registro DNS `A/AAAA` do hostname retornado pelo PTR do Nmap realmente aponta de volta para o IP antes de usar o hostname como SNI.

## Exemplo
```bash
# Executar auditoria TLS em paralelo a partir de um scan Nmap (-oG) exportando JSON estruturado e HTML
testssl.sh --parallel --warnings batch \
  --connect-timeout 5 --openssl-timeout 5 \
  --jsonfile-pretty /cases/audit/tls_fleet_report.json \
  --htmlfile /cases/audit/tls_fleet_report.html \
  --file /cases/audit/nmap_open_tls_ports.gnmap
```

## Limites e trade-offs
Se você passar um diretório existente para `--jsonfile /cases/audit/json_out/`, o `testssl.sh` criará automaticamente um arquivo JSON separado por host:porta escaneado dentro daquele diretório, ideal para processamento paralelo sem contenção.

## Como verificar
Filtre os achados de severidade `HIGH` ou `CRITICAL` nos relatórios JSON gerados usando `jq '.scanResult[].vulnerabilities[] | select(.severity == "HIGH" or .severity == "CRITICAL")'`.

## Conexões
- [[testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl]] — Veja também: `testssl.sh`: Simulação de Handshake de Clientes (`-c` / `--client-simulation`) e Cálculo de **Rating Qualys SSL Labs** (`--rating`).
- [[testssl-evasao-ids-sneaky-sni-vhost-mtls-client-certs-cicd]] — Veja também: `testssl.sh`: Teste de VirtualHosts (`--ip` / `--SNI`), Autenticação Mútua **mTLS** (`--mtls`), Modo Discreto (`--sneaky`) e Gate de CI/CD.
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Referência cruzada direta com testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico.
- [[testssl-auditoria-starttls-smtp-imap-pop3-ldap-postgres-xmpp]] — Referência cruzada direta com testssl-auditoria-starttls-smtp-imap-pop3-ldap-postgres-xmpp.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
