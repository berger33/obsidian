---
id: software.seguranca.tranche01.000032
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

# OWASP Dependency-Track Ingestão de SBOM em CI/CD: endpoint `/api/v1/bom`, autenticação `X-Api-Key` e criação automática de projetos

## Em uma frase
A integração do Dependency-Track com pipelines de CI/CD (GitHub Actions, GitLab CI, Jenkins, Tekton) ocorre enviando o manifesto CycloneDX (`bom.json` ou `bom.xml`) via `PUT` ou `POST` multipart para o endpoint **`/api/v1/bom`** autenticado pelo cabeçalho **`X-Api-Key`** de uma equipe com as permissões `BOM_UPLOAD` e `PROJECT_CREATION_UPLOAD`.

## Por que importa
Cadastrar manualmente centenas de microsserviços e suas versões na interface web antes de permitir o upload de SBOMs inviabilizaria a adoção em frotas cloud-native.

## Como funciona
Ao passar `autoCreate=true`, `projectName` e `projectVersion` na chamada `POST /api/v1/bom`, o Dependency-Track cria o projeto/versão automaticamente caso ainda não exista, processa o grafo de dependências de forma assíncrona e retorna um `token` UUID para consultar o término do processamento (`/api/v1/bom/token/{uuid}`).

## Exemplo
```bash
# Enviando um SBOM CycloneDX gerado no CI para o Dependency-Track com autoCreate=true:
curl -fsS -X POST "https://dtrack-api.internal.corp/api/v1/bom" \
  -H "Content-Type: multipart/form-data" \
  -H "X-Api-Key: ${DTRACK_API_KEY}" \
  -F "autoCreate=true" \
  -F "projectName=payments-service" \
  -F "projectVersion=2.4.0" \
  -F "bom=@sbom.cdx.json"
```

## Limites e trade-offs
Consulte `GET /api/v1/bom/token/{uuid}` em loop curto na pipeline se você precisar aguardar o fim da análise (`"processing": false`) antes de consultar as violações de política para decidir o quality gate.

## Como verificar
Verifique na UI ou via `GET /api/v1/project/lookup?name=payments-service&version=2.4.0` os componentes importados.

## Conexões
- [[deptrack-arquitetura-owasp-dependency-track-sbom-cyclonedx-api-first]] — Veja também: OWASP Dependency-Track: arquitetura da plataforma contínua de análise de risco de cadeia de suprimentos baseada em SBOM `CycloneDX`.
- [[deptrack-vex-vulnerability-exploitability-exchange-cyclonedx-triagem]] — Veja também: OWASP Dependency-Track e `CycloneDX VEX`: consumo e exportação de *Vulnerability Exploitability Exchange* para triagem auditável.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
