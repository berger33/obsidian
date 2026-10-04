---
id: software.testes.tranche22.001609
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://jqwik.net/docs/current/user-guide.html", "https://search.maven.org/search?q=g:net.jqwik"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# jqwik: configuração central e módulos de nicho

## Em uma frase
O guia fecha o ciclo com configuração e alcance: defaults de atributos por classe com @PropertyDefaults, a configuração legada em arquivo jqwik.properties, rerun de propriedades falsificadas, e módulos adicionais — Web (geração de email e domínio), Time (datas, horas e datetimes) e Kotlin (nullable types, coroutines, coleções).

## Por que importa
Propriedades bem configuradas param de ser código: times, shrinking e seed podem subir para defaults de projeto em vez de poluir cada anotação.

## Como funciona
Statistics com @Label, histogramas e "checking coverage of collected statistics" completam o pacote: dá para exigir percentuais e até cobertura de um regex sobre as amostras geradas.

## Exemplo
Domain e Domain Context centralizam geradores de um domínio de negócio (o exemplo do guia são endereços americanos), e contract tests oferecem verificação de contrato por propriedade.

## Limites e trade-offs
A config legacy em jqwik.properties está marcada como legada no próprio guia; novo projeto deveria viver no mecanismo atual, não no arquivo antigo.

## Como verificar
Ative a verificação de cobertura de estatísticas com um threshold absurdo (50% para um caso raro) e veja o run falhar só pela régua estatística.

## Conexões
- [[jqwik-shrinking-assumptions]] — Veja também: jqwik: shrinking, discard ratio e dados fixos.

## Fontes
- [jqwik — User Guide 1.10.1](https://jqwik.net/docs/current/user-guide.html) — properties, geração, shrinking, lifecycle, config e módulos; consultado em 2026-10-03.
- [jqwik — busca no Maven Central](https://search.maven.org/search?q=g:net.jqwik) — artefatos publicados citados pelo guia; consultado em 2026-10-03.
