---
id: software.seguranca.tranche17.001659
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
fontes: ["https://pnpm.io/cli/audit#signatures", "https://pnpm.io/settings/dependency-resolution#registries"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `pnpm audit signatures`: verificar assinaturas ECDSA do registry instalado

## Em uma frase
O comando separado `pnpm audit signatures` compara assinaturas ECDSA de pacotes instalados com chaves públicas publicadas pelos registries configurados.

## Por que importa
Auditar advisories não valida que bytes baixados correspondem a uma assinatura do registry; integridade de distribuição requer checagem separada.

## Como funciona
Execute após instalação, observe registries sem chaves publicadas e trate pacote sem assinatura ou assinatura inválida conforme política do registry.

## Exemplo
Uma pipeline pode guardar saída JSON da verificação de assinatura ao lado do lockfile, SBOM e digest do artefato construído.

```text
pnpm audit signatures --json
```

## Limites e trade-offs
Registries sem convenção de chaves podem ser ignorados; uma assinatura válida identifica integridade segundo chave, mas não prova que o pacote seja benigno.

## Como verificar
Confirme quais registries foram verificados, revise resultados por pacote e verifique a chave publicada no endpoint documentado pelo registry.

## Conexões
- [[pnpm-audit-registry-errors-nao-mascarar-falha]] — `--ignore-registry-errors`: não confundir indisponibilidade do serviço com resultado limpo.
- [[pnpm-audit-minimum-release-age-correcoes-seguranca]] — `minimumReleaseAge` e correções no pnpm: equilibrar atraso contra janela de ataque.

## Fontes
- [pnpm — `audit signatures`](https://pnpm.io/cli/audit#signatures) — verificação ECDSA de pacotes instalados e chaves publicadas; consultado em 2026-10-04.
- [pnpm — Registry Settings](https://pnpm.io/settings/dependency-resolution#registries) — registries configurados que fornecem metadata/chaves de pacote; consultado em 2026-10-04.
