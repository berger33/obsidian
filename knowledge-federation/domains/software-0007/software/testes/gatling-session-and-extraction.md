---
id: software.testes.tranche17.001060
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
fontes: ["https://docs.gatling.io/concepts/session/", "https://docs.gatling.io/concepts/checks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Gatling: transportar dados pela sessão

## Em uma frase
Valores extraídos das respostas ficam guardados na sessão do usuário virtual e podem alimentar requisições posteriores do mesmo cenário.

## Por que importa
Fluxos reais dependem de identificadores gerados pelo servidor, e repetir valores fixos deixa de representar o encadeamento verdadeiro.

## Como funciona
Extraia o campo com uma checagem de captura, nomeie a variável e referencie-a nos pedidos seguintes, evitando presumir o conteúdo.

## Exemplo
Um pedido de carrinho pode salvar o identificador devolvido e usá-lo na finalização, sem que o teste conheça o valor de antemão.

## Limites e trade-offs
Extração mal configurada falha silenciosamente e propaga valor vazio; convém checar a presença do campo antes de depender dele.

## Como verificar
Execute o cenário apontando para um recurso inexistente e confirme que a falha aparece no passo que depende do valor extraído.

## Conexões
- [[gatling-checks]] — Veja também: Gatling: validar respostas com checagens.
- [[gatling-feeders]] — Veja também: Gatling: alimentar cenários com dados externos.

## Fontes
- [Gatling — Session](https://docs.gatling.io/concepts/session/) — armazenamento de valores extraídos e uso em requisições seguintes; consultado em 2026-10-03.
- [Gatling — Checks](https://docs.gatling.io/concepts/checks/) — checagens de resposta, captura de valores e contabilização de falhas; consultado em 2026-10-03.
