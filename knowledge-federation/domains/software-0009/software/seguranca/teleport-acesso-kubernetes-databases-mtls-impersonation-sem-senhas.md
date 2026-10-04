---
id: software.seguranca.tranche14.001373
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

# Acesso Zero-Trust a **Clusters Kubernetes (`tsh kube login`)** e **Bancos de Dados (`tsh db connect` — PostgreSQL, MySQL, MongoDB, Redis)** sem Senhas Compartilhadas

## Em uma frase
Como eliminar de vez os dois artefatos mais vazados em equipes de Cloud e Dados: **(1) Arquivos `kubeconfig` estáticos com privilégios `cluster-admin`** salvos em notebooks e **(2) Senhas compartilhadas de bancos de dados de produção (`postgres`, `mysql`, `mongodb`, `redis`, `RDS IAM`)** coladas em clientes como DBeaver, DataGrip ou `psql`?

## Por que importa
Com o **Teleport Kubernetes Service** e o **Teleport Database Service**!

## Como funciona
No **Kubernetes**: o agente Teleport roda como um Pod dentro do cluster K8s e abre um túnel reverso de saída para o Proxy. Quando o engenheiro roda `tsh kube login cluster-prod` e executa `kubectl get pods`, o `kubectl` fala mTLS com o Teleport, que valida o RBAC, **registra no log de auditoria exatamente qual requisição `kubectl` (e todo comando `kubectl exec -it`!) foi executada** e repassa a chamada para o API Server do Kubernetes usando **Kubernetes Impersonation (`Impersonate-User` / `Impersonate-Group`)**! Nos **Bancos de Dados**: o engenheiro roda `tsh db connect --db-user=leitura_bi --db-name=vendas pg-producao` (ou `tsh proxy db` para conectar o DBeaver/DataGrip local!). O **Teleport Database Service** autentica no PostgreSQL/MySQL/RDS usando **mTLS de curta duração ou IAM Token efêmero**, sem que o usuário jamais veja ou possua uma senha do banco, e **audita cada query SQL executada (`db.session.query`)**!

## Exemplo
```bash
# Autenticar no cluster Kubernetes e abrir um proxy local mTLS autenticado para um banco PostgreSQL sem usar nenhuma senha de banco
tsh kube login k8s-producao-sp
kubectl get pods -n pagamentos
tsh db login pg-pagamentos-ro --db-user=analista_ro --db-name=pagamentos
tsh db connect pg-pagamentos-ro
```

## Limites e trade-offs
Olhe o ganho de segurança e conformidade PCI-DSS / LGPD no **Teleport Database Service**: como o protocolo nativo do PostgreSQL, MySQL, MariaDB, MongoDB, Redis, ClickHouse e SQL Server é interpretado pelo agente do Teleport no caminho, o log de auditoria registra **cada instrução `SELECT`, `UPDATE` ou `DROP` executada, vinculada nominalmente ao e-mail do funcionário no SSO**, mesmo que 20 analistas usem o mesmo role lógico `analista_ro` dentro do banco!

## Como verificar
Ative sempre `per_session_mfa: true` no role de acesso aos bancos e clusters Kubernetes de produção para exigir um toque físico na YubiKey/Passkey no momento exato de abrir a conexão.

## Conexões
- [[teleport-acesso-ssh-certificados-openssh-gravacao-sessao-ebpf]] — Veja também: Acesso SSH com **Gravação Completa de Sessão Interativa** e **Auditoria Enriquecida por eBPF (`enhanced_recording`)** no Teleport.
- [[teleport-acesso-web-apps-jwt-headers-windows-desktop-rdp-mcp]] — Veja também: Acesso Seguro a **Aplicações Web Internas (`Application Service` + JWT)**, **Windows Desktops (`RDP` Sem Senha via Smartcard Virtual)** e **Servidores MCP (IA)** no Teleport.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.
- [[teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn]] — Referência cruzada direta com teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
