---
id: software.testes.tranche11.000475
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
fontes: ["https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html", "https://robotframework.org/robotframework/latest/libraries/BuiltIn.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Robot Framework: distinguir resource file de test library

## Em uma frase
Resource files compartilham user keywords e dados Robot; libraries fornecem keywords implementadas em Python ou outra integração suportada.

## Por que importa
Robot Framework interpreta arquivos de teste por seções e executa keywords de bibliotecas ou recursos; a legibilidade da suíte depende de escopo de variáveis, setup e teardown bem delimitados. Importar um resource como se fosse library ou depender de import implícito cria falhas de descoberta e acoplamento difícil de rastrear.

## Como funciona
Modele cada caso pelo comportamento observável, mantenha preparações e limpeza no nível apropriado, use tags e templates para organização explícita e prefira keywords de domínio em vez de fluxo condicional espalhado. Mantenha keywords de domínio em resources reutilizáveis e importe bibliotecas externas com nome e dependências explícitos.

## Exemplo
Um resource define “Criar Pedido”; uma library fornece keyword de banco com configuração injetada pelo ambiente de teste.

## Limites e trade-offs
Keywords e bibliotecas externas têm ciclo de vida e estado próprios; um teardown não desfaz efeitos fora do ambiente de teste. O formato de dados não torna automaticamente um teste independente ou determinístico. Escopo e lifecycle dependem da library importada; variáveis de resource também podem ser sobrescritas por fontes de maior prioridade.

## Como verificar
Rode descoberta no ambiente limpo do CI e confirme que imports e versões estão declarados no repositório.

## Conexões
- [[robot-variaveis-escopo-prioridade]] — Veja também: Robot Framework: controlar escopo e precedência de variáveis.
- [[robot-keyword-argumentos-e-conversao]] — Veja também: Robot Framework: declarar argumentos de keyword como interface de teste.

## Fontes
- [Robot Framework 7.5 — User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) — formato de testes, setups, teardowns, tags, templates, variáveis, libraries e arquivos de saída; consultado em 2026-10-02.
- [Robot Framework 7.5 — BuiltIn library](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) — keywords incorporadas de fluxo, logging, execução, variáveis e assertions; consultado em 2026-10-02.
