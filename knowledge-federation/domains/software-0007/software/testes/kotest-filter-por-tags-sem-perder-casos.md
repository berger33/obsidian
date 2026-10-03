---
id: software.testes.tranche15.000908
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/framework-config-props.html", "https://kotest.io/docs/framework/project-config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: usar tags como classificação sem transformar filtro em suíte completa

## Em uma frase
Tags agrupam casos por dimensão como banco, plataforma ou custo, e filtros de inclusão/exclusão selecionam um subconjunto antes da execução.

## Por que importa
A seleção explícita é útil para jobs específicos, mas um job que só roda `Slow` ou só exclui `Integration` não satisfaz o contrato de validar todos os casos.

## Como funciona
Tags devem compor uma matriz de CI consciente, não esconder testes fora da rotina principal.

## Exemplo
Marque os casos de integração com tag própria e use uma etapa rápida dedicada, mantendo outro job que executa todos os testes sem filtro restritivo.

## Limites e trade-offs
Herança de tags e expressão de filtro podem variar por configuração do engine; a lista de tags associadas precisa estar visível para a equipe.

## Como verificar
Liste os casos por filtro e sem filtro, compare os totais e configure uma verificação que falhe se o conjunto completo tiver zero testes.

## Conexões
- [[kotest-platforms-defaults-de-concorrencia]] — Veja também: Kotest 6.2: evitar aplicar expectativa JVM a todas as plataformas.
- [[kotest-test-discovery-filtro-vazio-como-falha]] — Veja também: Kotest 6.2: tornar uma suíte vazia uma falha explícita.

## Fontes
- [Kotest 6.2 — Framework configuration properties](https://kotest.io/docs/framework/framework-config-props.html) — filtros, tags, discovery, isolamento e parâmetros de execução; consultado em 2026-10-02.
- [Kotest 6.2 — Project Level Config](https://kotest.io/docs/framework/project-config.html) — configuração de engine no nível do projeto e precedência; consultado em 2026-10-02.
