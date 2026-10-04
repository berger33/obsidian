---
id: software.testes.stateful-hypothesis.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://hypothesis.readthedocs.io/en/latest/stateful.html", "https://hypothesis.works/articles/rule-based-stateful-testing/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Stateful property-based testing, RuleBasedStateMachine, Model-based testing]
lote: software-testes-2000-0001
---

# Testes stateful com modelos e Hypothesis

## Em uma frase
Testes stateful geram sequências de ações sobre um sistema, permitindo procurar falhas que só aparecem após transições de estado.

## Por que importa
Um teste de função com entradas independentes pode cobrir chamadas isoladas, mas não necessariamente combinações de operações como criar, atualizar e remover o mesmo recurso. Uma máquina de estados permite descrever ações permitidas e invariantes que devem persistir após cada etapa. Isso é útil para APIs com estado, estruturas de dados, filas, transações e protocolos.

## Como funciona
No Hypothesis, `RuleBasedStateMachine` define regras que podem ser encadeadas em uma execução. As regras podem receber valores de estratégias e valores produzidos por regras anteriores; invariantes verificam propriedades do sistema ao longo da sequência. Uma referência simples, ou modelo, pode manter o resultado esperado e ser comparada com o sistema real depois de operações geradas. Pré-condições limitam quando uma ação é válida, como impedir `pop` quando uma fila está vazia.

## Exemplo
Um modelo de carteira mantém saldo esperado. Regras geradas depositam, debitam ou consultam saldo; uma invariante exige que o sistema real e o modelo concordem depois de cada operação válida. A falha pode surgir apenas em uma sequência específica, como depósito, débito no limite e nova consulta.

## Limites e trade-offs
Um modelo independente e correto é essencial; duplicar o mesmo erro do sistema sob teste no modelo pode fazer ambos concordarem. Máquinas com estado muito grande, regras excessivas ou pré-condições raras podem tornar as buscas lentas. Um teste stateful complementa exemplos unitários e testes de integração, não substitui requisitos de domínio nem cobertura de efeitos reais.

## Como verificar
Comece com poucas regras e um modelo pequeno. Confirme que cada ação representa uma transição permitida pelo contrato e que invariantes são executadas nos pontos adequados. Introduza deliberadamente um defeito no modelo de teste ou no sistema sob teste em ambiente local para confirmar que a suíte consegue detectar divergências; examine e preserve sequências falsificadoras.

## Conexões
- [[property-based-testing-hypothesis]] — estratégias geram valores para regras e propriedades.
- [[shrinking-contraexemplos-hypothesis]] — reduz sequências de operações que produzem falhas.
- [[testes-hermeticos-dependencias]] — o ambiente e as dependências do sistema sob teste precisam ser reproduzíveis.

## Fontes
- [Hypothesis — Stateful tests](https://hypothesis.readthedocs.io/en/latest/stateful.html) — máquinas de estado, regras, bundles e invariantes; acesso em 2026-10-01.
- [Hypothesis — Rule-Based Stateful Testing](https://hypothesis.works/articles/rule-based-stateful-testing/) — modelagem de operações e exemplos de sequências de falha; acesso em 2026-10-01.
