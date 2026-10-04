---
id: software.seguranca.tranche17.001638
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://docs.sigstore.dev/cosign/overview/", "https://docs.sigstore.dev/cosign/verifying/verify/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sigstore Cosign: Chaves locais e KMS

## Em uma frase
**Sigstore Cosign — Chaves locais e KMS:** Cosign pode usar chaves locais ou referências a serviços de gerenciamento de chaves para separar segredo da pipeline.

## Por que importa
O recorte de **chaves locais e kms** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **chaves locais e kms**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em staging, assine um digest com chave de teste em KMS e configure verificação com material público apropriado. Teste em staging autorizado.

## Limites e trade-offs
Perda, rotação ou permissões excessivas de chave afetam confiança e disponibilidade do processo de release. Exceções exigem responsável e prazo.

## Como verificar
Verifique permissões mínimas, rotação, backup e recuperação antes de adotar uma chave de produção. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-assinatura-de-blobs-e-bundles]] — Complementa o tópico com sigstore cosign: assinatura de blobs e bundles.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
