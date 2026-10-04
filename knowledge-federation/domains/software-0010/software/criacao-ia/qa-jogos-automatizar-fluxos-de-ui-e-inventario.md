---
id: software.criacao_ia.tranche02.000188
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/", "https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# QA de UI: automatizar navegação em telas de inventário e menus

## Em uma frase
Scripts automatizados de teste de interface navegam por todos os menus, inventários e árvores de habilidades para validar integridade de fluxo.

## Por que importa
Bugs de interface como travamento ao arrastar itens ou textos truncados passam facilmente em revisões pontuais de código.

## Como funciona
Crie testes automatizados que emulam cliques de mouse e toques na tela em sequências aleatórias de compra, venda, equipagem de itens e abertura de configurações, checando integridade dos dados de inventário.

## Exemplo
```csharp
// Emulando fluxo de compra no inventario com Unity Test Framework
[UnityTest]
public IEnumerator Test_PurchaseItem_DeductsGold_AndAddsToInventory()
{
    shopManager.BuyItem("sword_iron_01");
    yield return null;
    Assert.IsTrue(playerInventory.HasItem("sword_iron_01"));
    Assert.AreEqual(900, playerWallet.Gold);
}
```

## Limites e trade-offs
Testes baseados em coordenadas de tela quebram se a resolução ou o layout responsivo forem modificados.

## Como verificar
Execute o teste de inventário no Unity Test Runner e valide se a asserção de saldo de moedas e adição de item passa em 100% dos ciclos.

## Conexões
- [[qa-jogos-validar-determinismo-de-fisica-em-fixed-ticks]] — Veja também: QA de Física: validar determinismo em replays com passos de tempo fixos.
- [[qa-jogos-isolar-cenarios-de-regressao-de-gameplay]] — Veja também: QA de Gameplay: criar microcenários isolados para regressão de mecânicas.
- [[documentacao-executar-exemplos-de-codigo]] — Conexão temática direta com documentacao-executar-exemplos-de-codigo.
- [[qa-jogos-executar-playtests-headless-em-ci]] — Conexão temática direta com qa-jogos-executar-playtests-headless-em-ci.
- [[anthropic-api-depurar-layout-com-mensagens-de-visao]] — Conexão temática direta com anthropic-api-depurar-layout-com-mensagens-de-visao.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
