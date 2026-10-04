---
id: software.seguranca.tranche17.001632
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

# Sigstore Cosign: Assinatura keyless com OIDC

## Em uma frase
**Sigstore Cosign — Assinatura keyless com OIDC:** O fluxo keyless usa uma identidade autenticada por OIDC e evidencia o emissor e a identidade no certificado efêmero.

## Por que importa
O recorte de **assinatura keyless com oidc** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **assinatura keyless com oidc**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em um pipeline de teste, assine usando o provedor OIDC configurado e capture identidade e issuer esperados. Teste em staging autorizado.

## Limites e trade-offs
Confiança em qualquer identidade do mesmo provedor é ampla demais; a política deve fixar os valores esperados. Exceções exigem responsável e prazo.

## Como verificar
Rode verificação negativa com identidade e issuer incorretos e confirme que a assinatura é rejeitada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-verificacao-por-identidade-e-issuer]] — Complementa o tópico com sigstore cosign: verificação por identidade e issuer.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
