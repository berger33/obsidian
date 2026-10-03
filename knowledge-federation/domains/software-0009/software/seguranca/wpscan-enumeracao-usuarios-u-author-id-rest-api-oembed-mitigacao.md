---
id: software.seguranca.tranche09.000843
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

# WPScan (`-e u1-50`): Vetores de **Enumeração de Usuários WordPress** (`/?author=N`, REST API `/wp-json/wp/v2/users`, `oEmbed`, `wp-sitemap.xml` e RSS) e Hardening

## Em uma frase
Quando você executa **`wpscan --url https://alvo/ --enumerate u`** (ou especifica um intervalo de IDs de banco de dados com **`--enumerate u1-100`**), o WPScan não usa apenas um método: ele testa sistematicamente **todos os vetores nativos pelos quais o WordPress vaza os `slugs` / logins dos usuários cadastrados**!

## Por que importa
Os principais vetores testados pelo WPScan são: **(1) Author Archives (`/?author=1`, `/?author=2`)** — onde o WordPress responde com `HTTP 301 Moved Permanently` para `/author/<username>/`; **(2) WordPress REST API (`/wp-json/wp/v2/users`)** — que retorna um JSON público com `id`, `name` e `slug` dos autores; **(3) Endpoints `oEmbed` (`/wp-json/oembed/1.0/embed?url=...`)**; **(4) Sitemaps nativos (`/wp-sitemap-users-1.xml`)**; **(5) Feeds RSS (`/feed/`)**; e **(6) Mensagens de erro distintas na tela de login (`wp-login.php`)**!

## Como funciona
Para defender um site WordPress corporativo contra `wpscan -e u`, não basta bloquear `/?author=1` no Nginx: é preciso desabilitar ou exigir autenticação na rota `/wp-json/wp/v2/users`, remover o sitemap de usuários, desvincular o `display_name` / `user_nicename` do `user_login` real e uniformizar as mensagens de erro de login!

## Exemplo
```bash
# Enumerar os primeiros 50 IDs de usuarios cadastrados no WordPress para auditar exposicao de identidades administrativas
wpscan --url https://blog.internal.corp/ \
  --enumerate u1-50 \
  --no-update \
  -o /cases/pentest/wpscan_users.txt
```

## Limites e trade-offs
Depois de aplicar o hardening no WordPress/WAF para bloquear `/wp-json/wp/v2/users`, `/wp-sitemap-users-*.xml` e `/?author=*`, reexecute `wpscan --url https://blog.internal.corp/ -e u1-50` como teste de regressão para comprovar que nenhum login é enumerado.

## Como verificar
Verifique se existe alguma conta utilizando o login padrão inseguro `admin` (ID `1`) e recomende substituí-la imediatamente.

## Conexões
- [[wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed]] — Veja também: WPScan (`--enumerate` / `-e`): Enumeração de **Plugins (`vp`, `ap`, `p`) e Temas (`vt`, `at`, `t`)** e Modos de Detecção (`passive`, `aggressive`, `mixed`).
- [[wpscan-auditoria-senhas-forca-bruta-wp-login-xmlrpc-multicall]] — Veja também: WPScan: Auditoria de Senhas (`-P`) via **`wp-login.php`** vs Amplificação **`xmlrpc.php` (`system.multicall`)** e Como Mitigar no Servidor.
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
