---
id: software.seguranca.tranche05.000432
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

# BloodHound CE: Coletores Oficiais `SharpHound` (Active Directory) e `AzureHound` (Microsoft Entra ID / Azure RM)

## Em uma frase
O BloodHound é alimentado por dois coletores oficiais open-source mantidos pela SpecterOps: **`SharpHound`** (C#/.NET para Active Directory on-premises via LDAP/SMB/RPC) e **`AzureHound`** (Go para Microsoft Entra ID e assinaturas Azure via Microsoft Graph e Azure Resource Manager APIs).

## Por que importa
Sem a coleta combinada de AD local e nuvem Entra ID, caminhos híbridos críticos — como um administrador local que compromete a conta de sincronização `MSOL_` / `AADConnect` para assumir o tenant inteiro na nuvem — permanecem invisíveis.

## Como funciona
No `SharpHound`, a flag `-c` (`--collectionmethods`) controla exatamente quais dados são coletados: `DCOnly` (consulta exclusivamente o Domain Controller via LDAP/LDAPS sem enviar tráfego SMB para estações de trabalho) vs `All` ou `Session` (que interroga estações e servidores na rede para mapear sessões de logon ativas `HasSession` e grupos locais `AdminTo`).

## Exemplo
```powershell
# Executar coleta defensiva DCOnly no Active Directory sem tocar nas estações de trabalho via SMB
.\SharpHound.exe --CollectionMethods DCOnly `
  --Domain corp.internal `
  --OutputDirectory C:\Temp\BHAudit `
  --EncryptZip
```

## Limites e trade-offs
Os arquivos `.zip` ou `.json` gerados pelo `SharpHound` e `AzureHound` contêm toda a topologia de segurança do diretório; use `--EncryptZip` na coleta, transfira os artefatos por canal cifrado para o servidor BloodHound e apague os arquivos temporários do host de coleta.

## Como verificar
Faça upload do pacote `.zip` na aba *File Ingest* do BloodHound CE e verifique no log de ingestão o término com status `Complete`.

## Conexões
- [[bloodhound-arquitetura-attack-path-management-neo4j-postgres-go-api]] — Veja também: BloodHound CE: Arquitetura de Gestão de Caminhos de Ataque em Grafos (Go REST API, PostgreSQL e Neo4j).
- [[bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword]] — Veja também: BloodHound CE: Arestas de Abuso de ACLs no Active Directory (`GenericAll`, `GenericWrite`, `WriteDacl`, `WriteOwner`, `ForceChangePassword`).
- [[bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets]] — Referência cruzada direta com bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
