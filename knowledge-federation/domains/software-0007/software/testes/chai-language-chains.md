---
id: software.testes.tranche21.001481
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-21.md"
fontes: ["https://www.chaijs.com/api/bdd/", "https://www.chaijs.com/api/should/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Chai: correntes de linguagem de leitura

## Em uma frase
Os getters to, be, been, is, that, which, and, has, have, with, at, of, same, but, does, still e also existem para melhorar a legibilidade e não alteram o resultado.

## Por que importa
A gramaticalidade encadeável torna a asserção uma frase, e isso reduz o esforço de ler e revisar dezenas de verificações em arquivo de teste.

## Como funciona
Encadeie o que soar natural, sem medo: os elos decorativos não adicionam comportamento, e o valor da asserção está nos elos terminais.

## Exemplo
expect(usuario).to.be.an('object') lê melhor que a versão mínima expect(usuario).a('object') pelo mesmo efeito prático.

## Limites e trade-offs
Cadeias excessivamente longas escondem qual elo realmente verifica; encadeamentos sem elo terminal não verificam nada e passam em silêncio.

## Como verificar
Remova um elo decorativo de uma asserção existente e confirme que o resultado da verificação não muda.

## Conexões
- [[chai-three-styles]] — Veja também: Chai: três estilos, um núcleo.
- [[chai-not-assert-positive]] — Veja também: Chai: negar com .not é poder, não dever.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — API should](https://www.chaijs.com/api/should/) — atualização do protótipo e uso do estilo should; consultado em 2026-10-03.
