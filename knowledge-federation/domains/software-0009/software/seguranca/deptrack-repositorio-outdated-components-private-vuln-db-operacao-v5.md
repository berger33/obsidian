---
id: software.seguranca.tranche01.000040
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

# OWASP Dependency-Track Risco de Desatualização, Banco Privado de Vulnerabilidades e Evolução Arquitetural (`v4` -> `v5`)

## Em uma frase
Além de CVEs públicas, o Dependency-Track consulta diretamente os repositórios oficiais de pacotes (**Maven Central**, **npm**, **PyPI**, **Cargo**, **NuGet**, **Gems**, **Composer**, **Hex**, **CPAN**) para identificar **componentes desatualizados (*Out-of-date components*)**, permite manter um **banco privado de vulnerabilidades internas** (`INTERNAL`) e prepara a transição arquitetural documentada em `V5_MIGRATION.md`.

## Por que importa
Uma biblioteca interna da própria empresa que possui uma falha de segurança corrigida na versão `1.8.2` nunca aparecerá no NVD público; o banco privado de vulnerabilidades do Dependency-Track permite cadastrar um ID interno (`INT-2026-001`) e rastrear todos os serviços internos que ainda usam `< 1.8.2`!

## Como funciona
Ao cadastrar uma vulnerabilidade interna mapeada ao PURL do pacote corporativo, o motor de análise do Dependency-Track passa a sinalizar e aplicar políticas sobre ela exatamente como faz com CVEs do NVD/OSV.

## Exemplo
```bash
# Consultando métricas consolidadas de risco e desatualização do portfólio inteiro via API:
curl -fsS -H "X-Api-Key: ${DTRACK_API_KEY}" \
  "https://dtrack-api.internal.corp/api/v1/metrics/portfolio/current" | jq .
```

## Limites e trade-offs
Conforme destacado no aviso de topo do README oficial, consulte o guia `V5_MIGRATION.md` ao planejar upgrades para a geração cloud-native v5 do Dependency-Track.

## Como verificar
Verifique em *Administration -> Repositories* os espelhos de repositórios de linguagens configurados para checagem de versões mais recentes (`latest version`).

## Conexões
- [[deptrack-autenticacao-oidc-oauth2-ldap-teams-rbac-permissions]] — Veja também: OWASP Dependency-Track Autenticação e RBAC (`OIDC`, `LDAP`, `API Keys` e *Portfolio Access Control*): governança multi-equipe.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
