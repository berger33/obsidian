---
id: software.seguranca.tranche05.000434
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

# BloodHound CE: Movimentação Lateral (`AdminTo` + `HasSession`), Roubo de Credenciais e `DCSync` (`GetChanges` + `GetChangesAll`)

## Em uma frase
O BloodHound modela a movimentação lateral e o comprometimento total do domínio correlacionando privilégios de administração local (`AdminTo`, `CanRDP`, `CanPSRemote`, `ExecuteDCOM`), sessões autenticadas na memória (`HasSession`) e direitos de replicação de diretório (`DCSync`).

## Por que importa
Se um grupo de suporte tem `AdminTo` em um servidor de arquivos onde um `Domain Admin` possui uma sessão ativa (`HasSession`), qualquer membro do suporte pode extrair o ticket Kerberos ou hash NT da memória (`LSASS`) daquele servidor e assumir o domínio.

## Como funciona
Na camada de domínio, o ataque **`DCSync`** é representado pela presença simultânea das arestas **`GetChanges`** e **`GetChangesAll`** (combinadas na aresta `DCSync`) partindo de um usuário ou computador em direção ao nó `Domain`, o que permite simular um Domain Controller via protocolo MS-DRSR (`DsGetNCChanges`) e extrair o hash de todas as contas (incluindo o `krbtgt`).

## Exemplo
```cypher
// Identificar todos os principais fora do Tier Zero que possuem permissões de DCSync no domínio
MATCH p=(n)-[:DCSync|GetChanges|GetChangesAll*1..2]->(d:Domain)
WHERE NOT (n.system_tags CONTAINS "admin_tier_0")
RETURN p
```

## Limites e trade-offs
Apenas Domain Controllers legítimos (e em cenários específicos a conta do Entra Connect, se estritamente necessário para *Password Hash Sync*) devem possuir `Replicating Directory Changes All`; revogue imediatamente essa ACE de contas de serviço ou administradores comuns.

## Como verificar
Audite o resultado da query Cypher de `DCSync` e confirme que apenas o grupo `Domain Controllers` e `Enterprise Domain Controllers` retêm essas arestas.

## Conexões
- [[bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword]] — Veja também: BloodHound CE: Arestas de Abuso de ACLs no Active Directory (`GenericAll`, `GenericWrite`, `WriteDacl`, `WriteOwner`, `ForceChangePassword`).
- [[bloodhound-delegacao-kerberos-unconstrained-constrained-rbcd]] — Veja também: BloodHound CE: Mapeamento de Delegações Kerberos (`Unconstrained`, `Constrained` `AllowedToDelegate` e `RBCD` `AllowedToAct`).
- [[bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio]] — Referência cruzada direta com bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
