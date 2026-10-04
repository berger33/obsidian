---
id: software.seguranca.tranche03.000260
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/in-toto/attestation/main/README.md", "https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md", "https://github.com/in-toto/attestation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# in-toto + `SLSA`, `Witness` e `Sigstore`: implementação prática de cadeias verificáveis do commit ao Kubernetes

## Em uma frase
Conforme destacado no README de `in-toto/attestation` (*"how the two frameworks intersect and how you can use in-toto for SLSA"*), o **in-toto** fornece a camada de formato e verificação (`Statement`, `Predicate`, `Layout`), enquanto o **SLSA (*Supply-chain Levels for Software Artifacts*)** define os requisitos graduais de maturidade (SLSA Build L1, L2, L3) e ferramentas como **TestifySec Witness** (`in-toto/witness`), **Tekton Chains** e **GitHub Attestations** automatizam a emissão dos atestados in-toto no CI/CD!

## Por que importa
Entender como in-toto, SLSA e Sigstore se conectam evita sobreposição de ferramentas: **in-toto** é o formato do atestado e da política de cadeia; **SLSA** é o vocabulário de proveniência (`https://slsa.dev/provenance/v1`) e níveis de segurança; e **Sigstore (Fulcio + Rekor + Cosign)** provê a assinatura sem chave estática (*keyless OIDC*) e o log de transparência!

## Como funciona
No deploy para o Kubernetes, controladores de admissão (como Kyverno, Gatekeeper ou Sigstore Policy Controller) verificam o envelope DSSE in-toto assinado via Sigstore antes de permitir a criação de qualquer Pod.

## Exemplo
```yaml
# Exemplo conceitual de política exigindo Attestation in-toto com predicado SLSA Provenance v1 na admissão:
predicateType: "https://slsa.dev/provenance/v1"
issuer: "https://token.actions.githubusercontent.com"
subjectRegex: "^https://github.com/minha-org/meu-repo/.github/workflows/release.yml@refs/tags/v.*"
```

## Limites e trade-offs
Combine layouts in-toto (ou políticas Witness/Kyverno) com identidades OIDC efêmeras da sua pipeline de CI para eliminar a necessidade de guardar chaves privadas de *functionaries* de longa duração nos runners de build.

## Como verificar
Verifique de ponta a ponta um artefato gerado no CI confirmando a assinatura Sigstore e o conteúdo do Statement in-toto v1.

## Conexões
- [[intoto-bindings-go-python-rust-java-protobuf-validacao-programatica]] — Veja também: in-toto SDKs e Protobuf Bindings (`in-toto-golang`, `in-toto-rs`, `Python`, `Java`): geração e validação de atestados em código.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/attestation) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
