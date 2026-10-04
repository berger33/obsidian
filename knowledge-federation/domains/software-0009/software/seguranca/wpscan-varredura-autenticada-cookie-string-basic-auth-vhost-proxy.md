---
id: software.seguranca.tranche09.000847
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md", "https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec", "https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# WPScan: Varredura Autenticada (**`--cookie-string`**, **`--cookie-jar`**, `--http-auth`), Cabeçalho **`--vhost`** e Encaminhamento por Proxy (`--proxy`)

## Em uma frase
Em ambientes de homologação (*staging*) protegidos por HTTP Basic Auth (`401 Unauthorized`), atrás de um proxy reverso exigindo cabeçalho `Host:` específico ou quando você quer auditar o WordPress usando uma sessão já autenticada de usuário comum (*Subscriber* / *Author*), o WPScan fornece suporte completo de sessão e transporte.

## Por que importa
As flags de autenticação e rede incluem: **`--cookie-string "wordpress_logged_in_...=..."`** (ou **`--cookie-jar /caminho/cookies.txt`**), **`--http-auth login:password`** (Basic/Digest Auth), **`--headers "X-Custom: valor"`**, **`--vhost blog.internal.corp`** (permite apontar `--url https://10.20.30.40/` para o IP real do servidor de origem ignorando o DNS da CDN enquanto envia `Host: blog.internal.corp`!) e **`--proxy http://127.0.0.1:8080`** (ou `socks5://127.0.0.1:1080`)!

## Como funciona
Usar **`--url https://<IP_ORIGEM>/ --vhost blog.exemplo.com.br --disable-tls-checks`** é a técnica padrão para auditar diretamente o servidor de origem quando a equipe de infraestrutura liberou o IP da estação de pentest no firewall!

## Exemplo
```bash
# Auditar diretamente o IP de origem do servidor WordPress enviando o cabecalho Host via --vhost e encaminhando pelo mitmproxy
wpscan --url https://10.20.30.40/ \
  --vhost blog.internal.corp \
  --disable-tls-checks \
  --http-auth "staging_user:StagingPass2026!" \
  --proxy http://127.0.0.1:8080 \
  -e vp,vt,u1-20
```

## Limites e trade-offs
Sempre que testar com `--cookie-string` de uma sessão autenticada, verifique antes no `mitmproxy` que o cookie `wordpress_logged_in_<hash>` e `wordpress_sec_<hash>` estão ativos e pertençam a uma conta de teste dedicada.

## Como verificar
Confirme nos fluxos capturados pelo `mitmproxy` (`127.0.0.1:8080`) que o cabeçalho `Host: blog.internal.corp` está sendo enviado em todas as requisições do WPScan.

## Conexões
- [[wpscan-modo-stealthy-controle-taxa-throttle-random-user-agent-waf]] — Veja também: WPScan: Modo Furtivo (**`--stealthy`**), Controle de Taxa (**`--throttle`**, **`--max-threads`**), `--random-user-agent` e Bypass/Detecção de WAF.
- [[wpscan-customizacao-diretorios-wp-content-dir-wp-plugins-dir-escopo]] — Veja também: WPScan: Instalações WordPress Customizadas (**`--wp-content-dir`**, **`--wp-plugins-dir`**) e Exclusão de Conteúdo (`--exclude-content-based`).
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros]] — Referência cruzada direta com gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
