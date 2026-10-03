---
id: software.seguranca.tranche07.000612
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

# Certbot: Validação de Domínio **`HTTP-01`** (`--webroot`, `--standalone`, `--nginx`, `--apache`) e Operação sem Interrupção de Serviço

## Em uma frase
O desafio **`HTTP-01`** (RFC 8555 Seção 8.3) valida o controle sobre um FQDN instruindo o cliente ACME a disponibilizar um arquivo de token assinado pelo thumbprint da conta ACME no caminho exato **`http://<dominio>/.well-known/acme-challenge/<token>`** na porta TCP `80`.

## Por que importa
Em servidores de produção que já estão rodando Nginx, Envoy ou HAProxy, o autenticador **`certonly --webroot -w /var/www/acme`** é o modo mais seguro e não-intrusivo: o Certbot apenas grava o arquivo de desafio no diretório estático sem tocar nos arquivos de configuração do servidor web e sem parar o processo.

## Como funciona
Já o autenticador **`--standalone`** sobe um servidor HTTP temporário próprio na porta `80` (útil em servidores de e-mail ou gateways VPN que não rodam um servidor web permanente, ou atrás de um proxy reverso que encaminha `/.well-known/acme-challenge/` para uma porta alta local via `--http-01-port 8080`).

## Exemplo
```bash
# Emitir certificado sem tocar na configuracao do servidor web (certonly --webroot) e testar antes no ambiente de Staging
sudo certbot certonly --webroot \
  -w /var/www/acme-challenges \
  -d api.exemplo.com.br -d auth.exemplo.com.br \
  --staging --non-interactive --agree-tos -m secops@exemplo.com.br
```

## Limites e trade-offs
O desafio `HTTP-01` **sempre inicia a verificação na porta `80/TCP`** (embora siga redirecionamentos `301`/`302` para `https://` na porta `443`) e **não** pode emitir certificados curinga (*Wildcard* `*.exemplo.com.br`), que exigem obrigatoriamente o desafio `DNS-01`.

## Como verificar
Configure no Nginx um bloco dedicado `location ^~ /.well-known/acme-challenge/ { root /var/www/acme-challenges; }` que sirva os desafios em HTTP e redirecione todo o restante do tráfego da porta 80 para HTTPS.

## Conexões
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Veja também: EFF Certbot & Protocolo **ACME (RFC 8555)**: Arquitetura de Conta, Separação entre *Authenticators* e *Installers* e Estrutura `/etc/letsencrypt/`.
- [[certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns]] — Veja também: Certbot: Validação **`DNS-01`** para Certificados *Wildcard* e Isolamento de Credenciais DNS com **Delegação `CNAME` (`acme-dns`)**.
- [[certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy]] — Referência cruzada direta com certbot-renovacao-automatica-systemd-timers-hooks-pre-post-deploy.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
