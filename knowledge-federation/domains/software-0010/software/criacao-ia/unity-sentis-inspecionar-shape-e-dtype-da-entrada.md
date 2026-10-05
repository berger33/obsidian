---
id: software.criacao_ia.tranche05.000433
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-input-tensor.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/models-concept.html#model-inputs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: construir input tensor conforme shape e tipo esperados pelo modelo

## Em uma frase
O tensor de entrada precisa ter formato e tipo de dados compatíveis com o input declarado no modelo, e sua forma deve respeitar `DynamicTensorShape`.

## Por que importa
Um tensor com número correto de valores mas eixos invertidos ou tipo divergente pode falhar ou produzir inferência semanticamente incorreta.

## Como funciona
Inspecione os inputs do modelo antes de alocar `TensorShape`, escolha o tipo `Tensor<T>` apropriado e forneça dados na ordem de eixos esperada. Para múltiplas entradas, associe cada tensor ao nome correspondente.

## Exemplo
Antes de agendar uma rede de classificação, a aplicação confirma o shape esperado, prepara um tensor float compatível e passa o valor pelo input nomeado documentado pelo grafo.

## Limites e trade-offs
A forma não define sozinha a normalização ou a semântica dos valores; esses requisitos vêm do modelo exportado e não podem ser deduzidos apenas da classe Tensor.

## Como verificar
Teste shape mínimo, dimensão variável permitida e tipo de dados do modelo; confirme rejeição controlada para dimensões incompatíveis e compare saída com fixture de referência.

## Conexões
- [[unity-sentis-escolher-backend-por-modelo]] — Unity Sentis 2.5: escolher backend após medir modelo, dados e plataforma.
- [[unity-sentis-shapes-dinamicos-compatibilidade]] — Unity Sentis 2.5: tratar dimensões dinâmicas como contrato explícito de entrada.

## Fontes
- [Unity Sentis 2.5 — Create input for a model](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-input-tensor.html) — Exige inspecionar shapes e tipos e relaciona TensorShape a DynamicTensorShape. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Model inputs](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/models-concept.html#model-inputs) — Descreve metadados de entrada do modelo usados para criar tensores compatíveis. Consulta: 2026-10-04.
