---
id: software.criacao_ia.tranche03.000240
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-03.md"
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG GPU: tratar escopo Beta como dependência de engine

## Em uma frase
Na documentação UE 5.8, PCG GPU Processing é feature Beta com cautela explícita para shipping e suporte restrito a um subconjunto de nós.

## Por que importa
Um graph que mistura CPU e GPU depende de cobertura específica por nó, distribuição de dados e estabilidade da engine. Marcar a feature como Beta evita apresentá-la como substituto universal de execução CPU e torna visíveis os riscos de release e migração.

## Como funciona
Confira a lista de nós GPU suportados na versão exata do projeto; a página 5.8 destaca Copy Points, Static Mesh Spawner e Custom HLSL, entre um conjunto limitado. Teste o graph numa versão de engine fixada, use inspeção e debug de dados GPU e mantenha alternativa CPU para caminhos que não têm cobertura aceitável.

## Exemplo
Um protótipo usa Custom HLSL para editar milhares de pontos e um spawner GPU, mas mantém um caminho de geração CPU para plataforma de validação sem suporte. Um teste de cook e runtime confirma os resultados em cada alvo antes da escolha de shipping.

## Limites e trade-offs
Status Beta e lista de nós podem mudar entre versões do Unreal. HLSL customizado exige conhecimento de layouts e saída de dados; APIs, atributos e comportamento em alvo final não devem ser inferidos apenas pelo Editor.

## Como verificar
Consulte a documentação correspondente à versão travada, compile todos os targets, inspecione dados em nós GPU e execute testes visuais, de determinismo e desempenho em hardware representativo. Registre fallback e risco Beta no gate de release.

## Conexões
- [[ue-pcg-gpu-compute-graph-transferencias]] — Unreal PCG GPU: agrupar nós para reduzir transferências.

## Fontes
- [Unreal Engine 5.8 — PCG GPU processing](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-with-gpu-processing-in-unreal-engine?application_version=5.8) — rotula a feature Beta, alerta sobre shipping e enumera suporte limitado a nodes Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG runtime debugging](https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8) — detalha debug de GPU, inspeção de buffers e profiling de kernels Consulta: 2026-10-04.
