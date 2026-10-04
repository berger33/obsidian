---
id: software.criacao_ia.tranche04.000340
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/conversion-intro.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/index.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: o baking é a fronteira de conversão cena↔ECS, e o runtime tem outra porta

## Em uma frase
Subscenes convertem GameObjects em entidades no build (Baker executa na editor), e mudanças em jogo que o baking não previu precisam da via runtime — são duas portas distintas com contratos distintos.

## Por que importa
O manual separa as seções ('Convert data — Change GameObject data to ECS data with baking') porque as fases do pipeline têm custos diferentes: baking roda no editor, alimenta o cache de conteúdo e aceita trabalho por-scene; a conversão em runtime contorna o cache, cria dados fora do pipeline e tem o custo que os docs documentam como não-recomendado por default. Misturar as duas no mesmo problema é a origem de perfis confusos e builds que mudam sozinhos.

## Como funciona
Um Baker por tipo de Authoring: 'Build(entity, state)' compõe os componentes ECS a partir do MonoBehaviour e referencia assets por handle — é aqui que entra o blob do preset de stats. O output entra em content archives e Subscenes. A via runtime existe para o imprevisível (spawn de conteúdo do servidor); as opções de runtime baking têm trade-offs de perf documentados, e a regra de revisão é anotar explicitamente qual porta um prefab precisa atravessar.

## Exemplo
O prefab de árvore com LOD e colisor vira entidades num único baker (com blob de dados de variação); ao iniciar o nível, o streaming das Subscenes carrega o resultado. Spawnar 10 mil árvores de um seed procedural é caso declarado para a porta de runtime, não para 'inventa-authoring'.

## Limites e trade-offs
Baker é código de editor — mudanças no baking invalidam caches e podem silenciosamente alterar conteúdo (o 're-bake' é parte do ciclo de revisão). O runtime baking mantém a responsabilidade por GC/alloc que o baking de editor absorve; e os dois caminhos não se anulam: conteúdo pré-baked + adição runtime é a configuração realista. Autoria do GameObject (gameobject-remoting) tem regras próprias para Transform sincronizada.

## Como verificar
Um teste de pipeline: altere um campo do Baker, force o rebuild e confirme que a entidade no world do PlayMode reflete a mudança — é o contrato do cache. Meça o tempo de 'add to scene' por mil entidades nas duas portas e registre o resultado na decisão do time. O inspector de content archives mostra onde cada tipo de dado pousa.

## Conexões
- [[unity-aspects-limpeza-de-assinatura]] — Unity Entities: RefAspect limpa a assinatura do sistema, não o armazenamento.

## Fontes
- [Unity Entities @1.4 — Convert data (intro)](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/conversion-intro.html) — página oficial do fluxo de conversão via baking Consulta: 2026-10-04.
- [Unity Entities @1.4 — Manual index](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/index.html) — taxonomia das seções (content management, performance and debugging) que delimitam o escopo da conversão Consulta: 2026-10-04.
