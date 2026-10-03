---
id: software.seguranca.tranche01.000097
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

# OpenSSF Scorecard Código Seguro: checks `SAST`, `Fuzzing`, `Vulnerabilities` (OSV) e `Dependency-Update-Tool`

## Em uma frase
O Scorecard verifica práticas contínuas de engenharia de segurança no código por meio de quatro checks complementares: **`SAST`** (execução de CodeQL, SonarCloud, Semgrep ou Snyk nos workflows), **`Fuzzing`** (integração com OSS-Fuzz, ClusterFuzzLite ou testes `Fuzz*` nativos em Go/Rust/Python/C++), **`Vulnerabilities`** (consulta ao banco **OSV.dev** para checar CVEs abertas) e **`Dependency-Update-Tool`** (configuração de Dependabot ou Renovate).

## Por que importa
Um projeto que possui `Branch-Protection` perfeita mas nunca atualiza suas dependências (`Dependency-Update-Tool: 0`), possui vulnerabilidades abertas conhecidas no OSV (`Vulnerabilities: 0`) e não executa análise estática (`SAST: 0`) continua expondo seus consumidores.

## Como funciona
Adicionar funções nativas de fuzzing em Go (`func FuzzParse(f *testing.F)`) ou integrar o **ClusterFuzzLite** no GitHub Actions, junto ao workflow do **CodeQL** e a um arquivo `.github/dependabot.yml` ou `renovate.json`, eleva simultaneamente esses quatro indicadores.

## Exemplo
```bash
# Auditando os quatro checks de qualidade de código e vulnerabilidades com o Scorecard:
scorecard --repo=github.com/google/osv-scanner \
  --checks=SAST,Fuzzing,Vulnerabilities,Dependency-Update-Tool \
  --show-details
```

## Limites e trade-offs
O check `Fuzzing` reconhece tanto o cadastro do projeto no **OSS-Fuzz** central quanto a presença de fuzzers nativos da linguagem (como `testing.F` do Go) ou workflows do **ClusterFuzzLite** no próprio repositório.

## Como verificar
Execute `scorecard --local=. --checks=Dependency-Update-Tool,SAST --show-details` no repositório local para validar a detecção.

## Conexões
- [[scorecard-checks-signed-releases-packaging-slsa-provenance-cosign]] — Veja também: OpenSSF Scorecard `Signed-Releases` e `Packaging`: assinatura de artefatos, atestados de proveniência SLSA e pacotes oficiais.
- [[scorecard-checks-maintained-cii-best-practices-security-policy-license]] — Veja também: OpenSSF Scorecard Governança e Saúde do Projeto: `Maintained`, `Security-Policy` (`SECURITY.md`), `License` e `CII-Best-Practices`.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
