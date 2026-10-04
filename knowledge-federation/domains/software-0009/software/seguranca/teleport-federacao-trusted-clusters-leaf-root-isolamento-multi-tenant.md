---
id: software.seguranca.tranche14.001380
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/gravitational/teleport/master/README.md", "https://goteleport.com/docs/reference/architecture/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Federação Multi-Cluster e Multi-Cloud com **Trusted Clusters (`Root Cluster` e `Leaf Clusters`)** no Teleport

## Em uma frase
E quando uma corporação global, holding de várias empresas ou provedor de serviços gerenciados (MSP) possui **dezenas de ambientes isolados (múltiplas contas AWS/GCP, datacenters regionais ou redes de clientes distintos)** onde cada ambiente deve ter sua própria Autoridade Certificadora independente e continuar funcionando mesmo se a conexão WAN com a matriz cair, mas a equipe central de SRE precisa acessar todos eles com **um único `tsh login` no SSO da matriz**?

## Por que importa
A arquitetura do Teleport resolve isso com **Trusted Clusters (`Root Cluster` e `Leaf Clusters`)**!

## Como funciona
Funciona assim: cada datacenter ou cliente roda o seu próprio cluster Teleport completo e autônomo (**`Leaf Cluster`**, com seu próprio `Auth Service` e `Proxy Service`). O `Leaf Cluster` estabelece um túnel reverso de saída para o **`Root Cluster`** da matriz e define um **`role_map`** explícito (ex.: mapeando a role `sre-global` do Root Cluster para a role local `admin-filial` do Leaf Cluster)! Com isso, o engenheiro faz `tsh login` uma única vez no `Root Cluster` e alterna entre qualquer filial ou cliente com **`tsh login <nome-leaf-cluster>`** (ou `tsh proxy ssh -J`!), enquanto **o dono do `Leaf Cluster` mantém soberania total para alterar o `role_map` ou desligar a confiança a qualquer instante**!

## Exemplo
```yaml
# Recurso kind: trusted_cluster aplicado no Leaf Cluster estabelecendo federacao e mapeamento de roles (role_map) com o Root Cluster
kind: trusted_cluster
version: v2
metadata:
  name: matriz-root.exemplo.br
spec:
  enabled: true
  token: token-federacao-trusted-cluster
  tunnel_addr: matriz-root.exemplo.br:3024
  web_proxy_addr: matriz-root.exemplo.br:443
  role_map:
    - remote: "sre-global"
      local: ["sre-producao"]
```

## Limites e trade-offs
Qual é a grande vantagem de segurança de um **`Trusted Cluster` (`Leaf Cluster`)** em relação a simplesmente conectar todos os agentes de todas as filiais a um único `Root Cluster` gigante? **Isolamento de Domínio de Falha e Soberania de Auditoria**: cada `Leaf Cluster` possui suas próprias chaves de Autoridade Certificadora (`Host CA` e `User CA`) e grava localmente suas próprias sessões de auditoria — se o link WAN entre a filial industrial e a matriz cair, os operadores locais da filial continuam autenticando diretamente no `Leaf Cluster` local sem interrupção!

## Como verificar
Use `tsh clusters` após o login para listar o `Root Cluster` e todos os `Leaf Clusters` conectados e verificar o status de conectividade de cada um.

## Conexões
- [[teleport-auditoria-eventos-gravacao-s3-dynamodb-integracao-siem]] — Veja também: Arquitetura de Alta Disponibilidade, **Armazenamento de Auditoria e Gravações (S3 / GCS / MinIO)** e Exportação de Eventos para **SIEM (`event-handler`)** no Teleport.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.
- [[teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn]] — Referência cruzada direta com teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn.
- [[freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba]] — Referência cruzada direta com freeipa-trust-active-directory-cross-forest-idviews-kerberos-samba.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
