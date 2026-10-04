---
id: software.testes.accessibility.000001
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
fontes: ["https://www.w3.org/TR/WCAG22/", "https://www.w3.org/WAI/test-evaluate/tools/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Accessibility testing, Web accessibility testing, Teste de acessibilidade web, WCAG testing]
lote: software-testes-2000-0001
---

# Teste de acessibilidade: automação e avaliação humana

## Em uma frase
Teste de acessibilidade combina ferramentas automatizadas com avaliação manual de fluxos e tecnologias assistivas para encontrar barreiras que métricas automáticas não conseguem julgar por completo.

## Por que importa
WCAG 2.2 define critérios testáveis de acessibilidade web e cobre diversas necessidades, mas nem toda propriedade depende apenas do código visível ao analisador. Uma ferramenta pode identificar ausência de nome acessível ou contraste em casos calculáveis; não consegue decidir sozinha se um texto alternativo comunica a intenção da imagem ou se um fluxo faz sentido para pessoas usuárias.

## Como funciona
A recomendação W3C WCAG 2.2 organiza critérios de sucesso independentes de tecnologia. A WAI explica que ferramentas podem economizar tempo e evitar barreiras, mas alguns checks exigem intervenção manual e resultados podem ser imprecisos. Uma estratégia combina varredura automatizada em páginas e componentes com navegação por teclado, revisão de foco, zoom, leitura com tecnologia assistiva e testes de tarefas representativas. Pessoas com deficiência podem revelar impactos que uma inspeção exclusivamente técnica não mostra.

## Exemplo
Num formulário de cadastro, um scanner pode sinalizar campos sem rótulo programático. Uma avaliação manual pode investigar se a mensagem de erro é anunciada, se o foco vai para o problema, se instruções são compreensíveis e se todo o fluxo pode ser concluído apenas pelo teclado. Cada evidência deve ser associada ao critério aplicável e ao contexto da página.

## Limites e trade-offs
Passar num scanner não demonstra conformidade integral, e um relatório pode conter falsos positivos ou falsos negativos. A cobertura automática depende das regras implementadas e do conteúdo avaliado. Testar algumas páginas não comprova que todas as combinações dinâmicas, estados, documentos e fluxos sejam acessíveis.

## Como verificar
Declare versão WCAG e escopo de páginas e jornadas; automatize verificações repetíveis em CI para evitar regressões. Complete com revisão manual baseada em tarefas e critérios, registre evidências e teste novamente após correções. Não apresente uma pontuação de ferramenta como declaração de conformidade.

## Conexões
- [[exploratory-testing-aprendizado-design-execucao]] — sessões podem investigar jornadas complexas e barreiras contextuais.
- [[snapshot-testing-jest-revisao]] — snapshots podem capturar alterações estruturais, mas não avaliam por si sós experiência acessível.
- [[risk-based-testing-priorizacao-risco]] — ajuda a escolher páginas e fluxos de maior impacto para revisão inicial.

## Fontes
- [W3C Recommendation — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — critérios de sucesso e escopo normativo; acesso em 2026-10-01.
- [W3C WAI — Evaluation Tools Overview](https://www.w3.org/WAI/test-evaluate/tools/) — capacidades, limitações e necessidade de intervenção manual; acesso em 2026-10-01.
