---
id: software.testes.tranche17.001153
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-17.md"
fontes: ["https://rspec.info/features/3-12/rspec-core/example-groups/shared-examples/", "https://github.com/rspec/rspec-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec: reutilizar comportamento com exemplos compartilhados

## Em uma frase
Blocos de exemplos compartilhados descrevem comportamento comum e são incluídos em grupos diferentes, com parâmetros e contexto próprio.

## Por que importa
Comportamentos esperados de várias classes semelhantes ficam descritos uma vez, evitando duplicação de exemplos idênticos.

## Como funciona
Extraia o comportamento quando dois grupos descrevem a mesma regra, parametrize as diferenças e inclua o bloco com o contexto que fornece os valores necessários.

## Exemplo
Um comportamento de coleção pode ser compartilhado por listas e conjuntos, cada um definindo como criar a instância testada.

## Limites e trade-offs
Compartilhar cedo demais força abstrações inadequadas, e blocos com muitos parâmetros opcionais indicam que o comportamento não é realmente o mesmo.

## Como verificar
Aplique o bloco a um novo tipo e verifique se os exemplos inclusos fazem sentido sem adaptações especiais.

## Conexões
- [[rspec-argument-matchers]] — Veja também: RSpec: casar argumentos com critérios flexíveis.
- [[rspec-metadata-and-filtering]] — Veja também: RSpec: selecionar exemplos por metadados.

## Fontes
- [RSpec — Shared examples](https://rspec.info/features/3-12/rspec-core/example-groups/shared-examples/) — exemplos compartilhados, parâmetros e inclusão em grupos; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
