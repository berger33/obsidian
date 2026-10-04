---
id: software.testes.session-based.000001
tipo: tecnica
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001.md"
fontes: ["https://www.satisfice.com/download/session-based-test-management", "https://www.infoq.com/articles/session-based-test-management/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Session-based testing, Session-Based Test Management, SBTM, Teste exploratório baseado em sessões]
lote: software-testes-2000-0001
---

# Session-based testing com charters e debriefs

## Em uma frase
Session-Based Test Management organiza exploração em sessões com missão, evidências e debrief, tornando visível o trabalho sem prescrever cada passo como roteiro fixo.

## Por que importa
Exploração precisa de autonomia para seguir evidências novas, mas uma equipe também precisa entender o que foi investigado, o que foi encontrado e o que falta. Uma sessão com charter e relatório oferece uma unidade de conversa e planejamento, especialmente quando requisitos evoluem ou a cobertura não se resume a executar uma lista pré-escrita.

## Como funciona
O artigo de James e Jonathan Bach apresenta SBTM como gestão orientada à atividade, alternativa a gerir apenas artefatos. Na descrição prática publicada pela InfoQ, a sessão é praticamente ininterrupta, foca uma missão, produz algum tipo de relatório e é debriefada pelo líder, salvo quando este próprio executa a sessão. O relatório pode separar esforço de execução, investigação/relato de bugs e preparação/administração; essas estimativas ajudam a conversar sobre processo, não a medir valor individual.

## Exemplo
Charter: “Explore recuperação de senha com links expirados, repetidos e usados em dispositivos distintos para investigar risco de reuso de token”. Ao final, o relatório registra dados e ambiente, sequências tentadas, defeitos, bloqueios e perguntas. No debrief, equipe e tester decidem se o risco foi coberto, se é preciso nova sessão e quais achados devem virar teste reproduzível.

## Limites e trade-offs
Sessões e métricas não garantem cobertura completa nem defeitos encontrados. Relatórios podem se tornar burocracia se campos não apoiarem decisões; estimativas de tempo são aproximadas e não servem para comparar testadores isoladamente. Uma missão muito ampla perde foco; uma missão estreita demais pode impedir seguir pistas importantes sem registrar desvio.

## Como verificar
Um charter deve identificar foco e pergunta de teste sem antecipar todas as ações. Confirme que o relato permite reconstituir evidências relevantes e que o debrief atualiza riscos e próximos passos. Trate tempo por atividade como informação de fluxo e impedimentos, não como produtividade individual.

## Conexões
- [[exploratory-testing-aprendizado-design-execucao]] — descreve a técnica exploratória que SBTM estrutura.
- [[risk-based-testing-priorizacao-risco]] — charters podem focar riscos priorizados.
- [[test-oracles-resultados-esperados]] — debriefs ajudam a registrar como resultados inesperados foram julgados.

## Fontes
- [James e Jonathan Bach — Session-Based Test Management](https://www.satisfice.com/download/session-based-test-management) — origem e foco em gestão por atividade; acesso em 2026-10-01.
- [InfoQ — A Journey in Test Engineering Leadership: Applying SBTM](https://www.infoq.com/articles/session-based-test-management/) — elementos de sessão, relatório, debrief e categorias de atividade; acesso em 2026-10-01.
