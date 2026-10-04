---
id: software.seguranca.tranche14.001377
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

# Identidade de Máquina e Automação CI/CD com **Teleport Machine ID (`tbot`)**: Aposentando Segredos de Longa Duração no GitHub Actions, GitLab CI e Ansible

## Em uma frase
Nós já vimos como o `tsh login` elimina chaves estáticas para **usuários humanos**. Mas e os **robôs, pipelines de CI/CD (GitHub Actions, GitLab CI, Jenkins), playbooks do Ansible e microsserviços** que precisam fazer deploy via SSH, rodar `helm upgrade` no Kubernetes ou executar migrações de schema no PostgreSQL sem intervenção humana?

## Por que importa
Colocar uma chave SSH privada sem senha (`id_ed25519`) ou um `kubeconfig` eterno nos *Secrets* do GitHub/GitLab cria um risco enorme de vazamento!

## Como funciona
A solução oficial da arquitetura do Teleport é o **Teleport Machine ID (`tbot`)**! O binário **`tbot`** autentica o workload ou pipeline no cluster Teleport usando **Join Tokens criptográficos sem segredo estático** — como o token **OIDC do GitHub Actions / GitLab CI**, o **AWS IAM Role / Instance Identity Document**, o **GCP/Azure Workload Identity**, o **Kubernetes ServiceAccount JWT** ou o **TPM 2.0 de hardware**! Após validar a identidade da máquina/pipeline, o `tbot` gera e renova continuamente em disco/memória certificados efêmeros de curta duração (ex.: TTL de 20 minutos!) prontos para o `ssh`, `ansible`, `kubectl` ou cliente de banco de dados!

## Exemplo
```bash
# Executar o agente tbot (Teleport Machine ID) em modo one-shot dentro de um job de CI/CD para gerar certificados efemeros de deploy K8s/SSH
tbot start \
  --auth-server=teleport.exemplo.br:443 \
  --token=github-actions-join-token \
  --join-method=github \
  --destination-dir=/tmp/tbot-creds \
  --oneshot
```

## Limites e trade-offs
Veja o poder do **`--join-method=github` (ou `gitlab`, `kubernetes`, `iam`, `tpm`)** com `--oneshot` no comando acima: você **não precisa armazenar nenhum segredo ou chave privada nos Secrets do GitHub**! O Teleport valida criptograficamente o token OIDC emitido pelo GitHub Actions (checando repositório, branch `refs/heads/main` e ambiente!), emite um certificado que vive apenas pelos 15 minutos daquele deploy e audita todas as ações executadas pelo pipeline!

## Como verificar
Para servidores de automação permanentes (como um control node do Ansible ou Prometheus), o `tbot` roda como um serviço `systemd` contínuo renovando os certificados em `/opt/machine-id` a cada 20 minutos em background.

## Conexões
- [[teleport-fluxos-just-in-time-access-requests-chatops-slack-jira]] — Veja também: Privilégio Zero Permanente (**Zero Standing Privilege — ZSP**) com **Just-In-Time (JIT) Access Requests** no Teleport: Aprovação via Slack, Mattermost, PagerDuty ou Jira.
- [[teleport-ingresso-seguro-nos-join-tokens-cloud-iam-tpm-node-joining]] — Veja também: Ingresso Seguro de Agentes (**Node Joining**) no Teleport: Eliminando Tokens Estáticos com **Cloud Auto-Joining (AWS IAM, GCP, Azure, Kubernetes)** e **TPM Joining**.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.
- [[teleport-acesso-kubernetes-databases-mtls-impersonation-sem-senhas]] — Referência cruzada direta com teleport-acesso-kubernetes-databases-mtls-impersonation-sem-senhas.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
