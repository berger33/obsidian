---
id: software.testes.tranche17.001147
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
fontes: ["https://rspec.info/features/3-12/rspec-expectations/", "https://github.com/rspec/rspec-core"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# RSpec: escrever expectativas

## Em uma frase
As expectativas combinam um valor observado com um matcher, cobrindo igualdade, correspondência de padrão, mudança de estado e exceções.

## Por que importa
Matchers expressam a intenção do exemplo em vez de comparar valores manualmente, tornando a falha autoexplicativa.

## Como funciona
Escolha o matcher que expressa exatamente a intenção e prefira matchers específicos a comparações genéricas.

## Exemplo
Um exemplo pode verificar que a coleção passou a conter o item, em vez de comparar o tamanho total antes e depois.

## Limites e trade-offs
Matchers frouxos aceitam resultado incorreto, e expectativas sobre estruturas grandes escondem a divergência real.

## Como verificar
Troque o valor esperado por outro e confirme que a saída de falha mostra de forma clara o que foi observado.

## Conexões
- [[rspec-describe-and-context]] — Veja também: RSpec: organizar exemplos em grupos.
- [[rspec-let-and-subject]] — Veja também: RSpec: preparar dados com memorização preguiçosa.

## Fontes
- [RSpec — Expectations](https://rspec.info/features/3-12/rspec-expectations/) — matchers embutidos e expressão de intenção nas expectativas; consultado em 2026-10-03.
- [RSpec — repositório oficial](https://github.com/rspec/rspec-core) — código-fonte e documentação do núcleo do framework; consultado em 2026-10-03.
