---
id: software.testes.tranche16.000963
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

# Artillery: encadear requisições com capturas

## Em uma frase
Valores extraídos da resposta podem ser guardados em variáveis nomeadas e reutilizados nos passos seguintes do mesmo cenário.

## Por que importa
Fluxos autenticados dependem de identificadores gerados pelo servidor, e repetir valores fixos deixa de representar o comportamento real.

## Como funciona
Capture o campo necessário com a expressão adequada e referencie a variável nos passos posteriores, tratando-a como dado opaco.

## Exemplo
Um identificador de produto extraído da listagem pode alimentar a requisição de detalhe e, depois do pedido, o identificador do carrinho orienta a finalização.

## Limites e trade-offs
A captura falha silenciosamente quando o caminho não existe, e a etapa seguinte recebe valor vazio; o cenário precisa verificar o resultado esperado de cada passo crítico.

## Como verificar
Altere o campo capturado no serviço de teste e confirme que a execução falha no ponto correto, em vez de seguir com valor ausente.

## Conexões
- [[artillery-scenario-flow]] — Veja também: Artillery: compor a jornada do usuário virtual.
- [[artillery-thresholds]] — Veja também: Artillery: impor limites de desempenho.

## Fontes
- [Artillery — First test](https://www.artillery.io/docs/get-started/first-test) — config, fases, cenários, capturas, métricas e execução de carga; consultado em 2026-10-03.
- [Artillery — repositório oficial](https://github.com/artilleryio/artillery) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
