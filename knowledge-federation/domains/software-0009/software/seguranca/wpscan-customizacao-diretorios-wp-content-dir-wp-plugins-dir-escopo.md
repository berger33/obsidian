---
id: software.seguranca.tranche09.000848
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

# WPScan: Instalações WordPress Customizadas (**`--wp-content-dir`**, **`--wp-plugins-dir`**) e Exclusão de Conteúdo (`--exclude-content-based`)

## Em uma frase
Muitos tutoriais de "obscuridade" (*Security by Obscurity*) e frameworks de boilerplate WordPress modernos (como **Roots Bedrock**) alteram a estrutura de diretórios padrão do WordPress: movendo `/wp-content/` para `/app/` e `/wp-content/plugins/` para `/app/plugins/` (ou `/assets/modules/`).

## Por que importa
Quando o WPScan não consegue deduzir automaticamente no HTML da home page que a pasta `wp-content` foi renomeada para `app`, a enumeração ativa de plugins e backups falharia se testasse o caminho padrão `/wp-content/plugins/`.

## Como funciona
Para auditar instalações Bedrock ou com diretórios customizados com 100% de precisão, basta informar **`--wp-content-dir app`** e **`--wp-plugins-dir app/plugins`** na linha de comando! E se o servidor retornar páginas "Soft 404" com um texto específico (ex.: `"Página não encontrada no portal"`), passe **`--exclude-content-based "<regex>"`** para descartar falsos positivos!

## Exemplo
```bash
# Auditar uma instalacao WordPress customizada (estilo Roots Bedrock com /app/ e /app/plugins/) filtrando Soft-404 por regex
wpscan --url https://portal.internal.corp/ \
  --wp-content-dir app \
  --wp-plugins-dir app/plugins \
  --exclude-content-based "Pagina nao encontrada|Erro 404 Customizado" \
  -e vp,vt,cb
```

## Limites e trade-offs
Lembre-se de que renomear `/wp-content/` para `/app/` ajuda contra bots cegos em massa, mas **não substitui manter os plugins atualizados**, pois qualquer visitante consegue ver `<script src="/app/plugins/nome-do-plugin/...">` no código-fonte HTML ou basta passar `--wp-content-dir app` no WPScan!

## Como verificar
Verifique no código-fonte da página inicial (`curl -s https://portal.internal.corp/ | grep -oE '/[^/]+/plugins/' | head -n 1`) qual caminho de plugins a instalação utiliza.

## Conexões
- [[wpscan-varredura-autenticada-cookie-string-basic-auth-vhost-proxy]] — Veja também: WPScan: Varredura Autenticada (**`--cookie-string`**, **`--cookie-jar`**, `--http-auth`), Cabeçalho **`--vhost`** e Encaminhamento por Proxy (`--proxy`).
- [[wpscan-arquivos-configuracao-scan-yml-json-relatorios-cicd]] — Veja também: WPScan: Configuração Segura de Token e Opções em **`~/.config/wpscan/scan.yml`** e Formatos de Saída (**`-f json`, `cli`, `cli-no-color`**).
- [[wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg]] — Referência cruzada direta com wpscan-arquitetura-scanner-wordpress-wpvulndb-cache-xdg.
- [[wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed]] — Referência cruzada direta com wpscan-enumeracao-plugins-temas-vp-ap-vt-modos-passive-aggressive-mixed.
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Referência cruzada direta com gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length.

## Fontes
- [WPScan Official GitHub — WordPress Security Scanner CLI & Enumeration Options](https://raw.githubusercontent.com/wpscanteam/wpscan/master/README.md) — repositório oficial do WPScan cobrindo modos de detecção (`mixed`, `passive`, `aggressive`), enumeração `-e`, ataques de senha e formatos de saída; consultado em 2026-10-03.
- [WPScan Official RubyGems Specification & Dependencies (`cms_scanner`)](https://raw.githubusercontent.com/wpscanteam/wpscan/master/wpscan.gemspec) — especificação oficial da gem Ruby `wpscan` e sua arquitetura sobre `cms_scanner` e `typhoeus`; consultado em 2026-10-03.
- [WPScan Official User Documentation & CLI Guide](https://github.com/wpscanteam/wpscan/wiki/WPScan-User-Documentation) — documentação oficial de uso da CLI do WPScan e integração com a API de vulnerabilidades; consultado em 2026-10-03.
