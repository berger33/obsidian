---
id: software.criacao_ia.tranche04.000350
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
fontes: ["https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html", "https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Godot 4: nas shaders, matrizes são colunares — m[1][0] é a segunda coluna, primeira linha

## Em uma frase
A linguagem de shading do Godot indexa matriz como [coluna][linha], com colunas contíguas em memória, e os escalares são int/float de 32 bits — heranças diretas do dialeto GLSL ES 3.0 em que a linguagem se baseia.

## Por que importa
Composição de transforms (projeção × view × model) é onde portas de outros motores e matemática 'de papel' divergem silenciosamente: quem assume ordem de multiplicação ou layout de linha de um lado e escreve do outro obtém a matriz transposta, sintoma clássico de 'objeto espelhado/rotação trocada' que sobrevive ao primeiro teste porque identidades são simétricas. A doc fixa os dois fatos: colunar e 32-bit.

## Como funciona
Escreva o acesso ciente da ordem: 'mat4x4 m; float v = m[col][row];' — e nas operações, a posição da matriz à esquerda vs. direita define se a transformação compõe em espaço local ou global (composição por colunas: a coluna k de A·B é A vezes a coluna k de B). Vetores de 2–4 componentes ('vec2/vec3/vec4', 'ivec', 'uvec', 'bvec') e os construtores por componente/expansão seguem o mesmo dialeto; não existe 'matNxM' com N≠M genérico fora dos tipos da linguagem. Quando um script CPU precisa 'ler' o que o shader espera, o upload precisa casar o layout — que é exatamente por que Godot usa as builtins de matriz em vez de você montar floats na mão.

## Exemplo
O MikkTSpace tangent frame de um importador é 'mat3 tbn' composto por colunas (T, B, N): a troca de normal world→tangent é 'v_tangent = transpose(tbn) * v_world' pensada em colunas — e o diff visual na normal map é o detector da ordem invertida.

## Limites e trade-offs
A lista de tipos de matriz aceitos é a da tabela da linguagem — confira a página antes de assumir variantes retangulares ou precisões extras; o que não está lá não compila, mas 'não compila' só ajuda quem testa. Precisão de 32 bits vale para int e float: posição de mundo grande perde granularidade antes do wrap — e o workaround é shift local no CPU, não 'float64 no shader'. A semelhança com GLSL ES 3.0 não importa extensões nem #define de desktop — o parser é do motor.

## Como verificar
Um shader de teste que projeta a UV de um quad 2x2 com m[i][j] e valida o layout na tela é o teste unitário da convenção (coluna na horizontal da memória). Compare o resultado de tbn e transpose(tbn) na mesma normal — a troca é visível em normal map direcional. Na fronteira CPU↔GPU, um golden test do buffer de uniforms montado à mão vs. o setado por API valida a suposição de layout que você fez.

## Conexões
- [[godot-render-flags-sombras-wireframe]] — Godot 4: flags de render do shader espacial que economizam passes inteiros.

## Fontes
- [Godot — Shading language](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/shading_language.html) — define os tipos vetoriais/matrizes (indexação colunar) e a precisão dos escalares Consulta: 2026-10-04.
- [Godot — Spatial shader](https://docs.godotengine.org/en/stable/tutorials/shaders/shader_reference/spatial_shader.html) — onde as matrizes de transform built-in do estágio consomem a convenção Consulta: 2026-10-04.
