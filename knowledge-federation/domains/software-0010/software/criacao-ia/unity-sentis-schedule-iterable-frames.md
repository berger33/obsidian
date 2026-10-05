---
id: software.criacao_ia.tranche05.000440
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/split-inference-over-multiple-frames.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/run-an-imported-model.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: distribuir camadas de inferência entre frames com ScheduleIterable

## Em uma frase
`ScheduleIterable` permite percorrer o trabalho de um worker em partes, útil quando uma inferência concentrada em um frame causa stutter.

## Por que importa
Em jogo interativo, uma carga de inferência longa pode disputar o orçamento de frame com lógica, física e renderização.

## Como funciona
Guarde o enumerador retornado por `ScheduleIterable`, avance um número limitado de camadas por frame e só consuma a saída quando o enumerador terminar.

## Exemplo
Uma experiência de NPC distribui a execução em iterações durante `Update`, ajusta camadas por frame conforme o dispositivo e apresenta a ação quando a inferência finaliza.

## Limites e trade-offs
A distribuição troca latência total por menor trabalho concentrado; o número de camadas adequado depende do hardware e a API não garante duração fixa por iteração.

## Como verificar
Compare frame time e tempo até resultado com inferência em um frame e em vários, em dispositivos alvo; confirme que nenhum consumidor lê output antes de terminar o enumerador.

## Conexões
- [[unity-sentis-readback-and-clone-async-lifecycle]] — Unity Sentis 2.5: usar ReadbackAndCloneAsync com sincronização e descarte explícitos.

## Fontes
- [Unity Sentis 2.5 — Split inference over multiple frames](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/split-inference-over-multiple-frames.html) — Documenta `ScheduleIterable`, a iteração por camada e o padrão de retornar entre frames. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Run an imported model](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/run-an-imported-model.html) — Situa agendamento, execução e leitura de saída no ciclo de inferência. Consulta: 2026-10-04.
