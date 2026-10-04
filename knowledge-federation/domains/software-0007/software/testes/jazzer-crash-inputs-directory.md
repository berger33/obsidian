---
id: software.testes.tranche21.001556
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

# Jazzer: inputs que quebram viram arquivo no repositório

## Em uma frase
Toda entrada que provoca falha é salva no diretório de inputs do teste, derivado do pacote e da classe — src/test/resources/<pacote>/<Classe>Inputs/<metodo> — ou no diretório atual quando a pasta não existe.

## Por que importa
Um crash sem arquivo reprodutível é um bug não reportável; o diretório dedicado dá ao bug o anexo que ele precisa.

## Como funciona
Mantenha a pasta de inputs no repositório para que o modo regressão execute cada crash gravado como teste unitário permanente.

## Exemplo
Cada entrada na pasta vira um caso JUnit que precisa continuar passando depois da correção — a regressão fica blindada.

## Limites e trade-offs
Se a pasta de resources não existir, o input do crash cai no diretório de execução e pode se perder entre jobs de CI.

## Como verificar
Provque uma exceção em um alvo, encontre o arquivo gravado e rode a suíte de regressão para vê-lo virar caso.

## Conexões
- [[jazzer-generated-corpus]] — Veja também: Jazzer: o corpus gerado pelo fuzzer.
- [[jazzer-gitattributes-binary]] — Veja também: Jazzer: marcar corpus e inputs como binários no git.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
