---
id: software.seguranca.tranche07.000607
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

# `testssl.sh`: Inspeção de Cabeçalhos de Segurança HTTP (`-h` — HSTS, CSP, X-Frame-Options, Cookies `Secure`/`HttpOnly` e Banners de Servidor)

## Em uma frase
A opção **`-h` (`--header`)** do `testssl.sh` analisa a resposta HTTP retornada sobre o túnel TLS para auditar cabeçalhos de proteção de navegador, flags de segurança de cookies de sessão e vazamento de versões de software nos banners.

## Por que importa
Uma configuração TLS 1.3 perfeita na porta 443 ainda deixa o usuário vulnerável a interceptação no primeiro acesso (`http://`) se o servidor não enviar o cabeçalho **`Strict-Transport-Security` (HSTS)** com `max-age` adequado (`>= 180 dias` / `15552000` segundos, ou `31536000` para preload) ou se emitir cookies de sessão sem o atributo **`Secure`**.

## Como funciona
O teste `-h` verifica `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, códigos de redirecionamento HTTP (`301`/`302`/`307`/`308`), flags `Secure`/`HttpOnly`/`SameSite` em todos os cabeçalhos `Set-Cookie` e banners `Server` / `X-Powered-By`.

## Exemplo
```bash
# Auditar cabecalhos de seguranca HTTP, HSTS e flags de cookies (passando cabecalho customizado se necessario)
testssl.sh -h --reqheader "X-Audit-Source: SecOps-Scanner" https://app.internal.corp:443
```

## Limites e trade-offs
Se a aplicação exigir autenticação HTTP Basic para devolver os cabeçalhos das páginas internas, utilize `--basicauth usuario:senha` (ou a variável de ambiente `BASICAUTH`) durante a verificação `-h`.

## Como verificar
Confirme na saída de `testssl.sh -h` que `Strict-Transport-Security` está ativo com `max-age >= 31536000` e que 100% dos cookies possuem `Secure` e `HttpOnly`.

## Conexões
- [[testssl-auditoria-starttls-smtp-imap-pop3-ldap-postgres-xmpp]] — Veja também: `testssl.sh`: Auditoria de Criptografia Oportunista e Obrigatória via **`STARTTLS`** (`-t smtp,imap,pop3,ftp,ldap,postgres,mysql,xmpp`).
- [[testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl]] — Veja também: `testssl.sh`: Simulação de Handshake de Clientes (`-c` / `--client-simulation`) e Cálculo de **Rating Qualys SSL Labs** (`--rating`).
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Referência cruzada direta com testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
