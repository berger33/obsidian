---
id: software.seguranca.tranche11.001004
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md", "https://docs.cartography.dev/usage/tutorial.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Grafo de Identidade Cross-Platform no Cartography: Correlacionando **Okta, Microsoft Entra ID, Keycloak, Google Workspace, GitHub e AWS IAM**

## Em uma frase
Em empresas modernas, a identidade de um engenheiro não existe em um único lugar: ele possui uma conta corporativa no **Okta** ou **Microsoft Entra ID** (com dispositivos gerenciados no **Intune / Kandji** e MFA no **Duo**), faz parte de times no **GitHub** e no **Jira Cloud**, autentica em aplicações internas via **Keycloak** e assume Roles na **AWS (`AWSRole`)** via federação SAML/OIDC ou **AWS IAM Identity Center**!

## Por que importa
O Cartography conecta todos esses silos no mesmo grafo Neo4j: os módulos **`okta`**, **`entra`**, **`keycloak`**, **`googleworkspace`** e **`github`** criam arestas diretas entre o nó da pessoa humana (`OktaUser` / `EntraUser` / `GitHubUser`), seus grupos, seus fatores de autenticação e as **`AWSRole`s que ela pode assumir nas contas da AWS** (`CAN_ASSUME_ROLE`)!

## Como funciona
Isso permite auditar instantaneamente quem possui acesso administrativo efetivo (*Blast Radius* de identidade) através de múltiplos provedores de identidade e nuvens!

## Exemplo
```cypher
// Rastrear quais usuarios humanos do Okta (ou Entra ID) conseguem assumir IAM Roles com privilegios administrativos em contas AWS
MATCH path = (u:OktaUser)-[:MEMBER_OF_OKTA_GROUP|CAN_ASSUME_ROLE*1..4]->(r:AWSRole)<-[:RESOURCE]-(a:AWSAccount)
WHERE r.name CONTAINS "Admin" OR r.arn CONTAINS "AdministratorAccess"
RETURN u.email AS usuario_okta, r.arn AS iam_role_aws, a.name AS conta_aws;
```

## Limites e trade-offs
Por que essa visão unificada `IdP (Okta/Entra/Keycloak) -> Cloud (AWS/GCP/Azure) -> Code (GitHub)` é indispensável durante uma resposta a incidentes (DFIR)? Se o SOC detectar o comprometimento do laptop de um desenvolvedor, uma única query Cypher no Cartography lista **todas as contas AWS, clusters Kubernetes, repositórios GitHub e workspaces de IA (OpenAI/Anthropic) que aquele usuário alcança**, guiando a revogação imediata de sessões e chaves!

## Como verificar
Combine o módulo `entra` (que sincroniza inclusive dispositivos e políticas de conformidade do **Microsoft Intune**) com o módulo `crowdstrike` para verificar se todos os usuários com acesso a produção operam a partir de endpoints saudáveis.

## Conexões
- [[cartography-consultas-cypher-caminhos-ataque-iam-ec2-rds-k8s]] — Veja também: Threat Hunting e Descoberta de **Caminhos de Ataque (*Attack Paths*)** no Cartography com Consultas **OpenCypher** Multi-Hop.
- [[cartography-motor-regras-cartography-rules-auditoria-automatizada]] — Veja também: Execução Automatizada de Regras de Segurança no Grafo com **`cartography-rules`** (`list`, `run`, `object_storage_public` e Frameworks).
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam]] — Referência cruzada direta com steampipe-joins-multi-cloud-aws-gcp-kubernetes-github-iam.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
