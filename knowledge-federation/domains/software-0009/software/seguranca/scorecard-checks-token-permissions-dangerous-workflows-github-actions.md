---
id: software.seguranca.tranche01.000094
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
fontes: ["https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md", "https://raw.githubusercontent.com/ossf/scorecard/main/README.md", "https://github.com/ossf/scorecard"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF Scorecard `Token-Permissions` e `Dangerous-Workflows`: prevenção de escalação de privilégio e injeção em GitHub Actions

## Em uma frase
Os checks **`Token-Permissions`** (`Risk: High`) e **`Dangerous-Workflows`** (`Risk: Critical`) inspecionam os arquivos `.github/workflows/*.yml` do repositório para identificar permissões excessivas do `GITHUB_TOKEN` e padrões perigosos de execução de código não confiável.

## Por que importa
Dois erros clássicos em workflows do GitHub Actions comprometem repositórios inteiros: 1) deixar o `GITHUB_TOKEN` com permissão padrão `read-all`/`write-all` no topo do workflow; e 2) usar o gatilho `pull_request_target` (ou `workflow_run`) fazendo checkout e execução do código de um PR externo ou interpolando `${{ github.event.issue.title }}` diretamente dentro de um bloco `run:` (vulnerabilidade de *Script Injection*).

## Como funciona
Para pontuar `10/10` em **`Token-Permissions`**, declare **`permissions: read-all`** (ou `permissions: contents: read` / `permissions: {}`) no nível raiz do workflow e conceda permissões de escrita (`packages: write`, `id-token: write`, `security-events: write`) exclusivamente no nível do `job` individual que realmente precisa delas!

## Exemplo
```yaml
name: CI Segura
on: [push, pull_request]

# Permissão mínima no topo do workflow (exigida pelo check Token-Permissions):
permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
      - run: go test ./...
```

## Limites e trade-offs
Nunca interpole variáveis controladas pelo autor do PR (como `${{ github.event.pull_request.title }}` ou `head.ref`) diretamente em comandos shell `run:`; passe-as primeiro como variáveis de ambiente (`env:`) do step.

## Como verificar
Audite seus workflows localmente sem fazer push executando `scorecard --local=. --checks=Token-Permissions,Dangerous-Workflows --show-details`.

## Conexões
- [[scorecard-check-binary-artifacts-reproducible-builds-supply-chain]] — Veja também: OpenSSF Scorecard `Binary-Artifacts`: detecção de executáveis e binários não revisáveis commitados no repositório de código-fonte.
- [[scorecard-check-pinned-dependencies-hash-sha-imutavel-containers-actions]] — Veja também: OpenSSF Scorecard `Pinned-Dependencies`: fixação de GitHub Actions, imagens Docker e downloads por hash criptográfico SHA.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
