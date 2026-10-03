---
id: software.testes.tranche21.001485
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

# Chai: .own ignora propriedades herdadas

## Em uma frase
O elo .own restringe property e include às propriedades próprias do objeto, ignorando o que veio do protótipo.

## Por que importa
Verificar posse real protege contra falsos positivos quando a herança ou monkey-patching global injetam chaves que o teste acreditava ausentes.

## Como funciona
Prefira .to.have.own.property('a') quando a presença em Object.prototype poderia contaminar a verificação do contrato do objeto.

## Exemplo
Com b definido no protótipo, {a: 1} tem a propriedade b por herança, mas não por posse: as duas asserções divergem.

## Limites e trade-offs
.own não se combina com .nested, e abusar dele onde a herança é aceitável cria testes mais estritos que o próprio código de produção.

## Como verificar
Injete uma chave no Object.prototype e confirme que property simples passa enquanto a variante own falha.

## Conexões
- [[chai-nested-property-paths]] — Veja também: Chai: caminhos aninhados com .nested.
- [[chai-ordered-members]] — Veja também: Chai: ordem exigida com .ordered.

## Fontes
- [Chai — API BDD (expect/should)](https://www.chaijs.com/api/bdd/) — correntes de linguagem, negação, deep, nested, own, ordered, keys, tipos e include; consultado em 2026-10-03.
- [Chai — repositório oficial](https://github.com/chaijs/chai) — código-fonte, versões e documentação do projeto; consultado em 2026-10-03.
