---
id: software.testes.tranche20.001411
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-20.md"
fontes: ["https://assertj.github.io/doc/", "https://github.com/assertj/assertj"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# AssertJ: descrever asserções

## Em uma frase
O encadeamento permite anexar uma descrição que aparece na mensagem de falha, identificando o que estava sendo verificado.

## Por que importa
A descrição transforma a falha em informação acionável quando vários campos do mesmo objeto são verificados.

## Como funciona
Descreva cada asserção com o campo verificado e evite descrições genéricas que se repetem em todo o arquivo.

## Exemplo
A asserção pode declarar que verifica o prazo de entrega calculado, tornando imediata a leitura da falha.

## Limites e trade-offs
Descrições copiadas entre asserções escondem qual verificação falhou, e descrever o óbvio acrescenta ruído sem informar.

## Como verificar
Faça uma asserção falhar e confirme que a descrição aparece antes do detalhe da comparação na mensagem.

## Conexões
- [[assertj-collections]] — Veja também: AssertJ: verificar coleções e mapas.
- [[assertj-soft-assertions]] — Veja também: AssertJ: acumular falhas com asserções suaves.

## Fontes
- [AssertJ — Documentação](https://assertj.github.io/doc/) — asserções fluentes, coleções, descrições, asserções suaves e próprias; consultado em 2026-10-03.
- [AssertJ — repositório oficial](https://github.com/assertj/assertj) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
