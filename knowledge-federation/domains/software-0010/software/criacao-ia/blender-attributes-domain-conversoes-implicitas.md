---
id: software.criacao_ia.tranche03.000244
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
fontes: ["https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html", "https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Blender Geometry Nodes: auditar domínio e conversão de atributos

## Em uma frase
O domínio de um atributo identifica o elemento geométrico associado a cada valor e determina como o dado pode ser interpolado e usado.

## Por que importa
Um valor numérico no domínio Point não é automaticamente equivalente a um no domínio Face ou Face Corner. Conversões implícitas também podem truncar inteiros, reduzir vetores à média ou converter valores float maiores que zero em Boolean, produzindo resultados plausíveis mas incorretos.

## Como funciona
Confira domain e tipo em Spreadsheet e na busca de atributos do modifier. Quando operações combinam geometrias ou domains, conheça a interpolação e as conversões válidas documentadas. Atributos com mesmo nome podem exigir tipo compatível; ao unir geometrias, o tipo de maior complexidade pode ser escolhido, o que altera os valores de saída esperados.

## Exemplo
Uma máscara float por face convertida para Point pode se tornar interpolada em vértices compartilhados. Se a intenção é uma decisão discreta, converta explicitamente em local controlado e confirme que cada ponto recebe o valor esperado em vez de depender da redução automática.

## Limites e trade-offs
As regras de conversão dependem dos tipos, domains e nós envolvidos. Não assuma que domínio preserva correspondência um para um após remesh, subdivisão, instancing ou Join Geometry.

## Como verificar
Inspecione atributo antes e depois de cada operação que altera topologia ou domain, compare número de elementos e valores de fronteira, e habilite Geometry Randomization para detectar dependência indevida de ordem de elementos.

## Conexões
- [[blender-anonymous-versus-named-attributes]] — Blender Geometry Nodes: escolher atributo anônimo ou nomeado.
- [[blender-repeat-zone-iters-e-inputs-externos]] — Blender Repeat Zone: distinguir feedback de entradas constantes.

## Fontes
- [Blender 5.2 LTS — Attributes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html) — define domains, conversões implícitas e escolha de tipo ao combinar geometria Consulta: 2026-10-04.
- [Blender 5.2 LTS — Inspection](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/inspection.html) — descreve inspeção de sockets, atributos e randomização da geometria Consulta: 2026-10-04.
