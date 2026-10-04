---
id: software.seguranca.tranche02.000165
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

# DefectDojo Fluxo de Triagem e `Risk Acceptance`: estados `Active`, `Verified`, `False Positive`, `Out of Scope` e Aceite Formal de Risco

## Em uma frase
O DefectDojo modela o ciclo completo de triagem de uma vulnerabilidade por meio de flags booleanas ortogonais em cada `Finding` (**`active`**, **`verified`**, **`false_p`**, **`out_of_scope`**, **`risk_accepted`**, **`under_review`**, **`is_mitigated`**) e do objeto formal de **Risk Acceptance (Aceite de Risco)** com data de expiração, justificativa, recomendação e anexo de evidência.

## Por que importa
Em auditorias PCI-DSS, ISO 27001 e SOC 2, simplesmente deletar ou fechar uma vulnerabilidade que a empresa decidiu não corrigir agora é uma não-conformidade grave; é obrigatório manter um registro formal assinado de *Risk Acceptance* com data de vencimento.

## Como funciona
Quando uma vulnerabilidade é marcada com `false_p=true` (Falso Positivo) no DefectDojo, o motor de `reimport-scan` lembra dessa decisão: nas próximas execuções do scanner na pipeline, aquela mesma vulnerabilidade **permanece silenciada como Falso Positivo** sem voltar a abrir alertas!

## Exemplo
```bash
# Marcando um Finding como verificado pela equipe de AppSec via PATCH na API v2:
curl -fsS -X PATCH "https://dojo.internal.corp/api/v2/findings/1042/" \
  -H "Authorization: Token ${DOJO_API_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"verified": true, "notes": [{"entry": "Confirmado em staging; encaminhado para correção no sprint 42."}]}'
```

## Limites e trade-offs
Habilite a configuração de expiração de *Risk Acceptance* para que o DefectDojo reative o alerta e emita notificação automaticamente quando o prazo do aceite de risco vencer.

## Como verificar
Consulte `/api/v2/risk_acceptance/` para listar todos os aceites de risco ativos e suas datas de expiração (`expiration_date`).

## Conexões
- [[defectdojo-deduplicacao-algoritmos-hash-code-unique-id-from-tool]] — Veja também: DefectDojo Algoritmos de Deduplicação (`HASH_CODE`, `UNIQUE_ID_FROM_TOOL`, `LEGACY`): eliminação de duplicatas intra-scanner e cross-scanner.
- [[defectdojo-sla-configuration-enforcement-severidade-notificacoes-atraso]] — Veja também: DefectDojo SLA Engine (`SLA Configuration`): prazos de remediação por severidade (`Critical`, `High`, `Medium`, `Low`) e alertas de violação.

## Fontes
- [OWASP DefectDojo Official Documentation — About DefectDojo (Data Hierarchy, 500+ Parsers, Deduplication Algorithms, SLA Engine & Jira Integration)](https://docs.defectdojo.com/get_started/about/about_defectdojo/) — Documentação oficial About DefectDojo explicando o modelo hierárquico de dados, ingestão via import-scan/reimport-scan, algoritmos de deduplicação, SLAs e integrações DevSecOps; consultado em 2026-10-03.
- [OWASP DefectDojo GitHub — README.md (Open-Source ASPM & Vulnerability Management Platform, Docker Compose Stack & OpenAPI v3)](https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/master/README.md) — README oficial do DefectDojo/django-DefectDojo detalhando implantação via Docker Compose, arquitetura de containers e recursos principais da plataforma; consultado em 2026-10-03.
- [OWASP DefectDojo — Official GitHub Repository](https://github.com/DefectDojo/django-DefectDojo) — Repositório oficial BSD-3-Clause do OWASP DefectDojo; consultado em 2026-10-03.
