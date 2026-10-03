---
id: software.seguranca.tranche02.000163
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

# DefectDojo `import-scan` vs `reimport-scan`: automação de pipelines CI/CD com fechamento automático de vulnerabilidades corrigidas

## Em uma frase
A diferença mais importante na automação do DefectDojo via REST API v2 está entre os endpoints **`POST /api/v2/import-scan/`** (que cria sempre um **novo `Test`** dentro do Engagement) e **`POST /api/v2/reimport-scan/`** (que atualiza um **`Test` existente** do mesmo scanner, **fechando automaticamente como `Mitigated`** os `Findings` que deixaram de aparecer no novo relatório e reabrindo os que reapareceram)!

## Por que importa
Se a sua pipeline de CI/CD chamar `import-scan` a cada commit diário em vez de `reimport-scan`, o Engagement acumulará 365 objetos `Test` por ano e as vulnerabilidades já corrigidas pelos desenvolvedores nunca serão marcadas como `Mitigated` automaticamente!

## Como funciona
Passando `auto_create_context=true`, `product_type_name`, `product_name`, `engagement_name`, `scan_type` (ex.: `"SARIF"`, `"Gitleaks Scan"`, `"Nuclei Scan"`, `"Trivy Scan"`), `close_old_findings=true` e `minimum_severity="Low"` para **`/api/v2/reimport-scan/`**, o próprio DefectDojo cria o Produto/Engagement na primeira execução e mantém um estado vivo impecável nas execuções seguintes.

## Exemplo
```bash
# Reimportando um relatório SARIF no DefectDojo via CI/CD com auto-criação de contexto e fechamento de itens corrigidos:
curl -fsS -X POST "https://dojo.internal.corp/api/v2/reimport-scan/" \
  -H "Authorization: Token ${DOJO_API_TOKEN}" \
  -F "auto_create_context=true" \
  -F "product_type_name=Pagamentos" \
  -F "product_name=checkout-api" \
  -F "engagement_name=ci-main-branch" \
  -F "scan_type=SARIF" \
  -F "close_old_findings=true" \
  -F "active=true" \
  -F "verified=false" \
  -F "file=@results.sarif"
```

## Limites e trade-offs
Quando um mesmo scanner roda por serviço/subcomponente dentro do mesmo repositório, passe também os parâmetros **`service`** (ex.: `service=auth-worker`) e `close_old_findings_product_scope=false` para que o reimport de um subserviço não feche os achados de outro subserviço!

## Como verificar
Verifique no retorno JSON do `reimport-scan` os contadores de `findings` criados, mitigados e reativados.

## Conexões
- [[defectdojo-modelo-hierarquico-product-type-product-engagement-test-finding]] — Veja também: DefectDojo Modelo de Dados Hierárquico: `Product Type` -> `Product` -> `Engagement` -> `Test` -> `Finding` e `Endpoint`.
- [[defectdojo-deduplicacao-algoritmos-hash-code-unique-id-from-tool]] — Veja também: DefectDojo Algoritmos de Deduplicação (`HASH_CODE`, `UNIQUE_ID_FROM_TOOL`, `LEGACY`): eliminação de duplicatas intra-scanner e cross-scanner.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
