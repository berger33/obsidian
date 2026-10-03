---
id: software.seguranca.tranche01.000093
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

# OpenSSF Scorecard `Binary-Artifacts`: detecção de executáveis e binários não revisáveis commitados no repositório de código-fonte

## Em uma frase
O check **`Binary-Artifacts`** (`Risk: High — non-reviewable code`, documentado em `docs/checks.md`) verifica se o repositório de código-fonte contém artefatos executáveis binários gerados (como binários ELF/PE/Mach-O, arquivos `.class`/`.jar` Java, `.pyc` Python, `.dll`/`.so` ou wasm compilados).

## Por que importa
Como destaca `docs/checks.md`, revisões de código humanas auditam arquivos de texto, não binários: um executável `.jar`, `.exe` ou biblioteca `.so` commitado diretamente na árvore Git pode estar desatualizado em relação ao código-fonte ou conter um backdoor invisível na revisão de PR (como ocorreu em ataques reais de supply chain).

## Como funciona
O Scorecard diferencia e **permite** scripts interpretados legíveis (como scripts shell), código-fonte gerado em texto revisável (como saídas de `bison`/`yacc`/`flex`) e documentação gerada para humanos, mas penaliza qualquer binário executável opaco presente no repositório.

## Exemplo
```bash
# Auditando um repositório local ou remoto para detectar artefatos binários commitados no código:
scorecard --local=. --checks=Binary-Artifacts --show-details
```

## Limites e trade-offs
Para atingir nota `10/10` em `Binary-Artifacts`, remova binários pré-compilados e wrappers `.jar` (ou valide-os via checksum oficial) da árvore Git e compile todos os executáveis a partir do código-fonte durante o pipeline de CI.

## Como verificar
Execute `scorecard --local=. --checks=Binary-Artifacts --show-details` para listar o caminho e a linha exata de qualquer binário detectado.

## Conexões
- [[scorecard-check-branch-protection-tiers-1-a-5-code-review]] — Veja também: OpenSSF Scorecard `Branch-Protection` e `Code-Review`: pontuação em 5 Tiers contra injeção maliciosa na branch principal.
- [[scorecard-checks-token-permissions-dangerous-workflows-github-actions]] — Veja também: OpenSSF Scorecard `Token-Permissions` e `Dangerous-Workflows`: prevenção de escalação de privilégio e injeção em GitHub Actions.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
