---
id: software.seguranca.tranche09.000849
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

# WPScan: Configuração Segura de Token e Opções em **`~/.config/wpscan/scan.yml`** e Formatos de Saída (**`-f json`, `cli`, `cli-no-color`**)

## Em uma frase
Passar `--api-token SEU_TOKEN_SECRETO` diretamente na linha de comando expõe o token da API WPVulnDB no histórico do shell (`~/.bash_history`) e na tabela de processos (`ps aux`) de servidores compartilhados.

## Por que importa
Conforme documentado na seção `Load CLI options from file/s` do `README.md` oficial, o WPScan carrega automaticamente todas as opções de configuração (incluindo `api-token`, `max-threads`, `random-user-agent` e `disable-tls-checks`) a partir do arquivo YAML ou JSON em **`~/.config/wpscan/scan.yml`** (ou `~/.wpscan/scan.yml`)!

## Como funciona
Para integração com pipelines de DevSecOps, SIEM ou **OWASP DefectDojo**, combine **`-f json`** (`--format json`) com **`-o relatorio.json`** para obter um documento JSON estruturado contendo todas as vulnerabilidades, referências CVE/WPScan ID, CVSS e versões corrigidas (`fixed_in`).

## Exemplo
```yaml
# ~/.config/wpscan/scan.yml — Configuracao persistente do WPScan (proteger com chmod 0600)
cli_options:
  api_token: "SEU_TOKEN_WPVULNDB_AQUI"
  random_user_agent: true
  max_threads: 5
  format: json
```

## Limites e trade-offs
Proteja o arquivo `~/.config/wpscan/scan.yml` com permissão **`chmod 0600 ~/.config/wpscan/scan.yml`** para que nenhum outro usuário local consiga ler o seu `api_token`.

## Como verificar
Faça um parse rápido de todas as vulnerabilidades encontradas no relatório JSON usando **`jq '.. | objects | select(has("vulnerabilities")) | .vulnerabilities[] | select(length > 0)' /cases/pentest/wpscan_plugins_themes.json`**.

## Conexões
- [[wpscan-customizacao-diretorios-wp-content-dir-wp-plugins-dir-escopo]] — Veja também: WPScan: Instalações WordPress Customizadas (**`--wp-content-dir`**, **`--wp-plugins-dir`**) e Exclusão de Conteúdo (`--exclude-content-based`).
- [[wpscan-hardening-defensivo-wordpress-wp-cron-xmlrpc-file-edit-headers]] — Veja também: Hardening Defensivo de **WordPress** Guiado pelos Achados do WPScan (`DISABLE_WP_CRON`, `DISALLOW_FILE_EDIT`, `xmlrpc.php` e `readme.html`).
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.
- [[rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis]] — Referência cruzada direta com rustscan-arquivo-configuracao-persistente-rustscan-toml-perfis.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
