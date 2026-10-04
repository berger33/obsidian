---
id: software.seguranca.tranche05.000438
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

# BloodHound CE: Governança do Perímetro **Tier Zero** (`admin_tier_0`) e Erradicação de *Chokepoints*

## Em uma frase
O BloodHound estrutura a defesa de diretórios em torno do conceito de **Tier Zero** (grupo de ativos `admin_tier_0`, anteriormente *High Value*): o conjunto de todos os usuários, grupos, computadores, CAs e Service Principals que possuem controle administrativo direto ou indireto sobre a própria plataforma de identidade.

## Por que importa
Em vez de tentar corrigir milhares de permissões isoladas aleatoriamente, a engenharia defensiva foca nos **Chokepoints** (as últimas arestas que cruzam a fronteira de *Non-Tier Zero* para dentro do perímetro *Tier Zero*).

## Como funciona
O BloodHound marca automaticamente grupos nativos críticos (`Domain Admins`, `Enterprise Admins`, `Administrators`, `Account Operators`, `Backup Operators`, `Server Operators`, Domain Controllers e `Global Administrator`) com a tag de sistema `admin_tier_0`. Os defensores adicionam ativos customizados (como servidores de PKI ADCS, servidores Entra Connect, cofres de senha e grupos de administração delegada) ao *Asset Group* `Tier Zero` para auditar qualquer caminho externo que os alcance.

## Exemplo
```bash
# Consultar via API REST do BloodHound CE a lista de Asset Groups e membros do perímetro Tier Zero (admin_tier_0)
curl -sS "http://127.0.0.1:8080/api/v2/asset-groups" \
  -H "Authorization: Bearer ${BHCE_JWT}" | jq '.data.asset_groups[] | select(.tag == "admin_tier_0")'
```

## Limites e trade-offs
Esquecer de classificar o servidor Windows onde roda o **Microsoft Entra Connect** ou o servidor de backup corporativo (Veeam/Commvault que faz backup dos Domain Controllers) dentro do grupo `Tier Zero` oculta caminhos triviais de comprometimento total do domínio.

## Como verificar
Adicione os servidores de PKI, backup e sincronização de identidade ao grupo `Tier Zero` no BloodHound CE e audite todos os caminhos de entrada na aba *Explore*.

## Conexões
- [[bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets]] — Veja também: BloodHound CE: Caminhos de Ataque no Microsoft Entra ID e Ambientes Híbridos (`AZAddSecret`, `AZGlobalAdmin`, `SyncedTo`).
- [[bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao]] — Veja também: BloodHound CE: Consultas `Cypher` Customizadas (`shortestPath`, `allShortestPaths`) e Priorização de Remediação.
- [[bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api]] — Referência cruzada direta com bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api.
- [[bloodhound-movimentacao-lateral-hassession-adminto-dcsync-adminsdholder]] — Referência cruzada direta com bloodhound-movimentacao-lateral-hassession-adminto-dcsync-adminsdholder.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
