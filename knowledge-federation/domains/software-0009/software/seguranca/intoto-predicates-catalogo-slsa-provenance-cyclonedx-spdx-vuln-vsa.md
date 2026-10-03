---
id: software.seguranca.tranche03.000256
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

# in-toto Attestation Predicates: catálogo oficial de predicados (`SLSA Provenance`, `SPDX`/`CycloneDX SBOM`, `Vuln Scan`, `VSA` e `Test Result`)

## Em uma frase
Conforme destacado em `in-toto/attestation` (*"We also provide a set of attestation predicates, which are metadata formats vetted by our maintainers"*), o framework mantém um catálogo de **`predicateType` padronizados** que cobrem todo o ciclo de vida de DevSecOps.

## Por que importa
Com um único formato de `Statement`, diferentes ferramentas anexam predicados especializados ao mesmo digest de imagem: o construtor CI anexa a proveniência **SLSA (`https://slsa.dev/provenance/v1`)**, o gerador de SBOM anexa **`https://cyclonedx.org/bom`** ou **`https://spdx.dev/Document`**, o scanner anexa **`https://in-toto.io/attestation/vulns/v0.2`**, o executor de testes anexa **`https://in-toto.io/attestation/test-result/v0.1`** e o verificador emite um **SLSA Verification Summary Attestation (`https://slsa.dev/verification_summary/v1`)**!

## Como funciona
Isso permite que o controlador de admissão do Kubernetes (Kyverno / Sigstore Policy Controller) exija, em uma única política, tanto um predicado de build SLSA quanto um predicado de scan de vulnerabilidades recente para o mesmo digest SHA-256.

## Exemplo
```bash
# Anexando um predicado de SBOM CycloneDX como uma Attestation in-toto assinada a uma imagem de container com Cosign:
cosign attest --yes \
  --predicate ./sbom.cdx.json \
  --type cyclonedx \
  ghcr.io/minha-org/checkout-api@sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Limites e trade-offs
Sempre que possível, utilize um `predicateType` oficial já revisado no repositório `in-toto/attestation/tree/main/spec/predicates` em vez de criar URIs proprietárias, garantindo interoperabilidade imediata com verificadores do ecossistema.

## Como verificar
Verifique um predicado anexado com `cosign verify-attestation --type slsaprovenance ...`.

## Conexões
- [[intoto-attestation-framework-v1-statement-subject-predicate-dsse]] — Veja também: in-toto Attestation Framework (`v1`): arquitetura das camadas `Envelope (DSSE)`, `Statement`, `subject` e `predicate`.
- [[intoto-dsse-dead-simple-signing-envelope-pae-prevencao-ambiguidade]] — Veja também: in-toto Envelope de Assinatura `DSSE` (*Dead Simple Signing Envelope*) e `PAE`: proteção contra ataques de confusão de parser e tipo.

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/attestation) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
