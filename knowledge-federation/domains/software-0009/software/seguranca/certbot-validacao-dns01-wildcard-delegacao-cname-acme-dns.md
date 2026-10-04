---
id: software.seguranca.tranche07.000613
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

# Certbot: Validação **`DNS-01`** para Certificados *Wildcard* e Isolamento de Credenciais DNS com **Delegação `CNAME` (`acme-dns`)**

## Em uma frase
O desafio **`DNS-01`** (RFC 8555 Seção 8.4) prova o controle sobre um domínio ou certificado curinga (`*.exemplo.com.br`) publicando um registro DNS **`TXT`** em **`_acme-challenge.<dominio>`** contendo o hash SHA-256 Base64url da autorização ACME.

## Por que importa
Um grande risco de segurança ao usar plugins de DNS diretos (`certbot-dns-route53`, `certbot-dns-cloudflare`) é armazenar na máquina web uma chave de API com permissão para alterar registros `A`/`MX`/`TXT` de toda a zona DNS de produção: se o servidor web sofrer RCE, o atacante sequestra o DNS inteiro da empresa.

## Como funciona
A arquitetura padrão-ouro para eliminar esse risco é a **Delegação `CNAME` para uma zona ACME isolada** (ou servidor **`acme-dns`** dedicado): na zona DNS principal de produção cria-se uma única vez um registro estático `_acme-challenge.api.exemplo.com.br. IN CNAME d4e5f6.auth.acme-zones.exemplo.com.br.`, e o servidor web recebe credenciais restritas apenas para atualizar aquele único registro TXT no subdomínio delegado.

## Exemplo
```bash
# Emitir certificado Wildcard via plugin DNS com tempo de propagacao controlado e arquivo de credenciais restrito (0600)
chmod 0600 /etc/letsencrypt/secrets/dns-provider.ini
sudo certbot certonly \
  --dns-cloudflare \
  --dns-cloudflare-credentials /etc/letsencrypt/secrets/dns-provider.ini \
  --dns-cloudflare-propagation-seconds 30 \
  -d "exemplo.com.br" -d "*.exemplo.com.br"
```

## Limites e trade-offs
Todo arquivo de credenciais de API DNS (`.ini` / `.json`) deve ter permissão **`0600` (`root:root`)** e o token de API na nuvem deve ser restrito por política IAM/ Escopo apenas ao verbo `ChangeResourceRecordSets` / `DNS:Edit` do registro `_acme-challenge` específico.

## Como verificar
Verifique com `dig +short TXT _acme-challenge.exemplo.com.br` a resolução do CNAME delegado durante um teste com `certbot renew --dry-run`.

## Conexões
- [[certbot-validacao-http01-webroot-standalone-nginx-apache-seguranca]] — Veja também: Certbot: Validação de Domínio **`HTTP-01`** (`--webroot`, `--standalone`, `--nginx`, `--apache`) e Operação sem Interrupção de Serviço.
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Veja também: Certbot: Automação de Renovação (`certbot renew`), `systemd` Timers e Diferença entre `--pre-hook`, `--post-hook` e **`--deploy-hook`**.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Referência cruzada direta com certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
