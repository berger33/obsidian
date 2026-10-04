---
id: software.testes.tranche17.001071
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
fontes: ["https://docs.locust.io/en/stable/writing-a-locustfile.html", "https://github.com/locustio/locust"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Locust: marcar falhas com validação explícita

## Em uma frase
O cliente permite capturar a resposta e declarar sucesso ou falha, cobrindo casos em que o código de status não expressa o resultado da operação.

## Por que importa
Uma resposta com código de sucesso pode conter erro de aplicação, e sem validação explícita a medição registra comportamento saudável onde não há.

## Como funciona
Use o bloco de resposta como contexto, marque a falha com mensagem específica e verifique as condições do contrato antes de liberar o resultado.

## Exemplo
Um endpoint que devolve lista vazia por falha interna pode ser marcado como falho a partir da presença de campo de erro no corpo.

## Limites e trade-offs
Marcar falha manualmente exige lembrar de liberar a resposta; esquecer o encerramento deixa a métrica de sucesso distorcida.

## Como verificar
Provoque um erro de aplicação no serviço de teste e confirme que a requisição aparece como falha no resumo.

## Conexões
- [[locust-user-lifecycle]] — Veja também: Locust: preparar e encerrar o usuário.
- [[locust-tags-and-selection]] — Veja também: Locust: selecionar tarefas por etiquetas.

## Fontes
- [Locust — Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html) — classes de usuário, tarefas, pesos, tempos de espera e ciclo de vida; consultado em 2026-10-03.
- [Locust — repositório oficial](https://github.com/locustio/locust) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
