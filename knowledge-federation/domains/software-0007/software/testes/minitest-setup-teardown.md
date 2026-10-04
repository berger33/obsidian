---
id: software.testes.tranche15.000883
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
fontes: ["https://docs.seattlerb.org/minitest/Minitest/Test.html", "https://docs.seattlerb.org/minitest/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Minitest: preparar e limpar cada caso

## Em uma frase
Os métodos `setup` e `teardown` executam antes e depois de cada teste da classe, mantendo o estado de preparação isolado entre casos individuais.

## Por que importa
Preparar dados em variável de classe compartilhada cria dependência de ordem e deixa resíduos que aparecem somente quando a suíte completa é executada.

## Como funciona
Inicialize no `setup` tudo que varia por caso, libere recursos no `teardown` correspondente e reserve estado imutável para constantes seguras.

## Exemplo
`def setup; @arquivo = Tempfile.new('dados'); end` e `def teardown; @arquivo.close!; end` garantem um arquivo novo por teste, sem vazamento.

## Limites e trade-offs
O ciclo roda por método e pode se repetir em cada linha de um teste parametrizado; recursos caros repetidos muitas vezes encarecem a suíte e pedem outra estratégia.

## Como verificar
Faça o primeiro caso falhar no meio do `setup` e confirme que o teste seguinte ainda recebe estado limpo, sem herdar resíduo do anterior.

## Conexões
- [[minitest-assert-raises]] — Veja também: Minitest: inspecionar a exceção capturada.
- [[minitest-spec-dsl]] — Veja também: Minitest: usar a DSL de spec.

## Fontes
- [Minitest — Test](https://docs.seattlerb.org/minitest/Minitest/Test.html) — classes de teste, ciclos de vida, ordem aleatória e paralelização; consultado em 2026-10-02.
- [Minitest — README](https://docs.seattlerb.org/minitest/) — visão geral do projeto, plugins e formas de execução; consultado em 2026-10-02.
