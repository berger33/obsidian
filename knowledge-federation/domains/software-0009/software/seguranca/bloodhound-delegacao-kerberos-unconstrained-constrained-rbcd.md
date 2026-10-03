---
id: software.seguranca.tranche05.000435
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

# BloodHound CE: Mapeamento de Delegações Kerberos (`Unconstrained`, `Constrained` `AllowedToDelegate` e `RBCD` `AllowedToAct`)

## Em uma frase
O BloodHound identifica e conecta automaticamente os três tipos de delegação Kerberos no Active Directory que permitem personificação de usuários privilegiados: **Unconstrained Delegation**, **Constrained Delegation** (`AllowedToDelegate`) e **Resource-Based Constrained Delegation — RBCD** (`AllowedToAct`).

## Por que importa
Computadores ou contas com *Unconstrained Delegation* armazenam o TGT completo de qualquer usuário que se conecte a eles; combinados com coerção de autenticação (PrintSpooler / PetitPotam), permitem capturar TGTs de Domain Controllers.

## Como funciona
No grafo, nós com propriedade `unconstraineddelegation: true` são sinalizados; a delegação restrita clássica (`msDS-AllowedToDelegateTo`) gera a aresta **`AllowedToDelegate`** para os computadores alvo (onde `S4U2Self` + `S4U2Proxy` permitem personificar qualquer conta não marcada como *Account is sensitive and cannot be delegated*); e a delegação baseada em recurso (`msDS-AllowedToActOnBehalfOfOtherIdentity`) gera a aresta **`AllowedToAct`** (ou o caminho onde `GenericWrite` em um computador permite configurar RBCD).

## Exemplo
```cypher
// Localizar servidores (exceto Domain Controllers) com Unconstrained Delegation habilitada
MATCH (c:Computer {unconstraineddelegation: true})
WHERE NOT (c.system_tags CONTAINS "admin_tier_0")
RETURN c.name, c.operatingsystem
```

## Limites e trade-offs
Marque todas as contas administrativas do Tier Zero com o atributo de conta `Account is sensitive and cannot be delegated` (`NOT_DELEGATED`) e migre serviços legados de *Unconstrained Delegation* para *Constrained Delegation* ou *RBCD*.

## Como verificar
Execute a query Cypher acima no BloodHound CE e confirme que nenhum servidor membro fora dos Domain Controllers possui `unconstraineddelegation: true`.

## Conexões
- [[bloodhound-movimentacao-lateral-hassession-adminto-dcsync-adminsdholder]] — Veja também: BloodHound CE: Movimentação Lateral (`AdminTo` + `HasSession`), Roubo de Credenciais e `DCSync` (`GetChanges` + `GetChangesAll`).
- [[bloodhound-escalacao-adcs-certificados-esc1-a-esc13-pkinit]] — Veja também: BloodHound CE: Caminhos de Escalação via Active Directory Certificate Services (`ADCS ESC1` a `ESC13`).
- [[bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio]] — Referência cruzada direta com bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
