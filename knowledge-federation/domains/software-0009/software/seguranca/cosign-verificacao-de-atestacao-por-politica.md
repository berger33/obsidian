---
id: software.seguranca.tranche17.001637
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

# Sigstore Cosign: Verificação de atestação por política

## Em uma frase
**Sigstore Cosign — Verificação de atestação por política:** Verificar atestação deve avaliar predicate e identidade do emissor, não apenas constatar que existe um objeto associado.

## Por que importa
O recorte de **verificação de atestação por política** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **verificação de atestação por política**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Crie uma imagem de teste sem campo de build exigido e confirme que a política de atestação a recusa. Teste em staging autorizado.

## Limites e trade-offs
Uma política permissiva pode aceitar predicates que não comprovam requisitos de build ou revisão. Exceções exigem responsável e prazo.

## Como verificar
Teste casos positivos e negativos e guarde a política versionada junto do relatório. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-chaves-locais-e-kms]] — Complementa o tópico com sigstore cosign: chaves locais e kms.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
