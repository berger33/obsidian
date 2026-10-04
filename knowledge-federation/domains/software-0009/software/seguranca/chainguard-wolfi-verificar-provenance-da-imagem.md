---
id: software.seguranca.tranche20.001964
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

# Chainguard Images e Wolfi: Verificar provenance da imagem

## Em uma frase
**Chainguard Images e Wolfi — Verificar provenance da imagem:** Provenance descreve como imagem foi produzida e pode ser consultada no catálogo do artefato.

## Por que importa
O recorte de **verificar provenance da imagem** ajuda a reduzir componentes desnecessários em imagens e facilitar atualização e verificação de supply chain. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificar provenance da imagem**, imagem é escolhida por propósito, puxada por tag ou digest e inspecionada por SBOM, provenance e compatibilidade de runtime. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Recupere provenance para digest e compare produtor e processo com política de consumo. Teste em staging autorizado.

## Limites e trade-offs
Existência da attestation não comprova que os claims satisfazem modelo de ameaça da equipe. Exceções exigem responsável e prazo.

## Como verificar
Verifique assinatura, source e identidade do builder usando ferramenta compatível. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[chainguard-wolfi-preferir-digest-para-deploy]] — Complementa o tópico com chainguard images e wolfi: preferir digest para deploy.

## Fontes
- [Chainguard Images — Wolfi base](https://images.chainguard.dev/directory/image/wolfi-base/overview) — catálogo oficial da imagem Wolfi base, finalidade e pacotes; consultado em 2026-10-04.
- [Chainguard Images — Provenance](https://images.chainguard.dev/directory/image/wolfi-base/provenance) — página oficial de provenance, assinaturas e evidências da imagem Wolfi base; consultado em 2026-10-04.
