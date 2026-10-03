---
id: software.seguranca.tranche07.000601
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

# `testssl.sh`: Arquitetura de Auditoria de Servidores TLS/SSL via Sockets TCP Nativo e Binários OpenSSL Estáticos

## Em uma frase
**`testssl.sh`** (`testssl/testssl.sh`, GPLv2, mantido por Dirk Wetter) é a ferramenta de linha de comando portável escrita em Bash que audita qualquer serviço TLS/SSL em qualquer porta TCP (HTTPS, SMTP/IMAP/POP3/FTP/XMPP/LDAP/Postgres `STARTTLS`) quanto ao suporte de protocolos, cifras, curvas elípticas, certificados X.509 e falhas criptográficas.

## Por que importa
Ao contrário de serviços online de terceiros (como o Qualys SSL Labs Server Test, que só alcança servidores públicos na porta 443 e expõe os resultados externamente), o `testssl.sh` roda **100% localmente dentro da LAN ou datacenter privado** contra qualquer porta ou IPv4/IPv6 interno sem enviar dados a terceiros.

## Como funciona
A arquitetura moderna do `testssl.sh` executa a grande maioria dos handshakes TLS diretamente via **sockets TCP nativos em Bash**, recorrendo ao binário auxiliar `openssl` (incluindo o binário `openssl` compilado estaticamente com suporte a cifras antigas/export em `./bin/` para diagnóstico completo) apenas quando estritamente necessário.

## Exemplo
```bash
# Exibir o banner de versao, o binario openssl detectado e listar as 370+ cifras suportadas localmente
testssl.sh --banner
testssl.sh -V | head -n 25
```

## Limites e trade-offs
O `openssl` padrão instalado em distribuições Linux modernas vem compilado sem SSLv2, SSLv3, RC4, 3DES e cifras *EXPORT*; use a imagem container oficial (`drwetter/testssl.sh`) ou o binário estático em `./bin/` do repositório do `testssl.sh` para garantir que servidores legados vulneráveis sejam testados contra 100% das cifras obsoletas.

## Como verificar
Execute `testssl.sh -V AES` para inspecionar a tabela local de cifras (hexcode, nome OpenSSL, nome IANA, troca de chaves e bits).

## Conexões
- [[testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn]] — Veja também: `testssl.sh`: Verificação de Versões de Protocolo (`-p` — SSLv2/SSLv3/TLS 1.0/1.1/1.2/1.3, QUIC/HTTP3 e ALPN).
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Referência cruzada direta com testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
