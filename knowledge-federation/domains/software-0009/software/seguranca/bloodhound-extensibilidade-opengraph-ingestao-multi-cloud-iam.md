---
id: software.seguranca.tranche05.000440
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md", "https://bloodhound.specterops.io/home", "https://bloodhound.specterops.io/opengraph/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# BloodHound CE: Extensibilidade com **BloodHound OpenGraph** para Plataformas Multi-Cloud, SaaS e CI/CD

## Em uma frase
O **BloodHound OpenGraph** estende o motor de grafos do BloodHound CE além do Active Directory e Entra ID, fornecendo um esquema JSON aberto e API de ingestão para modelar nós, ícones customizados e arestas de ataque de qualquer plataforma de identidade (AWS IAM, GCP IAM, GitHub Enterprise, Okta, Kubernetes RBAC ou bancos de dados).

## Por que importa
Os caminhos de ataque reais raramente ficam confinados a um único provedor: um desenvolvedor no AD local acessa o Okta, assume um papel no GitHub Actions, obtém credenciais AWS via OIDC e compromete um banco de produção; o OpenGraph unifica essas plataformas no mesmo grafo.

## Como funciona
Coletores OpenGraph exportam um documento JSON contendo arrays de `nodes` (com `id`, `kinds`, `properties`) e `edges` (com `kind`, `start`, `end`, `properties`). Ao ser ingerido na API do BloodHound CE, o grafo conecta as entidades externas aos nós existentes de AD/Entra ID e habilita travessias Cypher multi-plataforma.

## Exemplo
```json
{
  "graph": {
    "nodes": [
      {
        "id": "arn:aws:iam::111122223333:role/ProdBreakGlassAdmin",
        "kinds": ["AWSRole", "AWSPrincipal"],
        "properties": { "name": "ProdBreakGlassAdmin@111122223333" }
      }
    ],
    "edges": [
      {
        "kind": "CanAssumeRole",
        "start": { "value": "S-1-5-21-1000-2000-3000-1105" },
        "end": { "value": "arn:aws:iam::111122223333:role/ProdBreakGlassAdmin" }
      }
    ]
  }
}
```

## Limites e trade-offs
Para que as arestas de um coletor OpenGraph se conectem perfeitamente aos nós do `SharpHound`/`AzureHound` existentes, utilize identificadores canônicos consistentes (`ObjectID` / `SID` / `UPN` normalizado em maiúsculas) nos campos `start` e `end`.

## Como verificar
Submeta o arquivo JSON OpenGraph de teste via endpoint de ingestão do BloodHound CE e execute `MATCH p=()-[:CanAssumeRole]->() RETURN p` para confirmar a renderização do caminho híbrido.

## Conexões
- [[bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao]] — Veja também: BloodHound CE: Consultas `Cypher` Customizadas (`shortestPath`, `allShortestPaths`) e Priorização de Remediação.
- [[bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api]] — Referência cruzada direta com bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api.
- [[bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets]] — Referência cruzada direta com bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
