---
id: software.seguranca.tranche11.001064
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

# Bloqueio em Tempo Real com **`detect-secrets-hook`**: Integração com **Framework `pre-commit`** e Pipelines CI/CD (`git diff --staged` & `git ls-files`)

## Em uma frase
Como o **`detect-secrets-hook`** consegue rodar em uma fração de segundo a cada `git commit` mesmo em um monorepo com 100.000 arquivos?

## Por que importa
Porque o `detect-secrets-hook` recebe como argumentos apenas os arquivos em *stage* (passados automaticamente pelo framework **`pre-commit`** ou via `git diff --staged --name-only -z | xargs -0`), escaneia somente esses arquivos com os plugins definidos em `.secrets.baseline` e compara os achados contra o dicionário `results` do `.secrets.baseline`!

## Como funciona
Há dois resultados possíveis onde o `detect-secrets-hook` interrompe o commit (código de saída `!= 0`): **(1)** Ele encontrou nos arquivos modificados um **segredo novo que não consta no `.secrets.baseline`** (ou um segredo que já estava no baseline mas foi marcado na auditoria como `"is_secret": true`!); ou **(2)** Os números de linha de um segredo antigo do baseline mudaram porque alguém editou o arquivo acima dele, e o hook atualiza automaticamente os números de linha no `.secrets.baseline` pedindo para o desenvolvedor incluir o `.secrets.baseline` atualizado no commit!

## Exemplo
```yaml
# .pre-commit-config.yaml — Configurar o detect-secrets-hook oficial passando o arquivo .secrets.baseline
repos:
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
        args: ["--baseline", ".secrets.baseline"]
        exclude: package.lock.json
```

## Limites e trade-offs
E como evitar o ruído de *merge conflicts* nos números de linha (`line_number`) do `.secrets.baseline` em equipes muito grandes onde dezenas de desenvolvedores editam os mesmos arquivos simultaneamente? Ao gerar ou atualizar o baseline, passe a flag **`--slim`** (`detect-secrets scan --slim > .secrets.baseline`)!

## Como verificar
O modo **`--slim`** omite os números de linha (`line_number`) e ordena as entradas deterministicamente apenas por `filename + hashed_secret`, eliminando 100% dos conflitos de merge por deslocamento de linhas!

## Conexões
- [[detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao]] — Veja também: Auditoria Interativa e Verificação Ativa com **`detect-secrets audit`**: Rotulação (`is_secret`), Relatório (`--report`) e Comparação (**`--diff`**).
- [[detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist]] — Veja também: Arquitetura de **Filtros Heurísticos (`filters_used`)**, Dicionários (**`--word-list`**), Exclusões Regex e **Allowlists Inline (`pragma: allowlist secret`)**.
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.
- [[talisman-instalacao-global-git-template-framework-pre-commit-husky]] — Referência cruzada direta com talisman-instalacao-global-git-template-framework-pre-commit-husky.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
