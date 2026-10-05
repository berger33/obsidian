---
id: software.criacao_ia.tranche05.000432
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-engine.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/profile-a-model.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: escolher backend após medir modelo, dados e plataforma

## Em uma frase
`BackendType` altera onde as operações do worker são executadas, e a opção mais rápida depende de modelo, hardware, plataforma e local dos dados.

## Por que importa
Mover tensores entre CPU e GPU pode custar mais que a inferência em si, enquanto alguns operadores ou plataformas não suportam todos os backends.

## Como funciona
Considere CPU para modelos pequenos ou dados que já estão na CPU, GPUCompute para muitos modelos quando suportado e GPUPixel em plataformas sem compute shaders; meça o cenário alvo com o profiler.

## Exemplo
Uma classificação pequena que recebe valores da CPU é comparada em CPU e GPUCompute; uma rede de imagem mantém os dados na GPU e é medida no dispositivo de destino.

## Limites e trade-offs
A documentação descreve tendências, não uma regra universal; se o backend não suportar uma camada, o worker pode afirmar erro. Verifique plataforma e formatos reais.

## Como verificar
Execute o mesmo conjunto de entradas nos backends compatíveis, compare correção e latência em hardware alvo e confira o uso de memória e transferências no profiler.

## Conexões
- [[unity-sentis-modelasset-runtime-model-worker]] — Unity Sentis 2.5: separar ModelAsset, runtime Model e Worker de execução.
- [[unity-sentis-inspecionar-shape-e-dtype-da-entrada]] — Unity Sentis 2.5: construir input tensor conforme shape e tipo esperados pelo modelo.

## Fontes
- [Unity Sentis 2.5 — Create an engine](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-engine.html) — Compara CPU, GPUCompute e GPUPixel e alerta sobre camadas não suportadas. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Profile a model](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/profile-a-model.html) — Documenta perfilamento para medir desempenho do modelo com ferramentas Unity. Consulta: 2026-10-04.
