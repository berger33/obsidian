---
id: software.seguranca.tranche01.000100
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

# OpenSSF Scorecard em Escala: *Probes* estruturadas (V5), API REST (`api.scorecard.dev`) e dataset público no BigQuery

## Em uma frase
Conforme destacado no README oficial do Scorecard, para avaliar políticas corporativas sobre centenas de dependências open-source sem consumir cota da API do GitHub localmente, o ecossistema oferece **Probes granulares (`--probes`)**, a **Scorecard REST API** (`https://api.scorecard.dev/projects/github.com/{org}/{repo}`) e o dataset público semanal no **Google BigQuery (`openssf:scorecardcron.scorecard-v2_latest`)**.

## Por que importa
Ao avaliar 500 dependências de um projeto, rodar o binário `scorecard` do zero contra os 500 repositórios remotos esgotaria rapidamente o limite de 5.000 requisições/hora do token do GitHub; consultar a REST API pública ou a view do BigQuery retorna os resultados pré-computados instantaneamente.

## Como funciona
Além disso, o sistema de **Probes** (introduzido como base dos *Structured Results* na V5) desacopla a observação factual (ex.: `archived`, `hasSecurityPolicy`, `fuzzed`, `codeApproved`, `pinsDependencies`) da opinião de peso numérico dos checks tradicionais, permitindo criar políticas internas precisas.

## Exemplo
```bash
# Consultando o resultado mais recente de um projeto via Scorecard REST API pública:
curl -fsS "https://api.scorecard.dev/projects/github.com/ossf/scorecard" | jq '{score: .score, date: .date}'

# Executando probes específicas diretamente pela CLI do Scorecard:
scorecard --repo=github.com/ossf/scorecard --probes=archived,hasSecurityPolicy
```

## Limites e trade-offs
Ao automatizar auditorias de portfólio sobre milhares de repositórios públicos, utilize a tabela `openssf.scorecardcron.scorecard-v2_latest` no BigQuery ou a REST API `api.scorecard.dev` como primeira fonte antes de disparar scans ativos.

## Como verificar
Execute o `curl` acima contra `api.scorecard.dev` e inspecione a matriz `.checks[]` retornada.

## Conexões
- [[scorecard-github-action-sarif-code-scanning-badge-monitoramento-continuo]] — Veja também: OpenSSF Scorecard GitHub Action (`ossf/scorecard-action`): publicação de alertas SARIF no GitHub Code Scanning e Badge oficial.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
