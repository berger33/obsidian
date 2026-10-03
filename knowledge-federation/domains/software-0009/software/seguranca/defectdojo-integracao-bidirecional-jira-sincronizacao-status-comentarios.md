---
id: software.seguranca.tranche02.000167
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

# DefectDojo Integração Bidirecional com Jira: criação automática de Issues, sincronização de comentários e fechamento por resolução

## Em uma frase
A integração nativa do DefectDojo com o **Jira** (Cloud e Data Center) opera de forma **bidirecional**: 1) do DefectDojo para o Jira, criando automaticamente Issues (respeitando limiar mínimo de severidade ou apenas achados `verified=true`), atualizando descrições e **fechando a Issue no Jira quando o `reimport-scan` confirma que a vulnerabilidade foi mitigada**; e 2) do Jira para o DefectDojo (via webhook do Jira), sincronizando comentários e transições de status!

## Por que importa
Se o engenheiro de segurança abre um ticket no Jira manualmente e o desenvolvedor corrige o bug, ninguém lembra de voltar na planilha de segurança para dar baixa — ou vice-versa, o scanner já viu que o código foi corrigido mas o ticket continua aberto no backlog do Jira.

## Como funciona
Vinculando cada `Product` ou `Engagement` ao projeto Jira e `Epic` da própria squad de engenharia, o trabalho de segurança entra diretamente no fluxo normal da sprint do desenvolvedor com o link de volta para o `Finding` no DefectDojo.

## Exemplo
```bash
# Verificando os vínculos de projetos Jira configurados nos produtos do DefectDojo:
curl -sS -H "Authorization: Token ${DOJO_API_TOKEN}" \
  "https://dojo.internal.corp/api/v2/jira_project_configurations/" | jq .
```

## Limites e trade-offs
Para evitar inundar o backlog da engenharia com falsos positivos brutos de scanners não calibrados, configure a integração Jira do produto para empurrar automaticamente apenas `Findings` com `verified=true` ou acima da severidade `High`.

## Como verificar
Confira o webhook do Jira em `/jira/webhook/<secret>` e teste a transição de status entre uma Issue de teste e o Finding correspondente.

## Conexões
- [[defectdojo-sla-configuration-enforcement-severidade-notificacoes-atraso]] — Veja também: DefectDojo SLA Engine (`SLA Configuration`): prazos de remediação por severidade (`Critical`, `High`, `Medium`, `Low`) e alertas de violação.
- [[defectdojo-arquitetura-servicos-nginx-uwsgi-celery-beat-worker-postgres-redis]] — Veja também: DefectDojo Arquitetura de Produção: papéis dos componentes `nginx`, `uwsgi` (Django), `celeryworker`, `celerybeat`, `postgres` e `redis`/`valkey`.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
