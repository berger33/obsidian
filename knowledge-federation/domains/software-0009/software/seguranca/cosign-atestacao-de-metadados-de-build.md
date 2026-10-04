---
id: software.seguranca.tranche17.001636
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

# Sigstore Cosign: Atestação de metadados de build

## Em uma frase
**Sigstore Cosign — Atestação de metadados de build:** Atestações carregam uma predicate estruturada associada ao artefato e podem expressar evidências além da assinatura simples.

## Por que importa
O recorte de **atestação de metadados de build** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **atestação de metadados de build**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Anexe uma predicate de build de laboratório ao digest produzido por CI e registre seu tipo e origem. Teste em staging autorizado.

## Limites e trade-offs
O formato não valida a veracidade dos campos por si só; a procedência do emissor continua central. Exceções exigem responsável e prazo.

## Como verificar
Valide tipo, digest, signer e campos obrigatórios com uma política explícita. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-verificacao-de-atestacao-por-politica]] — Complementa o tópico com sigstore cosign: verificação de atestação por política.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
