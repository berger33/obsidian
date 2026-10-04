---
id: software.seguranca.tranche01.000034
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
fontes: ["https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md", "https://docs.dependencytrack.org/getting-started/initial-startup/", "https://github.com/DependencyTrack/dependency-track"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OWASP Dependency-Track Inteligência de Vulnerabilidades e `EPSS`: correlação multi-fonte e priorização preditiva de exploração

## Em uma frase
O Dependency-Track integra múltiplas fontes de inteligência de vulnerabilidades simultaneamente — **NVD**, **GitHub Advisories**, **OSV**, **Sonatype OSS Index**, **Snyk**, **Trivy** e **VulnDB** — e incorpora nativamente o **EPSS (*Exploit Prediction Scoring System*, da FIRST.org)** para priorizar a remediação com base na probabilidade real de exploração na natureza.

## Por que importa
Priorizar correções olhando apenas o score **CVSS Base** faz as equipes tratarem como equivalentes uma CVE de score 8.8 puramente teórica e outra CVE de score 7.5 que já possui exploit público ativo e probabilidade EPSS de `0.94` (94% de chance de exploração nos próximos 30 dias).

## Como funciona
O Dependency-Track sincroniza diariamente os scores e percentis do **EPSS** junto aos feeds de CVEs, permitindo ordenar achados, criar políticas de risco e focar os esforços de engenharia nas vulnerabilidades que combinam alta severidade CVSS com alta probabilidade de exploração EPSS.

## Exemplo
```bash
# Consultando via API do Dependency-Track a lista de vulnerabilidades e scores CVSS/EPSS de um projeto:
curl -fsS -H "X-Api-Key: ${DTRACK_API_KEY}" \
  "https://dtrack-api.internal.corp/api/v1/finding/project/${PROJECT_UUID}" | jq '.[0]'
```

## Limites e trade-offs
Para habilitar o analisador do **GitHub Advisories** ou do **Sonatype OSS Index** nas configurações de *Analyzers*, configure o Personal Access Token / credenciais correspondentes para evitar rate-limiting nas sincronizações.

## Como verificar
Verifique em *Administration -> Analyzers* e *Vulnerability Sources* se os espelhos do NVD, OSV e EPSS estão sincronizados e atualizados.

## Conexões
- [[deptrack-vex-vulnerability-exploitability-exchange-cyclonedx-triagem]] — Veja também: OWASP Dependency-Track e `CycloneDX VEX`: consumo e exportação de *Vulnerability Exploitability Exchange* para triagem auditável.
- [[deptrack-policy-engine-seguranca-licencas-risco-operacional]] — Veja também: OWASP Dependency-Track Policy Engine: políticas globais e por projeto para risco de segurança, conformidade de licenças e risco operacional.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
