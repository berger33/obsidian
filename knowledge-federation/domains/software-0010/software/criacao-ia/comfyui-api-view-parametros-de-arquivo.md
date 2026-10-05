---
id: software.criacao_ia.tranche05.000416
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_routes.md", "https://docs.comfy.org/development/comfyui-server/api-examples.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: recuperar arquivos de saída pela rota view e seus parâmetros

## Em uma frase
A rota `/view` serve um arquivo identificado por nome, subpasta e tipo, dados que devem vir da saída conhecida do workflow.

## Por que importa
Construir uma URL de saída a partir de um caminho local arbitrário confunde a referência do servidor com a localização do cliente e amplia risco de acesso indevido.

## Como funciona
Leia do registro de saída os campos `filename`, `subfolder` e `type`, codifique-os como parâmetros de consulta e envie uma requisição à rota `/view`. Trate a resposta como bytes, não como caminho local da máquina do servidor.

## Exemplo
Uma miniatura usa a referência que o workflow retornou, escapa os parâmetros para URL e exibe o conteúdo servido pelo endpoint, sem concatenar `C:\` ou `/tmp` no browser.

## Limites e trade-offs
O retorno depende do arquivo e do tipo informado; a rota não converte automaticamente conteúdo nem fornece uma política de autorização para um servidor exposto publicamente.

## Como verificar
Teste arquivo em pasta principal e subpasta, confira o parâmetro de tipo e valide que erros HTTP ou ausência do arquivo não viram uma miniatura de sucesso em cache.

## Conexões
- [[comfyui-api-history-resultado-por-prompt-id]] — ComfyUI: recuperar o histórico da execução usando o prompt_id.
- [[comfyui-api-object-info-nos-instalados]] — ComfyUI: consultar object_info para descobrir o esquema dos nós disponíveis.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Documenta a rota `/view` e os parâmetros de consulta usados para visualizar arquivo. Consulta: 2026-10-04.
- [ComfyUI Server — API Examples](https://docs.comfy.org/development/comfyui-server/api-examples.md) — Mostra como os dados de arquivo da execução conduzem à recuperação da saída. Consulta: 2026-10-04.
