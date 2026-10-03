---
id: software.testes.tranche21.001483
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
fontes: ["https://www.chaijs.com/api/bdd/", "https://github.com/chaijs/chai"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Chai: igualdade profunda com .deep

## Em uma frase
Adicionar .deep à cadeia faz as asserções equal, include, members, keys e property compararem por igualdade profunda em vez da estrita do operador de três sinais de igual.

## Por que importa
Em JavaScript, objetos comparados por referência falham mesmo com conteúdo idêntico; .deep declara que o que importa são os valores do documento.

## Como funciona
Compare payloads com to.deep.equal e confirme que a falha aponta exatamente a chave divergente com diff legível.

## Exemplo
expect({a: 1}).to.deep.equal({a: 1}) passa, enquanto a versão sem .deep falha — a distinção é documentada com esses dois casos.

## Limites e trade-offs
Igualdade profunda em objetos com estado interno ou instâncias de classe pode aceitar o que você rejeitaria à mão; .deep.property aceita o mesmo risco.

## Como verificar
Escreva dois objetos de mesmo conteúdo por referências diferentes e confirme que só a versão .deep passa.

## Conexões
- [[chai-not-assert-positive]] — Veja também: Chai: negar com .not é poder, não dever.
- [[chai-nested-property-paths]] — Veja também: Chai: caminhos aninhados com .nested.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — repositório oficial](https://github.com/chaijs/chai) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
