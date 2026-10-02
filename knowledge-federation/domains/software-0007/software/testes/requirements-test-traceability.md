---
id: software.testes.traceability.000001
tipo: pratica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-01
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-04.md"
fontes: ["https://astqb.org/1-4-test-activities-testware-and-test-roles/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Requirements traceability, Test traceability, Rastreabilidade de requisitos e testes]
lote: software-testes-2000-0001
---

# Rastreabilidade entre requisitos, testes e resultados

## Em uma frase
Rastreabilidade conecta elementos da base de teste a condições/casos, resultados e defeitos para avaliar cobertura, impacto de mudança e estado do teste.

## Por que importa
Uma lista de testes sem relação com requisitos ou riscos dificulta saber o que está coberto e o que será afetado por uma mudança. Conexões claras ajudam a explicar progresso, encontrar áreas sem evidência e selecionar testes de regressão com base no impacto real.

## Como funciona
O syllabus ISTQB recomenda manter ligações entre elementos da base de teste (como requisitos e riscos), testware relacionado (condições, casos), resultados e defeitos. Test cases ligados a requisitos ajudam a avaliar cobertura; resultados ligados a riscos ajudam a avaliar risco residual. Rastreabilidade pode também apoiar auditorias, análise de impacto e comunicação de progresso/conclusão. O modelo pode ser uma matriz, links em ferramentas ou metadados nos testes; o importante é que seja atualizável e tenha granularidade útil.

## Exemplo
Para uma exigência “uma solicitação repetida com a mesma chave não cria nova cobrança”, ligue requisito a casos de repetição, resultados de execução e qualquer defeito encontrado. Se a regra mudar, use a relação para identificar casos a revisar; um vínculo com risco de duplicação pode orientar regressões relacionadas. Um requisito sem caso associado sinaliza uma pergunta de cobertura, não prova automaticamente que haja defeito.

## Limites e trade-offs
Links desatualizados geram confiança enganosa; uma matriz enorme sem manutenção vira burocracia. Rastreabilidade demonstra relações entre artefatos, não adequação do requisito, qualidade do oracle ou eficácia da execução. Evite inferir “coberto” apenas porque existe um caso vinculado: verifique resultado e critério de cobertura.

## Como verificar
Defina identificadores estáveis e relações necessárias para o contexto. Gere relatórios de requisitos sem casos, casos sem base, resultados sem requisito e defeitos sem execução relacionada. Após mudanças, revise os vínculos e registre qual evidência sustenta a decisão de cobertura e risco residual.

## Conexões
- [[test-planning-objetivos-escopo-comunicacao]] — o plano define base e objetivos que orientarão a rastreabilidade.
- [[test-case-prioritization-dependencies]] — requisitos e riscos ligados aos casos podem influenciar a ordem.
- [[test-progress-metrics-relatorios-conclusao]] — cobertura rastreável informa relatórios de progresso.

## Fontes
- [ASTQB — ISTQB CTFL §1.4: Test Activities, Testware and Test Roles](https://astqb.org/1-4-test-activities-testware-and-test-roles/) — relações entre base de teste, testware, resultados e defeitos; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 1.4.4, avaliação de cobertura, impacto de mudança e risco residual; acesso em 2026-10-01.
