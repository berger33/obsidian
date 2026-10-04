---
id: software.seguranca.tranche01.000007
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

# Gitleaks Relatórios e Integração DevSecOps: geração de saídas `sarif`, `junit`, `json`, `csv` e templates Go (`--report-template`)

## Em uma frase
Por meio das flags **`-f` / `--report-format`** (`json`, `csv`, `junit`, `sarif`, `template`), **`-r` / `--report-path`** e **`--report-template`**, o Gitleaks exporta os achados em formatos padronizados para integração direta com GitHub Advanced Security / Code Scanning, GitLab Security Dashboard, Jenkins e DefectDojo.

## Por que importa
Em pipelines automatizados, apenas falhar o job com texto no console obriga o desenvolvedor a vasculhar logs brutos; exportar um relatório **SARIF** ou **JUnit** anota exatamente a linha do Pull Request na interface do repositório.

## Como funciona
Além dos quatro formatos estruturados embutidos (`json`, `csv`, `junit`, `sarif`), informar `--report-template meu-template.tmpl` aciona automaticamente `--report-format=template`, permitindo formatar payloads customizados para webhooks do Slack, Jira ou sistemas internos.

## Exemplo
```bash
# Gerando relatório SARIF com segredos redigidos para upload no GitHub Code Scanning:
gitleaks git \
  --redact=100 \
  --report-format sarif \
  --report-path results.sarif \
  --exit-code 1 \
  .
```

## Limites e trade-offs
Ao enviar relatórios SARIF para plataformas de código, mantenha sempre `--redact=100` ativo para que o valor bruto do segredo não fique armazenado nos metadados da aba Security.

## Como verificar
Valide o JSON/SARIF gerado executando `jq . results.sarif | head -n 30`.

## Conexões
- [[gitleaks-decodificacao-recursiva-arquivos-compactados-max-decode-archive-depth]] — Veja também: Gitleaks Inspeção Profunda: decodificação recursiva (`--max-decode-depth`) e varredura de arquivos compactados (`--max-archive-depth`).
- [[gitleaks-allowlist-global-paths-regexes-stopwords-padroes]] — Veja também: Gitleaks Anatomia da `[allowlist]` Global: exclusão de lockfiles (`go.sum`, `package-lock.json`), binários e `stopwords`.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
