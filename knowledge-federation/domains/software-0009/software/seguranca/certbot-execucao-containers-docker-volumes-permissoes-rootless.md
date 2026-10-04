---
id: software.seguranca.tranche07.000620
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

# Certbot: Execução Isolada em Containers Docker (`certbot/certbot`), Volumes Persistentes e Operação *Non-Root* (`--config-dir`, `--work-dir`, `--logs-dir`)

## Em uma frase
O projeto Certbot publica imagens oficiais em containers Docker (`certbot/certbot` e `certbot/dns-<provedor>`) para ambientes imutáveis onde não se instalam pacotes Python/`snap` diretamente no host Linux.

## Por que importa
O erro mais comum ao executar o Certbot em container efêmero (`docker run --rm`) é esquecer de montar um volume persistente para **`/etc/letsencrypt`**: a cada execução o container gera uma nova conta ACME e solicita um novo certificado do zero, estourando o **Rate Limit de 5 certificados duplicados por semana** da Let's Encrypt em poucas horas.

## Como funciona
Para rodar o Certbot sem privilégios de `root` no host (como um usuário dedicado `acme-runner`), utilize as flags **`--config-dir`**, **`--work-dir`**, **`--logs-dir`** e **`--http-01-port 8080`** apontando para diretórios de propriedade do usuário não-privilegiado.

## Exemplo
```bash
# Executar o Certbot como usuario sem privilegios (non-root) usando diretorios dedicados e porta alta local
certbot certonly --webroot \
  --config-dir /var/lib/acme-runner/config \
  --work-dir /var/lib/acme-runner/work \
  --logs-dir /var/lib/acme-runner/logs \
  -w /var/lib/acme-runner/webroot \
  -d portal.exemplo.com.br \
  --non-interactive --agree-tos -m secops@exemplo.com.br
```

## Limites e trade-offs
Ao desenvolver ou testar automações de containers e scripts de provisionamento ACME, passe **sempre** a flag **`--staging`** (ou `--dry-run`) até que o volume persistente `/etc/letsencrypt` esteja validado, pois o ambiente de Staging da Let's Encrypt tem limites de taxa muito mais altos e não consome a cota de produção.

## Como verificar
Verifique que as permissões da pasta `archive/` e `accounts/` dentro de `--config-dir` permanecem `0700` restritas ao usuário `acme-runner`.

## Conexões
- [[certbot-hardening-nginx-apache-ssl-config-perfis-intermediate-modern]] — Veja também: Certbot: Perfis de Configuração TLS gerados para Nginx/Apache (`options-ssl-nginx.conf`), *Session Tickets* e **Mozilla SSL Configuration Generator**.
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Referência cruzada direta com certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy.
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
