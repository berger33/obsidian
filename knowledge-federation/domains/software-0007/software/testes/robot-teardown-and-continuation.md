---
id: software.testes.tranche17.001081
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://github.com/robotframework/robotframework"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: continuar após falhas quando faz sentido

## Em uma frase
Palavras-chave de verificação e o comportamento de continuidade permitem executar todas as verificações de um caso mesmo quando uma delas falha.

## Por que importa
Falhar na primeira verificação esconde a extensão de um problema, e em relatórios de conformidade convém reunir todas as divergências de uma vez.

## Como funciona
Agrupe verificações independentes em uma palavra-chave que continua após falha, mantendo os passos dependentes encadeados normalmente.

## Exemplo
Uma auditoria de página pode verificar título, cabeçalhos e rodapé na mesma execução, reportando todas as divergências encontradas.

## Limites e trade-offs
Continuar após falha em passos dependentes produz erros em cascata que confundem o diagnóstico, então a técnica vale apenas para verificações independentes.

## Como verificar
Introduza duas divergências independentes e confirme que o relatório registra ambas, em vez de interromper na primeira.

## Conexões
- [[robot-tags-and-selection]] — Veja também: Robot Framework: etiquetar e selecionar testes.
- [[robot-variables-and-scopes]] — Veja também: Robot Framework: entender escopos de variáveis.

## Fontes
- [Robot Framework — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — sintaxe de casos, palavras-chave, variáveis, modelos, etiquetas e relatórios; consultado em 2026-10-03.
- [Robot Framework — repositório oficial](https://github.com/robotframework/robotframework) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
