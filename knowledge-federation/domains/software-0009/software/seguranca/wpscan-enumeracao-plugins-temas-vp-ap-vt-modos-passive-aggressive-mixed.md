---
id: software.seguranca.tranche09.000842
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

# WPScan (`--enumerate` / `-e`): Enumeração de **Plugins (`vp`, `ap`, `p`) e Temas (`vt`, `at`, `t`)** e Modos de Detecção (`passive`, `aggressive`, `mixed`)

## Em uma frase
Mais de 90% das vulnerabilidades críticas (SQLi, Unauthenticated RCE, Arbitrary File Upload, Privilege Escalation) exploradas em sites WordPress residem em **plugins e temas de terceiros**, e não no Core do WordPress.

## Por que importa
No WPScan, a flag **`-e` / `--enumerate`** controla o escopo da enumeração de componentes: **`vp`** (apenas plugins com vulnerabilidades conhecidas), **`ap`** (todos os plugins do catálogo), **`p`** (plugins populares, padrão), **`vt`** (temas vulneráveis), **`at`** (todos os temas) e **`t`** (temas populares).

## Como funciona
Crucialmente, como destaca o `README.md` oficial: **por padrão, o `--plugins-detection` do WPScan é `passive`** (analisa apenas o código-fonte HTML/JS/CSS da página inicial sem fazer brute-force de pastas `/wp-content/plugins/<slug>/`)! Se um plugin vulnerável não injetar nenhum script visível na home page, o modo `passive` não o verá: para uma auditoria profunda, combine **`-e vp,vt` com `--plugins-detection mixed` (ou `aggressive`)**!

## Exemplo
```bash
# Enumerar plugins e temas vulneraveis (-e vp,vt) combinando deteccao passiva e ativa (--plugins-detection mixed)
wpscan --url https://blog.internal.corp/ \
  --enumerate vp,vt \
  --plugins-detection mixed \
  --plugins-version-detection mixed \
  --api-token "${WPSCAN_API_TOKEN}" \
  -f json -o /cases/pentest/wpscan_plugins_themes.json
```

## Limites e trade-offs
Por que o WPScan também possui a flag **`--plugins-version-detection`** (`passive`, `aggressive`, `mixed`)? Porque depois de descobrir que um plugin existe, o WPScan precisa determinar a sua **versão exata** lendo quer o parâmetro `?ver=X.Y.Z` no HTML (`passive`), quer buscando diretamente os arquivos `readme.txt` e `changelog.txt` dentro da pasta do plugin (`aggressive`/`mixed`)!

## Como verificar
Inspecione no JSON de saída a chave `.plugins` e verifique o nível de confiança (`confidence`) da versão detectada de cada plugin.

## Conexões
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Veja também: **WPScan (`wpscanteam/wpscan`)**: Arquitetura do Scanner de Segurança WordPress em Ruby (`Typhoeus`/`Nokogiri`), Banco Local `~/.cache/wpscan/db` e **API WPVulnDB**.
- [[wpscan-enumeracao-usuarios-u-author-id-rest-api-oembed-mitigacao]] — Veja também: WPScan (`-e u1-50`): Vetores de **Enumeração de Usuários WordPress** (`/?author=N`, REST API `/wp-json/wp/v2/users`, `oEmbed`, `wp-sitemap.xml` e RSS) e Hardening.
- [[wpscan-descoberta-backups-config-exports-db-timthumbs-medias]] — Referência cruzada direta com wpscan-descoberta-backups-config-exports-db-timthumbs-medias.
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
