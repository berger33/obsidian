---
id: software.seguranca.tranche05.000436
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

# BloodHound CE: Caminhos de Escalação via Active Directory Certificate Services (`ADCS ESC1` a `ESC13`)

## Em uma frase
O BloodHound modela nativamente a infraestrutura de PKI corporativa do Active Directory (**ADCS** — *Enterprise CAs*, *Certificate Templates*, *RootCA*, *NTAuthStore* e *AIACA*) e calcula automaticamente as arestas de escalação de privilégio **`ADCSESC1`** até **`ADCSESC13`**.

## Por que importa
Um único *Certificate Template* mal configurado (por exemplo, permitindo que `Domain Users` solicitem um certificado com *Client Authentication* e especifiquem um `SubjectAltName` arbitrário — **ESC1**) permite que qualquer usuário emita um certificado em nome de um `Domain Admin` e obtenha um TGT via `PKINIT`.

## Como funciona
O `SharpHound` coleta os objetos do container `CN=Public Key Services,CN=Services,CN=Configuration,...` e o motor de pós-processamento do BloodHound avalia todas as pré-condições simultâneas (se o template está publicado em uma Enterprise CA confiável em `NTAuthCertificates`, se exige aprovação do gerente de certificados, quantas assinaturas de RA exige e quem tem `Enroll`/`AutoEnroll` ou `WriteDacl` no template), sintetizando arestas diretas como `ADCSESC1`, `ADCSESC3`, `ADCSESC4`, `ADCSESC6a/b`, `ADCSESC8`, `ADCSESC9a/b`, `ADCSESC10a/b` e `ADCSESC13`.

## Exemplo
```cypher
// Encontrar todos os caminhos de escalação ADCS (ESC1 a ESC13) que levam ao comprometimento do domínio
MATCH p=()-[:ADCSESC1|ADCSESC3|ADCSESC4|ADCSESC6a|ADCSESC6b|ADCSESC8|ADCSESC9a|ADCSESC10a|ADCSESC13]->(:Domain)
RETURN p
```

## Limites e trade-offs
Apenas desabilitar ou excluir o objeto do *Certificate Template* no console sem removê-lo da lista de templates publicados nas Enterprise CAs (ou sem revogar certificados de longa validade já emitidos) exige auditoria cuidadosa.

## Como verificar
Execute a consulta Cypher de arestas `ADCSESC*` no BloodHound CE e confirme que todas as configurações inseguras (como `CT_FLAG_ENROLLEE_supplies_subject` sem aprovação de gerente para grupos amplos) foram corrigidas.

## Conexões
- [[bloodhound-delegacao-kerberos-unconstrained-constrained-rbcd]] — Veja também: BloodHound CE: Mapeamento de Delegações Kerberos (`Unconstrained`, `Constrained` `AllowedToDelegate` e `RBCD` `AllowedToAct`).
- [[bloodhound-caminhos-hibridos-entra-id-azure-ad-sync-roles-app-secrets]] — Veja também: BloodHound CE: Caminhos de Ataque no Microsoft Entra ID e Ambientes Híbridos (`AZAddSecret`, `AZGlobalAdmin`, `SyncedTo`).
- [[bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword]] — Referência cruzada direta com bloodhound-arestas-abuso-acl-genericall-writedacl-forcechangepassword.
- [[bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao]] — Referência cruzada direta com bloodhound-consultas-cypher-caminhos-curtos-tier-zero-remediacao.

## Fontes
- [BloodHound CE Official GitHub — Architecture & Collectors](https://raw.githubusercontent.com/SpecterOps/BloodHound/main/README.md) — documentação oficial do BloodHound Community Edition (Go API, PostgreSQL, Neo4j, SharpHound, AzureHound e OpenGraph); consultado em 2026-10-03.
- [BloodHound Official Documentation Portal — SpecterOps](https://bloodhound.specterops.io/home) — portal oficial de documentação de coleta, análise de caminhos de ataque, Tier Zero e Cypher; consultado em 2026-10-03.
- [BloodHound OpenGraph Documentation](https://bloodhound.specterops.io/opengraph/overview) — documentação oficial do esquema OpenGraph para ingestão multi-plataforma; consultado em 2026-10-03.
