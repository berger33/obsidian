---
id: software.seguranca.tranche07.000611
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

# EFF Certbot & Protocolo **ACME (RFC 8555)**: Arquitetura de Conta, Separação entre *Authenticators* e *Installers* e Estrutura `/etc/letsencrypt/`

## Em uma frase
**Certbot** (`certbot/certbot`, Apache-2.0, desenvolvido pela *Electronic Frontier Foundation — EFF*) é o cliente de referência do protocolo **ACME (*Automated Certificate Management Environment*, IETF RFC 8555)** para emissão, instalação, renovação e revogação automatizada de certificados digitais X.509.

## Por que importa
Elimina a principal causa histórica de indisponibilidade e falhas de segurança em HTTPS: certificados gerados manualmente com validades longas, chaves privadas copiadas por e-mail e esquecimento de renovação anual.

## Como funciona
Arquiteturalmente, o Certbot separa os plugins em duas funções independentes: **Authenticators** (provam o controle do domínio perante a Autoridade Certificadora ACME, ex.: `--webroot`, `--standalone`, `--dns-cloudflare`, `--dns-route53`) e **Installers** (modificam os arquivos de configuração do servidor web como `--nginx` ou `--apache`). Os artefatos são organizados em `/etc/letsencrypt/accounts/` (chave privada da conta ACME), `/etc/letsencrypt/archive/<dom>/` (histórico versionado), `/etc/letsencrypt/live/<dom>/` (symlinks `privkey.pem`, `cert.pem`, `chain.pem` e `fullchain.pem`) e `/etc/letsencrypt/renewal/<dom>.conf`.

## Exemplo
```bash
# Listar todos os certificados gerenciados pelo Certbot, seus dominios SAN, datas de expiracao e caminhos em /etc/letsencrypt/live/
sudo certbot certificates
```

## Limites e trade-offs
Nunca apague ou mova arquivos manualmente dentro de `/etc/letsencrypt/archive/` ou `/etc/letsencrypt/live/`, pois isso quebra os links simbólicos esperados pelo processo de renovação; use sempre `certbot delete --cert-name <nome>` quando precisar remover um certificado antigo.

## Como verificar
Verifique com `ls -la /etc/letsencrypt/live/<dominio>/` que `fullchain.pem` e `privkey.pem` são links simbólicos válidos apontando para a revisão mais recente em `../../archive/<dominio>/`.

## Conexões
- [[certbot-validacao-http01-webroot-standalone-nginx-apache-seguranca]] — Veja também: Certbot: Validação de Domínio **`HTTP-01`** (`--webroot`, `--standalone`, `--nginx`, `--apache`) e Operação sem Interrupção de Serviço.
- [[certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns]] — Referência cruzada direta com certbot-validacao-dns01-wildcard-delegacao-cname-acme-dns.
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — Referência cruzada direta com testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa.

## Fontes
- [EFF Certbot Official User Guide — Commands, Plugins & Automated Renewal](https://eff-certbot.readthedocs.io/en/latest/using.html) — guia oficial do Certbot cobrindo Authenticators vs Installers, webroot, standalone, DNS-01, hooks de renovação e chaves ECDSA; consultado em 2026-10-03.
- [EFF Certbot Official GitHub — certbot/certbot README](https://raw.githubusercontent.com/certbot/certbot/main/certbot/README.rst) — documentação oficial do projeto Certbot mantido pela Electronic Frontier Foundation (EFF); consultado em 2026-10-03.
- [IETF RFC 8555 — Automatic Certificate Management Environment (ACME)](https://datatracker.ietf.org/doc/html/rfc8555) — especificação oficial IETF RFC 8555 do protocolo ACME; consultado em 2026-10-03.
