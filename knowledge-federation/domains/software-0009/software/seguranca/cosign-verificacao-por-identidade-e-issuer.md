---
id: software.seguranca.tranche17.001633
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

# Sigstore Cosign: Verificação por identidade e issuer

## Em uma frase
**Sigstore Cosign — Verificação por identidade e issuer:** A verificação pode exigir que certificado corresponda a identidade e emissor previamente autorizados.

## Por que importa
O recorte de **verificação por identidade e issuer** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificação por identidade e issuer**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina identidade do workflow e issuer permitidos na política de implantação antes de consumir uma imagem. Teste em staging autorizado.

## Limites e trade-offs
Verificar apenas existência de assinatura sem validar identidade pode aceitar artefato assinado por origem não autorizada. Exceções exigem responsável e prazo.

## Como verificar
Teste tanto a identidade aprovada quanto uma assinatura válida de identidade diferente. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-verificacao-de-claim-de-digest]] — Complementa o tópico com sigstore cosign: verificação de claim de digest.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
