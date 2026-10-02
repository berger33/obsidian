---
id: software.testes.tranche11.000473
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates", "https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: usar Test Template para repetir keyword com dados

## Em uma frase
Um test template transforma as linhas de argumentos de um caso em chamadas repetidas à keyword-template escolhida.

## Por que importa
Robot Framework interpreta arquivos de teste por seções e executa keywords de bibliotecas ou recursos; a legibilidade da suíte depende de escopo de variáveis, setup e teardown bem delimitados. Duplicar casos quase idênticos aumenta manutenção e torna difícil perceber se entradas de fronteira foram cobertas.

## Como funciona
Modele cada caso pelo comportamento observável, mantenha preparações e limpeza no nível apropriado, use tags e templates para organização explícita e prefira keywords de domínio em vez de fluxo condicional espalhado. Declare o template uma vez e forneça exemplos de entrada/resultado com nomes que identifiquem cada variação.

## Exemplo
A mesma keyword valida códigos válidos e inválidos com linhas de argumento, enquanto a assertion continua observando resposta completa.

## Limites e trade-offs
Keywords e bibliotecas externas têm ciclo de vida e estado próprios; um teardown não desfaz efeitos fora do ambiente de teste. O formato de dados não torna automaticamente um teste independente ou determinístico. Linhas do template são iterações dentro do caso configurado, não devem ser confundidas automaticamente com casos independentes no runner.

## Como verificar
Inspecione report.xml e o log para saber como cada linha é apresentada e force uma linha inválida para validar diagnóstico.

## Conexões
- [[robot-tags-selecao-sem-substituir-assertions]] — Veja também: Robot Framework: usar tags para selecionar casos, não para definir seu resultado.
- [[robot-variaveis-escopo-prioridade]] — Veja também: Robot Framework: controlar escopo e precedência de variáveis.

## Fontes
- [Robot Framework 7.5 — Test templates](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#test-templates) — execução orientada a dados por template e linhas de argumentos; consultado em 2026-10-02.
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
