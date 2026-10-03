---
id: software.seguranca.tranche07.000605
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

# `testssl.sh`: Varredura de Vulnerabilidades Criptográficas TLS (`-U` — Heartbleed, ROBOT,Ticketbleed, CCS, DROWN, POODLE, Sweet32, FREAK, Logjam e CRIME/BREACH)

## Em uma frase
A opção **`-U` (`--vulnerable`)** executa toda a bateria de testes de vulnerabilidades históricas e modernas de implementações SSL/TLS, ou permite testar cada falha individualmente com flags dedicadas.

## Por que importa
Mesmo em empresas com gestão de patches ativa, balanceadores de carga F5/Citrix antigos, appliances VPN, impressoras, BMCs/iDRAC/iLO e sistemas legados frequentemente permanecem expostos a ataques de oráculo de PKCS#1 v1.5 (**ROBOT**) ou reutilização de chaves RSA com SSLv2 (**DROWN**).

## Como funciona
As flags individuais abrangem: **`-H` Heartbleed** (CVE-2014-0160), **`-I` CCS Injection** (CVE-2014-0224), **`-T` Ticketbleed** (CVE-2016-9244), **`--robot` ROBOT** (*Return Of Bleichenbacher's Oracle Threat*), **`-O` POODLE SSLv3 / Zombie POODLE / GOLDENDOODLE**, **`-Z` TLS Fallback SCSV** (RFC 7507), **`-W` Sweet32** (cifras de bloco de 64 bits 3DES/Blowfish, CVE-2016-2183), **`-A` BEAST**, **`-C` CRIME** (compressão TLS), **`-B` BREACH** (compressão HTTP), **`-F` FREAK**, **`-D` DROWN** e **`-J` Logjam** (grupos Diffie-Hellman fracos `<= 1024 bits`).

## Exemplo
```bash
# Executar exclusivamente a bateria de testes de vulnerabilidades criptograficas TLS (-U) contra um appliance
testssl.sh -U --warnings batch https://vpn-legacy.internal.corp:443
```

## Limites e trade-offs
A vulnerabilidade **BREACH (`-B`)** explora a compressão HTTP (`gzip`/`deflate`/`br`) em respostas dinâmicas que refletem entrada do usuário junto com segredos (como tokens CSRF) na mesma resposta; mitigue desativando compressão HTTP em endpoints sensíveis ou usando máscaras por requisição nos tokens CSRF.

## Como verificar
Confirme na seção `Testing vulnerabilities` que todas as verificações retornam `not vulnerable (OK)`.

## Conexões
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — Veja também: `testssl.sh`: Auditoria de Certificados X.509 (`-S`), Cadeia de Confiança, **OCSP Stapling**, *Certificate Transparency* e Registros **DNS CAA**.
- [[testssl-auditoria-starttls-smtp-imap-pop3-ldap-postgres-xmpp]] — Veja também: `testssl.sh`: Auditoria de Criptografia Oportunista e Obrigatória via **`STARTTLS`** (`-t smtp,imap,pop3,ftp,ldap,postgres,mysql,xmpp`).
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Referência cruzada direta com testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico.
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Referência cruzada direta com testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
