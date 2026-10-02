---
id: software.testes.checklist-testing.000001
tipo: pratica
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
fontes: ["https://astqb.org/4-4-experience-based-test-techniques/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Checklist-based testing", "Checklist-based testing usa condições focadas e revisáveis"]
lote: software-testes-2000-0001
---

# Checklist-based testing usa condições focadas e revisáveis

## Em uma frase
Checklist-based testing deriva, implementa e executa testes para cobrir condições reunidas em uma lista de verificação focada.

## Por que importa
Checklists preservam conhecimento sobre riscos, necessidades de usuário e modos conhecidos de falha, reduzindo omissões em avaliações repetidas sem exigir que cada sessão comece do zero.

## Como funciona
O CTFL permite que a lista venha de experiência, conhecimento sobre o que importa para usuários ou compreensão de como o software falha. O tester transforma itens em condições e testes concretos. A lista precisa ser mantida: alguns itens deixam de fazer sentido após mudanças, enquanto novos defeitos podem revelar lacunas.

## Exemplo
Uma checklist de formulário de cadastro pode lembrar de verificar campos obrigatórios, mensagens de erro, persistência após voltar e suporte a colagem. Cada item deve conduzir a observação específica, não só ser marcado “ok”.

## Limites e trade-offs
O syllabus recomenda não incluir verificações que possam ser automatizadas, condições de entrada/saída ou itens vagos demais. Lista extensa e genérica pode gerar falsa confiança sem testar variações importantes.

## Como verificar
Para cada item, confirme que descreve uma condição testável, tem critério observável e dono de manutenção; revise a lista quando produto e riscos mudam.

## Conexões
- [[test-entry-exit-criteria]] — separa pré-condições de condições de teste.
- [[experience-based-testing-techniques]] — situa checklists entre técnicas baseadas em experiência.

## Fontes
- [ASTQB — CTFL §4.4.3, Checklist-Based Testing](https://astqb.org/4-4-experience-based-test-techniques/) — origem e restrições das checklists; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.4.3; acesso em 2026-10-01.
