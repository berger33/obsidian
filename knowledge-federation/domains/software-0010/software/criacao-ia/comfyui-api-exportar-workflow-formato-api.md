---
id: software.criacao_ia.tranche05.000411
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
fontes: ["https://docs.comfy.org/development/api-development/workflow-api-format.md", "https://docs.comfy.org/development/comfyui-server/api-examples.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: exportar o grafo no formato API em vez de reutilizar o arquivo visual

## Em uma frase
O JSON de execução da API não é o mesmo documento salvo pela interface visual; exporte a forma destinada à API antes de enviar um workflow.

## Por que importa
Misturar os dois formatos pode entregar metadados de layout onde o servidor espera nós executáveis, ou perder valores de widgets necessários à geração.

## Como funciona
A documentação recomenda `File → Export Workflow (API)` para obter o formato de API, que usa identificadores numéricos de nó, mantém valores de widget e omite dados puramente visuais. Guarde essa exportação como artefato de integração.

## Exemplo
Uma ferramenta de renderização exporta um workflow mínimo pelo menu API, substitui apenas o valor de prompt identificado e envia esse JSON para `/prompt`, sem serializar novamente o arquivo do canvas.

## Limites e trade-offs
A exportação registra uma forma de workflow, não garante que os nós personalizados estejam instalados em outro servidor nem que valores de entrada continuem válidos após mudanças de versão.

## Como verificar
Compare o JSON de API exportado com o payload esperado e execute uma submissão pequena; se houver erro de validação, leia `node_errors` em vez de corrigir o JSON visual por tentativa.

## Conexões
- [[comfyui-api-prompt-validacao-e-fila]] — ComfyUI: interpretar POST prompt como validação e enfileiramento, não como resultado.

## Fontes
- [ComfyUI — Workflow API Format](https://docs.comfy.org/development/api-development/workflow-api-format.md) — Distingue o formato API do formato visual e descreve exportação e IDs de nós. Consulta: 2026-10-04.
- [ComfyUI Server — API Examples](https://docs.comfy.org/development/comfyui-server/api-examples.md) — Demonstra o uso de workflows exportados em chamadas da API do servidor. Consulta: 2026-10-04.
