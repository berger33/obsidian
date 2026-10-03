---
id: software.seguranca.tranche01.000098
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

# OpenSSF Scorecard Governança e Saúde do Projeto: `Maintained`, `Security-Policy` (`SECURITY.md`), `License` e `CII-Best-Practices`

## Em uma frase
Para avaliar a saúde operacional e a governança de resposta a incidentes de uma dependência open-source, o Scorecard executa os checks **`Maintained`** (atividade de commits e issues nos últimos 90 dias), **`Security-Policy`** (presença de um arquivo `SECURITY.md` com instruções de divulgação coordenada de vulnerabilidades), **`License`** (licença aprovada pela OSI/FSF) e **`CII-Best-Practices`** (selo do *OpenSSF Best Practices Badge Program*).

## Por que importa
Se um pesquisador descobrir uma vulnerabilidade 0-day em uma biblioteca que você usa, mas o repositório não possui `SECURITY.md` nem canal privado de relato (`Security-Policy: 0`) e está abandonado há anos (`Maintained: 0`), a vulnerabilidade acabará sendo divulgada em uma issue pública sem patch.

## Como funciona
Conforme documentado no README oficial do Scorecard (V5), além do check agregado `Maintained`, consumidores podem consultar **Probes** específicas (como a probe `archived`) para bloquear o uso de dependências cujos repositórios foram arquivados.

## Exemplo
```bash
# Avaliando os indicadores de governança, manutenção e política de segurança de uma dependência:
scorecard --repo=github.com/openfga/openfga \
  --checks=Maintained,Security-Policy,License,CII-Best-Practices \
  --show-details
```

## Limites e trade-offs
Coloque um arquivo `SECURITY.md` na raiz do repositório (ou no repositório `.github` da organização) detalhando o processo e o contato/GitHub Private Vulnerability Reporting para pontuar `10/10` em `Security-Policy`.

## Como verificar
Verifique seu arquivo `SECURITY.md` local rodando `scorecard --local=. --checks=Security-Policy --show-details`.

## Conexões
- [[scorecard-checks-sast-fuzzing-vulnerabilities-dependency-update-tool]] — Veja também: OpenSSF Scorecard Código Seguro: checks `SAST`, `Fuzzing`, `Vulnerabilities` (OSV) e `Dependency-Update-Tool`.
- [[scorecard-github-action-sarif-code-scanning-badge-monitoramento-continuo]] — Veja também: OpenSSF Scorecard GitHub Action (`ossf/scorecard-action`): publicação de alertas SARIF no GitHub Code Scanning e Badge oficial.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
