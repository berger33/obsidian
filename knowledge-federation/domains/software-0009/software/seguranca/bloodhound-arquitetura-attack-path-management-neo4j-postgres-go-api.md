---
id: software.seguranca.tranche05.000431
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

# BloodHound CE: Arquitetura de Gestão de Caminhos de Ataque em Grafos (Go REST API, PostgreSQL e Neo4j)

## Em uma frase
**BloodHound Community Edition (BHCE)** (`SpecterOps/BloodHound`, Apache-2.0) é uma plataforma de análise de segurança baseada em teoria dos grafos que revela relações ocultas e caminhos de escalação de privilégio em ambientes Active Directory, Microsoft Entra ID (Azure AD) e plataformas híbridas via OpenGraph.

## Por que importa
Auditores humanos analisam permissões em listas planas, enquanto atacantes pensam em grafos: encadeando 5 ou 6 permissões aparentemente inofensivas (grupos aninhados, sessões ativas, ACLs de objetos, delegações Kerberos), um usuário comum chega a `Domain Admin` ou `Global Administrator`.

## Como funciona
A arquitetura moderna do BloodHound CE consiste em um backend REST API escrito em Go, uma interface React com renderização de grafos via Sigma.js, um banco relacional **PostgreSQL** (para usuários, RBAC, estado de ingestão e metadados da aplicação) e um banco de grafos **Neo4j** (onde residem os nós de identidade e as arestas de ataque consultáveis via linguagem Cypher).

## Exemplo
```bash
# Subir a pilha oficial do BloodHound Community Edition via Docker Compose em loopback seguro
curl -sSfLO https://ghst.ly/getbhce
docker compose -f docker-compose.yml up -d
```

## Limites e trade-offs
Nunca exponha a porta `7474`/`7687` do container Neo4j ou a interface `8080` do BloodHound CE diretamente na rede corporativa sem TLS e autenticação forte, pois o grafo contém o mapa completo de escalação de privilégio do domínio.

## Como verificar
Acesse `http://127.0.0.1:8080/api/version` autenticado e confirme o estado saudável dos serviços Go, PostgreSQL e Neo4j.

## Conexões
- [[bloodhound-coletores-sharphound-azurehound-metodos-coleta-furtividade]] — Veja também: BloodHound CE: Coletores Oficiais `SharpHound` (Active Directory) e `AzureHound` (Microsoft Entra ID / Azure RM).
- [[bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword]] — Referência cruzada direta com bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword.
- [[bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao]] — Referência cruzada direta com bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
