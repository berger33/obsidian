---
id: software.seguranca.tranche09.000850
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

# Hardening Defensivo de **WordPress** Guiado pelos Achados do WPScan (`DISABLE_WP_CRON`, `DISALLOW_FILE_EDIT`, `xmlrpc.php` e `readme.html`)

## Em uma frase
Além de vulnerabilidades de plugins, a seção **`Interesting Findings`** do WPScan aponta exposições estruturais padrão do WordPress que todo engenheiro de segurança deve remediar no `wp-config.php` e no servidor web Nginx/Apache.

## Por que importa
Os cinco controles de hardening fundamentais que neutralizam os achados do WPScan são: **(1) Desativar o editor de código PHP no painel admin (`define('DISALLOW_FILE_EDIT', true);`)** — impedindo que um administrador comprometido edite `functions.php` para ganhar RCE imediato; **(2) Desativar o `wp-cron.php` disparado por visitantes (`define('DISABLE_WP_CRON', true);`)** e movê-lo para um timer `systemd`/cron real do Linux — eliminando ataques de DoS em `/wp-cron.php`; **(3) Bloquear `/xmlrpc.php` e `/readme.html` / `/license.txt`** no Nginx; **(4) Restringir `/wp-json/wp/v2/users`**; e **(5) Montar o código PHP de core/plugins como somente-leitura** no container!

## Como funciona
Em servidores onde ninguém deve instalar plugins pelo navegador em produção (fluxo GitOps/Composer), defina também **`define('DISALLOW_FILE_MODS', true);`** no `wp-config.php`!

## Exemplo
```php
// Hardening essencial no wp-config.php contra execucao de codigo pos-comprometimento e DoS em wp-cron.php
define( 'DISALLOW_FILE_EDIT', true );
define( 'DISALLOW_FILE_MODS', true );
define( 'DISABLE_WP_CRON', true );
define( 'FORCE_SSL_ADMIN', true );
```

## Limites e trade-offs
Por que `DISALLOW_FILE_MODS = true` é um divisor de águas na segurança de containers WordPress em produção? Porque ele desativa completamente a instalação/modificação de plugins e temas via interface web, permitindo montar os diretórios `/wp-admin/`, `/wp-includes/` e `/wp-content/plugins/` em modo **estritamente somente-leitura (`ro`)**!

## Como verificar
Reexecute o WPScan após aplicar essas diretivas e confirme que `/readme.html`, `/wp-cron.php` e `/xmlrpc.php` não são mais reportados como expostos.

## Conexões
- [[wpscan-arquivos-configuracao-scan-yml-json-relatorios-cicd]] — Veja também: WPScan: Configuração Segura de Token e Opções em **`~/.config/wpscan/scan.yml`** e Formatos de Saída (**`-f json`, `cli`, `cli-no-color`**).
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.
- [[wpscan-enumeracao-usuarios-u-author-id-rest-api-oembed-mitigacao]] — Referência cruzada direta com wpscan-enumeracao-usuarios-u-author-id-rest-api-oembed-mitigacao.
- [[wpscan-auditoria-senhas-forca-bruta-wp-login-xmlrpc-multicall]] — Referência cruzada direta com wpscan-auditoria-senhas-forca-bruta-wp-login-xmlrpc-multicall.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
