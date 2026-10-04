---
id: software.seguranca.tranche17.001639
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

# Sigstore Cosign: Assinatura de blobs e bundles

## Em uma frase
**Sigstore Cosign — Assinatura de blobs e bundles:** Artefatos que não são imagens podem ser assinados e verificados com dados de assinatura e certificado preservados em bundle.

## Por que importa
O recorte de **assinatura de blobs e bundles** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **assinatura de blobs e bundles**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Assine um arquivo de release de teste e distribua o blob junto do bundle de verificação. Teste em staging autorizado.

## Limites e trade-offs
Se blob e bundle forem substituídos juntos sem um canal independente de confiança, a validação perde valor. Exceções exigem responsável e prazo.

## Como verificar
Valide hash do arquivo e identidade, usando a identidade esperada fora do pacote distribuído. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-politica-de-confianca-no-deploy]] — Complementa o tópico com sigstore cosign: política de confiança no deploy.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
