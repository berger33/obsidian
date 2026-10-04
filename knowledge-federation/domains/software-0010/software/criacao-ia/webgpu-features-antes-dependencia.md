---
id: software.criacao_ia.tranche04.000304
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
fontes: ["https://www.w3.org/TR/webgpu/#features", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: features são opcionais e viram dependência de plataforma

## Em uma frase
Recursos nomeados, como timestamps e subgrupos, só existem se a aplicação os exigir no pedido de dispositivo e o adaptador os suportar.

## Por que importa
Cada feature habilita comportamento que não está nos piores casos da Web: sem pedir 'timestamp-query', qualquer QuerySet desse tipo falha; sem 'texture-compression-bc', formatos bloqueados ficam indisponíveis. Tratar feature como garantida produz bugs que aparecem apenas em parte do parque de hardware.

## Como funciona
Antes de requestDevice, teste adapter.features.has(nome) e inclua em requiredFeatures apenas o conjunto que o código realmente usa; decida o que fazer quando faltar (degradar, avisar ou recusar o dispositivo). Depois da criação, a fonte de verdade é device.features, não a memória do pedido. Features não substituem limites: um recurso pode estar presente com limites pequenos, e vice-versa.

## Exemplo
O painel de profiling do motor usa timestamps; se 'timestamp-query' não estiver em device.features, o painel desenha barras relativas medidas por CPU e exibe um aviso 'precisão limitada por plataforma' em vez de lançar exceção.

## Limites e trade-offs
Suporte por navegador e driver muda entre versões, então cada feature solicitada é uma decisão de compatibilidade, não um custo zero. Haver com lista vazia não é falha do motor: pode ser hardware real, e o produto precisa responder com degradação definida.

## Como verificar
Imprima device.features na inicialização em três GPUs diferentes e confirme as diferenças. Peça uma feature inexistente via URL de depuração e verifique se a criação do dispositivo falha com mensagem clara. Teste o caminho degradado com a feature removida da lista de requisitos.

## Conexões
- [[webgpu-requiredlimits-calcular-custo]] — WebGPU: pedir limites maiores e calcular antes do limite suportado.
- [[webgpu-leitura-gpu-staging-buffer]] — WebGPU: ler dados da GPU exige buffer staging com MAP_READ.

## Fontes
- [W3C — WebGPU: seção Features](https://www.w3.org/TR/webgpu/#features) — lista as features normativas e a regra de solicitação por dispositivo Consulta: 2026-10-04.
- [W3C — WebGPU (especificação)](https://www.w3.org/TR/webgpu/) — texto geral que define a negociação de features entre adaptador e dispositivo Consulta: 2026-10-04.
