---
id: software.criacao_ia.tranche03.000245
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/repeat_zone.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Repeat Zone: distinguir feedback de entradas constantes

## Em uma frase
Repeat Zone encaminha outputs internos para a iteração seguinte, mas inputs ligados a nós externos permanecem iguais em todas as iterações.

## Por que importa
Um loop geométrico só evolui se a saída de uma passagem voltar ao estado de entrada correto. Confundir parâmetro externo com feedback pode recalcular uma operação a partir do estado original repetidas vezes, sem acumular o resultado esperado.

## Como funciona
Declare os Repeat Items que devem cruzar a fronteira da zona e conecte cada valor de estado do output ao input da iteração seguinte. O socket `Iteration` começa em zero. Inputs provenientes de fora podem parametrizar cada passagem, mas seus valores não mudam dentro do loop; outputs da zona ficam disponíveis após a última iteração.

## Exemplo
Para construir uma pilha, leve geometria acumulada pelo Repeat Output ao próximo Repeat Input, adicione a nova peça por iteração e use `Iteration` para altura ou escala. Um deslocamento conectado de fora permanece igual, a menos que seja combinado explicitamente com o índice da iteração.

## Limites e trade-offs
Repeat Zone não é memória temporal de frames; seu número de iterações e custo ocorrem na avaliação atual do node tree. A geometria pode crescer rapidamente em cada volta e elevar o consumo de memória.

## Como verificar
Inspecione vários `Inspection Index` na zona, compare geometria entre iterações e defina um caso mínimo de duas passagens para provar que feedback muda estado e parâmetro externo continua constante.

## Conexões
- [[blender-attributes-domain-conversoes-implicitas]] — Blender Geometry Nodes: auditar domínio e conversão de atributos.
- [[blender-repeat-versus-simulation-zone]] — Blender Geometry Nodes: escolher Repeat ou Simulation Zone.

## Fontes
- [Blender 5.2 LTS — Repeat Zone](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/repeat_zone.html) — define inputs externos, feedback, índice de iteração e Inspection Index Consulta: 2026-10-04.
- [Blender 5.2 LTS — Inspection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html) — explica inspeção do último resultado avaliado e limites de sockets Consulta: 2026-10-04.
