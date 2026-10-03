---
id: software.seguranca.tranche07.000618
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
fontes: ["https://eff-certbot.readthedocs.io/en/latest/using.html", "https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst", "https://datatracker.ietf.org/doc/html/rfc8555"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Governança de Emissão ACME: Registros **DNS CAA (`issue`, `issuewild`, `iodef`, `accounturi`)** (RFC 8659 / RFC 8657) e *Certificate Transparency*

## Em uma frase
Qualquer Autoridade Certificadora pública compatível com os requisitos do CA/Browser Forum é obrigada a consultar os registros **DNS CAA (*Certification Authority Authorization*, RFC 8659)** do domínio antes de emitir um certificado, além de publicar todos os certificados emitidos em registros públicos de **Certificate Transparency (CT)**.

## Por que importa
Sem um registro DNS CAA na zona do domínio, qualquer uma das dezenas de CAs públicas confiadas pelos navegadores no mundo pode emitir certificados para a sua empresa caso ocorra um sequestro de BGP ou falha de validação HTTP.

## Como funciona
A extensão **RFC 8657 (`accounturi` e `validationmethods`)** eleva o DNS CAA a um bloqueio criptográfico exato: além de restringir a CA (`letsencrypt.org`), ela trava no DNS o **URI exato da sua conta ACME** (`accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/123456789`) e o método permitido (`validationmethods=dns-01`), impedindo que um atacante crie outra conta na mesma CA para emitir certificados.

## Exemplo
```zone
; Registros DNS CAA (RFC 8659 + RFC 8657) travando a CA, o URI da conta ACME corporativa e o metodo DNS-01
exemplo.com.br. 3600 IN CAA 0 issue "letsencrypt.org; validationmethods=dns-01; accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/123456789"
exemplo.com.br. 3600 IN CAA 0 issuewild "letsencrypt.org; validationmethods=dns-01; accounturi=https://acme-v02.api.letsencrypt.org/acme/acct/123456789"
exemplo.com.br. 3600 IN CAA 0 iodef "mailto:secops-pki@exemplo.com.br"
```

## Limites e trade-offs
Para descobrir o `accounturi` exato da sua instalação do Certbot, inspecione o campo `"uri"` dentro do arquivo `/etc/letsencrypt/accounts/acme-v02.api.letsencrypt.org/directory/<hash>/regr.json`.

## Como verificar
Valide os registros publicados com `dig +short CAA exemplo.com.br` e monitore os logs públicos de *Certificate Transparency* (`crt.sh`) para detectar qualquer tentativa de emissão não reconhecida.

## Conexões
- [[certbot-integracao-cas-privadas-eab-external-account-binding-server]] — Veja também: Certbot: Uso com CAs Corporativas e Comerciais via **`--server`** e **EAB (*External Account Binding*)** (`--eab-kid` / `--eab-hmac-key`).
- [[certbot-hardening-nginx-apache-ssl-config-perfis-intermediate-modern]] — Veja também: Certbot: Perfis de Configuração TLS gerados para Nginx/Apache (`options-ssl-nginx.conf`), *Session Tickets* e **Mozilla SSL Configuration Generator**.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns]] — Referência cruzada direta com certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
