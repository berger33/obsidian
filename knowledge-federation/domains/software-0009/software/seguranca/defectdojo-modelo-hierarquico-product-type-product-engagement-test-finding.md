---
id: software.seguranca.tranche02.000162
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-02.md"
fontes: ["https://docs.defectdojo.com/get_started/about/about_defectdojo/", "https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md", "https://github.com/DefectDojo/django-DefectDojo"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# DefectDojo Modelo de Dados Hierárquico: `Product Type` -> `Product` -> `Engagement` -> `Test` -> `Finding` e `Endpoint`

## Em uma frase
Conforme documentado no guia oficial *About DefectDojo* (`docs.defectdojo.com/get_started/about/about_defectdojo/`), toda a organização de ativos, permissões RBAC e contexto de vulnerabilidades segue uma hierarquia de cinco níveis: **`Product Type`** (ex.: Tribo/Unidade de Negócio) -> **`Product`** (Aplicação/Serviço) -> **`Engagement`** (Ciclo CI/CD ou Pentest) -> **`Test`** (Execução de um scanner específico) -> **`Finding`** (Vulnerabilidade individual) associada a **`Endpoints`** (Hosts/URLs).

## Por que importa
Importar relatórios de segurança soltos sem estruturar `Product Type` e `Product` impede gerar métricas executivas por diretoria, aplicar políticas de SLA diferenciadas por criticidade do sistema ou restringir o acesso de cada squad apenas aos seus próprios produtos.

## Como funciona
No DefectDojo, os **`Engagements`** dividem-se em dois tipos: **CI/CD Engagements** (contínuos, projetados para receber uploads automatizados diários da pipeline de integração contínua) e **Interactive Engagements** (com datas de início e fim definidas, projetados para auditorias pontuais, *Bug Bounty* ou Pentests manuais).

## Exemplo
```bash
# Listando os Products cadastrados e seus metadados via REST API v2 do DefectDojo:
curl -sS -H "Authorization: Token ${DOJO_API_TOKEN}" \
  "https://dojo.internal.corp/api/v2/products/?limit=10" | jq '.results[] | {id, name, prod_type}'
```

## Limites e trade-offs
Atribua metadados de criticidade de negócio (`business_criticality`: `very high`, `high`, `medium`, `low`), `platform` e `lifecycle` em cada `Product` para alimentar relatórios executivos e priorização.

## Como verificar
Verifique a hierarquia criada na UI ou via `/api/v2/product_types/`, `/api/v2/products/` e `/api/v2/engagements/`.

## Conexões
- [[defectdojo-arquitetura-owasp-aspm-vulnerability-management-500-parsers]] — Veja também: OWASP DefectDojo: arquitetura da plataforma open-source de ASPM e gestão unificada de vulnerabilidades com 500+ parsers.
- [[defectdojo-api-v2-import-scan-vs-reimport-scan-ciclo-vida-ci-cd]] — Veja também: DefectDojo `import-scan` vs `reimport-scan`: automação de pipelines CI/CD com fechamento automático de vulnerabilidades corrigidas.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
