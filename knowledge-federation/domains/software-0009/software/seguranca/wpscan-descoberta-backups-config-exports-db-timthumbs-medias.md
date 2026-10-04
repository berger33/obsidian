---
id: software.seguranca.tranche09.000845
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

# WPScan (`-e cb,dbe,tt,m`): Descoberta de **Backups do `wp-config.php` (`cb`)**, **Dumps de Banco SQL (`dbe`)**, Timthumbs (`tt`) e Mídias (`m`)

## Em uma frase
Durante manutenções manuais via SSH/FTP ou migrações de servidores WordPress, administradores frequentemente criam cópias de segurança do arquivo de configuração (`wp-config.php.bak`, `wp-config.php~`, `.wp-config.php.swp`, `wp-config.txt`) ou exportam dumps do banco MySQL (`backup.sql`, `wordpress.sql`, `dump.sql`) diretamente na raiz `/var/www/html/`.

## Por que importa
Como arquivos `.bak`, `.txt`, `.swp` e `.sql` **não são interpretados pelo motor PHP-FPM**, se um scanner requisitar `https://site.com/wp-config.php.bak`, o Nginx/Apache serve o código-fonte PHP em texto claro contendo `DB_PASSWORD`, `AUTH_KEY` e credenciais de SMTP/AWS!

## Como funciona
No WPScan, passar **`--enumerate cb,dbe`** testa sistematicamente dezenas de padrões de **Config Backups (`cb`)** e **Database Exports (`dbe`)**, além de **`tt`** (scripts TimThumb legados) e **`m1-50`** (arquivos de mídia por ID).

## Exemplo
```bash
# Auditar especificamente a exposicao de backups do wp-config.php (cb) e dumps de banco de dados SQL (dbe) na raiz web
wpscan --url https://blog.internal.corp/ \
  --enumerate cb,dbe \
  --no-update \
  -o /cases/pentest/wpscan_config_db_exposures.txt
```

## Limites e trade-offs
No servidor web Nginx/Apache, adicione uma regra explícita bloqueando qualquer acesso HTTP a arquivos ocultos (`/\.(?!well-known)`), arquivos de backup (`~* \.(bak|old|orig|save|swp|sql|tar|gz|zip)$`) e ao próprio `wp-config.php*`.

## Como verificar
Confirme com `curl -I https://blog.internal.corp/wp-config.php` e `wp-config.php.bak` que o servidor responde `403`/`404` sem expor bytes do arquivo.

## Conexões
- [[wpscan-auditoria-senhas-forca-bruta-wp-login-xmlrpc-multicall]] — Veja também: WPScan: Auditoria de Senhas (`-P`) via **`wp-login.php`** vs Amplificação **`xmlrpc.php` (`system.multicall`)** e Como Mitigar no Servidor.
- [[wpscan-modo-stealthy-controle-taxa-throttle-random-user-agent-waf]] — Veja também: WPScan: Modo Furtivo (**`--stealthy`**), Controle de Taxa (**`--throttle`**, **`--max-threads`**), `--random-user-agent` e Bypass/Detecção de WAF.
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.
- [[gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups]] — Referência cruzada direta com gobuster-padroes-arquivos-patterns-p-wordlists-dinamicas-backups.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
