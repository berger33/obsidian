---
id: software.testes.tranche15.000890
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://www.jacoco.org/jacoco/trunk/doc/agent.html", "https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# JaCoCo: medir cobertura com o agente Java

## Em uma frase
O agente do JaCoCo instrumenta classes em tempo de execução e grava os dados coletados em um arquivo binário de execução durante a JVM.

## Por que importa
Instrumentar em memória evita alterar os artefatos compilados e permite medir exatamente o que a suíte executou no processo real.

## Como funciona
Configure o agente junto da execução dos testes, informe o destino do arquivo de execução e mantenha os dados separados por suíte quando houver mais de um conjunto.

## Exemplo
A configuração típica adiciona `-javaagent:jacocoagent.jar=destfile=target/jacoco.exec` ao comando da JVM que executa os testes.

## Limites e trade-offs
O agente só mede código carregado pela JVM instrumentada; bibliotecas de terceiros, geração de código em tempo real e classes excluídas podem distorcer a leitura.

## Como verificar
Confirme a criação e a atualização do arquivo de execução após a suíte e verifique se as classes sob teste aparecem na primeira geração de relatório.

## Conexões
- [[jacoco-counters-meaning]] — Veja também: JaCoCo: interpretar os contadores.

## Fontes
- [JaCoCo — Java agent](https://www.jacoco.org/jacoco/trunk/doc/agent.html) — instrumentação em tempo de execução, opções do agente e arquivo de execução; consultado em 2026-10-02.
- [JaCoCo — jacoco:report](https://www.jacoco.org/jacoco/trunk/doc/report-mojo.html) — formatos de relatório, fontes, agregação e configuração do goal; consultado em 2026-10-02.
