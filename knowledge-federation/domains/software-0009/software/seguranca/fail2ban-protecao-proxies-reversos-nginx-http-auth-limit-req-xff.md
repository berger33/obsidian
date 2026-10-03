---
id: software.seguranca.tranche07.000666
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
fontes: ["https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md", "https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5", "https://github.com/fail2ban/fail2ban/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Fail2ban: Proteção de Proxies Reversos **Nginx / Envoy** (`nginx-http-auth`, `nginx-limit-req`, `nginx-botsearch`) e Cuidados com `X-Forwarded-For`

## Em uma frase
Quando o Fail2ban protege servidores web **Nginx**, **Apache** ou **Envoy**, ele pode atuar em sinergia direta com o módulo `ngx_http_limit_req_module` do Nginx (`jail [nginx-limit-req]`): o Nginx aplica *rate limiting* leve em memória (`HTTP 429/503`) e grava `limiting requests, excess: ...` no `error.log`; se o mesmo IP insistir ultrapassando o limite repetidas vezes, o Fail2ban lê o `error.log` e corta a conexão diretamente na camada 3/4 (`nftables`) antes mesmo do handshake TLS!

## Por que importa
Porém, existe uma armadilha clássica quando o servidor Nginx está atrás de um balanceador de carga (Cloudflare, AWS ALB, HAProxy): se o Nginx não estiver configurado com **`set_real_ip_from <CIDR_DO_LB>;`** e **`real_ip_header X-Forwarded-For;`**, o IP gravado em `$remote_addr` será o IP do próprio balanceador de carga — e banir o IP do balanceador derrubará o site para 100% dos clientes!

## Como funciona
Inversamente, nunca extraia o IP de um cabeçalho `X-Forwarded-For` no filtro do Fail2ban se o servidor web estiver exposto diretamente à internet sem `set_real_ip_from` restrito aos IPs dos proxies confiáveis, pois qualquer atacante falsificaria `X-Forwarded-For: 1.2.3.4`.

## Exemplo
```nginx
# Configuracao obrigatoria no Nginx atras de Load Balancer confiavel antes de ativar jails do Fail2ban
set_real_ip_from 10.10.0.0/16;
real_ip_header X-Forwarded-For;
real_ip_recursive on;
```

## Limites e trade-offs
Se o tráfego passa por uma CDN pública (como Cloudflare ou AWS WAF) onde o pacote TCP na placa de rede vem dos IPs da CDN, bloquear no `nftables` local não surtirá efeito (e não deve bloquear a CDN); nesse cenário, configure a **Action** do Fail2ban (`action.d/cloudflare-apiv4.conf`) para banir o IP do cliente diretamente na API da borda da CDN.

## Como verificar
Teste o `nginx-limit-req` em homologação e confirme com `fail2ban-client status nginx-limit-req` que apenas o IP real do cliente ofensor é capturado.

## Conexões
- [[fail2ban-acoes-bloqueio-nftables-ipset-banimento-incremental-recidive]] — Veja também: Fail2ban: Escalabilidade de Firewall com Sets **`nftables` / `ipset`**, *Exponential Backoff* (`bantime.increment`) e Jail **`recidive`**.
- [[fail2ban-agrupamento-sessoes-tags-f-mlfid-f-id-no-failure]] — Veja também: Fail2ban: Correlação Multi-Linha com Tags de Sessão (**`<F-MLFID>`**, **`<F-ID>`**, **`<F-NOFAIL>`**) para Daemons que Logam IP e Falha em Linhas Separadas.
- [[fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos]] — Referência cruzada direta com fail2ban-desenvolvimento-filtros-failregex-ignoreregex-prevencao-redos.

## Fontes
- [Fail2ban Official GitHub — Daemon Architecture & Usage](https://raw.githubusercontent.com/fail2ban/fail2ban/master/README.md) — documentação oficial do Fail2ban cobrindo arquitetura, suporte IPv6, fail2ban-client e limites frente a autenticação fraca; consultado em 2026-10-03.
- [Fail2ban Official Manual Page — jail.conf(5) Configuration Reference](https://raw.githubusercontent.com/fail2ban/fail2ban/master/man/jail.conf.5) — manual oficial jail.conf(5) cobrindo precedência .conf vs .local, interpolação %(known/...)s, banco SQLite, filtros e actions; consultado em 2026-10-03.
- [Fail2ban Official Wiki — Hardening & Filter Best Practices](https://github.com/fail2ban/fail2ban/wiki) — wiki oficial do projeto Fail2ban sobre escrita segura de expressões regulares e prevenção de ReDoS/Log Injection; consultado em 2026-10-03.
