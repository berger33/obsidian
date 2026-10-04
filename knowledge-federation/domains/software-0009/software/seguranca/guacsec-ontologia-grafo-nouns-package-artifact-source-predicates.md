---
id: software.seguranca.tranche04.000372
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/guacsec/guac/main/README.md", "https://docs.guac.sh/guac/", "https://github.com/guacsec/guac/blob/main/use-cases.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF GUAC: Ontologia do Grafo — Substantivos (`Package`, `Artifact`, `Source`, `Builder`) e Predicados (`IsDependency`, `HasSLSA`, `CertifyVEX`)

## Em uma frase
O modelo de dados do GUAC separa estritamente **Nouns** (substantivos/entidades da cadeia de suprimentos: `Package`, `Artifact`, `Source`, `Builder`, `Vulnerability`, `License`) de **Predicates** (arestas semânticas baseadas em evidências que conectam esses nós).

## Por que importa
Impede a confusão comum entre o identificador lógico de um pacote (`pkg:oci/debian@sha256:...` via PURL), o artefato binário concreto identificado por digest criptográfico (`sha256:...`) e o repositório de código-fonte (`git+https://github.com/...`).

## Como funciona
Os predicados registram afirmações auditáveis: `IsDependency` (declarado por um SBOM), `IsOccurrence` (liga um `Package` ou `Source` a um `Artifact` binário por hash), `HasSourceAt` (liga `Package` ao `Source`), `HasSLSA` (liga `Artifact` ao `Builder` e materiais de build via proveniência SLSA), `CertifyVuln` (liga `Package` a `Vulnerability`), `CertifyVEXStatement` (declara se a vulnerabilidade é explorável ou `not_affected`) e `CertifyScorecard`.

## Exemplo
```graphql
query InspectPackageRelationships($purl: String!) {
  packages(pkgSpec: { purl: $purl }) {
    type
    namespaces {
      names {
        name
        versions { version }
      }
    }
  }
}
```

## Limites e trade-offs
Quando documentos SBOM omitirem identificadores padronizados (PURL ou hashes SHA-256), o GUAC precisa recorrer a heurísticas de correspondência de nomes, o que pode gerar nós órfãos se os geradores de SBOM não seguirem a especificação PURL.

## Como verificar
Consulte a API GraphQL filtrando por `IsOccurrence` e `HasSourceAt` para confirmar que um pacote PURL está conectado tanto ao seu digest `Artifact` quanto ao seu repositório `Source`.

## Conexões
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Veja também: OpenSSF GUAC: Arquitetura do Grafo de Composição de Artefatos (Collectors, Ingestor, Assembler e GraphQL).
- [[guacsec-ingestao-sboms-spdx-cyclonedx-dsse-intoto-slsa]] — Veja também: OpenSSF GUAC: Ingestão de Documentos SPDX, CycloneDX, Envelopes DSSE, in-toto ITE-6 e Proveniência SLSA.
- [[guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex]] — Referência cruzada direta com guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
