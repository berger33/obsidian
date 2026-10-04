---
id: software.seguranca.tranche03.000255
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

# in-toto Attestation Framework (`v1`): arquitetura das camadas `Envelope (DSSE)`, `Statement`, `subject` e `predicate`

## Em uma frase
Conforme documentado no repositório oficial `in-toto/attestation` (`README.md` e `spec/v1/`), o **in-toto Attestation Framework** define o formato padrão da indústria para emitir afirmações verificáveis (*attestations*) sobre como qualquer artefato de software foi produzido, estruturado em três camadas desacopladas: **1. Envelope (DSSE — *Dead Simple Signing Envelope*)**, **2. Statement (`_type: https://in-toto.io/Statement/v1`)** e **3. Predicate (`predicateType` + `predicate`)**.

## Por que importa
Antes do in-toto Attestation Framework, cada ferramenta de CI/CD, scanner ou gerador de SBOM inventava seu próprio envelope de assinatura incompatível; hoje, **SLSA**, **Sigstore Cosign**, **GitHub Artifact Attestations**, **Docker Buildx**, **Tekton Chains** e **Witness** usam todos o Statement v1 do in-toto!

## Como funciona
No `Statement` v1: o array **`subject`** identifica os artefatos aos quais o atestado se refere (por nome e `digest` criptográfico `sha256`), o campo **`predicateType`** declara a URI do schema da afirmação e o objeto **`predicate`** contém os metadados estruturados daquela evidência.

## Exemplo
```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    {
      "name": "ghcr.io/minha-org/checkout-api",
      "digest": {
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      }
    }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "https://actions.github.com/WorkflowBuilds@v1"
    }
  }
}
```

## Limites e trade-offs
Nunca confie apenas no nome (`subject[].name`) de um atestado in-toto: a verificação criptográfica deve sempre comparar o hash **`subject[].digest.sha256`** com o hash real do binário ou imagem de container que está prestes a ser executado!

## Como verificar
Extraia o payload de um atestado DSSE (`jq -r .payload attestation.intoto.jsonl | base64 -d | jq .`) e valide os campos `_type`, `subject` e `predicateType`.

## Conexões
- [[intoto-inspections-verificacao-final-in-toto-verify-untar]] — Veja também: in-toto `Inspections` e `in-toto-verify`: desempacotamento e validação criptográfica no momento da instalação pelo cliente.
- [[intoto-predicates-catalogo-slsa-provenance-cyclonedx-spdx-vuln-vsa]] — Veja também: in-toto Attestation Predicates: catálogo oficial de predicados (`SLSA Provenance`, `SPDX`/`CycloneDX SBOM`, `Vuln Scan`, `VSA` e `Test Result`).

## Fontes
- [CNCF in-toto GitHub — README.md (Supply Chain Layout, Functionaries, Artifact Rules, in-toto-run, in-toto-record, Inspections & in-toto-verify)](https://raw.githubusercontent.com/in-toto/attestation/main/README.md) — README oficial do in-toto/in-toto documentando a estrutura de layouts, regras de encadeamento de materials/products, geração de links e verificação final; consultado em 2026-10-03.
- [CNCF in-toto Attestation Framework GitHub — README.md (Statement v1 Specification, Vetted Predicates, DSSE, SLSA Intersection & Language Bindings)](https://raw.githubusercontent.com/in-toto/in-toto/develop/README.md) — README oficial do in-toto/attestation descrevendo a especificação do Attestation Framework v1, catálogo de predicados, definições Protobuf e interseção com SLSA; consultado em 2026-10-03.
- [CNCF in-toto — Official GitHub Repository](https://github.com/in-toto/attestation) — Repositório oficial Apache-2.0 do CNCF in-toto; consultado em 2026-10-03.
