---
id: software.seguranca.tranche04.000371
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

# OpenSSF GUAC: Arquitetura do Grafo de Composição de Artefatos (Collectors, Ingestor, Assembler e GraphQL)

## Em uma frase
**GUAC** (*Graph for Understanding Artifact Composition*, projeto OpenSSF sob Apache-2.0) agrega metadados dispersos de segurança da cadeia de suprimentos de software (SBOMs SPDX/CycloneDX, atestações SLSA/in-toto, alertas OSV/CVE, OpenSSF Scorecard e documentos VEX) em um grafo de alta fidelidade consultável via GraphQL.

## Por que importa
Organizações que geram milhares de arquivos SBOM e atestações em cada build não conseguem responder rapidamente *"quais imagens em produção dependem transitivamente desta biblioteca vulnerável e não possuem VEX de mitigação?"* apenas lendo arquivos JSON isolados em buckets S3.

## Como funciona
A arquitetura do GUAC divide-se em quatro estágios: **Collectors** (buscam documentos de OCI registries, Git, S3, `deps.dev`, OSV e ClearlyDefined), **Ingestor / Parsers** (validam envelopes DSSE e extraem entidades normalizadas), **Assembler** (conecta nós de substantivos e predicados no backend) e a **API GraphQL** (que serve consultas para a CLI `guacone`, visualizadores e motores de política).

## Exemplo
```bash
# Ingerir um diretório local de SBOMs e atestações SLSA diretamente no grafo GUAC via CLI guacone
guacone collect files --gql-addr http://guac-collector.internal.corp:8080/query /var/artifacts/sboms-and-attestations/
```

## Limites e trade-offs
O GUAC ocupa a camada de agregação e síntese: ele não substitui geradores de SBOM (`syft`, `trivy`) nem verificadores de assinatura de admissão (`cosign`, `kyverno`), mas unifica a inteligência produzida por todos eles.

## Como verificar
Acesse o endpoint GraphQL `http://127.0.0.1:8080/query` e execute `guacone query known package pkg:golang/github.com/prometheus/client_golang@v1.19.0` para validar o grafo.

## Conexões
- [[guacsec-ontologia-grafo-nouns-package-artifact-source-predicates]] — Veja também: OpenSSF GUAC: Ontologia do Grafo — Substantivos (`Package`, `Artifact`, `Source`, `Builder`) e Predicados (`IsDependency`, `HasSLSA`, `CertifyVEX`).
- [[guacsec-ingestao-sboms-spdx-cyclonedx-dsse-intoto-slsa]] — Referência cruzada direta com guacsec-ingestao-sboms-spdx-cyclonedx-dsse-intoto-slsa.
- [[guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex]] — Referência cruzada direta com guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
