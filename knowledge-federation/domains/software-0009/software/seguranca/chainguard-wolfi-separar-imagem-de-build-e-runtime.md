---
id: software.seguranca.tranche20.001968
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://images.chainguard.dev/directory/image/wolfi-base/overview", "https://images.chainguard.dev/directory/image/wolfi-base/provenance"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Chainguard Images e Wolfi: Separar imagem de build e runtime

## Em uma frase
**Chainguard Images e Wolfi — Separar imagem de build e runtime:** Imagem de build pode conter compiladores e ferramentas que não são necessárias na execução.

## Por que importa
O recorte de **separar imagem de build e runtime** ajuda a reduzir componentes desnecessários em imagens e facilitar atualização e verificação de supply chain. A equipe registra risco, evidência e responsável.

## Como funciona
Para **separar imagem de build e runtime**, imagem é escolhida por propósito, puxada por tag ou digest e inspecionada por SBOM, provenance e compatibilidade de runtime. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use multi-stage build e copie somente binário e bibliotecas necessárias para imagem final. Teste em staging autorizado.

## Limites e trade-offs
Biblioteca dinâmica omitida pode falhar somente em execução. Exceções exigem responsável e prazo.

## Como verificar
Execute imagem final em ambiente limpo sem ferramentas disponíveis no builder. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[chainguard-wolfi-usar-variante-de-debug-sem-expor-producao]] — Complementa o tópico com chainguard images e wolfi: usar variante de debug sem expor produção.

## Fontes
- [Chainguard Images — Wolfi base](https://images.chainguard.dev/directory/image/wolfi-base/overview) — catálogo oficial da imagem Wolfi base, finalidade e pacotes; consultado em 2026-10-04.
- [Chainguard Images — Provenance](https://images.chainguard.dev/directory/image/wolfi-base/provenance) — página oficial de provenance, assinaturas e evidências da imagem Wolfi base; consultado em 2026-10-04.
