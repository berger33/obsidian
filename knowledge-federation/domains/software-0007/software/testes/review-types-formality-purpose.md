---
id: software.testes.review-types.000001
tipo: conceito
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-05.md"
revisor: ""
fontes: ["https://astqb.org/3-2-feedback-and-review-process/", "https://istqb.org/wp-content/uploads/sdm-uploads/ISTQB_CTFL_v4.0_Sample-Exam-C-Answers_v1.6.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Review types, Informal review, Walkthrough, Technical review, Inspection]
lote: software-testes-2000-0001
---

# Tipos de revisão e níveis de formalidade

## Em uma frase
Informal review, walkthrough, technical review e inspection variam em objetivo, papéis e formalidade; escolha conforme work product, risco e necessidade.

## Por que importa
Chamar qualquer leitura de “inspeção” pode criar expectativa incorreta sobre documentação e papéis. Uma revisão informal pode dar feedback rápido; uma inspeção formal exige mais preparo e acompanhamento. O tipo deve servir ao objetivo, não ao prestígio do nome.

## Como funciona
O CTFL descreve revisão informal como sem processo definido e sem saída formal obrigatória. Walkthrough é conduzido pelo autor e pode ensinar, construir entendimento ou detectar anomalias. Technical review envolve pessoas tecnicamente qualificadas e costuma ser moderada para discutir problemas e alcançar decisões. Inspection é a forma mais formal, segue o processo genérico completo, tem papéis definidos e busca encontrar o maior número possível de anomalias; também pode coletar métricas para melhorar o SDLC e o próprio processo de inspeção. Nomes e práticas podem ser adaptados pela organização, mas as características relevantes devem ser acordadas.

## Exemplo
Uma equipe pode fazer leitura informal do primeiro rascunho de uma história, walkthrough para explicar fluxo a stakeholders e technical review de uma interface complexa. Uma inspeção estruturada pode ser escolhida para requisito crítico quando se busca o processo completo e uma coleta de métricas que possa apoiar melhorias do SDLC e da inspeção.

## Limites e trade-offs
Mais formal não significa automaticamente melhor: uma inspeção custa tempo e preparação. Uma revisão leve pode ser insuficiente para evidência regulatória ou alto risco. Objetivos podem se sobrepor e a mesma peça pode receber mais de um tipo de revisão.

## Como verificar
Antes de iniciar, declare objetivo, tipo, participantes, preparo, registro e follow-up. Compare se o processo realmente foi realizado; não renomeie uma leitura rápida como inspeção após o fato para sugerir rigor que não houve.

## Conexões
- [[review-process-activities]] — descreve as etapas que podem ser ajustadas conforme formalidade.
- [[static-testing-work-products]] — work products legíveis podem ser alvo de revisão.
- [[test-planning-objetivos-escopo-comunicacao]] — planejamento pode incluir recursos para revisões formais.

## Fontes
- [ASTQB — ISTQB CTFL §3.2: Feedback and Review Process](https://astqb.org/3-2-feedback-and-review-process/) — tipos, formalidade e critérios de seleção; acesso em 2026-10-01.
- [ISTQB — CTFL v4.0 Sample Exam C Answers, version 1.6](https://istqb.org/wp-content/uploads/sdm-uploads/ISTQB_CTFL_v4.0_Sample-Exam-C-Answers_v1.6.pdf) — diferenças de liderança e objetivos entre tipos de revisão; acesso em 2026-10-01.
