---
id: software.testes.tranche16.000962
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://www.artillery.io/docs/get-started/first-test", "https://github.com/artilleryio/artillery"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Artillery: compor a jornada do usuário virtual

## Em uma frase
O bloco de cenários descreve a sequência de passos que cada usuário virtual executa, incluindo requisições, pausas e agrupamentos.

## Por que importa
Uma carga sem jornada realista mede endpoint isolado e não revela o custo de uma sessão completa do ponto de vista da pessoa usuária.

## Como funciona
Ordene os passos como no uso real, intercale pausas de leitura e mantenha cada cenário focado em um objetivo verificável.

## Exemplo
Um cenário de compra pode listar produtos, pausar para simular leitura, adicionar ao carrinho e concluir o pedido na mesma sequência executada por uma pessoa.

## Limites e trade-offs
Cenários longos dificultam atribuir latência a um passo específico e tendem a misturar objetivos; a decomposição ajuda a interpretar as métricas.

## Como verificar
Execute a jornada e confira no relatório a latência por requisição, garantindo que cada passo aparece identificável no resultado.

## Conexões
- [[artillery-load-phases]] — Veja também: Artillery: descrever a carga em fases.
- [[artillery-capture-and-reuse]] — Veja também: Artillery: encadear requisições com capturas.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
