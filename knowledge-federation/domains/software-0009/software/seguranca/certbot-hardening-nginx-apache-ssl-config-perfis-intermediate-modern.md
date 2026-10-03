---
id: software.seguranca.tranche07.000619
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

# Certbot: Perfis de Configuração TLS gerados para Nginx/Apache (`options-ssl-nginx.conf`), *Session Tickets* e **Mozilla SSL Configuration Generator**

## Em uma frase
Quando o Certbot instala um certificado usando os plugins `--nginx` ou `--apache`, ele inclui um arquivo de parâmetros criptográficos gerenciados (`/etc/letsencrypt/options-ssl-nginx.conf` ou `options-ssl-apache.conf`) alinhado aos perfis de segurança da **Mozilla (*Intermediate* / *Modern*)**.

## Por que importa
Dois detalhes críticos na configuração TLS do Nginx/Apache exigem atenção de segurança: **`ssl_session_tickets off;`** (se os *TLS Session Tickets* ficarem ligados sem rotação frequente de chaves em memória compartilhada, eles comprometem o *Forward Secrecy*) e **`ssl_prefer_server_ciphers off;`** no perfil *Intermediate* moderno (permitindo que clientes sem AES-NI em hardware mobile negociem `ChaCha20-Poly1305` com a mesma segurança AEAD).

## Como funciona
Para ambientes de altíssima segurança onde todos os clientes suportam **TLS 1.3**, o perfil **Mozilla Modern** habilita exclusivamente `ssl_protocols TLSv1.3;`, eliminando toda a superfície legada de negociação do TLS 1.2.

## Exemplo
```nginx
# Configuracao Nginx endurecida (Mozilla Intermediate + HSTS) consumindo os certificados do Certbot
server {
    listen 443 ssl;
    http2 on;
    server_name api.exemplo.com.br;

    ssl_certificate     /etc/letsencrypt/live/api.exemplo.com.br/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/api.exemplo.com.br/privkey.pem;
    ssl_protocols       TLSv1.2 TLSv1.3;
    ssl_ciphers         ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305;
    ssl_prefer_server_ciphers off;
    ssl_session_tickets off;

    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
}
```

## Limites e trade-offs
Não edite diretamente o arquivo `/etc/letsencrypt/options-ssl-nginx.conf`, pois o Certbot pode gerenciá-lo em atualizações; se precisar de um perfil TLS customizado, defina as diretivas `ssl_*` no seu próprio snippet `/etc/nginx/snippets/tls-hardened.conf` usando `certbot certonly`.

## Como verificar
Após aplicar a configuração no Nginx (`nginx -t && systemctl reload nginx`), audite com `testssl.sh -p -s -f -h https://api.exemplo.com.br` e confirme nota `A+`.

## Conexões
- [[certbot-governanca-dns-caa-rfc8659-ct-logs-monitoramento-expiracao]] — Veja também: Governança de Emissão ACME: Registros **DNS CAA (`issue`, `issuewild`, `iodef`, `accounturi`)** (RFC 8659 / RFC 8657) e *Certificate Transparency*.
- [[certbot-execucao-containers-docker-volumes-permissoes-rootless]] — Veja também: Certbot: Execução Isolada em Containers Docker (`certbot/certbot`), Volumes Persistentes e Operação *Non-Root* (`--config-dir`, `--work-dir`, `--logs-dir`).
- [[certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores]] — Referência cruzada direta com certbot-arquitetura-protocolo-acme-rfc8555-plugins-autenticadores.
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Referência cruzada direta com testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem.
- [[testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl]] — Referência cruzada direta com testssl-simulacao-clientes-tls-compatibilidade-navegadores-java-openssl.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
