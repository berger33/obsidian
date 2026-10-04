---
id: software.seguranca.tranche14.001378
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

# Ingresso Seguro de Agentes (**Node Joining**) no Teleport: Eliminando Tokens Estáticos com **Cloud Auto-Joining (AWS IAM, GCP, Azure, Kubernetes)** e **TPM Joining**

## Em uma frase
Quando você provisiona automaticamente 50 novas máquinas virtuais na AWS/GCP/Azure via Auto-Scaling Group ou Terraform, ou sobe novos clusters Kubernetes, como esses novos agentes (`teleport`) se registram no `Teleport Auth Service` **sem que você precise embutir um token secreto estático no script `user-data` / `cloud-init` ou na imagem da VM**?

## Por que importa
Se você usar um token estático no `cloud-init`, qualquer pessoa com permissão de leitura nos metadados da instância na nuvem poderia ler o token e registrar uma máquina falsa (*Rogue Node*) no seu cluster!

## Como funciona
Conforme detalhado na arquitetura oficial do Teleport, você deve usar **Dynamic / Secretless Join Methods (`kind: provision_token`)**: **(1) `join_method: iam` (AWS)** — o Auth Service desafia o novo nó a assinar uma requisição `sts:GetCallerIdentity` com sua role IAM da AWS e verifica se a `Account ID` e a `IAM Role` batem com a regra permitida no `provision_token`!; **(2) `join_method: gcp` / `azure`** — valida o token de identidade assinado pelo hipervisor da nuvem; **(3) `join_method: kubernetes`** — valida o JWT da ServiceAccount via `TokenReview`; e **(4) `join_method: tpm`** — para servidores bare-metal on-premises, valida a **Endorsement Key (`EK`) do chip físico TPM 2.0** da placa-mãe!

## Exemplo
```yaml
# Criar um provision_token sem segredo (join_method: iam) que permite apenas instancias da conta AWS 123456789012 ingressarem no cluster Teleport
kind: token
version: v2
metadata:
  name: aws-auto-join-token
spec:
  roles: [Node, Db]
  join_method: iam
  allow:
    - aws_account: "123456789012"
      aws_arn: "arn:aws:iam::123456789012:role/TeleportAgentRole-*"
```

## Limites e trade-offs
Repare que o `provision_token` com `join_method: iam` acima (`name: aws-auto-join-token`) **não é um segredo**: mesmo que alguém descubra o nome `aws-auto-join-token`, ele é 100% inútil fora de uma instância real da conta AWS `123456789012` rodando com a role `TeleportAgentRole-*`!

## Como verificar
Além disso, como os agentes Teleport se conectam ao `Teleport Proxy Service` através de **Túneis Reversos de Saída (`Reverse Tunnels` sobre a porta TCP `:443`)**, seus servidores de produção, bancos de dados e clusters Kubernetes **não precisam ter nenhuma porta de entrada aberta no Security Group / Firewall (`Zero Inbound Ports`)**!

## Conexões
- [[teleport-identidade-maquina-machine-id-tbot-cicd-renovacao-automatica]] — Veja também: Identidade de Máquina e Automação CI/CD com **Teleport Machine ID (`tbot`)**: Aposentando Segredos de Longa Duração no GitHub Actions, GitLab CI e Ansible.
- [[teleport-auditoria-eventos-gravacao-s3-dynamodb-integracao-siem]] — Veja também: Arquitetura de Alta Disponibilidade, **Armazenamento de Auditoria e Gravações (S3 / GCS / MinIO)** e Exportação de Eventos para **SIEM (`event-handler`)** no Teleport.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
