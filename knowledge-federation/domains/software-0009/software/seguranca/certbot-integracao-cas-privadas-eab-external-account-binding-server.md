---
id: software.seguranca.tranche07.000617
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

# Certbot: Uso com CAs Corporativas e Comerciais via **`--server`** e **EAB (*External Account Binding*)** (`--eab-kid` / `--eab-hmac-key`)

## Em uma frase
Embora o Certbot venha pré-configurado para a Let's Encrypt, ele é um cliente ACME padrão RFC 8555 capaz de emitir certificados de qualquer **CA Privada Corporativa** (como Smallstep `step-ca`, HashiCorp Vault PKI ACME engine, FreeIPA/Dogtag) ou CAs comerciais (ZeroSSL, Google Trust Services, DigiCert, Sectigo) através da flag **`--server <URL_DIRETORIO_ACME>`**.

## Por que importa
Muitas CAs corporativas e comerciais exigem autenticar o cliente ACME contra uma conta pré-autorizada antes de registrar a chave da conta ACME, utilizando o mecanismo **EAB (*External Account Binding*, RFC 8555 Seção 7.3.4)**.

## Como funciona
O administrador passa `--server https://ca.internal.corp/acme/corp/directory` junto com **`--eab-kid <Key_ID>`** e **`--eab-hmac-key <HMAC_Base64url>`** no registro da conta (`certbot register` ou na primeira emissão), e aponta `REQUESTS_CA_BUNDLE=/etc/ssl/certs/corp-root-ca.pem` se a CA for interna.

## Exemplo
```bash
# Registrar conta ACME vinculada via External Account Binding (EAB) em uma Autoridade Certificadora corporativa
REQUESTS_CA_BUNDLE=/etc/ssl/certs/corp-root-ca.pem \
sudo -E certbot register \
  --server https://pki.internal.corp/acme/prod/directory \
  --eab-kid "CORP_PROVISIONER_KID_01" \
  --eab-hmac-key "dGhpcy1pcy1hLXNhbXBsZS1obWFjLWtleS1iYXNlNjR1cmw" \
  --agree-tos -m pki-ops@internal.corp
```

## Limites e trade-offs
O vínculo EAB (`--eab-kid` e `--eab-hmac-key`) só precisa ser informado uma única vez no momento do registro da conta ACME (`certbot register`); todas as emissões e renovações subsequentes naquele `--server` são autenticadas pela chave privada da conta ACME salva em `/etc/letsencrypt/accounts/`.

## Como verificar
Verifique o registro da conta inspecionando `/etc/letsencrypt/accounts/pki.internal.corp/` e emita um certificado de teste com `--server`.

## Conexões
- [[certbot-acme-renewal-information-ari-revogacao-comprometimento-chave]] — Veja também: Certbot: Suporte a **ARI (*ACME Renewal Information*)**, Resposta a Incidentes de Comprometimento de Chave e `certbot revoke`.
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Veja também: Governança de Emissão ACME: Registros **DNS CAA (`issue`, `issuewild`, `iodef`, `accounturi`)** (RFC 8659 / RFC 8657) e *Certificate Transparency*.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Referência cruzada direta com certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy.
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — Referência cruzada direta com testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
