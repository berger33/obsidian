---
id: software.testes.activities.000001
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
fontes: ["https://astqb.org/1-4-test-activities-testware-and-test-roles/", "https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Fundamental test process, Test activities, Atividades do processo de teste]
lote: software-testes-2000-0001
---

# Atividades do processo de teste

## Em uma frase
Testar envolve mais do que executar casos: o processo inclui planejar, acompanhar, analisar, desenhar, preparar, executar e concluir atividades de teste.

## Por que importa
Se o plano aloca tempo apenas para rodar scripts, faltará espaço para entender requisitos, elaborar casos, preparar dados e ambiente, analisar discrepâncias e registrar resultados. A enumeração das atividades ajuda a localizar trabalho omitido e a relacionar cada atividade a testware produzido.

## Como funciona
O CTFL apresenta grupos como planejamento e controle, análise, desenho, implementação, execução e conclusão. Eles podem seguir uma ordem lógica, mas são frequentemente iterativos ou paralelos, e precisam ser adaptados ao sistema e projeto. Análise identifica condições testáveis; desenho detalha casos, dados e ambiente; implementação prepara procedimentos, scripts e suítes; execução compara resultados reais e esperados; conclusão arquiva itens úteis e comunica lições/resultados.

## Exemplo
Em uma iteração, testers podem começar a analisar critérios enquanto uma história é refinada, elaborar casos antes de o código estar completo, atualizar dados após mudança de contrato, executar em CI e concluir o ciclo reportando risco restante. O trabalho não precisa esperar uma “fase de teste” isolada depois de todo desenvolvimento.

## Limites e trade-offs
A lista não deve virar uma sequência burocrática fixa. Em fluxos pequenos, tarefas podem ser combinadas; em ambientes regulados, algumas evidências ou aprovações podem ser separadas. O objetivo é cobrir o trabalho necessário, não preservar nomes de artefato sem utilidade.

## Como verificar
Para cada atividade, identifique entrada, decisão e saída útil: objetivo/plano, condições/casos, testware pronto, logs/resultados e relatório/lições. Compare o processo planejado à realidade do SDLC e ajuste quando tarefas são paralelas ou repetidas.

## Conexões
- [[test-planning-objetivos-escopo-comunicacao]] — organiza objetivos e recursos.
- [[test-progress-metrics-relatorios-conclusao]] — monitora execução e reporta conclusão.
- [[test-environment-configuration-management]] — mantém a identidade de testware ao longo das atividades.

## Fontes
- [ASTQB — ISTQB CTFL §1.4: Test Activities, Testware and Test Roles](https://astqb.org/1-4-test-activities-testware-and-test-roles/) — grupos de atividade, iteração/paralelismo e tailoring; acesso em 2026-10-01.
- [ISTQB CTFL Syllabus v4.0.1](https://astqb.org/assets/documents/ISTQB_CTFL_Syllabus_v4.0.1.pdf) — seção 1.4.1 e work products por atividade; acesso em 2026-10-01.
