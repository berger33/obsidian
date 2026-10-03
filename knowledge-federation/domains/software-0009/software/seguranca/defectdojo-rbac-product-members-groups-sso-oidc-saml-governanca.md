---
id: software.seguranca.tranche02.000170
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
fontes: ["https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md", "https://docs.defectdojo.com/get_started/about/about_defectdojo/", "https://github.com/DefectDojo/django-DefectDojo"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# DefectDojo Governança de Acesso (`RBAC`, `Product Type Members` e `SSO` OIDC/SAML/LDAP): isolamento de visibilidade por equipe

## Em uma frase
O DefectDojo implementa controle de acesso baseado em papéis (**RBAC**) com cinco perfis predefinidos (**`Reader`**, **`Technical User`**, **`Writer`**, **`Maintainer`** e **`Owner`**) que podem ser atribuídos por usuário ou por `Group` tanto no nível de `Product Type` (herdando acesso para todos os produtos daquela diretoria) quanto no nível de um `Product` individual, integrando-se a **OIDC/OAuth2**, **SAML 2.0** e **LDAP**.

## Por que importa
Dar permissão global de `Superuser` ou `Global Owner` para todos os desenvolvedores expõe vulnerabilidades críticas de outros sistemas (como RH ou Financeiro) para pessoas que não trabalham naqueles produtos.

## Como funciona
Ao mapear grupos do seu IdP corporativo (Keycloak, Okta, Microsoft Entra ID, Authelia) para `Dojo_Group` e associar cada grupo como **`Writer` ou `Maintainer`** apenas no seu respectivo `Product Type`, cada squad enxerga e faz triagem exclusivamente das suas próprias aplicações, enquanto a equipe de AppSec central mantém visão global.

## Exemplo
```bash
# Listando os grupos e membros associados aos Product Types via API v2 do DefectDojo:
curl -sS -H "Authorization: Token ${DOJO_API_TOKEN}" \
  "https://dojo.internal.corp/api/v2/product_type_groups/" | jq .
```

## Limites e trade-offs
Para tokens usados em pipelines de CI/CD (`/api/v2/reimport-scan/`), crie um usuário de serviço dedicado com papel restrito apenas ao `Product` ou `Product Type` daquela pipeline, nunca usando o token de um `Superuser` global!

## Como verificar
Autentique com o token do usuário de serviço e verifique que `GET /api/v2/products/` retorna apenas os produtos autorizados.

## Conexões
- [[defectdojo-universal-parser-sarif-conectores-customizados-ingestao]] — Veja também: DefectDojo Ingestão Universal: uso nativo de relatórios `SARIF` e criação de parsers customizados para ferramentas internas.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
