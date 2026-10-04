---
id: software.seguranca.tranche17.001649
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#audit-signatures", "https://docs.npmjs.com/generating-provenance-statements"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `npm audit signatures`: verificação separada de assinatura e proveniência do registry

## Em uma frase
O comando `npm audit signatures` verifica assinaturas de registry e proveniência de pacotes baixados em registries compatíveis; não é a mesma consulta de advisories.

## Por que importa
Vulnerabilidade conhecida e integridade/proveniência são perguntas diferentes, exigindo controles separados no ciclo de consumo de pacotes.

## Como funciona
Execute verificação de assinatura após instalação, atualize o CLI para suporte atual de attestations e arquive o bundle quando a investigação exigir evidência.

## Exemplo
Em uma release, rode `npm audit signatures` sobre as dependências instaladas e trate falha criptográfica como evento separado de CVE.

```text
npm audit signatures --json --include-attestations
```

## Limites e trade-offs
A verificação depende de registry que publique chaves e attestations conforme as convenções suportadas; não garante que o código assinado seja benigno.

## Como verificar
Confira o resultado por pacote, a identidade da chave e a evidência Sigstore retornada em JSON quando habilitada.

## Conexões
- [[npm-audit-metavulnerabilidades-cadeia-transitiva]] — Metavulnerabilidades no npm: quando uma dependência pai só resolve para versão vulnerável.
- [[npm-audit-exit-code-ci-severidade-politica]] — Códigos de saída do `npm audit`: transformar achados em política CI explícita.

## Fontes
- [npm CLI v11 — Audit Signatures](https://docs.npmjs.com/cli/v11/commands/npm-audit#audit-signatures) — verificação de assinaturas do registry e proveniência Sigstore; consultado em 2026-10-04.
- [npm — Generating provenance statements](https://docs.npmjs.com/generating-provenance-statements) — attestations de proveniência e limites do que demonstram; consultado em 2026-10-04.
