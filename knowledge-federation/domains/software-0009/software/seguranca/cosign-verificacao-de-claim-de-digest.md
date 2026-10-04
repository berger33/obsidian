---
id: software.seguranca.tranche17.001634
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

# Sigstore Cosign: Verificação de claim de digest

## Em uma frase
**Sigstore Cosign — Verificação de claim de digest:** A verificação de imagem checa que o digest declarado no payload corresponde ao artefato avaliado.

## Por que importa
O recorte de **verificação de claim de digest** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificação de claim de digest**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Confirme a imagem exata por digest e mantenha verificação de claims habilitada no caminho de release. Teste em staging autorizado.

## Limites e trade-offs
Desabilitar checagem de claims remove uma ligação relevante entre assinatura e conteúdo, mesmo se a assinatura criptográfica existir. Exceções exigem responsável e prazo.

## Como verificar
Use um digest alterado em teste e assegure que a verificação falhe antes do deploy. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-armazenamento-de-assinatura-como-oci-referrer]] — Complementa o tópico com sigstore cosign: armazenamento de assinatura como oci referrer.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
