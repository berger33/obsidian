---
id: software.seguranca.tranche07.000614
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

# Certbot: Automação de Renovação (`certbot renew`), `systemd` Timers e Diferença entre `--pre-hook`, `--post-hook` e **`--deploy-hook`**

## Em uma frase
O subcomando **`certbot renew`** verifica duas vezes ao dia (via `certbot.timer` do `systemd` com atraso aleatório `RandomizedDelaySec`) todos os certificados instalados e renova automaticamente aqueles que estão dentro da janela de renovação (por padrão a 30 dias da expiração, ou antes se sinalizado por **ARI**).

## Por que importa
Renovar os arquivos `.pem` em `/etc/letsencrypt/live/` **não** atualiza a memória RAM dos processos em execução (Nginx, HAProxy, Postfix, Dovecot, PostgreSQL, RabbitMQ): é indispensável configurar um **Hook de Implantação (`--deploy-hook`)** para recarregar graciosamente os serviços apenas quando uma renovação real ocorrer.

## Como funciona
O Certbot oferece três tipos de hooks: **`--pre-hook`** (roda antes da tentativa de renovação, ex.: abrir porta 80 no firewall para modo standalone), **`--post-hook`** (roda após a tentativa, tenha havido renovação ou não) e **`--deploy-hook`** (roda **uma única vez e exclusivamente se o certificado foi efetivamente emitido/renovado**, expondo as variáveis `$RENEWED_LINEAGE` e `$RENEWED_DOMAINS`).

## Exemplo
```bash
# Testar o fluxo completo de renovacao contra a CA de Staging (--dry-run) validando o script de deploy-hook
sudo certbot renew --dry-run \
  --deploy-hook "/usr/local/sbin/reload-tls-services.sh"
```

## Limites e trade-offs
Para copiar certificados renovados para serviços que não rodam como `root` (como `postgres` ou `rabbitmq`, que exigem que a chave privada pertença ao UID do serviço com modo `0600`), coloque um script executável em **`/etc/letsencrypt/renewal-hooks/deploy/`** que copie `$RENEWED_LINEAGE/fullchain.pem` e `$RENEWED_LINEAGE/privkey.pem` para `/etc/postgresql/tls/`, ajuste `chown postgres:postgres` + `chmod 0600` e execute `systemctl reload postgresql`.

## Como verificar
Confirme que `systemctl list-timers | grep certbot` mostra o timer ativo e que `sudo certbot renew --dry-run` conclui com sucesso.

## Conexões
- [[certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns]] — Veja também: Certbot: Validação **`DNS-01`** para Certificados *Wildcard* e Isolamento de Credenciais DNS com **Delegação `CNAME` (`acme-dns`)**.
- [[certbot-chaves-ecdsa-p256-p384-rsa-ocsp-must-staple-reuse-key]] — Veja também: Certbot: Criptografia de Chave Pública (**ECDSA `secp256r1` / `secp384r1`** vs RSA), `--reuse-key` e `--must-staple`.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[certbot-validacao-http01-webroot-standalone-nginx-apache-seguranca]] — Referência cruzada direta com certbot-validacao-http01-webroot-standalone-nginx-apache-seguranca.
- [[certbot-acme-renewal-information-ari-revogacao-comprometimento-chave]] — Referência cruzada direta com certbot-acme-renewal-information-ari-revogacao-comprometimento-chave.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
