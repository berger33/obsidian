---
id: software.seguranca.tranche04.000375
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

# OpenSSF GUAC: Rastreamento de Vulnerabilidades Transitivas (`guacone query vuln`) e Filtragem por VEX (`OpenVEX` / `CSAF`)

## Em uma frase
O comando `guacone query vuln` percorre recursivamente as arestas `IsDependency` do grafo a partir de uma imagem OCI ou aplicação raiz até encontrar quaisquer pacotes transitivos ligados a nós `CertifyVuln`, confrontando-os com declarações `CertifyVEXStatement`.

## Por que importa
Permite descobrir em segundos o caminho completo de dependência (`App -> Lib A -> Lib B -> Lib C vulnerável`) e suprimir automaticamente alertas cujo status VEX seja `not_affected` ou `fixed` para aquele produto.

## Como funciona
Ao ingerir um documento OpenVEX ou CSAF 2.0 assinado pela equipe de segurança ou pelo fornecedor upstream, o GUAC cria um predicado `CertifyVEXStatement` ligando simultaneamente o `Package`/`Artifact` do produto e a `Vulnerability` (CVE/GHSA) com o status (`not_affected`, `affected`, `fixed`, `under_investigation`) e a justificativa (`component_not_present`, `vulnerable_code_not_in_execute_path`).

## Exemplo
```bash
# Consultar caminhos de vulnerabilidades transitivas para uma imagem OCI até profundidade 10
guacone query vuln pkg:oci/prod-payments-service@sha256:4a9c... \
  --search-depth 10 --gql-addr http://guac-vuln.internal.corp:8080/query
```

## Limites e trade-offs
Definir `--search-depth` muito raso (ex.: `1` ou `2`) em ecossistemas com árvores profundas como Node.js (`npm`) ou Java (`Maven`) omitirá vulnerabilidades localizadas no 5º ou 6º nível de dependência transitiva.

## Como verificar
Ingira um documento OpenVEX marcando um CVE como `not_affected` e verifique na consulta GraphQL `CertifyVEXStatement` que a justificativa está vinculada ao pacote e ao CVE.

## Conexões
- [[guacsec-certificadores-automaticos-osv-deps-dev-scorecard-clearlydefined]] — Veja também: OpenSSF GUAC: Enriquecimento Contínuo com Certifiers (`osv`, `deps_dev`, `scorecard` e `clearlydefined`).
- [[guacsec-backends-armazenamento-keyvalue-ent-postgresql-redis-tikv]] — Veja também: OpenSSF GUAC: Backends de Persistência (`keyvalue` In-Memory vs `ent` com PostgreSQL).
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[guacsec-ontologia-grafo-nouns-package-artifact-source-predicates]] — Referência cruzada direta com guacsec-ontologia-grafo-nouns-package-artifact-source-predicates.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
