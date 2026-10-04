---
id: software.criacao_ia.tranche01.000082
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://docs.comfy.org/basic-concepts/workflow", "https://docs.comfy.org/tutorials/video/wan/wan2_2"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: instalar modelos nos caminhos esperados

## Em uma frase

Nós de carregamento selecionam arquivos de modelo específicos e cada família precisa do formato e diretório esperados pelo workflow.

## Por que importa

Modelo errado ou não detectado gera falha de carregamento e pode produzir resultados que não correspondem ao método pretendido.

## Como funciona

Verifique família, variante, precisão e caminho na documentação; mantenha nomes e checksums registrados no projeto.

## Exemplo

O exemplo Wan carrega os diffusion models, encoder de texto e VAE indicados para aquela variante do workflow.

## Limites e trade-offs

Arquivo com nome parecido pode ter arquitetura incompatível; redistribuição de pesos também está sujeita a licenças próprias.

## Como verificar

Confirme nós sem erro, modelo realmente carregado e provenance/licença do arquivo antes de compartilhar ou publicar.

## Conexões
- [[comfyui-ler-um-workflow-como-grafo]] — ComfyUI: ler um workflow como grafo.
- [[comfyui-escolher-template-antes-de-montar-do-zero]] — ComfyUI: escolher template antes de montar do zero.

## Fontes
- [ComfyUI Docs — Workflows](https://docs.comfy.org/basic-concepts/workflow) — Define workflows como grafos de nós e descreve abrir, executar e salvar fluxos. Consulta: 2026-10-04.
- [ComfyUI Docs — Wan 2.2 video workflow](https://docs.comfy.org/tutorials/video/wan/wan2_2) — Apresenta workflows oficiais de geração de vídeo Wan 2.2, entradas, modelos e parâmetros. Consulta: 2026-10-04.
