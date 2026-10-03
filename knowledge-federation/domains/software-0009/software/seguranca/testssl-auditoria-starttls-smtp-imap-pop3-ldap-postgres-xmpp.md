---
id: software.seguranca.tranche07.000606
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

# `testssl.sh`: Auditoria de Criptografia Oportunista e Obrigatória via **`STARTTLS`** (`-t smtp,imap,pop3,ftp,ldap,postgres,mysql,xmpp`)

## Em uma frase
Muitos protocolos de infraestrutura não iniciam a conexão diretamente com um handshake TLS na camada de transporte, mas sim em texto claro e negociam o upgrade para TLS através do comando de aplicação **`STARTTLS`**; a opção **`-t <protocolo>` (`--starttls <protocolo>`)** do `testssl.sh` instrui o scanner a realizar o diálogo de protocolo antes de iniciar os testes TLS.

## Por que importa
Servidores de e-mail (**SMTP** portas 25/587, **IMAP** 143, **POP3** 110), diretórios (**LDAP** 389), bancos de dados (**PostgreSQL** 5432, **MySQL** 3306) e **FTP** (21) frequentemente têm configurações TLS separadas do servidor web principal e acabam esquecidos com certificados expirados ou TLS 1.0 ativo.

## Como funciona
O `testssl.sh -t <proto>` suporta nativamente `ftp`, `smtp`, `lmtp`, `pop3`, `imap`, `xmpp`, `xmpp-server`, `telnet`, `ldap`, `nntp`, `postgres`, `mysql`, `irc` e `sieve`.

## Exemplo
```bash
# Auditar a configuracao TLS de um relay SMTP corporativo na porta 587 e de um banco PostgreSQL na porta 5432
testssl.sh -t smtp -p -s -S mail-relay.internal.corp:587
testssl.sh -t postgres -p -s -S db-prod01.internal.corp:5432
```

## Limites e trade-offs
Ao importar um arquivo de saída greppable do Nmap (`nmap -oG scan.gnmap` via `testssl.sh --file scan.gnmap`), o `testssl.sh` adiciona automaticamente `-t smtp` para a porta 25 e `-t ftp` para a porta 21 com base na tabela interna de serviços.

## Como verificar
Verifique nos servidores SMTP e LDAP que o certificado apresentado via `STARTTLS` corresponde ao FQDN do serviço e não aceita cifras fracas.

## Conexões
- [[testssl-vulnerabilidades-criptograficas-heartbleed-robot-drown-poodle-logjam]] — Veja também: `testssl.sh`: Varredura de Vulnerabilidades Criptográficas TLS (`-U` — Heartbleed, ROBOT,Ticketbleed, CCS, DROWN, POODLE, Sweet32, FREAK, Logjam e CRIME/BREACH).
- [[testssl-cabecalhos-seguranca-http-hsts-hpkp-cookies-banners]] — Veja também: `testssl.sh`: Inspeção de Cabeçalhos de Segurança HTTP (`-h` — HSTS, CSP, X-Frame-Options, Cookies `Secure`/`HttpOnly` e Banners de Servidor).
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Referência cruzada direta com testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico.
- [[testssl-varredura-massa-file-nmap-gnmap-parallel-json-html-csv]] — Referência cruzada direta com testssl-varredura-massa-file-nmap-gnmap-parallel-json-html-csv.
- [[impacket-desenvolvimento-scripts-customizados-dcerpc-smbconnection-pytest]] — Referência cruzada direta com impacket-desenvolvimento-scripts-customizados-dcerpc-smbconnection-pytest.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
