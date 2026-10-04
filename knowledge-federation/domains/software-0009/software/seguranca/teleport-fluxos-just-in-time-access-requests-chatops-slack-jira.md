---
id: software.seguranca.tranche14.001376
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

# Privilégio Zero Permanente (**Zero Standing Privilege — ZSP**) com **Just-In-Time (JIT) Access Requests** no Teleport: Aprovação via Slack, Mattermost, PagerDuty ou Jira

## Em uma frase
Por que manter permissões permanentes de `root` ou `cluster-admin` em produção para todos os desenvolvedores 24 horas por dia, 365 dias por ano, viola o princípio moderno de **Zero Standing Privilege (ZSP)**?

## Por que importa
Porque 99% do tempo o desenvolvedor está apenas escrevendo código ou olhando métricas e não precisa de acesso mutável à produção; se a conta dele for comprometida numa sexta-feira à noite, o invasor já herda privilégios de produção imediatamente!

## Como funciona
O **Teleport Access Requests (Just-In-Time Privilege Elevation)** resolve isso de forma nativa: no dia a dia, o desenvolvedor tem apenas a role básica `dev-leitura` (que permite pedir elevação via **`request: roles: ['sre-producao']`** ou pedir acesso a um recurso específico *Resource Access Request*!). Quando surge um incidente, o desenvolvedor executa **`tsh request create --roles=sre-producao --reason="Incidente #4821 latencia no banco"`**: o plugin oficial do Teleport envia um card interativo no **Slack / Mattermost / MS Teams / Jira / PagerDuty** (ou no Web UI), o líder de plantão aprova com 1 clique, e o desenvolvedor recebe um certificado elevado **válido apenas durante a janela do chamado**!

## Exemplo
```bash
# Solicitar elevacao temporaria Just-In-Time (JIT) para a role sre-producao informando justificativa de auditoria e assumir a role apos aprovacao
tsh request create --roles=sre-producao --reason="Investigacao chamado INC-4821"
tsh request ls
tsh login --request-id=<REQUEST_UUID>
```

## Limites e trade-offs
Mais inteligente ainda: você pode integrar o plugin do Teleport ao **PagerDuty / Opsgenie** para **Auto-Aprovação Condicional de Plantão (*On-Call Auto-Approval*)** — se o engenheiro que abriu o `Access Request` for exatamente o plantonista escalado no PagerDuty naquele horário e houver um incidente ativo aberto, o próprio plugin aprova o acesso temporário em segundos e registra o número do incidente no log de auditoria!

## Como verificar
Configure na role de revisão que **um usuário nunca pode aprovar o seu próprio Access Request** e exija `min_approvals: 2` para papéis críticos de banco de dados ou infraestrutura core.

## Conexões
- [[teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn]] — Veja também: Controle de Acesso **RBAC + ABAC (`labels`)**, **Per-Session MFA (FIDO2 WebAuthn)** e Restrição de IP/Dispositivo em Roles do Teleport.
- [[teleport-identidade-maquina-machine-id-tbot-cicd-renovacao-automatica]] — Veja também: Identidade de Máquina e Automação CI/CD com **Teleport Machine ID (`tbot`)**: Aposentando Segredos de Longa Duração no GitHub Actions, GitLab CI e Ansible.
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Referência cruzada direta com teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
