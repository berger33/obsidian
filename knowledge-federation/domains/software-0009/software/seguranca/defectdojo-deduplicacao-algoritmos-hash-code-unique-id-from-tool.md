---
id: software.seguranca.tranche02.000164
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

# DefectDojo Algoritmos de Deduplicação (`HASH_CODE`, `UNIQUE_ID_FROM_TOOL`, `LEGACY`): eliminação de duplicatas intra-scanner e cross-scanner

## Em uma frase
Conforme destacado na documentação oficial do DefectDojo, o motor de **Deduplicação** identifica quando dois `Findings` representam a mesma vulnerabilidade subjacente — seja em execuções diferentes da mesma ferramenta ou entre ferramentas distintas (*cross-tool deduplication*) — utilizando algoritmos configuráveis por parser em `settings.dist.py`: **`DEDUPE_ALGO_UNIQUE_ID_FROM_TOOL`**, **`DEDUPE_ALGO_HASH_CODE`**, **`DEDUPE_ALGO_UNIQUE_ID_FROM_TOOL_OR_HASH_CODE`** e **`DEDUPE_ALGO_LEGACY`**.

## Por que importa
Se dois scanners SAST diferentes (por exemplo Semgrep e SonarQube, ou dois jobs distintos) reportarem o mesmo `CWE-89` na linha `42` de `src/db/user.go`, abrir dois tickets duplicados no Jira gera retrabalho para a engenharia.

## Como funciona
No algoritmo `HASH_CODE`, o DefectDojo calcula um hash SHA-256 determinístico a partir dos campos configurados em `HASHCODE_FIELDS_PER_SCANNER` (tipicamente `title`, `cwe`, `line`, `file_path`, `vuln_id_from_tool` ou `endpoints`). Quando um novo achado produz o mesmo `hash_code` dentro do mesmo `Product`, ele é marcado automaticamente como `duplicate: true` apontando para o `duplicate_finding` original!

## Exemplo
```bash
# Consultando via API apenas os Findings ativos e não-duplicados de um produto:
curl -sS -H "Authorization: Token ${DOJO_API_TOKEN}" \
  "https://dojo.internal.corp/api/v2/findings/?test__engagement__product=1&active=true&duplicate=false" \
  | jq '{count: .count}'
```

## Limites e trade-offs
Sempre que alterar a configuração de campos de hash (`HASHCODE_FIELDS_PER_SCANNER`), execute o comando de gerenciamento `dedupe.sh` / `python manage.py dedupe` para recalcular os `hash_code` históricos.

## Como verificar
Filtre na UI ou API por `duplicate=true` para auditar os achados agrupados pelo motor de deduplicação.

## Conexões
- [[defectdojo-api-v2-import-scan-vs-reimport-scan-ciclo-vida-ci-cd]] — Veja também: DefectDojo `import-scan` vs `reimport-scan`: automação de pipelines CI/CD com fechamento automático de vulnerabilidades corrigidas.
- [[defectdojo-triagem-findings-verified-false-positive-out-of-scope-risk-acceptance]] — Veja também: DefectDojo Fluxo de Triagem e `Risk Acceptance`: estados `Active`, `Verified`, `False Positive`, `Out of Scope` e Aceite Formal de Risco.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
