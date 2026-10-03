---
id: software.testes.tranche19.001271
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
fontes: ["https://testcafe.io/documentation/402833/guides/basic-guides/test-actions", "https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# TestCafe: encadear ações no controlador

## Em uma frase
Ações do controlador cobrem clique, digitação, teclas, arrasto, navegação e requisição, e podem ser encadeadas quando não retornam valor.

## Por que importa
O encadeamento deixa a intenção do fluxo explícita e reduz a verbosidade do caso sem esconder a sequência executada.

## Como funciona
Encadeie ações relacionadas, separe blocos por etapa com comentário e prefira ações de alto nível do projeto quando existirem.

## Exemplo
Um fluxo de login pode encadear digitar usuário, digitar senha, clicar em entrar e aguardar a navegação.

## Limites e trade-offs
Cadeias longas demais dificultam localizar o passo que falhou, e ações de baixo nível repetidas espalham detalhes de implementação.

## Como verificar
Introduza falha em uma ação intermediária da cadeia e confirme que o relatório aponta o passo exato.

## Conexões
- [[testcafe-assertions]] — Veja também: TestCafe: verificar valores com espera integrada.
- [[testcafe-roles]] — Veja também: TestCafe: reaproveitar autenticação com papéis.

## Fontes
- [TestCafe — Test actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) — ações do controlador, encadeamento, papéis e funções de cliente; consultado em 2026-10-03.
- [TestCafe — Element selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) — seletores, filtros, propriedades e Shadow DOM; consultado em 2026-10-03.
