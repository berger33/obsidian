---
id: software.criacao_ia.tranche05.000434
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-input-tensor.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/models-concept.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: tratar dimensões dinâmicas como contrato explícito de entrada

## Em uma frase
Uma forma variável só é válida quando corresponde às dimensões dinâmicas declaradas pelo modelo; `TensorShape` não substitui a definição de `DynamicTensorShape`.

## Por que importa
Assumir que qualquer largura, lote ou sequência é permitida pode deixar a aplicação gerar tensores aceitos pelo código C#, mas incompatíveis com o grafo carregado.

## Como funciona
Leia a definição do input e construa shapes concretos compatíveis com ela. Mantenha valores variáveis dentro dos eixos definidos pelo modelo, e trate dimensão fixa como requisito, não como sugestão de runtime.

## Exemplo
Um pipeline de texto permite variar o comprimento apenas no eixo marcado como dinâmico e recusa uma sequência que exceda a política do modelo antes de chamar `Schedule`.

## Limites e trade-offs
Os detalhes de quais eixos podem variar dependem do modelo e da importação; a documentação de Sentis não autoriza tornar dinâmico um eixo que o grafo declarou fixo.

## Como verificar
Monte testes para cada shape mínimo, típico e máximo documentado pelo modelo, mais um caso incompatível; confira que a aplicação valida antes de agendar inferência.

## Conexões
- [[unity-sentis-inspecionar-shape-e-dtype-da-entrada]] — Unity Sentis 2.5: construir input tensor conforme shape e tipo esperados pelo modelo.
- [[unity-sentis-texture-nchw-preprocessamento]] — Unity Sentis 2.5: conferir layout NCHW e escala ao converter Texture para Tensor.

## Fontes
- [Unity Sentis 2.5 — Create input for a model](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-input-tensor.html) — Explica que TensorShape criado deve ser compatível com DynamicTensorShape do input. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Sentis models](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/models-concept.html) — Apresenta o modelo e seus inputs como contrato para a execução em runtime. Consulta: 2026-10-04.
