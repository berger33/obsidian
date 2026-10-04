---
id: software.seguranca.tranche05.000439
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

# BloodHound CE: Consultas `Cypher` Customizadas (`shortestPath`, `allShortestPaths`) e Priorização de Remediação

## Em uma frase
A aba de busca Cypher e a API `/api/v2/graphs/cypher` do BloodHound CE permitem escrever consultas em linguagem **Cypher** (`shortestPath` e `allShortestPaths`) para responder perguntas precisas de auditoria de identidade e validar planos de remediação.

## Por que importa
Permite medir quantitativamente a redução de superfície de ataque (por exemplo, qual percentual de `Domain Users` possui caminho de ataque até `Tier Zero`) antes e depois de remover uma delegação ou sessão privilegiada exposta.

## Como funciona
O analista pode salvar suas consultas Cypher customizadas na biblioteca do BloodHound CE, filtrar por propriedades de nós (como contas com `hasspn: true` para *Kerberoasting*, `dontreqpreauth: true` para *AS-REP Roasting*, ou `pwdlastset` antigo) e simular qual aresta específica cortar para eliminar centenas de caminhos de ataque de uma só vez.

## Exemplo
```cypher
// Encontrar os caminhos mais curtos de qualquer usuário com Kerberoasting (hasspn=true) até o Tier Zero
MATCH (u:User {hasspn: true, enabled: true})
MATCH (t {system_tags: "admin_tier_0"})
WHERE NOT (u.system_tags CONTAINS "admin_tier_0")
MATCH p=shortestPath((u)-[*1..6]->(t))
RETURN p LIMIT 25
```

## Limites e trade-offs
Usar padrões de caminho de comprimento ilimitado `[*1..]` sem `shortestPath(...)` em grafos grandes com dezenas de milhares de nós causará exaustão de memória e timeout na consulta Cypher; use sempre `shortestPath` ou limite a profundidade (`[*1..6]`).

## Como verificar
Execute a consulta via `/api/v2/graphs/cypher` antes e depois do hardening de contas de serviço com SPN e confirme a eliminação dos caminhos até `admin_tier_0`.

## Conexões
- [[bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio]] — Veja também: BloodHound CE: Governança do Perímetro **Tier Zero** (`admin_tier_0`) e Erradicação de *Chokepoints*.
- [[bloodhound-extensibilidade-opengraph-ingestao-multi-cloud-iam]] — Veja também: BloodHound CE: Extensibilidade com **BloodHound OpenGraph** para Plataformas Multi-Cloud, SaaS e CI/CD.
- [[bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api]] — Referência cruzada direta com bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
