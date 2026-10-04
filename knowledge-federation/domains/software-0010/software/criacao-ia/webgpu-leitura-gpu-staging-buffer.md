---
id: software.criacao_ia.tranche04.000305
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
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/GPUBuffer/getMappedRange", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: ler dados da GPU exige buffer staging com MAP_READ

## Em uma frase
Um buffer somente pode ser mapeado para leitura se o uso combinado for exatamente MAP_READ mais COPY_DST, o que força uma cópia intermediária.

## Por que importa
A restrição da especificação elimina ambiguidade de aliasing: nunca há CPU e GPU escrevendo e lendo o mesmo armazenamento simultaneamente. O padrão staging copia o resultado do binding (uniform, storage) para um buffer de troca, cuja leitura aguarda a GPU terminar a cópia.

## Como funciona
Crie o buffer de leitura com usage COPY_DST | MAP_READ, grave um copyBufferToBuffer do recurso de origem para ele no command encoder e submeta a fila. Só então chame mapAsync(GPUMapMode.READ), leia via getMappedRange e, ao terminar, chame unmap() — enquanto está mapeado, qualquer outro uso do buffer é inválido. Um buffer de escrita do CPU segue o par MAP_WRITE | COPY_SRC com cópia na direção oposta.

## Exemplo
Para validar um compute de partículas que escreve posições num storage buffer, copie 1024 bytes para um staging, mapAsync, compare os primeiros vetores com a simulação de referência e unmap antes de novo ciclo.

## Limites e trade-offs
mapAsync resolve de forma assíncrona e pode esperar trabalho arbitrário da fila; não chame dentro do passo síncrono de render e espere o resultado. Cópias de leitura bloqueiam reuso imediato do staging até o unmap. O caminho é lento comparado a manter estado na CPU; use para diagnóstico e pontos de verificação.

## Como verificar
Confirme que criar buffer com MAP_READ isolado é rejeitado pela validação (use um error scope para capturar o TypeError de descrição inválida). Depois leia um valor conhecido gravado via writeBuffer e copiado, e verifique que o resultado aparece só após a promise de mapAsync.

## Conexões
- [[webgpu-features-antes-dependencia]] — WebGPU: features são opcionais e viram dependência de plataforma.
- [[webgpu-mappedatcreation-dado-inicial]] — WebGPU: mappedAtCreation para dados iniciais sem cópia adicional.

## Fontes
- [MDN — GPUBuffer: getMappedRange()](https://developer.mozilla.org/en-US/docs/Web/API/GPUBuffer/getMappedRange) — documenta a janela mapeada e a necessidade de cópia para leitura de resultados Consulta: 2026-10-04.
- [W3C — WebGPU: GPUBuffer Usage](https://www.w3.org/TR/webgpu/) — tabelas de uso definem 'MAP_READ may only be combined with COPY_DST' e o par simétrico de escrita Consulta: 2026-10-04.
