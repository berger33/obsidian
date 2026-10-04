---
id: software.seguranca.tranche01.000036
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

# OWASP Dependency-Track Portfolio Impact Analysis: resposta imediata a incidentes (*"O que está afetado, e onde?"*) via PURL e CPE

## Em uma frase
Uma das capacidades mais críticas do Dependency-Track destacadas no README oficial é responder em segundos à pergunta **"What is affected, and where?"** em todo o portfólio da organização quando uma nova vulnerabilidade zero-day (como Log4Shell ou XZ Utils) ou ataque de supply chain em um pacote npm/PyPI é anunciado.

## Por que importa
Sem um inventário centralizado de SBOMs indexado por **Package URL (`pkg:maven/...`, `pkg:npm/...`)**, responder à diretoria quais dos 400 microsserviços da empresa usam `log4j-core` entre `2.0-beta9` e `2.14.1` exige rodar builds ou greps manuais em centenas de repositórios.

## Como funciona
No Dependency-Track, a busca por componente (por nome, grupo, versão, **PURL**, **CPE** ou hash criptográfico SHA-256/SHA-512) ou por ID de vulnerabilidade retorna instantaneamente todos os projetos e versões ativos do portfólio que contêm aquela dependência direta ou transitiva.

## Exemplo
```bash
# Buscando todos os projetos do portfólio afetados por uma CVE específica via API REST:
curl -fsS -H "X-Api-Key: ${DTRACK_API_KEY}" \
  "https://dtrack-api.internal.corp/api/v1/vulnerability/source/NVD/vuln/CVE-2021-44228/projects" \
  | jq '.[] | {name: .name, version: .version, active: .active}'
```

## Limites e trade-offs
Marque versões antigas já descomissionadas de produção com `active: false` no Dependency-Track para que a busca de impacto de incidentes filtre apenas versões que estão efetivamente rodando em produção.

## Como verificar
Teste a busca por coordenada Package URL na seção *Component Search* da interface ou via `/api/v1/component/identity`.

## Conexões
- [[deptrack-policy-engine-seguranca-licencas-risco-operacional]] — Veja também: OWASP Dependency-Track Policy Engine: políticas globais e por projeto para risco de segurança, conformidade de licenças e risco operacional.
- [[deptrack-monitoramento-servicos-externos-apis-trust-boundary-cyclonedx]] — Veja também: OWASP Dependency-Track Inventário de Serviços e APIs: rastreamento de provedores externos, classificação de dados e *Trust Boundaries*.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
