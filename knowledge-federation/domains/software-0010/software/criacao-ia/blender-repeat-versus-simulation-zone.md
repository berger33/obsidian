---
id: software.criacao_ia.tranche03.000246
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/repeat_zone.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Geometry Nodes: escolher Repeat ou Simulation Zone

## Em uma frase
Repeat Zone itera várias vezes numa avaliação; Simulation Zone transporta estado entre frames da timeline.

## Por que importa
As duas caixas parecem loops, mas têm relógios e armazenamento diferentes. Usar Repeat para movimento dependente do tempo recria uma sequência por avaliação; usar Simulation para uma construção instantânea que só precisa de N passos introduz cache de frames desnecessário.

## Como funciona
Escolha Repeat para número configurável de passagens em uma avaliação e feedback entre iterações. Escolha Simulation quando o resultado do frame anterior deve influenciar o seguinte. Na simulação, valores ligados ao input inicial são avaliados uma vez, enquanto links externos para nós dentro da zona são reavaliados por frame; `Delta Time` expressa segundos entre frames.

## Exemplo
Um empilhamento procedural de blocos usa Repeat com índice como altura. Uma multidão de partículas que desloca posição a cada frame usa Simulation e incorpora delta time à velocidade, para manter movimento comparável quando a taxa de frames muda.

## Limites e trade-offs
Simulation está disponível em contexto Modifier, não Tool, e depende da avaliação da timeline. Repeat não mantém estado entre render frames. Parâmetros e caches exigem teste quando se altera frame rate ou sequência temporal.

## Como verificar
Mude o frame sem alterar número de iterações e observe qual grafo preserva estado anterior. Reproduza simulação em frame rate distinto e confira o uso de Delta Time; compare custo de cache para tarefa equivalente.

## Conexões
- [[blender-repeat-zone-iters-e-inputs-externos]] — Blender Repeat Zone: distinguir feedback de entradas constantes.
- [[blender-simulation-anonymous-attributes-state]] — Blender Simulation Zone: declarar atributos anônimos no estado.

## Fontes
- [Blender 5.2 LTS — Repeat Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/repeat_zone.html) — define repetição interna, iteração e fluxo de inputs/outputs Consulta: 2026-10-04.
- [Blender 5.2 LTS — Simulation Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/simulation/simulation_zone.html) — define dependência entre frames, Delta Time e avaliação de inputs externos Consulta: 2026-10-04.
