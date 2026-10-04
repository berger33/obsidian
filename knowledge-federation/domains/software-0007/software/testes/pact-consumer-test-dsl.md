---
id: software.testes.tranche17.001127
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
fontes: ["https://docs.pact.io/implementation_guides/javascript", "https://github.com/pact-foundation/pact-js"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pact: escrever a interação de teste

## Em uma frase
A interface de teste descreve o estado inicial, a requisição esperada e a resposta simulada, e executa o código do consumidor contra esse dublê.

## Por que importa
Rodar o consumidor contra o provedor simulado verifica que ele constrói a requisição correta e interpreta a resposta no formato acordado.

## Como funciona
Declare o estado do provedor, descreva a chamada e a resposta, e deixe o teste do consumidor validar o comportamento do cliente.

## Exemplo
Um caso de consulta pode declarar que existe um produto com identificador conhecido e verificar que o cliente monta a lista esperada.

## Limites e trade-offs
O teste de consumidor não verifica o provedor; ele confirma apenas que o cliente se comporta como o contrato descreve.

## Como verificar
Execute o teste apontando para o provedor simulado e confirme que o arquivo de contrato foi gerado com a interação declarada.

## Conexões
- [[pact-consumer-driven]] — Veja também: Pact: entender o contrato dirigido pelo consumidor.
- [[pact-matching-rules]] — Veja também: Pact: usar correspondência flexível.

## Fontes
- [Pact — Consumer tests](https://docs.pact.io/implementation_guides/javascript) — interface de teste do consumidor e geração do arquivo de contrato; consultado em 2026-10-03.
- [Pact — repositório oficial](https://github.com/pact-foundation/pact-js) — implementação de referência em JavaScript e exemplos; consultado em 2026-10-03.
