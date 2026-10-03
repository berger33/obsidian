---
id: software.seguranca.tranche04.000374
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

# OpenSSF GUAC: Enriquecimento Contínuo com Certifiers (`osv`, `deps_dev`, `scorecard` e `clearlydefined`)

## Em uma frase
Além dos coletores de arquivos, o GUAC executa **Certifiers** contínuos em background que percorrem os pacotes e repositórios presentes no grafo e buscam automaticamente inteligência externa nas APIs do `OSV.dev`, Google `deps.dev`, `OpenSSF Scorecard` e `ClearlyDefined`.

## Por que importa
Mantém a postura de risco atualizada: mesmo que uma imagem OCI tenha sido compilada há três meses, assim que um novo CVE/GHSA é publicado no OSV.dev hoje, o certificador do GUAC anexa o nó `CertifyVuln` ao pacote correspondente no grafo.

## Como funciona
O daemon `guaccertify` (ou `guacone certify`) consulta os nós `Package` e `Source` registrados via `collectsub` (Subscriber Service), interroga em lote a API do OSV para vulnerabilidades, o `deps.dev` para localização de código-fonte e scorecards, e o `ClearlyDefined` para metadados de licenciamento (`CertifyLegal`), inserindo as novas arestas via Assembler.

## Exemplo
```bash
# Executar o certificador OSV em modo one-shot para enriquecer todos os pacotes do grafo com CVEs/GHSAs
guacone certify osv --gql-addr http://guac-certifier.internal.corp:8080/query

# Enriquecer pacotes com metadados de repositório e OpenSSF Scorecard via deps.dev
guacone certify depsdev --gql-addr http://guac-certifier.internal.corp:8080/query
```

## Limites e trade-offs
Em ambientes corporativos *air-gapped* sem saída para `api.osv.dev` ou `api.deps.dev`, os certificadores online falharão; nesses cenários, ingira espelhos locais de bancos OSV/CSAF usando `guacone collect files`.

## Como verificar
Após rodar `guacone certify osv`, execute `guacone query known package <purl>` e confirme o aparecimento dos nós `certifyVuln` vinculados às versões afetadas.

## Conexões
- [[guacsec-ingestao-sboms-spdx-cyclonedx-dsse-intoto-slsa]] — Veja também: OpenSSF GUAC: Ingestão de Documentos SPDX, CycloneDX, Envelopes DSSE, in-toto ITE-6 e Proveniência SLSA.
- [[guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex]] — Veja também: OpenSSF GUAC: Rastreamento de Vulnerabilidades Transitivas (`guacone query vuln`) e Filtragem por VEX (`OpenVEX` / `CSAF`).
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[guacsec-governanca-politicas-certifybad-certifygood-pointofcontact]] — Referência cruzada direta com guacsec-governanca-politicas-certifybad-certifygood-pointofcontact.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
