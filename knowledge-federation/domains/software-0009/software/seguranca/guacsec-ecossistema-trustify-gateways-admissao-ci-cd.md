---
id: software.seguranca.tranche04.000380
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

# OpenSSF GUAC: Integração em Gates de Release CI/CD e Relação com o Ecossistema GUAC / Trustify

## Em uma frase
Sob o guarda-chuva do projeto GUAC na OpenSSF (que engloba o **GUAC** e o **Trustify**), as consultas ao grafo são integradas como *Release Gates* em pipelines de CI/CD e políticas de promoção de artefatos para ambientes de produção.

## Por que importa
Permite bloquear a promoção de uma imagem OCI se ela não possuir SBOM ingerido (`hasSBOM`), se sua proveniência SLSA não vier de um builder confiável (`HasSLSA`), se tiver pontuação baixa no OpenSSF Scorecard ou se depender de pacotes com `CertifyBad` / `CertifyVuln` sem `CertifyVEXStatement`.

## Como funciona
No pipeline de promoção de release, um job executa `guacone collect files` para registrar o SBOM e a atestação SLSA recém-gerados, aguarda o enriquecimento e executa `guacone query vuln` e consultas GraphQL de conformidade antes de assinar a tag de produção.

## Exemplo
```bash
# Gate de promoção: verificar se a imagem possui SBOM e SLSA registrados e zero vulnerabilidades abertas
guacone query known artifact sha256:${IMAGE_DIGEST} \
  --gql-addr http://guac.internal.corp:8080/query

guacone query vuln pkg:oci/app-release@sha256:${IMAGE_DIGEST} \
  --gql-addr http://guac.internal.corp:8080/query
```

## Limites e trade-offs
Bloquear builds em tempo real dependendo de chamadas síncronas a APIs externas lentas pode fragilizar o CI; consulte sempre o grafo local do GUAC já pré-populado pelos coletores e certificadores assíncronos.

## Como verificar
Simule a tentativa de promoção de uma imagem com dependência marcada via `CertifyBad` e confirme a detecção imediata pela consulta do gate.

## Conexões
- [[guacsec-api-graphql-rest-guac-visualizer-integracao]] — Veja também: OpenSSF GUAC: Consultas Customizadas na API GraphQL, REST API e Exploração Visual no GUAC Visualizer.
- [[guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex]] — Referência cruzada direta com guacsec-arquitetura-openssf-supply-chain-graph-sbom-slsa-vex.
- [[guacsec-governanca-politicas-certifybad-certifygood-pointofcontact]] — Referência cruzada direta com guacsec-governanca-politicas-certifybad-certifygood-pointofcontact.
- [[rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian]] — Referência cruzada direta com rekor-arquitetura-sigstore-transparency-log-merkle-tree-trillian.

## Fontes
- [OpenSSF GUAC GitHub — README.md (Graph for Understanding Artifact Composition Architecture, Supported Input Documents & GraphQL Backends)](https://raw.githubusercontent.com/guacsec/guac/main/README.md) — README oficial do guacsec/guac apresentando o modelo lógico de agregação e síntese da cadeia de suprimentos, formatos suportados e backends Ent/PostgreSQL e Keyvalue; consultado em 2026-10-03.
- [OpenSSF GUAC Official Documentation — GUAC Docs (Visualizer, Querying Vulnerabilities via CLI guacone, Known Package Queries & SBOM Mapping)](https://docs.guac.sh/guac/) — Documentação oficial do GUAC demonstrando consultas transitivas de vulnerabilidades, inspeção de pacotes PURL e enriquecimento com OSV.dev, deps.dev e Scorecard; consultado em 2026-10-03.
- [OpenSSF GUAC — Official Supply Chain Use Cases (use-cases.md)](https://github.com/guacsec/guac/blob/main/use-cases.md) — Documento oficial de casos de uso de auditoria, resposta a incidentes e políticas no OpenSSF GUAC; consultado em 2026-10-03.
