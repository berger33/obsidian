---
id: software.seguranca.tranche02.000168
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

# DefectDojo Arquitetura de Produção: papéis dos componentes `nginx`, `uwsgi` (Django), `celeryworker`, `celerybeat`, `postgres` e `redis`/`valkey`

## Em uma frase
Conforme documentado no guia de arquitetura oficial do DefectDojo (`docs.defectdojo.com/get_started/open_source/architecture/`), uma implantação de produção é composta por seis serviços coordenados: **`nginx`** (proxy reverso e arquivos estáticos), **`uwsgi`** (servidor de aplicação Python/Django da UI e API), **`celeryworker`** (processamento assíncrono em background), **`celerybeat`** (agendador de tarefas periódicas), **`postgres`** (banco relacional) e **`redis` / `valkey`** (broker de mensagens do Celery).

## Por que importa
Quando uma pipeline faz upload de um relatório SARIF ou CycloneDX grande com 5.000 itens, o cálculo de deduplicação, criação de endpoints, alertas de SLA e sincronização com o Jira são enfileirados em tarefas assíncronas do **Celery**; se o `celeryworker` estiver subdimensionado ou parado, os relatórios são importados mas a deduplicação e o Jira ficam travados na fila!

## Como funciona
Para ambientes de alto volume de pipelines CI/CD, escale horizontalmente o número de réplicas/concorrência do **`celeryworker`** e monitore o tamanho da fila no Redis/Valkey.

## Exemplo
```bash
# Verificando a saúde de todos os containers da stack do DefectDojo e inspecionando a fila do Celery Worker:
docker compose ps
docker compose logs --tail=50 celeryworker celerybeat
```

## Limites e trade-offs
Nunca exponha o container `uwsgi` diretamente sem o `nginx` (ou Ingress Controller) na frente, e configure variáveis `DD_SECRET_KEY`, `DD_CREDENTIAL_AES_256_KEY` e senhas de banco exclusivas antes de subir em produção.

## Como verificar
Verifique nos logs do `celeryworker` que tarefas `dedupe` e `calculate_grade` estão sendo consumidas sem backlog.

## Conexões
- [[defectdojo-integracao-bidirecional-jira-sincronizacao-status-comentarios]] — Veja também: DefectDojo Integração Bidirecional com Jira: criação automática de Issues, sincronização de comentários e fechamento por resolução.
- [[defectdojo-universal-parser-sarif-conectores-customizados-ingestao]] — Veja também: DefectDojo Ingestão Universal: uso nativo de relatórios `SARIF` e criação de parsers customizados para ferramentas internas.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
