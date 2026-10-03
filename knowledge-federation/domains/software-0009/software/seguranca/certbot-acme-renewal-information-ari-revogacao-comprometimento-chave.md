---
id: software.seguranca.tranche07.000616
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

# Certbot: Suporte a **ARI (*ACME Renewal Information*)**, Resposta a Incidentes de Comprometimento de Chave e `certbot revoke`

## Em uma frase
Versões modernas do Certbot implementam a extensão **ARI (*ACME Renewal Information*, draft-ietf-acme-ari)**: durante a checagem periódica do `certbot renew`, o Certbot consulta a API ARI da Autoridade Certificadora para saber a janela ideal de renovação.

## Por que importa
Se uma CA descobrir um bug de emissão ou precisar revogar um lote de certificados em 24 horas, o endpoint **ARI** sinaliza imediatamente aos clientes Certbot para renovarem o certificado naquele instante, mesmo que ainda faltem 75 dias para o vencimento normal.

## Como funciona
Já quando a própria empresa sofre vazamento de uma chave privada (`privkey.pem` exposta em backup ou invasão de host), o procedimento de resposta a incidentes utiliza **`certbot revoke --cert-path ... --reason keycompromise`** autenticando quer com a conta ACME original, quer com a própria chave privada vazada (`--key-path`).

## Exemplo
```bash
# Revogar imediatamente um certificado cuja chave privada foi comprometida durante um incidente de seguranca
sudo certbot revoke \
  --cert-path /etc/letsencrypt/live/compromised.exemplo.com.br/cert.pem \
  --key-path /etc/letsencrypt/live/compromised.exemplo.com.br/privkey.pem \
  --reason keycompromise \
  --no-delete-after-revoke
```

## Limites e trade-offs
Ao revogar por `--reason keycompromise`, a Autoridade Certificadora bloqueia permanentemente aquela chave pública (`SubjectPublicKeyInfo`) em sua *blocklist* para que nunca mais um certificado possa ser emitido para a chave comprometida.

## Como verificar
Após revogar o certificado comprometido em um host limpo, gere um novo par de chaves e emita o certificado substituto antes de atualizar os balanceadores.

## Conexões
- [[certbot-chaves-ecdsa-p256-p384-rsa-ocsp-must-staple-reuse-key]] — Veja também: Certbot: Criptografia de Chave Pública (**ECDSA `secp256r1` / `secp384r1`** vs RSA), `--reuse-key` e `--must-staple`.
- [[certbot-integracao-cas-privadas-eab-external-account-binding-server]] — Veja também: Certbot: Uso com CAs Corporativas e Comerciais via **`--server`** e **EAB (*External Account Binding*)** (`--eab-kid` / `--eab-hmac-key`).
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Referência cruzada direta com certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy.
- [[thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall]] — Referência cruzada direta com thehive-orquestracao-cortex-responders-contencao-ativa-edr-firewall.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
