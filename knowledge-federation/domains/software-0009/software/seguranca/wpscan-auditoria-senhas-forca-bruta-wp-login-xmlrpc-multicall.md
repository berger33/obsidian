---
id: software.seguranca.tranche09.000844
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

# WPScan: Auditoria de Senhas (`-P`) via **`wp-login.php`** vs Amplificação **`xmlrpc.php` (`system.multicall`)** e Como Mitigar no Servidor

## Em uma frase
Para testar a resistência das contas enumeradas contra senhas fracas de dicionário (`--passwords` / `-P <wordlist.txt>` e `--usernames` / `-U <lista>`), o WPScan implementa três transportes selecionáveis via **`--password-attack`**: **`wp-login`**, **`xmlrpc`** e **`xmlrpc-multicall`**!

## Por que importa
O modo **`xmlrpc-multicall`** explora um problema arquitetural clássico do arquivo **`/xmlrpc.php`** do WordPress: enquanto no `wp-login.php` cada requisição HTTP POST testa apenas **1 senha**, o método XML-RPC **`system.multicall`** permite empacotar até **`500` (ou mais, configurável com `--multicall-max-passwords`) chamadas `wp.getUsersBlogs` dentro de uma única requisição HTTP POST**!

## Como funciona
Isso significa que em apenas 2 requisições HTTP para `/xmlrpc.php` (que passam abaixo de muitos limites de *Rate Limiting* baseados apenas em contagem de requisições HTTP!), um atacante consegue testar **1.000 senhas**!

## Exemplo
```bash
# Testar uma lista curta de senhas corporativas padrao contra usuarios enumerados usando um limite estrito de threads (-t 2)
wpscan --url https://blog.internal.corp/ \
  --usernames /cases/pentest/discovered_wp_users.txt \
  --passwords /cases/pentest/corp_default_passwords.txt \
  --password-attack wp-login \
  --max-threads 2 --throttle 500
```

## Limites e trade-offs
Na **Engenharia Defensiva (Blue Team)** de qualquer instalação WordPress moderna: a menos que você utilize um aplicativo legado que dependa especificamente de XML-RPC, **bloqueie completamente o acesso a `/xmlrpc.php` diretamente no Nginx / Coraza WAF / Cloudflare (`location = /xmlrpc.php { deny all; return 403; }`)** e exija MFA (2FA/WebAuthn) para todos os administradores em `/wp-login.php`!

## Como verificar
Verifique no relatório inicial do WPScan (`Interesting Findings`) se `XML-RPC seems to be enabled: https://.../xmlrpc.php` foi detectado.

## Conexões
- [[wpscan-enumeracao-usuarios-u-author-id-rest-api-oembed-mitigacao]] — Veja também: WPScan (`-e u1-50`): Vetores de **Enumeração de Usuários WordPress** (`/?author=N`, REST API `/wp-json/wp/v2/users`, `oEmbed`, `wp-sitemap.xml` e RSS) e Hardening.
- [[wpscan-descoberta-backups-config-exports-db-timthumbs-medias]] — Veja também: WPScan (`-e cb,dbe,tt,m`): Descoberta de **Backups do `wp-config.php` (`cb`)**, **Dumps de Banco SQL (`dbe`)**, Timthumbs (`tt`) e Mídias (`m`).
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
