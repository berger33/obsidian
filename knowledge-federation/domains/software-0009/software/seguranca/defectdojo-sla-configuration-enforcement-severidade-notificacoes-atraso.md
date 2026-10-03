---
id: software.seguranca.tranche02.000166
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

# DefectDojo SLA Engine (`SLA Configuration`): prazos de remediação por severidade (`Critical`, `High`, `Medium`, `Low`) e alertas de violação

## Em uma frase
O DefectDojo possui um motor nativo de **SLA (*Service Level Agreement*)** onde você cria perfis de `SLA Configuration` (por exemplo: `Critical = 7 dias`, `High = 30 dias`, `Medium = 90 dias`, `Low = 180 dias`) e os associa a cada `Product`, calculando automaticamente os dias restantes (`sla_days_remaining`) e a data limite (`sla_expiration_date`) de cada `Finding`.

## Por que importa
Uma política escrita em PDF dizendo que vulnerabilidades críticas devem ser corrigidas em 7 dias não tem efeito prático se o sistema de gestão não calcular a contagem regressiva nem alertar os responsáveis antes do vencimento.

## Como funciona
Você pode ter múltiplas políticas de SLA no DefectDojo — por exemplo, um perfil **"PCI-DSS / Tier-0 Externo"** mais rigoroso (`Critical = 3 dias`) para serviços de pagamento e um perfil **"Ferramentas Internas Tier-3"** para sistemas administrativos — com opção de pausar ou manter a contagem e disparar notificações automáticas de violação de SLA.

## Exemplo
```bash
# Listando todos os Findings ativos que já violaram o prazo de SLA no DefectDojo:
curl -sS -H "Authorization: Token ${DOJO_API_TOKEN}" \
  "https://dojo.internal.corp/api/v2/findings/?active=true&outside_of_sla=1" \
  | jq '.results[] | {id, title, severity, sla_days_remaining}'
```

## Limites e trade-offs
Ative o envio de notificações de `sla_breach` (via Slack, Microsoft Teams, e-mail ou webhook) para alertar o Tech Lead do Produto alguns dias antes do vencimento do SLA.

## Como verificar
Verifique as políticas cadastradas em `/api/v2/sla_configurations/` e filtre achados por `outside_of_sla=1`.

## Conexões
- [[defectdojo-triagem-findings-verified-false-positive-out-of-scope-risk-acceptance]] — Veja também: DefectDojo Fluxo de Triagem e `Risk Acceptance`: estados `Active`, `Verified`, `False Positive`, `Out of Scope` e Aceite Formal de Risco.
- [[defectdojo-integracao-bidirecional-jira-sincronizacao-status-comentarios]] — Veja também: DefectDojo Integração Bidirecional com Jira: criação automática de Issues, sincronização de comentários e fechamento por resolução.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
