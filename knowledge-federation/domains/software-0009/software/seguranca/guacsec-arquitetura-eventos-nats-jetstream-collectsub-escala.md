---
id: software.seguranca.tranche04.000377
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

# OpenSSF GUAC: Pipeline Assíncrono em Escala com NATS JetStream, `collectsub` e `guacingest`

## Em uma frase
Em implantações de produção, o GUAC desacopla a coleta de documentos da montagem do grafo utilizando um barramento de mensagens **NATS JetStream** e o serviço de subscrição **`collectsub`** (*Collector Subscriber Service*).

## Por que importa
Evita que picos de milhares de builds simultâneos no CI/CD sobrecarreguem o servidor GraphQL: os coletores publicam os documentos brutos no NATS e múltiplos workers `guacingest` processam e montam o grafo de forma assíncrona.

## Como funciona
Quando um novo pacote é inserido no grafo (por exemplo, a partir de um SBOM recém-coletado), o Assembler publica pistas de coleta (*collection cues*) no `collectsub`. Os coletores de OCI, Git e `deps.dev` assinam o `collectsub`, descobrem que um novo PURL ou repositório apareceu no grafo e buscam automaticamente seus metadados e SBOMs upstream.

## Exemplo
```bash
# Iniciar o serviço collectsub e o worker guacingest conectado ao NATS JetStream e ao GraphQL
guaccsub --csub-listen-port 2782

guacingest \
  --pubsub-addr nats://nats.internal.corp:4222 \
  --csub-addr collectsub.internal.corp:2782 \
  --gql-addr http://guacgql.internal.corp:8080/query
```

## Limites e trade-offs
Se o serviço `collectsub` estiver inacessível pelos coletores dinâmicos (`deps_dev`, `oci`), os pacotes recém-ingeridos via SBOM não acionarão a busca automática de metadados transitivos.

## Como verificar
Verifique os logs do `guacingest` e do `guaccsub` ao ingerir um novo SBOM e confirme o consumo das mensagens nos streams do NATS JetStream.

## Conexões
- [[guacsec-backends-armazenamento-keyvalue-ent-postgresql-redis-tikv]] — Veja também: OpenSSF GUAC: Backends de Persistência (`keyvalue` In-Memory vs `ent` com PostgreSQL).
- [[guacsec-governanca-politicas-certifybad-certifygood-pointofcontact]] — Veja também: OpenSSF GUAC: Governança Proativa da Cadeia de Suprimentos com `CertifyBad`, `CertifyGood` e `PointOfContact`.
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[guacsec-certificadores-automaticos-osv-deps-dev-scorecard-clearlydefined]] — Referência cruzada direta com guacsec-certificadores-automaticos-osv-deps-dev-scorecard-clearlydefined.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
