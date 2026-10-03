---
id: software.seguranca.tranche04.000379
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

# OpenSSF GUAC: Consultas Customizadas na API GraphQL, REST API e Exploração Visual no GUAC Visualizer

## Em uma frase
Além da CLI `guacone`, o GUAC expõe um endpoint GraphQL completo (porta `8080`), uma API REST complementar (porta `8081`) e o **GUAC Visualizer** (interface web que renderiza subgrafos interativos a partir dos IDs de caminho retornados pelas consultas).

## Por que importa
Permite que engenheiros de segurança e auditores naveguem visualmente pelas relações `hasSBOM`, `IsDependency`, `HasSLSA` e `certifyVuln`, ou construam integrações automatizadas em Go/Python para portais internos de desenvolvedor (Backstage).

## Como funciona
Quase todos os comandos de consulta do `guacone` (como `guacone query vuln` e `guacone query known`) imprimem ao final da tabela uma URL pronta do tipo `Visualizer url: http://localhost:3000/?path=20041,20040,...` que carrega imediatamente os nós exatos envolvidos no achado.

## Exemplo
```bash
# Consultar todas as informações conhecidas (fontes, vulnerabilidades, SLSA, licenças) de um pacote
guacone query known package pkg:golang/golang.org/x/net@v0.22.0 \
  --gql-addr http://guac-api.internal.corp:8080/query
```

## Limites e trade-offs
Não exponha a porta `8080` do `guacgql` sem autenticação e controle de acesso em redes compartilhadas, pois mutações GraphQL (`ingestPackage`, `ingestCertifyBad`, `ingestVEX`) permitem inserir ou alterar afirmações de confiança no grafo.

## Como verificar
Execute `guacone query known package` para um pacote ingerido e valide que os IDs de nós retornados nas tabelas `Package Name Nodes` e `Package Version Nodes` resolvem na API GraphQL.

## Conexões
- [[guacsec-governanca-politicas-certifybad-certifygood-pointofcontact]] — Veja também: OpenSSF GUAC: Governança Proativa da Cadeia de Suprimentos com `CertifyBad`, `CertifyGood` e `PointOfContact`.
- [[guacsec-ecossistema-trustify-gateways-admissao-ci-cd]] — Veja também: OpenSSF GUAC: Integração em Gates de Release CI/CD e Relação com o Ecossistema GUAC / Trustify.
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[guacsec-ontologia-grafo-nouns-package-artifact-source-predicates]] — Referência cruzada direta com guacsec-ontologia-grafo-nouns-package-artifact-source-predicates.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
