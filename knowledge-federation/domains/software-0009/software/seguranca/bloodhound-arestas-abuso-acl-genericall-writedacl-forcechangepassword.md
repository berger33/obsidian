---
id: software.seguranca.tranche05.000433
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

# BloodHound CE: Arestas de Abuso de ACLs no Active Directory (`GenericAll`, `GenericWrite`, `WriteDacl`, `WriteOwner`, `ForceChangePassword`)

## Em uma frase
O modelo de grafo do BloodHound representa cada direito de controle de acesso (ACE na DACL de um objeto do Active Directory) capaz de comprometer o objeto de destino como uma aresta direcionada (`Edge`) entre o principal de origem e o alvo.

## Por que importa
Em domínios Active Directory antigos, permissões delegadas anos atrás para grupos de *Helpdesk* ou contas de serviço frequentemente concedem `WriteDacl` ou `GenericAll` sobre Unidades Organizacionais (OUs) ou grupos que foram posteriormente adicionados ao `Domain Admins`.

## Como funciona
As principais arestas de ACL incluem: **`GenericAll`** (controle total sobre o objeto), **`WriteDacl`** (permite modificar a DACL do alvo para conceder a si mesmo controle total), **`WriteOwner`** (permite assumir a propriedade do objeto), **`GenericWrite` / `AddKeyCredentialLink`** (permite injetar *Shadow Credentials* no atributo `msDS-KeyCredentialLink` ou *Targeted Kerberoasting* gravando um SPN) e **`ForceChangePassword`** (redefine a senha do usuário alvo sem conhecer a atual).

## Exemplo
```cypher
// Localizar usuários ou grupos não-administrativos que possuem arestas de controle de ACL sobre grupos Tier Zero
MATCH p=(n)-[r:GenericAll|GenericWrite|WriteDacl|WriteOwner|ForceChangePassword|AddMember]->(m:Group)
WHERE m.system_tags CONTAINS "admin_tier_0" AND NOT (n.system_tags CONTAINS "admin_tier_0")
RETURN p LIMIT 50
```

## Limites e trade-offs
Remover uma permissão explícita na OU pai não remove automaticamente ACEs herdadas caso o objeto filho tenha a herança desabilitada (*Inheritance Disabled* / `AdminSDHolder`); verifique também o objeto `AdminSDHolder` do domínio.

## Como verificar
Execute a query Cypher acima após remover as ACEs indevidas no AD e reingerir o `SharpHound`, confirmando `0` caminhos retornados.

## Conexões
- [[bloodhound-coletores-sharphound-azurehound-metodos-coleta-furtividade]] — Veja também: BloodHound CE: Coletores Oficiais `SharpHound` (Active Directory) e `AzureHound` (Microsoft Entra ID / Azure RM).
- [[bloodhound-movimentacao-lateral-hassession-adminto-dcsync-adminsdholder]] — Veja também: BloodHound CE: Movimentação Lateral (`AdminTo` + `HasSession`), Roubo de Credenciais e `DCSync` (`GetChanges` + `GetChangesAll`).
- [[bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api]] — Referência cruzada direta com bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api.
- [[bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao]] — Referência cruzada direta com bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
