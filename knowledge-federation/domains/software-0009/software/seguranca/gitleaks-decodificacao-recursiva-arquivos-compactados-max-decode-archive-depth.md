---
id: software.seguranca.tranche01.000006
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md", "https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml", "https://github.com/gitleaks/gitleaks"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gitleaks Inspeção Profunda: decodificação recursiva (`--max-decode-depth`) e varredura de arquivos compactados (`--max-archive-depth`)

## Em uma frase
O Gitleaks possui duas flags avançadas para descobrir segredos ofuscados ou empacotados: **`--max-decode-depth`** (que decodifica recursivamente strings codificadas em Base64, Hex, Percent-encoding/URL, etc. antes de aplicar as regras) e **`--max-archive-depth`** (que inspeciona o interior de arquivos compactados `.tar`, `.zip`, `.gz` até a profundidade configurada).

## Por que importa
Desenvolvedores ou scripts de build frequentemente salvam configurações completas codificadas em Base64 dentro de manifestos ou empacotam diretórios em arquivos `.tar.gz`/`.zip` dentro do repositório, escapando de scanners que leem apenas texto plano superficial.

## Como funciona
Por padrão, ambas as flags têm valor `0` (desabilitadas para máxima velocidade). Ao definir `--max-decode-depth 3` e `--max-archive-depth 2`, o Gitleaks decodifica camadas sucessivas de codificação e abre arquivos compactados aninhados em memória para aplicar todas as regras de detecção.

## Exemplo
```bash
# Varrendo diretório com decodificação recursiva (até 3 níveis) e inspeção de arquivos .zip/.tar.gz (até 2 níveis):
gitleaks dir \
  --max-decode-depth 3 \
  --max-archive-depth 2 \
  --max-target-megabytes 50 \
  ./releases
```

## Limites e trade-offs
Combine `--max-archive-depth` com **`--max-target-megabytes`** (ex.: `50`) e **`--timeout`** para evitar que um arquivo compactado gigante (*zip bomb* ou dump de banco) degrade o tempo da pipeline.

## Como verificar
Teste a detecção de um token codificado em Base64 passando-o por `echo "<base64>" | gitleaks stdin --max-decode-depth 2 -v`.

## Conexões
- [[gitleaks-baseline-scanning-adocao-repositorios-legados-baseline-path]] — Veja também: Gitleaks Baseline Scanning (`--baseline-path`): adoção incremental em repositórios legados sem bloquear o CI com dívida antiga.
- [[gitleaks-formatos-relatorio-sarif-junit-json-csv-template]] — Veja também: Gitleaks Relatórios e Integração DevSecOps: geração de saídas `sarif`, `junit`, `json`, `csv` e templates Go (`--report-template`).

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
