---
id: software.seguranca.tranche14.001371
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

# Arquitetura do **Gravitational Teleport (`gravitational/teleport`)**: Acesso **Zero-Trust Baseado em Identidade** e **Certificados de Curta Duração** (Sem Chaves Estáticas!)

## Em uma frase
Por que chaves SSH estáticas (`~/.ssh/authorized_keys`), arquivos `kubeconfig` de longa duração, senhas de banco de dados compartilhadas e VPNs tradicionais que colocam o notebook do desenvolvedor dentro da sub-rede inteira de produção são os alvos favoritos de invasores para movimentação lateral?

## Por que importa
Porque credenciais estáticas nunca expiram sozinhas, são copiadas para notebooks sem controle e não vinculam criptograficamente cada comando executado à identidade real do usuário no SSO!

## Como funciona
O **Gravitational Teleport** substitui chaves estáticas, `authorized_keys`, senhas compartilhadas e bastions legados por uma **Plataforma Unificada de Acesso Zero-Trust Baseada em Certificados de Curta Duração (ex.: TTL de 4 a 12 horas)**: **(1) `Teleport Auth Service`** — a Autoridade Certificadora (CA de SSH e X.509 mTLS) e motor de políticas RBAC/ABAC e auditoria do cluster; **(2) `Teleport Proxy Service`** — o gateway stateless de borda que autentica os usuários via **OIDC / SAML / Passkeys FIDO2** e roteia conexões sobre TLS via *ALPN Routing* e *Reverse Tunnels*; e **(3) `Teleport Agents`** (SSH Node, Kubernetes Service, Database Service, Application Service, Windows Desktop Service e MCP)!

## Exemplo
```bash
# Fazer login no cluster Teleport via SSO + WebAuthn (recebendo certificado efemero de 8h) e listar servidores, clusters K8s e bancos disponiveis
tsh login --proxy=teleport.exemplo.br:443 --auth=sso-corporativo
tsh status
tsh ls
tsh kube ls
tsh db ls
```

## Limites e trade-offs
Repare no que acontece quando você executa **`tsh login`**: o usuário se autentica no IdP corporativo (Authentik, Kanidm, Okta, Entra ID) com MFA/Passkey, e o `Teleport Auth Service` emite um **Certificado SSH e um Certificado X.509 mTLS efêmeros que expiram automaticamente ao fim do expediente (`TTL = 8h`)**! Quando o expediente acaba, o certificado expira sozinho sem precisar revogar chaves em milhares de servidores!

## Como verificar
Como o **Teleport Proxy Service** suporta multiplexação **`TLS ALPN Routing`**, todas as conexões de clientes (`tsh ssh`, `kubectl`, `psql`, `mysql`, Web UI e túneis reversos de agentes) podem trafegar por **uma única porta pública TCP `:443`**!

## Conexões
- [[teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf]] — Veja também: Acesso SSH com **Gravação Completa de Sessão Interativa** e **Auditoria Enriquecida por eBPF (`enhanced_recording`)** no Teleport.
- [[teleport-acesso-kubernetes-databases-mtls-impersonation-sem-senhas]] — Referência cruzada direta com teleport-acesso-kubernetes-databases-mtls-impersonation-sem-senhas.
- [[rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust]] — Referência cruzada direta com rustls-autenticacao-mutua-mtls-webpkiclientverifier-zero-trust.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
