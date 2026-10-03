---
id: software.seguranca.tranche01.000031
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

# OWASP Dependency-Track: arquitetura da plataforma contínua de análise de risco de cadeia de suprimentos baseada em SBOM `CycloneDX`

## Em uma frase
O **OWASP Dependency-Track** (projeto *OWASP Flagship* licenciado sob Apache 2.0) é uma plataforma inteligente de **Component Analysis** com design *API-first* que monitora continuamente o uso de componentes (bibliotecas, frameworks, sistemas operacionais, containers, firmware, hardware e serviços) em todo o portfólio de aplicações da organização por meio da ingestão de **Software Bill of Materials (SBOM) CycloneDX**.

## Por que importa
Rodar um scanner SCA pontual apenas durante o job de CI deixa uma lacuna crítica: se uma nova CVE zero-day for publicada três semanas após o último deploy de um serviço estável, nenhuma pipeline de build está rodando para avisar que aquele container em produção ficou vulnerável hoje.

## Como funciona
No Dependency-Track, cada pipeline de CI/CD gera e envia o **SBOM CycloneDX** da versão lançada para a API do Dependency-Track; a partir daí, a plataforma reavalia continuamente todos os projetos cadastrados contra múltiplas fontes de inteligência de vulnerabilidades (NVD, GitHub Advisories, OSV, Sonatype OSS Index, Snyk, Trivy, VulnDB) e dispara alertas assim que uma nova CVE afeta qualquer ativo em produção.

## Exemplo
```bash
# Subindo a stack oficial do OWASP Dependency-Track (API Server + Frontend) via Docker Compose:
curl -LO https://dependencytrack.org/docker-compose.yml
docker compose up -d
```

## Limites e trade-offs
Conforme documentado no README oficial, em ambientes de produção utilize as distribuições desacopladas recomendadas (**`dependencytrack/apiserver`** + **`dependencytrack/frontend`** SPA) em vez da variante legada `bundled`, alocando pelo menos 8 GB de RAM para o API Server.

## Como verificar
Após o primeiro boot (`initial-startup`), monitore `dependency-track.log` até a conclusão da sincronização inicial dos espelhos NVD/OSV (10 a 30 minutos) e altere imediatamente a senha inicial `admin`/`admin`.

## Conexões
- [[deptrack-ingestao-sbom-api-rest-bom-upload-ci-cd-auto-create]] — Veja também: OWASP Dependency-Track Ingestão de SBOM em CI/CD: endpoint `/api/v1/bom`, autenticação `X-Api-Key` e criação automática de projetos.

## Fontes
- [OWASP Dependency-Track GitHub — README.md (Continuous SBOM Analysis Platform, CycloneDX, VEX, EPSS, Policy Engine & Ecosystem Integrations)](https://raw.githubusercontent.com/DependencyTrack/dependency-track/master/README.md) — README oficial do DependencyTrack/dependency-track documentando arquitetura API-first, consumo de SBOM CycloneDX, fontes de inteligência, EPSS e VEX; consultado em 2026-10-03.
- [OWASP Dependency-Track Official Documentation — Initial Startup & Operational Configuration (Admin Setup, Feeds, Mirroring & Portfolio Management)](https://docs.dependencytrack.org/getting-started/initial-startup/) — Documentação oficial de inicialização e operação do Dependency-Track cobrindo provisionamento, sincronização de bases NVD/OSV/EPSS e controle de acesso; consultado em 2026-10-03.
- [OWASP Dependency-Track — Official GitHub Repository](https://github.com/DependencyTrack/dependency-track) — Repositório oficial Apache-2.0 do OWASP Dependency-Track; consultado em 2026-10-03.
