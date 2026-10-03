---
id: software.seguranca.tranche11.001063
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

# Auditoria Interativa e Verificação Ativa com **`detect-secrets audit`**: Rotulação (`is_secret`), Relatório (`--report`) e Comparação (**`--diff`**)

## Em uma frase
Uma vez que o arquivo `.secrets.baseline` foi gerado em um repositório legado, como a equipe de Segurança separa o que é um **Falso Positivo** (uma chave de mock de teste ou hash inofensivo) do que é um **Segredo Real (`True Positive`)** que precisa ser rotacionado e migrado para o Vault/Secrets Manager?

## Por que importa
Usando a ferramenta interativa **`detect-secrets audit .secrets.baseline`**! Ao executá-la no terminal, ela abre uma interface visual arquivo por arquivo, destacando em cores a linha exata do código onde o potencial segredo foi encontrado e perguntando **`Should this string be committed to the repository? (y/n)`** (onde responder `n` grava `"is_secret": true` e responder `y` grava `"is_secret": false` no JSON do `.secrets.baseline`!).

## Como funciona
Além da triagem manual, o `detect-secrets` possui **Verificação Ativa (`--only-verified` / `-n`)** para plugins que suportam validação de credencial viva, além de **`detect-secrets audit --report`** (para exportar em JSON os itens triados) e **`detect-secrets audit --diff old.baseline new.baseline`**!

## Exemplo
```bash
# Iniciar a sessao interativa de auditoria do baseline e exportar o relatorio apenas de segredos reais confirmados
detect-secrets audit .secrets.baseline
detect-secrets audit --report --only-real .secrets.baseline
```

## Limites e trade-offs
Veja como o workflow `detect-secrets audit --report --only-real .secrets.baseline` organiza o trabalho do time de AppSec: primeiro um engenheiro de segurança audita o baseline com `detect-secrets audit` marcando os verdadeiros positivos; depois, `--report --only-real` gera a **Checklist exata de Credenciais Reais para Rotação e Migração**, mantendo o histórico de auditoria versionado no próprio Git!

## Como verificar
Se durante um Code Review alguém modificar o `.secrets.baseline` em um Pull Request, rode `detect-secrets audit --diff main.baseline pr.baseline` para inspecionar visualmente apenas as diferenças introduzidas pelo PR.

## Conexões
- [[detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud]] — Veja também: Catálogo dos **27+ Plugins Detectores** do `detect-secrets`: `AWSKeyDetector`, `OpenAIDetector`, `GitHubTokenDetector`, `KeywordDetector` e Limiares de Entropia.
- [[detectsecrets-bloqueio-commits-detect-secrets-hook-pre-commit-cicd]] — Veja também: Bloqueio em Tempo Real com **`detect-secrets-hook`**: Integração com **Framework `pre-commit`** e Pipelines CI/CD (`git diff --staged` & `git ls-files`).
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
