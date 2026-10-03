---
id: software.seguranca.tranche01.000035
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

# OWASP Dependency-Track Policy Engine: políticas globais e por projeto para risco de segurança, conformidade de licenças e risco operacional

## Em uma frase
O **Policy Engine** do Dependency-Track permite definir políticas declarativas globais (ou restritas a projetos/tags específicos) que avaliam continuamente três categorias de risco: **Security** (severidade CVSS, score EPSS, CWEs proibidas), **License** (grupos de licenças SPDX *Copyleft* proibidas vs *Permissive* aprovadas) e **Operational** (idade/desatualização do componente, coordenadas PURL/CPE banidas ou hashes modificados).

## Por que importa
Sem um motor de políticas automatizado, cada equipe interpreta de forma subjetiva se um pacote desatualizado há 4 anos, uma licença `GPL-3.0` ou uma CVE `HIGH` deve ou não bloquear o lançamento (`FAIL`) ou apenas gerar aviso (`WARN` / `INFO`).

## Como funciona
Cada política no Dependency-Track define um **`Violation State`** (`INFO`, `WARN` ou `FAIL`), um operador (`ANY` ou `ALL`) e uma lista de condições (ex.: `SEVERITY IS CRITICAL`, `EPSS > 0.5`, `LICENSE_GROUP IS Copyleft`, `COMPONENT_AGE > P3Y`). Sempre que um SBOM é processado, as violações são calculadas e expostas na API e em webhooks.

## Exemplo
```bash
# Consultando as violações de política (Security, License, Operational) de um projeto para gate de CI/CD:
curl -fsS -H "X-Api-Key: ${DTRACK_API_KEY}" \
  "https://dtrack-api.internal.corp/api/v1/violation/project/${PROJECT_UUID}" \
  | jq '[.[] | select(.policyCondition.policy.violationState == "FAIL")] | length'
```

## Limites e trade-offs
Use **Project Tags** (como `tier:internet-facing`, `compliance:pci-dss` ou `distribution:saas`) para aplicar políticas de licença ou de EPSS diferenciadas conforme o perfil real de exposição da aplicação.

## Como verificar
Confirme na aba *Policy Violations* do projeto que cada violação indica a condição exata disparada e seu estado (`FAIL`/`WARN`/`INFO`).

## Conexões
- [[deptrack-fontes-inteligencia-vulnerabilidades-nvd-osv-github-epss]] — Veja também: OWASP Dependency-Track Inteligência de Vulnerabilidades e `EPSS`: correlação multi-fonte e priorização preditiva de exploração.
- [[deptrack-impact-analysis-portfolio-busca-componentes-afetados-log4shell]] — Veja também: OWASP Dependency-Track Portfolio Impact Analysis: resposta imediata a incidentes (*"O que está afetado, e onde?"*) via PURL e CPE.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
