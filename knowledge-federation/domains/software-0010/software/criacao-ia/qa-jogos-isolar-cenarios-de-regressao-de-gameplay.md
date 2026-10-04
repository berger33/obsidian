---
id: software.criacao_ia.tranche02.000189
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

# QA de Gameplay: criar microcenários isolados para regressão de mecânicas

## Em uma frase
Microcenários de teste isolam mecânicas específicas em salas limpas para reproduzir e evitar o retorno de bugs conhecidos.

## Por que importa
Testar mecânicas complexas apenas dentro do jogo completo é demorado e sujeito a interferências de outros sistemas não relacionados.

## Como funciona
Crie cenas de teste mínimas contendo apenas o jogador e o elemento testado (ex.: uma rampa com alavanca ou uma porta trancada) e execute asserções determinísticas sobre o evento esperado.

## Exemplo
```csharp
// Cenario minimo de teste de ativacao de armadilha
[UnityTest]
public IEnumerator Test_PressurePlate_TriggersTrapDoor()
{
    player.transform.position = pressurePlate.transform.position;
    yield return new WaitForSeconds(0.2f);
    Assert.IsTrue(trapDoor.IsOpen);
}
```

## Limites e trade-offs
Microcenários simplificados podem não capturar falhas que ocorrem somente quando múltiplos sistemas concorrentes operam simultaneamente.

## Como verificar
Rode a cena de teste isolada individualmente e assegure que o teste conclui em menos de 500 milissegundos.

## Conexões
- [[qa-jogos-automatizar-fluxos-de-ui-e-inventario]] — Veja também: QA de UI: automatizar navegação em telas de inventário e menus.
- [[qa-jogos-auditar-picos-de-frame-time-com-profiler-cli]] — Veja também: Performance de Jogos: auditar picos de frame time com profiler em linha de comando.
- [[context-engineering-usar-testes-como-especificacao]] — Conexão temática direta com context-engineering-usar-testes-como-especificacao.
- [[qa-jogos-executar-playtests-headless-em-ci]] — Conexão temática direta com qa-jogos-executar-playtests-headless-em-ci.
- [[godot-validar-navegacao-em-movimento-real]] — Conexão temática direta com godot-validar-navegacao-em-movimento-real.

## Fontes
- [Farama Gymnasium Documentation — Environment Creation](https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/) — Guia padrão para criação de ambientes de reinforcement learning (step, reset, action/observation spaces). Consulta: 2026-10-04.
- [Unity Test Framework Manual](https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html) — Documentação de testes de integração playmode, asserções de física e execução automatizada em ci. Consulta: 2026-10-04.
