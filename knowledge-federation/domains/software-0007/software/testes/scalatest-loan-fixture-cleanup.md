---
id: software.testes.tranche13.000716
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://www.scalatest.org/user_guide/sharing_fixtures", "https://www.scalatest.org/user_guide/writing_your_first_test"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ScalaTest: liberar fixture por loan pattern

## Em uma frase
Loan-fixture é opção quando testes diferentes precisam de objetos específicos que precisam ser limpos ao concluir.

## Por que importa
Gerenciar recurso no mesmo escopo que o usa evita vazamento de arquivo, conexão ou socket para o próximo caso.

## Como funciona
Passe o recurso como argumento de função, abra antes do callback e feche em `finally`; crie recurso fresco para cada teste que precisa dele.

## Exemplo
Um helper pode abrir arquivo temporário, fornecer stream ao corpo do teste e fechá-lo mesmo quando uma assertion lança falha.

## Limites e trade-offs
Fechar no escopo errado ou compartilhar stream entre testes serializa casos e torna falhas dependentes de ordem.

## Como verificar
Force exceção dentro do callback e confira no teste seguinte que handle foi liberado e que nenhum arquivo ficou bloqueado.

## Conexões
- [[scalatest-fixture-withfixture]] — Veja também: ScalaTest: escolher withFixture para tratamento comum.
- [[scalatest-table-driven-check]] — Veja também: ScalaTest: associar cada linha de tabela a uma propriedade.

## Fontes
- [ScalaTest — Sharing Fixtures](https://www.scalatest.org/user_guide/sharing_fixtures) — fixture factories, withFixture and cleanup; consultado em 2026-10-02.
- [ScalaTest — Writing Your First Test](https://www.scalatest.org/user_guide/writing_your_first_test) — test registration and suite examples; consultado em 2026-10-02.
