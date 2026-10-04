---
id: software.criacao_ia.tranche04.000331
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-manage-structural-changes.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: criar/destruir é caro porque o layout muda, e por isso é estrutural

## Em uma frase
Adicionar, remover componentes ou criar/destruir entidades são mudanças estruturais: movem dados entre chunks, e o manual exige planejá-las como episódios, não como linhas de código.

## Por que importa
O armazenamento por chunk organiza dados contíguos por arquétipo; mudar a composição de um entidade desloca bytes e invalida referências. Uma escrita dessas dentro de um laço de sistema é a receita para o gargalo clássico de ECS — o manual tem seção dedicada ('Manage structural changes') justamente porque o custo é estrutural, não de chamada.

## Como funciona
O manual distingue três portas: executar mudança estrutural pelo EntityManager (só na main thread, com o scheduler vazio), deferir com uma EntityCommandBuffer que reproduz as mudanças num ponto seguro, e evitar quando o objetivo não requer mudança (componentes habilitáveis podem ser apenas habilitados/desabilitados). A regra de bolso: sistemas fazem transformações de dados; eventos do jogo viram pedidos, e um sistema de commit executa a mudança estrutural em lote.

## Exemplo
Um hit que 'mata' 2000 inimigos por frame não remove componentes por inimigo: escreve um flag de morte (dado), e o sistema de limpeza roda um ECB em lote com as remoções estruturais uma vez por frame.

## Limites e trade-offs
Habilitar/desabilitar um componente habilitável não é mudança estrutural, mas o manual avisa que todo job que alterna o status precisa completar antes de leituras do estado. Mudanças estruturais não são proibidas — são episódios; um spawn de onda de inimigos na transição de fase é o caso onde o custo é aceitável. Fora do Entities, o custo de 'Destroy' do GameObject tem outras causas — não confunda os modelos.

## Como verificar
Profile com o counter de structural changes do Editor e confirme que o pico cai quando o ECB entra no desenho. Force a mudança dentro do job e observe o erro de segurança/ a queda de fps — as duas coisas documentadas. Teste de regressão: contagem de mudanças estruturais por frame num benchmark de spawn.

## Conexões
- [[unity-ecb-bufferfromentity-replay]] — Unity Entities: a EntityCommandBuffer é replay, não fila mágica.

## Fontes
- [Unity Entities @1.4 — Manage structural changes](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/systems-manage-structural-changes.html) — página oficial que categoriza as portas de mudança estrutural e a deferral Consulta: 2026-10-04.
- [Unity Entities @1.0 — Safety in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html) — explica por que a mudança estrutural move dados e invalida referências Consulta: 2026-10-04.
