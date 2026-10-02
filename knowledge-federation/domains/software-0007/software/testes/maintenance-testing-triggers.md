---
id: software.testes.maintenance-triggers.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: estavel
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-06.md"
revisor: ""
fontes: ["https://astqb.org/2-3-maintenance-testing/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Maintenance testing triggers", "Gatilhos para teste de manutenção"]
lote: software-testes-2000-0001
---

# Gatilhos para teste de manutenção

## Em uma frase
Teste de manutenção pode ser disparado por modificações do produto, mudanças no ambiente operacional ou retirada planejada do sistema.

## Por que importa
Equipes podem concentrar teste apenas em novas funcionalidades e ignorar migração de plataforma, conversão de dados ou arquivamento. Esses eventos alteram premissas operacionais mesmo quando a lógica de negócio muda pouco.

## Como funciona
O CTFL agrupa gatilhos em três categorias: modificações como melhorias planejadas, correções e hotfixes; atualizações ou migrações do ambiente de operação; e aposentadoria do sistema. Cada gatilho determina perguntas diferentes. Uma correção exige confirmação e regressão; uma migração inclui compatibilidade ambiental e conversão; a retirada pode exigir demonstrar arquivamento e recuperação.

## Exemplo
Uma aplicação legada pode receber hotfix urgente para falha em autenticação, ser migrada para uma nova plataforma no trimestre seguinte e, anos depois, ser retirada com retenção de registros. São três atividades de manutenção com objetivos de teste distintos.

## Limites e trade-offs
Nem todo gatilho exige a mesma bateria ou execução completa. A criticidade, os riscos e as obrigações de retenção determinam a profundidade adequada.

## Como verificar
Mantenha um inventário de mudanças e marcos ambientais; para cada evento, declare sistema afetado, risco, dados e critérios de aceitação.

## Conexões
- [[maintenance-testing-change-scope]] — dimensiona o escopo da mudança.
- [[system-integration-testing-external-systems]] — migração pode alterar interfaces externas.

## Fontes
- [ASTQB — CTFL §2.3, Maintenance Testing](https://astqb.org/2-3-maintenance-testing/) — categorias de gatilhos de manutenção; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §2.3; acesso em 2026-10-01.
