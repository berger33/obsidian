---
id: software.seguranca.tranche11.001067
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md", "https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Operando `detect-secrets` em **Monorepos de Grande Escala**: Modo **`--slim`**, Execução Paralela Multi-Core e Varredura de Arquivos Não-Rastreados (`--all-files`)

## Em uma frase
Em um monorepo corporativo onde 500 engenheiros fazem dezenas de merges por hora na branch `main`, manter um arquivo `.secrets.baseline` tradicional (que grava o `"line_number"` exato de cada falso positivo) gera um problema operacional clássico: se o Engenheiro A adiciona 5 linhas de `import` no topo de `auth.py` e o Engenheiro B adiciona 3 linhas no meio de `auth.py`, ambos os PRs tentarão atualizar o `"line_number"` no `.secrets.baseline`, gerando um **Conflito de Merge no Git**!

## Por que importa
Para eliminar 100% esse atrito em monorepos, a equipe do Yelp introduziu a flag **`--slim`** (`detect-secrets scan --slim > .secrets.baseline`)!

## Como funciona
No modo **`--slim`**, o `.secrets.baseline` remove o campo volátil `line_number` e mantém apenas a assinatura imutável (`filename` + `type` + `hashed_secret`), fazendo com que edições comuns de código nunca sujem o arquivo `.secrets.baseline`!

## Exemplo
```bash
# Gerar e manter um arquivo .secrets.baseline livre de conflitos de numero de linha (--slim) em um monorepo corporativo
detect-secrets scan --slim > .secrets.baseline
detect-secrets scan --baseline .secrets.baseline
```

## Limites e trade-offs
Atenção também ao comportamento padrão de descoberta de arquivos do `detect-secrets scan`: por padrão, ele usa `git ls-files` para varrer **apenas arquivos rastreados pelo Git** (muito mais rápido e ignora automaticamente `node_modules/`, `.venv/` e artefatos de build!). Se você estiver usando o `detect-secrets` para varrer um diretório de artefatos extraídos ou um pacote que **não é um repositório Git**, lembre-se de passar obrigatoriamente a flag **`--all-files`** (`detect-secrets scan /caminho/pasta --all-files`)!

## Como verificar
Use `-C /caminho/do/repo` quando quiser executar o `detect-secrets` a partir de outro diretório de trabalho.

## Conexões
- [[detectsecrets-extensibilidade-api-python-secretscollection-custom-plugins]] — Veja também: API Python do `detect-secrets` (**`SecretsCollection` & `transient_settings`**): Criando **Plugins e Filtros Customizados (`file://...`)**.
- [[detectsecrets-deteccao-bypasses-auditoria-ci-cd-github-actions-sarif]] — Veja também: Detecção de Bypass (`git commit --no-verify`) no CI/CD com `detect-secrets`: Como Auditar tanto **Novos Segredos** quanto **Adições Não-Auditadas ao Baseline**.
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.
- [[detectsecrets-bloqueio-commits-detect-secrets-hook-pre-commit-cicd]] — Referência cruzada direta com detectsecrets-bloqueio-commits-detect-secrets-hook-pre-commit-cicd.
- [[gitsecrets-modos-varredura-scan-cached-untracked-no-index-history]] — Referência cruzada direta com gitsecrets-modos-varredura-scan-cached-untracked-no-index-history.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
