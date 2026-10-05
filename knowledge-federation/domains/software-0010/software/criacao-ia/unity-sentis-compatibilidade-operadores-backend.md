---
id: software.criacao_ia.tranche05.000436
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/supported-operators.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-engine.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: validar operadores e tipos antes de fixar backend

## Em uma frase
A matriz de operadores registra compatibilidade por backend e tipo de dados; não basta que um modelo importe para garantir execução em toda combinação.

## Por que importa
Uma camada suportada em CPU pode ter restrições no backend escolhido, e a referência alerta que uma camada não suportada pode provocar assertion no worker.

## Como funciona
Inspecione a lista de operadores e tipos para o formato importado, teste o backend alvo durante build de validação e preserve uma configuração compatível conhecida em vez de assumir fallback automático.

## Exemplo
Uma equipe compara os operadores do ONNX exportado com a tabela GPUCompute para a versão do pacote e adiciona uma execução smoke test no dispositivo que será publicado.

## Limites e trade-offs
A tabela é específica da versão do pacote, formato, operador e tipo; não substitui teste na plataforma, driver e dispositivo reais.

## Como verificar
Carregue o mesmo modelo no backend selecionado em cada plataforma-alvo, percorra as saídas esperadas e trate assertion ou operador não suportado como incompatibilidade, não como resposta válida.

## Conexões
- [[unity-sentis-texture-nchw-preprocessamento]] — Unity Sentis 2.5: conferir layout NCHW e escala ao converter Texture para Tensor.
- [[unity-sentis-peekoutput-copyoutput-propriedade]] — Unity Sentis 2.5: escolher entre PeekOutput emprestado e CopyOutput próprio.

## Fontes
- [Unity Sentis 2.5 — Supported ONNX operators](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/supported-operators.html) — Lista operadores e tipos por backend CPU, GPUCompute e GPUPixel. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Create an engine](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/create-an-engine.html) — Afirma que backend sem suporte para uma layer pode gerar assertion no worker. Consulta: 2026-10-04.
