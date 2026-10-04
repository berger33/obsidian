---
id: software.seguranca.tranche02.000169
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

# DefectDojo Ingestão Universal: uso nativo de relatórios `SARIF` e criação de parsers customizados para ferramentas internas

## Em uma frase
Além dos mais de 500 parsers dedicados por ferramenta (`Trivy Scan`, `Gitleaks Scan`, `TruffleHog Scan`, `OSV Scan`, `ZAP Scan`, `Nuclei Scan`, `Prowler Scan`, `Semgrep JSON Report`, `CycloneDX`), o DefectDojo suporta nativamente o padrão OASIS **SARIF (`scan_type="SARIF"`)** e formatos genéricos (**`Generic Findings Import`** em JSON ou CSV).

## Por que importa
Quando sua equipe desenvolve um script interno de auditoria de segurança (por exemplo, um verificador customizado de configurações internas), você não precisa escrever um plugin Python novo dentro do código-fonte do DefectDojo para importar seus resultados.

## Como funciona
Basta fazer o seu script emitir o formato JSON simples do **`Generic Findings Import`** (ou **SARIF v2.1.0**), que já suporta todos os campos de título, severidade (`Critical`, `High`, `Medium`, `Low`, `Info`), CWE, CVE, `file_path`, `line`, `description`, `mitigation` e `unique_id_from_tool`!

## Exemplo
```json
{
  "findings": [
    {
      "title": "Bucket interno sem política de retenção de logs de auditoria",
      "severity": "High",
      "cwe": 778,
      "description": "O bucket corp-billing-exports não possui logging de acesso habilitado.",
      "mitigation": "Habilitar server_access_logging no módulo Terraform do bucket.",
      "file_path": "infra/s3.tf",
      "line": 28,
      "unique_id_from_tool": "CORP-SEC-S3-001:corp-billing-exports"
    }
  ]
}
```

## Limites e trade-offs
Preencha sempre o campo `unique_id_from_tool` de forma determinística no seu JSON genérico para que a deduplicação e o `reimport-scan` identifiquem cada ativo com 100% de precisão.

## Como verificar
Importe o JSON acima com `-F "scan_type=Generic Findings Import"` em `/api/v2/reimport-scan/`.

## Conexões
- [[defectdojo-arquitetura-servicos-nginx-uwsgi-celery-beat-worker-postgres-redis]] — Veja também: DefectDojo Arquitetura de Produção: papéis dos componentes `nginx`, `uwsgi` (Django), `celeryworker`, `celerybeat`, `postgres` e `redis`/`valkey`.
- [[defectdojo-rbac-product-members-groups-sso-oidc-saml-governanca]] — Veja também: DefectDojo Governança de Acesso (`RBAC`, `Product Type Members` e `SSO` OIDC/SAML/LDAP): isolamento de visibilidade por equipe.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
