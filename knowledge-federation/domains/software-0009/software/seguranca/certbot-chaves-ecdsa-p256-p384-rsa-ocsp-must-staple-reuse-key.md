---
id: software.seguranca.tranche07.000615
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

# Certbot: Criptografia de Chave Pública (**ECDSA `secp256r1` / `secp384r1`** vs RSA), `--reuse-key` e `--must-staple`

## Em uma frase
Desde o Certbot 2.0, o tipo de chave privada gerado por padrão para novos certificados passou de RSA 2048 para **ECDSA P-256 (`--key-type ecdsa --elliptic-curve secp256r1`)**, permitindo também selecionar **`secp384r1`** (P-384) ou **`--key-type rsa --rsa-key-size 3072/4096`**.

## Por que importa
Chaves **ECDSA P-256** oferecem segurança equivalente a RSA 3072 bits com assinaturas muito menores e handshakes TLS `ECDHE_ECDSA` significativamente mais rápidos e leves em CPU nos servidores de borda.

## Como funciona
Por padrão, a cada renovação o Certbot gera uma **nova chave privada** do zero (melhor prática de rotação criptográfica); a flag `--reuse-key` só deve ser usada quando o ambiente depende estritamente de *TLSA DANE pinning* (`3 1 1` SubjectPublicKeyInfo), enquanto `--must-staple` adiciona a extensão X.509 `tlsfeature = status_request` (RFC 7633).

## Exemplo
```bash
# Solicitar certificado com chave ECDSA P-384 (secp384r1) explicitamente via Certbot
sudo certbot certonly --webroot -w /var/www/acme-challenges \
  --key-type ecdsa --elliptic-curve secp384r1 \
  -d highsec-api.exemplo.com.br
```

## Limites e trade-offs
Habilitar `--must-staple` sem garantir que o servidor web (Nginx/Apache/HAProxy) tenha cache resiliente de **OCSP Stapling** causará falha dura de conexão nos navegadores caso o respondedor OCSP da CA fique temporariamente indisponível.

## Como verificar
Inspecione a chave pública e os algoritmos do certificado gerado com `openssl x509 -in /etc/letsencrypt/live/<dom>/cert.pem -noout -text | grep -E "Public Key Algorithm|ASN1 OID"`.

## Conexões
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Veja também: Certbot: Automação de Renovação (`certbot renew`), `systemd` Timers e Diferença entre `--pre-hook`, `--post-hook` e **`--deploy-hook`**.
- [[certbot-acme-renewal-information-ari-revogacao-comprometimento-chave]] — Veja também: Certbot: Suporte a **ARI (*ACME Renewal Information*)**, Resposta a Incidentes de Comprometimento de Chave e `certbot revoke`.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — Referência cruzada direta com testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa.
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Referência cruzada direta com testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
