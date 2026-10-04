---
id: software.seguranca.tranche20.001962
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

# Chainguard Images e Wolfi: Escolher imagem pelo papel da aplicação

## Em uma frase
**Chainguard Images e Wolfi — Escolher imagem pelo papel da aplicação:** Catálogo de imagens oferece variantes orientadas a runtime, ferramentas ou base, com diferentes conjuntos de pacotes.

## Por que importa
O recorte de **escolher imagem pelo papel da aplicação** ajuda a reduzir componentes desnecessários em imagens e facilitar atualização e verificação de supply chain. A equipe registra risco, evidência e responsável.

## Como funciona
Para **escolher imagem pelo papel da aplicação**, imagem é escolhida por propósito, puxada por tag ou digest e inspecionada por SBOM, provenance e compatibilidade de runtime. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Selecione imagem de runtime para produção e mantenha ferramentas de build fora da camada final. Teste em staging autorizado.

## Limites e trade-offs
Imagem mínima pode não conter shell ou utilitários usados por health checks e scripts legados. Exceções exigem responsável e prazo.

## Como verificar
Execute testes funcionais e confirme processos e arquivos realmente exigidos. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[chainguard-wolfi-inspecionar-sbom-da-imagem]] — Complementa o tópico com chainguard images e wolfi: inspecionar sbom da imagem.

## Fontes
- [Chainguard Images — Wolfi base](https://images.chainguard.dev/directory/image/wolfi-base/overview) — catálogo oficial da imagem Wolfi base, finalidade e pacotes; consultado em 2026-10-04.
- [Chainguard Images — Provenance](https://images.chainguard.dev/directory/image/wolfi-base/provenance) — página oficial de provenance, assinaturas e evidências da imagem Wolfi base; consultado em 2026-10-04.
