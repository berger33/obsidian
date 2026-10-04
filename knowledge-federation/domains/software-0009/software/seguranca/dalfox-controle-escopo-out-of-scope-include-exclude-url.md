---
id: software.seguranca.tranche05.000416
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/hahwul/dalfox/main/README.md", "https://dalfox.hahwul.com/reference/cli/", "https://github.com/hahwul/dalfox/releases"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Dalfox: Governança de Escopo (`--out-of-scope`, `--out-of-scope-file`, `--include-url`, `--exclude-url` e `--ignore-param`)

## Em uma frase
Em pipelines que consomem listas de URLs geradas por crawlers (`katana` / `httpx`), o Dalfox impõe barreiras de escopo estritas por host (`--out-of-scope` e `--out-of-scope-file`), por padrão de URL (`--include-url` / `--exclude-url`) e por nome de parâmetro (`--ignore-param`).

## Por que importa
Garante que redirecionamentos ou URLs coletadas em páginas HTML jamais façam o scanner disparar payloads de XSS contra domínios fora do contrato (ex.: `*.gov`, CDNs ou ambientes de produção) ou contra parâmetros de token anti-CSRF.

## Como funciona
Se o arquivo passado em `--out-of-scope-file` não puder ser lido, o Dalfox aborta imediatamente com erro fatal `FILE_READ_ERROR` (exit code `2`) em vez de prosseguir sem a lista de exclusão. Padrões `*.example.com` bloqueiam tanto `example.com` quanto qualquer subdomínio.

## Exemplo
```bash
# Escanear lista de URLs via pipe aplicando arquivo de exclusão de hosts, filtro de URL e ignorando csrf_token
cat discovered-urls.txt \
  | dalfox scan --input-type pipe \
    --out-of-scope-file /etc/secops/out-of-scope-hosts.txt \
    --exclude-url "logout|delete|reset-password" \
    --ignore-param csrf_token --ignore-param authenticity_token
```

## Limites e trade-offs
Em `--out-of-scope`, vírgulas **não** são separadores de hosts; repita a flag `--out-of-scope '*.gov' --out-of-scope 'cdn.example.corp'` para cada padrão ou utilize `--out-of-scope-file` com um padrão por linha.

## Como verificar
Teste passar uma URL de um host listado em `/etc/secops/out-of-scope-hosts.txt` e confirme que ela é ignorada sem envio de pacotes HTTP.

## Conexões
- [[dalfox-monitoramento-sessao-autenticada-session-check-abort]] — Veja também: Dalfox: Monitoramento Contínuo de Sessão Autenticada (`--session-check`, `--session-check-url` e `--on-session-loss`).
- [[dalfox-waf-fingerprinting-evasao-custom-payloads-encoders]] — Veja também: Dalfox: Fingerprinting de WAF (`--waf-min-confidence`), Rastreamento de Bypass e `--custom-payload`.
- [[katana-controle-escopo-field-scope-crawl-scope-out-of-scope]] — Referência cruzada direta com katana-controle-escopo-field-scope-crawl-scope-out-of-scope.
- [[subfinder-filtragem-escopo-match-filter-exclude-ip]] — Referência cruzada direta com subfinder-filtragem-escopo-match-filter-exclude-ip.

## Fontes
- [Dalfox Official GitHub — README & Key Features](https://raw.githubusercontent.com/hahwul/dalfox/main/README.md) — documentação oficial do Dalfox cobrindo subcomandos, parameter mining, DOM/AST e WAF; consultado em 2026-10-03.
- [Dalfox Official Documentation — CLI Reference](https://dalfox.hahwul.com/reference/cli/) — referência completa de flags, exit codes, monitoramento de sessão, escopo e baseline; consultado em 2026-10-03.
- [Dalfox GitHub Releases](https://github.com/hahwul/dalfox/releases) — notas de versão e distribuição oficial do Dalfox; consultado em 2026-10-03.
