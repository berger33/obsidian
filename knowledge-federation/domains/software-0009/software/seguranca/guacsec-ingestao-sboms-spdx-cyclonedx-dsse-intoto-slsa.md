---
id: software.seguranca.tranche04.000373
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

# OpenSSF GUAC: Ingestão de Documentos SPDX, CycloneDX, Envelopes DSSE, in-toto ITE-6 e Proveniência SLSA

## Em uma frase
O pipeline de ingestão do GUAC (`pkg/ingestor`) analisa nativamente SBOMs nos formatos SPDX (JSON/tag-value) e CycloneDX, declarações VEX (CSAF 2.0 e OpenVEX) e envelopes assinados DSSE contendo atestações in-toto v1 / SLSA Provenance.

## Por que importa
Garante que a árvore de dependências declarada no SBOM e os materiais exatos compilados pelo runner de CI/CD (registrados na proveniência SLSA) convergem para os mesmos nós `Artifact` e `Package` no grafo.

## Como funciona
Quando um envelope DSSE é coletado, o parser valida a estrutura do envelope, extrai o `Statement` in-toto (`_type`, `subject`, `predicateType`, `predicate`), cria nós `Artifact` para cada digest listado em `subject` e `materials`, e monta a aresta `HasSLSA` apontando para o nó `Builder` correspondente.

## Exemplo
```bash
# Ingerir um SBOM CycloneDX e uma atestação SLSA Provenance DSSE para o grafo GUAC
guacone collect files --gql-addr http://guac-ingestor.internal.corp:8080/query ./app-sbom.cdx.json
guacone collect files --gql-addr http://guac-ingestor.internal.corp:8080/query ./app-provenance.intoto.jsonl
```

## Limites e trade-offs
Para que o nó do SBOM e o nó da atestação SLSA se fundam automaticamente no mesmo ponto do grafo, o digest SHA-256 do `subject` na atestação SLSA deve corresponder ao hash do componente raiz ou imagem OCI descrito no SBOM.

## Como verificar
Execute `guacone query known artifact sha256:<digest-da-imagem>` e confirme que a saída exibe simultaneamente os predicados `hasSBOM` e `hasSLSA` para o mesmo artefato.

## Conexões
- [[guacsec-ontologia-grafo-nouns-package-artifact-source-predicates]] — Veja também: OpenSSF GUAC: Ontologia do Grafo — Substantivos (`Package`, `Artifact`, `Source`, `Builder`) e Predicados (`IsDependency`, `HasSLSA`, `CertifyVEX`).
- [[guacsec-certificadores-automaticos-osv-deps-dev-scorecard-clearlydefined]] — Veja também: OpenSSF GUAC: Enriquecimento Contínuo com Certifiers (`osv`, `deps_dev`, `scorecard` e `clearlydefined`).
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[intoto-attestation-framework-v1-statement-subject-predicate-dsse]] — Referência cruzada direta com intoto-attestation-framework-v1-statement-subject-predicate-dsse.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
