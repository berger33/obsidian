---
id: software.testes.tranche19.001269
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors", "https://testcafe.io/documentation"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestCafe: localizar elementos com seletores

## Em uma frase
Seletores consultam o DOM de forma assíncrona e aceitam filtros por texto, atributo, índice e relação entre elementos.

## Por que importa
Filtros expressivos evitam seletores frágeis presos à estrutura da marcação e aproximam a consulta da intenção do teste.

## Como funciona
Prefira atributos dedicados à automação, filtre por texto visível quando fizer sentido e verifique contagem e existência antes de agir.

## Exemplo
Um seletor pode pedir o botão cujo texto é confirmar dentro de um formulário específico, independentemente da posição na árvore.

## Limites e trade-offs
Consultar por posição ou classe de estilo quebra com a menor alteração visual, e seletores que casam vários elementos agem sempre no primeiro.

## Como verificar
Faça a consulta retornar zero elementos e confirme que o teste falha indicando o seletor usado.

## Conexões
- [[testcafe-fixtures-and-tests]] — Veja também: TestCafe: organizar fixtures e casos.
- [[testcafe-assertions]] — Veja também: TestCafe: verificar valores com espera integrada.

## Fontes
- [TestCafe — Element selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) — seletores, filtros, propriedades e Shadow DOM; consultado em 2026-10-03.
- [TestCafe — Documentação](https://testcafe.io/documentation) — guias de início, execução, depuração e relatórios; consultado em 2026-10-03.
