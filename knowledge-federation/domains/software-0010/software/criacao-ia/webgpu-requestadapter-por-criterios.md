---
id: software.criacao_ia.tranche04.000301
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/GPU/requestAdapter", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: filtrar adaptador por potência e modo de compatibilidade

## Em uma frase
O pedido de adaptador aceita opções para preferir alto desempenho, baixo consumo ou adaptador de software, e resolve para nulo quando nada atende aos requisitos.

## Por que importa
Um dispositivo pode ter mais de uma GPU — integrada, dedicada e até uma implementação por software. Sem critérios, a escolha fica com o navegador; ao explicitar a preferência, a aplicação evita gastar bateria num trabalho leve ou perder throughput numa cena pesada.

## Como funciona
Chame navigator.gpu.requestAdapter com um objeto de opções. Em powerPreference use 'high-performance' quando throughput importa mais que energia e 'low-power' para interfaces e simulações discretas. A flag forceFallbackAdapter seleciona explicitamente a implementação por software, útil em testes sem GPU. Adaptador nulo significa que nenhuma GPU atende: a aplicação deve degrada com aviso, não falhar. Recursos e limites pertencem primeiro ao adaptador e depois ao dispositivo lógico pedido a ele.

## Exemplo
Um visualizador de modelos 3D pede 'high-performance'; se o adaptador vier nulo, mostra um aviso e cai para render 2D. Uma ferramenta de revisão em laptop escolhe 'low-power' para sessões longas. O CI sem GPU roda com forceFallbackAdapter para validar pipelines.

## Limites e trade-offs
A preferência não é garantia: o navegador pode ignorá-la quando existe uma só GPU ou por política interna. O fallback de software é lento e serve a diagnóstico, não a produção. Dentro de um worker o ponto de entrada é WorkerNavigator.gpu, com as mesmas regras, e o acesso exige contexto seguro (HTTPS).

## Como verificar
Registre as opções enviadas e leia as informações do adaptador retornado para confirmar a GPU escolhida. Compare fps medido entre preferências na mesma máquina. Verifique o caminho nulo em ambiente sem WebGPU: a página deve continuar utilizável com aviso visível.

## Conexões
- [[webgpu-devicelost-camada-recuperacao]] — WebGPU: tratar device lost como fronteira de recuperação.

## Fontes
- [MDN — GPU: requestAdapter()](https://developer.mozilla.org/en-US/docs/Web/API/GPU/requestAdapter) — documenta powerPreference, forceFallbackAdapter e o retorno nulo Consulta: 2026-10-04.
- [W3C — WebGPU (especificação)](https://www.w3.org/TR/webgpu/) — define o modelo adaptador/dispositivo e o requisito de contexto seguro Consulta: 2026-10-04.
