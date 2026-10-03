---
id: software.testes.tranche22.001565
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
fontes: ["https://bats-core.readthedocs.io/en/latest/writing-tests.html", "https://bats-core.readthedocs.io/en/latest/usage.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# bats-core: tags, filtros e modo foco

## Em uma frase
Desde a versão 1.8.0 o Bats traz tags nativas: diretivas # bats test_tags= e # bats file_tags= anexam rótulos aos casos, e --filter-tags decide o que roda combinando os rótulos.

## Por que importa
Separar smoke tests de suítes longas por nome de arquivo é frágil; tags dão uma dimensão de seleção ortogonal ao caminho e ao regex de --filter.

## Como funciona
A diretiva de tags vale para o próximo @test encontrado e é esquecida depois; file_tags vale para todos os testes do arquivo até outra diretiva sobrepujar; tags aceitam alfanuméricos, _, - e : como separador de namespace.

## Exemplo
bats --filter-tags smoke,cli !slow seleciona o que tem as duas tags positivas e não tem slow; múltiplas ocorrências do flag formam um OU lógico.

## Limites e trade-offs
Listas com tag vazia ("test_tags=,b") são rejeitadas, e qualquer tag começando com bats: é reservada ao uso interno do framework.

## Como verificar
Rode bats -c com --filter-tags e confira que a contagem de casos muda conforme o conjunto selecionado, sem executar nada.

## Conexões
- [[bats-setup-teardown]] — Veja também: bats-core: ganchos por teste e por arquivo.
- [[bats-focus-mode]] — Veja também: bats-core: o que fica marcado roda sozinho.

## Fontes
- [Bats-core — Writing tests](https://bats-core.readthedocs.io/en/latest/writing-tests.html) — run, tags, setup/teardown, ganchos e armadilhas de escrita; consultado em 2026-10-03.
- [Bats-core — Usage](https://bats-core.readthedocs.io/en/latest/usage.html) — opções do CLI, formatters, relatórios e execução paralela; consultado em 2026-10-03.
