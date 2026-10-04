---
id: software.seguranca.tranche01.000091
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
fontes: ["https://raw.githubusercontent.com/ossf/scorecard/main/README.md", "https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md", "https://github.com/ossf/scorecard"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF Scorecard: arquitetura de avaliação automatizada de postura de segurança em repositórios open-source e supply chain

## Em uma frase
O **OpenSSF Scorecard** (`ossf/scorecard`, projeto da **Open Source Security Foundation** licenciado sob Apache 2.0 e publicado com proveniência **SLSA Nível 3**) é uma ferramenta automatizada que avalia dezenas de heurísticas de segurança (**Checks** e **Probes**) em repositórios de código (GitHub e GitLab), atribuindo notas de `0` a `10` para ajudar mantenedores a fortalecerem seus projetos e consumidores a avaliarem o risco de suas dependências.

## Por que importa
Adotar uma biblioteca open-source olhando apenas para o número de estrelas no GitHub ignora riscos graves de supply chain: o projeto aceita commits diretos na `main` sem revisão? Possui binários opacos commitados no Git? As actions de CI usam tags mutáveis vulneráveis a hijacking?

## Como funciona
Conforme o README oficial do Scorecard, o projeto opera em três frentes: 1) **Scorecard CLI** e **GitHub Action** (`ossf/scorecard-action`) para que mantenedores auditem seus próprios repositórios continuamente; 2) **varredura pública semanal** dos **1 milhão de projetos open-source mais críticos** publicada no dataset público do BigQuery (`openssf:scorecardcron.scorecard-v2`); e 3) **Structured Results (Probes)** para medição objetiva de políticas como o *OpenSSF Security Baseline*.

## Exemplo
```bash
# Executando o OpenSSF Scorecard via CLI contra um repositório remoto do GitHub:
export GITHUB_AUTH_TOKEN="ghp_..."
scorecard --repo=github.com/ossf/scorecard --show-details
```

## Limites e trade-offs
Como documenta a seção *Project Non-Goals* do README oficial, a nota agregada única (`X/10`) não conta toda a história: avalie sempre os checks individuais e as **Probes** específicas relevantes para a política de risco da sua organização.

## Como verificar
Execute `scorecard --repo=github.com/ossf/scorecard --format=json` para inspecionar o relatório detalhado por check.

## Conexões
- [[scorecard-check-branch-protection-tiers-1-a-5-code-review]] — Veja também: OpenSSF Scorecard `Branch-Protection` e `Code-Review`: pontuação em 5 Tiers contra injeção maliciosa na branch principal.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
