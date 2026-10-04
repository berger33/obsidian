---
id: software.seguranca.tranche14.001375
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

# Controle de Acesso **RBAC + ABAC (`labels`)**, **Per-Session MFA (FIDO2 WebAuthn)** e Restrição de IP/Dispositivo em Roles do Teleport

## Em uma frase
Como escrever uma política de acesso (`role`) no **Teleport** que garanta: *"Membros do grupo `sre-oncall` do SSO só podem acessar servidores rotulados com `env: producao` se: (1) tocarem fisicamente em sua chave FIDO2/Passkey a cada nova sessão SSH/K8s (`require_session_mfa`), (2) tiverem uma sessão máxima de 4 horas e (3) nunca puderem acessar recursos rotulados com `pci: restrito`"*?

## Por que importa
No Teleport, os recursos (`node_labels`, `kube_labels`, `db_labels`, `app_labels`) são combinados com variáveis dinâmicas vindas do IdP OIDC/SAML (`{{external.groups}}`, `{{external.email}}`) dentro de um recurso declarativo **`kind: role` (`v7`)** contendo blocos explícitos **`allow`** e **`deny`**!

## Como funciona
Regra de ouro de avaliação do Teleport: **as regras `deny` têm precedência absoluta sobre qualquer regra `allow`**! E dentro de `options`, você ativa travas como **`require_session_mfa: true`** (que exige presença física WebAuthn/TOTP no momento de cada `tsh ssh` ou `kubectl exec`, impedindo que um malware roube o certificado da memória da estação e abra uma sessão oculta!), **`max_session_ttl: 4h`**, **`client_idle_timeout: 15m`** e **`pin_source_ip: true`**!

## Exemplo
```yaml
# Role declarativa (kind: role v7) no Teleport com ABAC por labels, Per-Session MFA obrigatorio, Pinning de IP e bloqueio explicito (deny)
kind: role
version: v7
metadata:
  name: sre-producao
spec:
  options:
    max_session_ttl: 4h0m0s
    client_idle_timeout: 15m0s
    require_session_mfa: true
    pin_source_ip: true
    record_session:
      default: strict
  allow:
    logins: ['ubuntu', '{{internal.logins}}']
    node_labels:
      'env': 'producao'
    kubernetes_labels:
      'env': 'producao'
    kubernetes_groups: ['system:masters']
  deny:
    node_labels:
      'pci': 'restrito'
```

## Limites e trade-offs
Olhe três opções de segurança excepcionais no bloco `spec.options` acima: **(1) `record_session: default: strict`** (se por qualquer falha de rede/disco o servidor de auditoria não conseguir gravar a sessão em tempo real, a sessão SSH é encerrada imediatamente — *Fail-Closed Audit*!); **(2) `pin_source_ip: true`** (vincula o certificado emitido ao endereço IP exato do cliente no momento do login, tornando o certificado inútil se exfiltrado para outra rede!); e **(3) `require_session_mfa: true`**!

## Como verificar
Aplique e versione todas as suas roles via GitOps usando **`tctl create -f role-sre.yaml`** ou através do provedor oficial **Terraform do Teleport**.

## Conexões
- [[teleport-acesso-web-apps-jwt-headers-windows-desktop-rdp-mcp]] — Veja também: Acesso Seguro a **Aplicações Web Internas (`Application Service` + JWT)**, **Windows Desktops (`RDP` Sem Senha via Smartcard Virtual)** e **Servidores MCP (IA)** no Teleport.
- [[teleport-fluxos-just-in-time-access-requests-chatops-slack-jira]] — Veja também: Privilégio Zero Permanente (**Zero Standing Privilege — ZSP**) com **Just-In-Time (JIT) Access Requests** no Teleport: Aprovação via Slack, Mattermost, PagerDuty ou Jira.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
