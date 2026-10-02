---
id: software.testes.stakeholder-feedback.000001
tipo: pratica
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
fontes: ["https://astqb.org/3-2-feedback-and-review-process/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Early stakeholder feedback, Frequent feedback, Feedback antecipado]
lote: software-testes-2000-0001
---

# Feedback frequente de stakeholders durante o SDLC

## Em uma frase
Feedback antecipado e frequente de stakeholders ajuda a detectar mal-entendidos de requisitos enquanto mudanças ainda podem ser ajustadas com menos retrabalho.

## Por que importa
Se usuários e representantes de negócio só avaliam o produto no fim, a equipe pode descobrir tarde que construiu a funcionalidade errada ou interpretou critérios de outra forma. Feedback torna visíveis expectativas atuais e permite concentrar trabalho em valor e riscos relevantes.

## Como funciona
O CTFL recomenda envolver stakeholders ao longo do ciclo de vida e usar feedback para comunicar potenciais problemas de qualidade cedo. Isso pode ocorrer em revisão de requisitos, demonstração de incremento, refinamento de histórias ou avaliação de protótipo. O feedback deve ser registrado contra comportamento ou critério; a equipe então confirma a interpretação e atualiza itens afetados.

## Exemplo
Antes de implementar “expirar sessão após inatividade”, testers e product owner discutem qual ação conta como atividade e como avisar o usuário. Uma demonstração com protótipo pode revelar que a equipe interpretou “inatividade” como ausência de mouse, enquanto o requisito pretendia considerar qualquer solicitação autenticada.

## Limites e trade-offs
Feedback não substitui critérios verificáveis, análise técnica ou usuários representativos. Muitos comentários contraditórios exigem priorização e decisão explícita. Consultas tardias ainda podem ser necessárias, mas não devem ser a única forma de validar expectativas.

## Como verificar
Convide stakeholders apropriados nos pontos de decisão, registre perguntas abertas, decisão e impacto em requisitos/casos, e confirme alterações após feedback. Avalie se a mudança reduziu ambiguidade e risco sem ampliar escopo inadvertidamente.

## Conexões
- [[test-entry-exit-criteria]] — critérios compartilhados ajudam a decidir quando um incremento está concluído.
- [[test-oracles-resultados-esperados]] — stakeholders podem ajudar a definir resultados e oracles.
- [[test-planning-objetivos-escopo-comunicacao]] — feedback pode alterar objetivo e abordagem do plano.

## Fontes
- [ASTQB — ISTQB CTFL §3.2: Feedback and Review Process](https://astqb.org/3-2-feedback-and-review-process/) — benefícios do feedback antecipado e frequente; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 3.2.1 e relação com entendimento de requisitos; acesso em 2026-10-01.
