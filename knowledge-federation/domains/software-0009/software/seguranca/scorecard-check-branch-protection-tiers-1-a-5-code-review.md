---
id: software.seguranca.tranche01.000092
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

# OpenSSF Scorecard `Branch-Protection` e `Code-Review`: pontuação em 5 Tiers contra injeção maliciosa na branch principal

## Em uma frase
Os checks **`Branch-Protection`** e **`Code-Review`** (ambos classificados com `Risk: High` em `docs/checks.md`) avaliam se as branches padrão e de release do repositório estão protegidas contra reescrita de histórico (`git push --force`), exclusão acidental e commits diretos sem revisão humana ou sem aprovação em testes de CI.

## Por que importa
Se a conta de um único mantenedor sofrer comprometimento de credenciais ou se um contribuidor malicioso obtiver permissão de escrita, a ausência de proteção de branch e revisão obrigatória permite injetar um backdoor diretamente na branch `main`.

## Como funciona
Conforme detalhado na documentação oficial de checks do Scorecard (`docs/checks.md`), o **`Branch-Protection`** utiliza uma **pontuação em 5 níveis (Tiered Scoring)** onde cada Tier precisa ser 100% satisfeito para pontuar no Tier seguinte: **Tier 1 (3/10)**: bloquear force-push e deleção de branch; **Tier 2 (6/10)**: exigir pelo menos 1 revisor e PRs antes de merge; **Tier 3 (8/10)**: exigir aprovação de pelo menos 1 status check de CI; **Tier 4 (9/10)**: exigir pelo menos 2 revisores e revisão de `CODEOWNERS`; e **Tier 5 (10/10)**: descartar aprovações obsoletas (*Dismiss stale reviews*) em novos commits e aplicar regras a administradores.

## Exemplo
```bash
# Executando especificamente os checks Branch-Protection e Code-Review com detalhes de remediação:
scorecard --repo=github.com/minha-org/meu-repo \
  --checks=Branch-Protection,Code-Review \
  --show-details
```

## Limites e trade-offs
Observe a nota oficial em `docs/checks.md`: configurações administrativas de Branch Protection no GitHub (como `DismissStaleReviews` e `EnforceAdmins`) só são visíveis via token com permissão de admin ou quando configuradas via **GitHub Repository Rulesets**.

## Como verificar
Confira os requisitos de cada Tier atingido no array `details` da saída de `--checks=Branch-Protection --show-details`.

## Conexões
- [[scorecard-arquitetura-openssf-avaliacao-seguranca-open-source-supply-chain]] — Veja também: OpenSSF Scorecard: arquitetura de avaliação automatizada de postura de segurança em repositórios open-source e supply chain.
- [[scorecard-check-binary-artifacts-reproducible-builds-supply-chain]] — Veja também: OpenSSF Scorecard `Binary-Artifacts`: detecção de executáveis e binários não revisáveis commitados no repositório de código-fonte.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
