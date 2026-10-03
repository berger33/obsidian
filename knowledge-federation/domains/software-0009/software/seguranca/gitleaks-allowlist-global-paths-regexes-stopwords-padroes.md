---
id: software.seguranca.tranche01.000008
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
fontes: ["https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml", "https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md", "https://github.com/gitleaks/gitleaks"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gitleaks Anatomia da `[allowlist]` Global: exclusão de lockfiles (`go.sum`, `package-lock.json`), binários e `stopwords`

## Em uma frase
O arquivo oficial `config/gitleaks.toml` define uma seção **`[allowlist]`** global que ignora automaticamente arquivos de lock de dependências, imagens/fontes binárias, diretórios `node_modules`/`vendor`, variáveis de template (`${VAR}`, `${{ secrets.X }}`) e palavras comuns (`stopwords`).

## Por que importa
Arquivos como `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`, `go.sum` e `poetry.lock` estão repletos de hashes de integridade SHA-512/SHA-256 de alta entropia que parecem chaves secretas para qualquer detector ingênuo.

## Como funciona
Na `[allowlist]` oficial do Gitleaks: 1) `paths` exclui extensões binárias (`.png`, `.pdf`, `.exe`, `.woff2`), diretórios `node_modules`/`vendor`/`virtualenv` e lockfiles; 2) `regexes` ignora referências a variáveis de ambiente e expressões do GitHub Actions (`^\$\{\{.*\}\}$`) ou caminhos Unix (`/usr/local/...`); e 3) `stopwords` descarta strings contendo termos inócuos dentro de capturas genéricas.

## Exemplo
```toml
[allowlist]
description = "Allowlist customizada por repositório"
paths = [
  '''(^|/)tests/fixtures/.*\.json$''',
  '''(^|/)docs/examples/.*\.md$''',
]
stopwords = [
  "mock",
  "placeholder",
  "example_only",
]
```

## Limites e trade-offs
Prefira definir `[allowlist]` escopada dentro de uma tabela `rules` específica (em vez da `[allowlist]` global) quando quiser abrir exceção apenas para um tipo de token sem cegar as demais regras no mesmo arquivo.

## Como verificar
Verifique quais arquivos foram ignorados executando o Gitleaks com `--log-level debug`.

## Conexões
- [[gitleaks-formatos-relatorio-sarif-junit-json-csv-template]] — Veja também: Gitleaks Relatórios e Integração DevSecOps: geração de saídas `sarif`, `junit`, `json`, `csv` e templates Go (`--report-template`).
- [[gitleaks-varredura-commits-especificos-git-log-options-ci-pr]] — Veja também: Gitleaks no CI/CD (`gitleaks git` + opções `git log`): varredura rápida apenas dos commits de um Pull Request.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
