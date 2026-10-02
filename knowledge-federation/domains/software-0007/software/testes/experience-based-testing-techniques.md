---
id: software.testes.experience-based.000001
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
fontes: ["https://astqb.org/4-4-experience-based-test-techniques/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: ["Experience-based test techniques", "Técnicas baseadas em experiência complementam especificações"]
lote: software-testes-2000-0001
---

# Técnicas baseadas em experiência complementam especificações

## Em uma frase
Técnicas baseadas em experiência usam conhecimento do produto, do domínio e de defeitos anteriores para orientar a criação e execução de testes.

## Por que importa
Requisitos e modelos nem sempre registram todos os usos inesperados, erros comuns ou áreas frágeis. Experiência ajuda a formular hipóteses e explorar lacunas que técnicas sistemáticas podem não destacar.

## Como funciona
O CTFL Foundation apresenta error guessing, exploratory testing e checklist-based testing. Elas dependem de conhecimento e julgamento, mas podem ser organizadas: registrar suposições, executar testes focados, anotar observações e relacionar findings a condições ou riscos. Podem complementar abordagens black-box e white-box; não substituem critérios explícitos quando estes são necessários.

## Exemplo
Depois de mapear partições válidas de um formulário, uma tester experiente adiciona hipóteses sobre separadores incomuns, cópia e colagem e combinações históricas que causaram falhas.

## Limites e trade-offs
Resultados podem variar entre pessoas e sessões. Experiência insuficiente, listas desatualizadas ou viés de confirmação deixam áreas importantes sem exploração.

## Como verificar
Registre contexto, hipótese, dados e observações para que outro tester consiga compreender o que foi explorado; complemente os achados com casos repetíveis quando houver risco.

## Conexões
- [[exploratory-testing-aprendizado-design-execucao]] — aprofunda testes desenhados durante a exploração.
- [[risk-based-testing-priorizacao-risco]] — usa risco para concentrar atenção.

## Fontes
- [ASTQB — CTFL §4.4, Experience-Based Test Techniques](https://astqb.org/4-4-experience-based-test-techniques/) — técnicas e uso de experiência; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — §4.4; acesso em 2026-10-01.
