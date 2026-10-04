---
id: software.criacao_ia.tranche03.000235
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
fontes: ["https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8", "https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unreal PCG runtime: equilibrar scheduler e células concorrentes

## Em uma frase
A política de scheduling decide a ordem das células e `NumGeneratingComponents` limita quantos componentes PCG geram em paralelo.

## Por que importa
Priorizar distância e direção pode reduzir demora percebida, mas um limite muito baixo ainda mantém células relevantes na fila e muda a qualidade aparente da prioridade. O scheduler é parte do orçamento de frame e deve ser observado com workload representativo.

## Como funciona
O modo padrão prioriza por distância e direção da fonte. Ajuste a quantidade de componentes concorrentes para equilibrar uso de CPU e tempo até conteúdo aparecer; use `FramesBetweenGraphSchedules` principalmente para inspeção da ordem. Em execução e desenvolvimento, correlacione decisões do scheduler com `pcg.FrameTime`, overlays e tamanho de células.

## Exemplo
Para uma cena com densidade alta, compare dois limites de geração concorrente enquanto percorre a mesma rota. Se os componentes mais próximos continuam atrasados, examine tempo por graph e quantidade de dados antes de aumentar a concorrência, que pode competir com simulação e renderização.

## Limites e trade-offs
Aumentar paralelismo não garante aumento proporcional de throughput: CPU, tarefas de geração e criação de atores têm gargalos distintos. Pesos de direção mudaram de importância relativa com HiGen Grid Size Exponential no UE 5.5, então configurações antigas devem ser reavaliadas.

## Como verificar
Grave vídeo junto do overlay, habilite log detalhado temporariamente e compare ordem e duração de Generate Calls por rota. Faça profiling com contagens, hardware e graph idênticos, sem extrapolar resultados de Editor para Shipping.

## Conexões
- [[ue-pcg-runtime-generation-sources-radii]] — Unreal PCG runtime: fontes, raios de geração e limpeza.
- [[ue-pcg-overlay-runtime-generation]] — Unreal PCG: interpretar overlay de geração em runtime.

## Fontes
- [Unreal Engine 5.8 — PCG generation modes](https://dev.epicgames.com/documentation/unreal-engine/using-pcg-generation-modes-in-unreal-engine?application_version=5.8) — detalha scheduler por distância/direção e limite de componentes que geram em paralelo Consulta: 2026-10-04.
- [Unreal Engine 5.8 — PCG runtime debugging](https://dev.epicgames.com/documentation/unreal-engine/pcg-runtime-generation-debugging-in-unreal-engine?application_version=5.8) — documenta cvars, métricas de overlay e budgets de runtime Consulta: 2026-10-04.
