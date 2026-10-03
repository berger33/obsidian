---
id: software.seguranca.tranche09.000846
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

# WPScan: Modo Furtivo (**`--stealthy`**), Controle de Taxa (**`--throttle`**, **`--max-threads`**), `--random-user-agent` e Bypass/Detecção de WAF

## Em uma frase
Quando um site WordPress está protegido por plugins de segurança em aplicação (como Wordfence, Solid Security / iThemes, All-In-One WP Security ou Cerber) ou por um WAF de borda, uma varredura padrão agressiva com User-Agent `WPScan v3.x` é bloqueada nas primeiras requisições.

## Por que importa
O WPScan inclui o alias composto **`--stealthy`**, que equivale a ativar simultaneamente **`--random-user-agent --detection-mode passive --plugins-version-detection passive`**: fazendo apenas requisições mínimas com User-Agent de navegador real!

## Como funciona
Para auditorias autorizadas onde você precisa de detecção ativa (`mixed`) sem derrubar o pool de workers PHP-FPM do servidor e sem disparar bloqueios por *Rate Limit*, combine **`--random-user-agent`** (`--rua`), **`--max-threads 2`** (`-t 2`) e **`--throttle 500`** (pausa de 500 milissegundos entre cada requisição HTTP, limitando o scan a 2 requisições por segundo!).

## Exemplo
```bash
# Executar varredura controlada (2 req/s via --throttle 500) com User-Agent aleatorio para preservar a estabilidade do PHP-FPM
wpscan --url https://blog.internal.corp/ \
  --random-user-agent \
  --max-threads 2 \
  --throttle 500 \
  --request-timeout 15 \
  --connect-timeout 10
```

## Limites e trade-offs
Note na documentação do WPScan: quando você define **`--throttle <milissegundos>`**, o WPScan força automaticamente `--max-threads 1` para garantir que o intervalo entre requisições seja respeitado de forma estrita!

## Como verificar
Se um WAF retornar uma página de bloqueio que impeça o WPScan de reconhecer que o alvo é um WordPress, a flag **`--force`** obriga o WPScan a prosseguir com os checks mesmo assim.

## Conexões
- [[wpscan-descoberta-backups-config-exports-db-timthumbs-medias]] — Veja também: WPScan (`-e cb,dbe,tt,m`): Descoberta de **Backups do `wp-config.php` (`cb`)**, **Dumps de Banco SQL (`dbe`)**, Timthumbs (`tt`) e Mídias (`m`).
- [[wpscan-varredura-autenticada-cookie-string-basic-auth-vhost-proxy]] — Veja também: WPScan: Varredura Autenticada (**`--cookie-string`**, **`--cookie-jar`**, `--http-auth`), Cabeçalho **`--vhost`** e Encaminhamento por Proxy (`--proxy`).
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.
- [[wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed]] — Referência cruzada direta com wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed.
- [[gobuster-controle-taxa-delay-timeout-user-agent-evasao-waf-deteccao]] — Referência cruzada direta com gobuster-controle-taxa-delay-timeout-user-agent-evasao-waf-deteccao.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
