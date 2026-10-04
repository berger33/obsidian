---
id: software.seguranca.tranche09.000810
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
fontes: ["https://raw.githubusercontent.com/Checkmarx/kics/master/README.md", "https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md", "https://docs.kics.io/latest/queries/all-queries/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KICS em Pipelines CI/CD: Configuração Declarativa (`kics.config`), Códigos de Saída (**`--fail-on`**, **`--ignore-on-exit`**) e Relatórios **SARIF / SonarQube / GitLab**

## Em uma frase
Para transformar o KICS em um *Quality Gate* determinístico no GitHub Actions, GitLab CI ou Jenkins sem precisar manter linhas de comando gigantescas, o KICS suporta um arquivo de configuração centralizado (**`--config kics.config`** em formato JSON, YAML ou TOML).

## Por que importa
O controle de falha do pipeline é governado por duas flags cruciais documentadas em `docs/commands.md`: **(1) `--fail-on <severidades>`** (padrão `critical,high,medium,low,info`; em pipelines de produção configure **`--fail-on critical,high`** para que achados `low`/`info` não bloqueiem o deploy!) e **(2) `--ignore-on-exit <all|results|errors|none>`** (que define se o KICS deve retornar exit code `0` mesmo quando encontra vulnerabilidades, útil quando o step seguinte faz upload do relatório **SARIF**!).

## Como funciona
Com **`--report-formats sarif,json,html,glsast,sonarqube,cyclonedx`**, o KICS exporta nativamente para a aba *GitHub Security Code Scanning* (`sarif`), *GitLab SAST* (`glsast`) e *SonarQube*!

## Exemplo
```yaml
# /cases/iac/kics.yaml — Arquivo de configuracao declarativo do KICS para Quality Gate em CI/CD
path: "."
type:
  - Terraform
  - Kubernetes
  - Dockerfile
  - OpenAPI
exclude-paths:
  - "./tests/*"
  - "./.terraform/*"
fail-on:
  - critical
  - high
report-formats:
  - sarif
  - json
output-path: "./kics-reports"
output-name: "kics-result"
ci: true
```

## Limites e trade-offs
Conhecer os códigos de saída numéricos do KICS facilita o diagnóstico em scripts de CI: **`0`** = zero vulnerabilidades nas severidades de `--fail-on`; **`50`** = encontrou vulnerabilidades `CRITICAL`; **`40`** = `HIGH`; **`30`** = `MEDIUM`; **`20`** = `LOW`; **`126`** = erro interno de motor!

## Como verificar
Execute `kics scan --config /cases/iac/kics.yaml` e verifique a geração do arquivo `kics-result.sarif`.

## Conexões
- [[kics-deteccao-segredos-embutidos-passwords-keys-regex-rules]] — Veja também: KICS: Detecção Integrada de **Segredos e Credenciais Hardcoded** em IaC (`passwords_and_secrets`, `--secrets-regexes-path` e `--disable-secrets`).
- [[kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast]] — Referência cruzada direta com kics-arquitetura-iac-sast-multi-plataforma-opa-rego-ast.
- [[kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id]] — Referência cruzada direta com kics-supressao-granular-comentarios-kics-scan-ignore-similarity-id.

## Fontes
- [Checkmarx KICS Official GitHub — Keeping Infrastructure as Code Secure Architecture & Supported Platforms](https://raw.githubusercontent.com/Checkmarx/kics/master/README.md) — repositório oficial do Checkmarx KICS cobrindo arquitetura Go + OPA/Rego, 22+ plataformas IaC suportadas e execução via CLI/Docker; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — CLI Commands, Flags & Exit Codes Reference](https://raw.githubusercontent.com/Checkmarx/kics/master/docs/commands.md) — documentação oficial de comandos, flags, códigos de saída, formatos de relatório e arquivo de configuração do KICS; consultado em 2026-10-03.
- [Checkmarx KICS Official Documentation — Architecture & Custom OPA Rego Queries](https://docs.kics.io/latest/queries/all-queries/) — documentação oficial da arquitetura interna de parsers/AST JSON e autoria de queries customizadas em Rego (`CxPolicy`); consultado em 2026-10-03.
