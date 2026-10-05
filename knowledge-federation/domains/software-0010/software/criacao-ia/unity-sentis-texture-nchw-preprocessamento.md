---
id: software.criacao_ia.tranche05.000435
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/convert-texture-to-tensor.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/tensor-fundamentals.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: conferir layout NCHW e escala ao converter Texture para Tensor

## Em uma frase
`TextureConverter.ToTensor` converte texturas para tensores float e assume por padrão o layout batch, channels, height, width, que deve corresponder ao modelo.

## Por que importa
Canal trocado, origem invertida ou escala errada altera os pixels entregues à rede mesmo quando a dimensão total do tensor parece correta.

## Como funciona
Crie tensor com shape compatível, use `TextureConverter.ToTensor`, e aplique `TextureTransform` se precisar mudar channel swizzle, origem ou layout. Confira também o intervalo de valor exigido pelo modelo.

## Exemplo
Um classificador RGB usa shape `(1, 3, height, width)`, transforma a textura de webcam com um tensor pré-alocado e normaliza a faixa somente se o modelo exigir.

## Limites e trade-offs
A conversão padrão não decide a normalização específica da rede; o Unity também pode redimensionar linearmente quando as dimensões da textura e do tensor diferem.

## Como verificar
Passe uma imagem de teste com cores distintas por canal, inspecione shape e valores de amostra e compare a inferência com a mesma entrada pré-processada fora do jogo.

## Conexões
- [[unity-sentis-shapes-dinamicos-compatibilidade]] — Unity Sentis 2.5: tratar dimensões dinâmicas como contrato explícito de entrada.
- [[unity-sentis-compatibilidade-operadores-backend]] — Unity Sentis 2.5: validar operadores e tipos antes de fixar backend.

## Fontes
- [Unity Sentis 2.5 — Convert a texture to a tensor](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/convert-texture-to-tensor.html) — Define conversão, layout NCHW padrão, transforms e reamostragem. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Tensor fundamentals](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/tensor-fundamentals.html) — Explica formatos, dimensões e localização de dados de tensores. Consulta: 2026-10-04.
