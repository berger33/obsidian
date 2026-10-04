---
id: software.seguranca.tranche05.000437
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

# BloodHound CE: Caminhos de Ataque no Microsoft Entra ID e Ambientes Híbridos (`AZAddSecret`, `AZGlobalAdmin`, `SyncedTo`)

## Em uma frase
Com os dados ingeridos pelo `AzureHound`, o BloodHound mapeia caminhos de escalação na nuvem Microsoft Entra ID e assinaturas Azure, conectando usuários sincronizados do AD on-premises (`SyncedToEntraUser` / `SyncedToADUser`) a *App Registrations*, *Service Principals*, *Managed Identities*, Key Vaults e VMs.

## Por que importa
No Entra ID, conceder a um desenvolvedor a permissão `Application Administrator` ou `Owner` sobre um *App Registration* cujo *Service Principal* correspondente possui papéis privilegiados no diretório permite adicionar uma nova senha/certificado (`AZAddSecret`) na aplicação e autenticar-se como ela.

## Como funciona
O grafo modela arestas específicas de nuvem como **`AZAddSecret`**, **`AZAddOwner`**, **`AZMGGrantAppRoles`**, **`AZResetPassword`**, **`AZVMAdminLogin`**, **`AZKeyVaultGetSecret`** e **`AZRunsAs`**, revelando como o comprometimento de uma VM Azure com *Managed Identity* ou de uma conta sincronizada on-premises escala até `Global Administrator` ou `Subscription Owner`.

## Exemplo
```cypher
// Localizar caminhos onde usuários comuns podem adicionar credenciais (AZAddSecret) em Apps/Service Principals privilegiados
MATCH p=(u:AZUser)-[:AZOwns|AZAddSecret|AZAppAdmin*1..2]->(app:AZApp)-[:AZRunsAs]->(sp:AZServicePrincipal)
WHERE sp.system_tags CONTAINS "admin_tier_0"
RETURN p
```

## Limites e trade-offs
Tratar *Service Principals* de automação CI/CD (Terraform, GitHub Actions) como contas comuns sem incluí-los no perímetro de proteção **Tier Zero** quando possuem `Directory.ReadWrite.All` ou `RoleManagement.ReadWrite.Directory` deixa um caminho crítico aberto.

## Como verificar
Execute a query Cypher acima após ingerir o `AzureHound` e remova proprietários (`Owners`) desnecessários de *App Registrations* privilegiados.

## Conexões
- [[bloodhound-escalacao-adcs-certificados-esc1-a-esc13-pkinit]] — Veja também: BloodHound CE: Caminhos de Escalação via Active Directory Certificate Services (`ADCS ESC1` a `ESC13`).
- [[bloodhound-governanca-tier-zero-high-value-assets-isolamento-privilegio]] — Veja também: BloodHound CE: Governança do Perímetro **Tier Zero** (`admin_tier_0`) e Erradicação de *Chokepoints*.
- [[bloodhound-coletores-sharphound-azurehound-metodos-coleta-furtividade]] — Referência cruzada direta com bloodhound-coletores-sharphound-azurehound-metodos-coleta-furtividade.
- [[bloodhound-extensibilidade-opengraph-ingestao-multi-cloud-iam]] — Referência cruzada direta com bloodhound-extensibilidade-opengraph-ingestao-multi-cloud-iam.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
