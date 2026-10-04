---
id: software.seguranca.tranche20.001967
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

# Chainguard Images e Wolfi: Migrar aplicando compatibilidade

## Em uma frase
**Chainguard Images e Wolfi — Migrar aplicando compatibilidade:** Migração para imagem nova requer verificar package manager, usuário, certificados e caminhos assumidos.

## Por que importa
O recorte de **migrar aplicando compatibilidade** ajuda a reduzir componentes desnecessários em imagens e facilitar atualização e verificação de supply chain. A equipe registra risco, evidência e responsável.

## Como funciona
Para **migrar aplicando compatibilidade**, imagem é escolhida por propósito, puxada por tag ou digest e inspecionada por SBOM, provenance e compatibilidade de runtime. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Teste entrypoint e usuário não-root de uma aplicação existente em ambiente isolado. Teste em staging autorizado.

## Limites e trade-offs
Diferenças de shell e pacote podem quebrar scripts instaladores ou debugging. Exceções exigem responsável e prazo.

## Como verificar
Compare ambiente anterior e novo com teste funcional, não apenas build bem-sucedido. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[chainguard-wolfi-separar-imagem-de-build-e-runtime]] — Complementa o tópico com chainguard images e wolfi: separar imagem de build e runtime.

## Fontes
- [Chainguard Images — Wolfi base](https://images.chainguard.dev/directory/image/wolfi-base/overview) — catálogo oficial da imagem Wolfi base, finalidade e pacotes; consultado em 2026-10-04.
- [Chainguard Images — Provenance](https://images.chainguard.dev/directory/image/wolfi-base/provenance) — página oficial de provenance, assinaturas e evidências da imagem Wolfi base; consultado em 2026-10-04.
