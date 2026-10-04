---
id: software.seguranca.tranche07.000604
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

# `testssl.sh`: Auditoria de Certificados X.509 (`-S`), Cadeia de Confiança, **OCSP Stapling**, *Certificate Transparency* e Registros **DNS CAA**

## Em uma frase
A opção **`-S` (`--server-defaults`)** do `testssl.sh` inspeciona profundamente o certificado X.509 (ou múltiplos certificados, caso o servidor apresente cadeias duplas RSA + ECDSA): algoritmo e tamanho da chave, algoritmo de assinatura, `Subject Alternative Names` (SAN), validade, cadeia de intermediárias, **OCSP Stapling**, *Must-Staple*, *Certificate Transparency* (SCTs) e registros **DNS CAA** (RFC 8659).

## Por que importa
Um erro operacional recorrente em produção é instalar no Nginx/Envoy apenas o certificado folha (`cert.pem`) esquecendo de concatenar o certificado da Autoridade Certificadora Intermediária (`fullchain.pem`): navegadores desktop às vezes mascaram o erro via *AIA Fetching*, mas clientes CLI (`curl`, SDKs Python/Go, webhooks e apps mobile) falham com `unable to get local issuer certificate`.

## Como funciona
O `testssl.sh -S` detecta imediatamente cadeias incompletas (`Chain of trust: NOT ok (chain incomplete)`), certificados intermediários enviados fora de ordem ou envio desnecessário do certificado Root CA na cadeia TLS.

## Exemplo
```bash
# Auditar exclusivamente os padroes do servidor, cadeia de certificados X.509, OCSP Stapling e DNS CAA
testssl.sh -S --phone-out https://portal.internal.corp:443
```

## Limites e trade-offs
Por padrão, o `testssl.sh` não contata servidores externos para verificar revogação OCSP/CRL ao vivo (para preservar privacidade OPSEC); passe **`--phone-out`** quando quiser que ele consulte ativamente o respondedor OCSP e baixe a CRL do certificado.

## Como verificar
Verifique na saída de `testssl.sh -S` que `Chain of trust` reporta `Ok`, `OCSP stapling` está `offered` e o registro `DNS CAA` existe.

## Conexões
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Veja também: `testssl.sh`: Auditoria de Categorias de Cifras (`-s` / `-E`), **Forward Secrecy** (`-f`), Curvas Elípticas e Híbridas Pós-Quânticas (**ML-KEM**).
- [[testssl-vulnerabilidades-criptograficas-heartbleed-robot-drown-poodle-logjam]] — Veja também: `testssl.sh`: Varredura de Vulnerabilidades Criptográficas TLS (`-U` — Heartbleed, ROBOT,Ticketbleed, CCS, DROWN, POODLE, Sweet32, FREAK, Logjam e CRIME/BREACH).
- [[testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico]] — Referência cruzada direta com testssl-arquitetura-auditoria-tls-sockets-bash-openssl-estatico.
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Referência cruzada direta com certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
