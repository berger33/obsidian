---
id: software.testes.sdlc-models.000001
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
fontes: ["https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Testing in sequential and iterative SDLCs", "Testes em ciclos sequenciais, iterativos e incrementais"]
lote: software-testes-2000-0001
---

# Testes em ciclos sequenciais, iterativos e incrementais

## Em uma frase
Modelos sequenciais e iterativos organizam o trabalho de forma diferente, então a ligação temporal entre desenvolvimento, níveis de teste e feedback também muda.

## Por que importa
Se uma equipe pressupõe que todos os modelos usam fases idênticas, pode atrasar análise e revisão até haver código executável, ou impor artefatos pesados a cada incremento. O objetivo é encaixar controles e evidências no fluxo escolhido.

## Como funciona
Em modelos sequenciais, níveis de teste podem ser organizados de modo que os critérios de saída de um nível componham entradas do seguinte. Em alguns modelos iterativos isso não se aplica: atividades de desenvolvimento podem atravessar vários níveis, e níveis podem sobrepor-se no tempo. Cada iteração que entrega um incremento pode incluir teste estático e dinâmico; entregas frequentes exigem feedback rápido e regressão adequada.

## Exemplo
Num ciclo incremental de um serviço de reservas, revisão de critérios e testes de componente podem começar durante a história; testes de sistema ocorrem quando o incremento está integrado. Num ciclo mais sequencial, uma equipe pode planejar níveis e transições por etapas, ainda revisando rascunhos cedo.

## Limites e trade-offs
Sobreposição não elimina a necessidade de distinguir objetivos. A sequência de atividades depende do modelo concreto, não apenas do rótulo “ágil” ou “waterfall”.

## Como verificar
Mapeie entregas, critérios de entrada/saída e pontos de feedback; procure intervalos em que nenhuma atividade verifica requisitos ou riscos relevantes.

## Conexões
- [[test-levels-overview]] — explica os cinco níveis e seus objetivos.
- [[early-frequent-stakeholder-feedback]] — apoia ciclos de feedback frequente.

## Fontes
- [ASTQB — CTFL §2.1, Testing in the Context of an SDLC](https://astqb.org/2-1-testing-in-the-context-of-a-software-development-lifecycle-sdlc/) — diferenças de temporalidade por SDLC; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §§2.1.1–2.1.2; acesso em 2026-10-01.
