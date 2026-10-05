---
id: software.criacao_ia.tranche05.000431
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/import-a-model-file.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-engine.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: separar ModelAsset, runtime Model e Worker de execução

## Em uma frase
O fluxo documentado carrega um `ModelAsset` para um modelo de runtime e cria um `Worker` que executa esse modelo usando um backend escolhido.

## Por que importa
Distinguir o asset armazenado do objeto de execução torna o ciclo de inicialização e a propriedade dos recursos mais claros em componentes Unity.

## Como funciona
Importe o modelo por uma fonte compatível, carregue-o com `ModelLoader.Load` e construa `Worker(runtimeModel, backendType)`. Guarde o worker para as inferências seguintes e libere-o quando o componente encerrar seu uso.

## Exemplo
Um componente serializa uma referência `ModelAsset`, carrega o modelo em `OnEnable`, cria um worker e, em `OnDisable`, descarta o worker e os tensores que alocou.

## Limites e trade-offs
Sentis suporta vários formatos e a compatibilidade depende de operadores e plataforma; carregar o asset não garante que o grafo poderá executar no backend selecionado.

## Como verificar
Use um modelo de amostra do pacote, confirme carregamento e execução em uma cena de teste e faça a cena ser ativada e desativada repetidamente para detectar vazamentos.

## Conexões
- [[unity-sentis-escolher-backend-por-modelo]] — Unity Sentis 2.5: escolher backend após medir modelo, dados e plataforma.

## Fontes
- [Unity Sentis 2.5 — Import a model file](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/import-a-model-file.html) — Explica importação de arquivo e criação do modelo de runtime a partir de um asset. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Create an engine](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-engine.html) — Demonstra `ModelLoader.Load` e criação de um Worker com backend explícito. Consulta: 2026-10-04.
