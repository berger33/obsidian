---
id: software.testes.tranche21.001555
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://github.com/CodeIntelligenceTesting/jazzer", "https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jazzer: o corpus gerado pelo fuzzer

## Em uma frase
Entradas que abrem nova cobertura vão para o diretório gerado em .cifuzz-corpus/<pacote>.<ClasseTeste>/<metodo>, formando o ponto de partida das próximas corridas.

## Por que importa
Persistir o que descobriu transforma cada execução em acréscimo: o fuzzer seguinte continua do corpus, não do zero.

## Como funciona
Versione o diretório .cifuzz-corpus (como arquivo binário) e rode o fuzzing regularmente para o corpus crescer no ritmo do código.

## Exemplo
Um parser ganha dezenas de sementes que exercitam suportes raros apenas por permanecer no repositório do projeto de teste.

## Limites e trade-offs
Corpus aceito cegamente embute dados de terceiros sensíveis; revisar conteúdo antes de versionar é parte do trabalho.

## Como verificar
Compare a listagem do diretório antes e depois de uma corrida mais longa e confirme o aumento do conjunto.

## Conexões
- [[jazzer-junit-fuzzing-mode]] — Veja também: Jazzer: fuzzing a partir de testes normais.
- [[jazzer-crash-inputs-directory]] — Veja também: Jazzer: inputs que quebram viram arquivo no repositório.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
