---
id: software.seguranca.tranche17.001631
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

# Sigstore Cosign: Assinatura de imagem por digest

## Em uma frase
**Sigstore Cosign — Assinatura de imagem por digest:** A assinatura fica vinculada ao conteúdo identificado pelo digest, em vez de depender somente de uma tag mutável.

## Por que importa
O recorte de **assinatura de imagem por digest** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **assinatura de imagem por digest**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Assine a imagem de release aprovada e verifique `registry.example/app@sha256:...` em ambiente de implantação controlado. Teste em staging autorizado.

## Limites e trade-offs
A assinatura não substitui a revisão do build nem determina se o digest veio de um pipeline confiável. Exceções exigem responsável e prazo.

## Como verificar
Compare digest publicado, payload assinado e digest implantado; qualquer divergência deve falhar fechado. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-assinatura-keyless-com-oidc]] — Complementa o tópico com sigstore cosign: assinatura keyless com oidc.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
