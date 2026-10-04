---
id: software.seguranca.tranche09.000841
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

# **WPScan (`wpscanteam/wpscan`)**: Arquitetura do Scanner de Segurança WordPress em Ruby (`Typhoeus`/`Nokogiri`), Banco Local `~/.cache/wpscan/db` e **API WPVulnDB**

## Em uma frase
**WPScan** (`wpscanteam/wpscan`, escrito em Ruby >= 3.3 sobre `typhoeus`/`libcurl`, `nokogiri` e `ferrum`) é o scanner de segurança black-box especializado para auditar instalações **WordPress**, cobrindo versão do Core, plugins instalados, temas, arquivos de backup de configuração (`wp-config.php.bak`), dumps de banco de dados SQL expostos, `xmlrpc.php`, `wp-cron.php` e enumeração de contas de usuários.

## Por que importa
Conforme documentado no `README.md` oficial, o WPScan mantém metadados locais de detecção no diretório compatível com a especificação XDG (**`~/.cache/wpscan/db`**, atualizado via **`wpscan --update`**) e consulta em tempo real a **WordPress Vulnerability Database API (`--api-token <TOKEN>`)** para correlacionar cada versão detectada de Core, plugin ou tema com CVEs e advisories verificados.

## Como funciona
Em execuções via container Docker oficial (`wpscanteam/wpscan`), monte sempre um volume nomeado em **`-v wpscan-db:/wpscan/.cache/wpscan/db`** para que as atualizações de banco (`--update`) persistam entre execuções.

## Exemplo
```bash
# Atualizar o banco de dados local do WPScan e verificar a versao e os metadados de instalacao
wpscan --update
wpscan --version
```

## Limites e trade-offs
Conforme detalhado no `README.md`, o plano gratuito da API do WPScan oferece **25 requisições de API por dia** (e consome 1 requisição para a versão do WordPress + 1 para o tema + 1 para cada plugin detectado): portanto, não desperdice sua cota de API rodando `-e ap` (todos os plugins) sem filtro; descubra os plugins primeiro ou passe o `--api-token` quando a lista estiver refinada!

## Como verificar
Verifique no final do relatório do WPScan a linha `Requests Done` e a cota restante da API.

## Conexões
- [[wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed]] — Veja também: WPScan (`--enumerate` / `-e`): Enumeração de **Plugins (`vp`, `ap`, `p`) e Temas (`vt`, `at`, `t`)** e Modos de Detecção (`passive`, `aggressive`, `mixed`).
- [[wpscan-arquivos-configuracao-scan-yml-json-relatorios-cicd]] — Referência cruzada direta com wpscan-arquivos-configuracao-scan-yml-json-relatorios-cicd.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
