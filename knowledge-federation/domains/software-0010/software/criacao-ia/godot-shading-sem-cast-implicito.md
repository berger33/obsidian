---
id: software.criacao_ia.tranche04.000346
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: a shading language não faz cast implícito — e suas variáveis locais nascem sem inicializar

## Em uma frase
Entre as regras da linguagem Godot: tipos não convertem sozinhos (escreva uint(2), não confie em 2 p/ uint), e locais não inicializadas têm valor indefinido, ao contrário de uniforms e varyings.

## Por que importa
Os dois são bugs silenciosos por natureza: misturar int e float numa expressão composta dá zero no dev e artefato no release; uma local não atribuída num ramo condicional lê lixo de registrador. A doc da linguagem enumera os dois como diferenças explícitas do comportamento que portadores esperam de C/GLSL frouxo.

## Como funciona
Construa explicitamente: 'uint(2)', 'float(2)', vetores por construtor ('vec2(x, y)'), sem depender de promoção. Declare e inicialize toda local no topo do uso ('float m = 0.0;'), inclusive quando o flow 'óbvio' cobre todos os caminhos — o compilador não garante. Uniform e varying têm defaults de inicialização garantidos pela doc, mas dependa disso só onde for intencional, não por omissão.

## Exemplo
O índice de atlas vindo de um varying int: 'int tile = int(V_TILE);' em vez de uso direto — e num shader de máscara, um 'float acc;' esquecido sem '= 0.0' antes do laço de soma vira tela com grão aleatório em GPUs específicas.

## Limites e trade-offs
A linguagem mira GLSL ES 3.0 — quem conhece GLSL antecipa o resto (funções, swizzling, precisão) com as divergências documentadas, mas não deve esperar extensões de desktop GLSL. Os tipos int/float são de 32 bits — cálculos de índice grandes precisam de cuidados de faixa. E 'uniformes inicializados' não significa imutáveis: são valores por-default, atualizados pelo material.

## Como verificar
Force a mistura 'float x = 1 + 1.0f' no seu estilo e observe o erro do compilador — a recusa é o contrato. Remova a inicialização de uma local acumuladora e rode em duas GPUs para ver a divergência que a regra previne. A página de linguagem serve de checklist em code review de shaders.

## Conexões
- [[godot-particulas-instance-custom]] — Godot 4: INSTANCE_CUSTOM é o canal de dados por-partícula para o shader 2D.
- [[godot-uniform-docs-inspector]] — Godot 4: o /** acima do uniform é documentação vira-inspetor, não comentário decorativo.

## Fontes
- [Godot — Shading language](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html) — lista as regras de tipos, ausência de cast implícito e inicialização por classe de variável Consulta: 2026-10-04.
- [Godot — Canvas item shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/canvas_item_shader.html) — exemplo de uso das regras na família 2D Consulta: 2026-10-04.
