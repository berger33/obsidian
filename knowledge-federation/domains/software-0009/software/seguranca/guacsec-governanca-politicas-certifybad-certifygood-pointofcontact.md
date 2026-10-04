---
id: software.seguranca.tranche04.000378
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

# OpenSSF GUAC: Governança Proativa da Cadeia de Suprimentos com `CertifyBad`, `CertifyGood` e `PointOfContact`

## Em uma frase
O GUAC fornece predicados de governança organizacional — **`CertifyBad`**, **`CertifyGood`** e **`PointOfContact`** — para que a equipe de AppSec anote pacotes, versões, repositórios ou artefatos diretamente no grafo e propague alertas para todos os serviços dependentes.

## Por que importa
Quando uma biblioteca open-source sofre um ataque de *typosquatting*, *protestware* ou *backdoor* (mesmo antes de receber um ID CVE oficial), anotar o pacote com `CertifyBad` no GUAC permite identificar instantaneamente todos os artefatos internos que o consomem.

## Como funciona
O comando `guacone certify bad` ou `guacone certify good` registra a justificativa técnica no nó alvo, enquanto `PointOfContact` associa o e-mail ou canal de equipe responsável por um artefato ou pacote interno, permitindo notificar automaticamente os donos dos microserviços afetados por uma dependência comprometida.

## Exemplo
```bash
# Marcar uma versão específica de pacote como maliciosa/proibida (CertifyBad) no grafo GUAC
guacone certify bad package \
  --justification "Pacote comprometido por ataque de supply chain (backdoor identificado pelo SOC)" \
  --gql-addr http://guac-policy.internal.corp:8080/query \
  pkg:npm/malicious-helper-lib@2.1.4
```

## Limites e trade-offs
Marcar apenas uma versão específica (`pkg:npm/lib@2.1.4`) com `CertifyBad` quando todas as versões do pacote são maliciosas deixará versões `2.1.3` ou `2.1.5` sem alerta; aplique `CertifyBad` no nível de nome do pacote quando o projeto inteiro for hostil.

## Como verificar
Execute uma query GraphQL em `CertifyBad` filtrando pelo pacote anotado e confirme o retorno da justificativa registrada e dos dependentes conectados via `IsDependency`.

## Conexões
- [[guacsec-arquitetura-eventos-nats-jetstream-collectsub-escala]] — Veja também: OpenSSF GUAC: Pipeline Assíncrono em Escala com NATS JetStream, `collectsub` e `guacingest`.
- [[guacsec-api-graphql-rest-guac-visualizer-integracao]] — Veja também: OpenSSF GUAC: Consultas Customizadas na API GraphQL, REST API e Exploração Visual no GUAC Visualizer.
- [[guacsec-ontologia-grafo-nouns-package-artifact-source-predicates]] — Referência cruzada direta com guacsec-ontologia-grafo-nouns-package-artifact-source-predicates.
- [[guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex]] — Referência cruzada direta com guacsec-consultas-vulnerabilidades-transitivas-guacone-query-vuln-vex.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
