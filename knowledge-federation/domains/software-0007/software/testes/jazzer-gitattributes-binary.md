---
id: software.testes.tranche21.001557
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

# Jazzer: marcar corpus e inputs como binários no git

## Em uma frase
Para versionar os diretórios de entradas, o README manda marcá-los como binários no .gitattributes, com src/test/resources/** e .cifuzz-corpus/** no exemplo.

## Por que importa
Arquivos de semente frequentemente contêm bytes que o diff e a normalização de fim de linha do git corrompem, quebrando a reprodutibilidade silenciosamente.

## Como funciona
Adicione as duas linhas do exemplo ao .gitattributes antes do primeiro commit dos corpus e inputs.

## Exemplo
git trata as sementes como blob opaco, sem reescrita de CRLF nem diff de texto.

## Limites e trade-offs
Esquecer a regra é descoberto tarde: o sintoma aparece como input que reproduz falha antiga localmente e passa no checkout limpo.

## Como verificar
Committe uma semente com bytes de CRLF e confirme que o conteúdo permanece idêntico no clone.

## Conexões
- [[jazzer-crash-inputs-directory]] — Veja também: Jazzer: inputs que quebram viram arquivo no repositório.
- [[jazzer-seeding-junit]] — Veja também: Jazzer: sementes vindas de parâmetros do JUnit.

## Fontes
- [Jazzer — repositório oficial](https://github.com/CodeIntelligenceTesting/jazzer) — modos standalone e JUnit, corpus, inputs e sanitizers; consultado em 2026-10-03.
- [Jazzer — Arguments and configuration options](https://github.com/CodeIntelligenceTesting/jazzer/blob/main/docs/arguments-and-configuration-options.md) — argumentos do agente e hooks desativáveis; consultado em 2026-10-03.
