---
id: software.seguranca.tranche05.000446
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
fontes: ["https://raw.githubusercontent.com/paralus/paralus/main/README.md", "https://www.paralus.io/docs/", "https://www.paralus.io/docs/usage/audit-logs"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CNCF Paralus: Acesso `kubectl` Browser-Based via Componente `Prompt` (Sessões Efêmeras sem Credenciais no Desktop)

## Em uma frase
O componente **`prompt`** do Paralus fornece um terminal `kubectl` interativo diretamente no navegador web autenticado via SSO, executando os comandos em um ambiente efêmero isolado sem que o usuário precise baixar um arquivo `kubeconfig` para sua máquina local.

## Por que importa
Em cenários de plantão (*on-call*) ou acesso por prestadores de serviço em máquinas não gerenciadas (*BYOD*), o terminal browser-based impede que certificados e chaves de acesso ao cluster fiquem persistidos no disco local do dispositivo.

## Como funciona
Quando o usuário abre o terminal web para um cluster autorizado, o serviço `prompt` no cluster instancia uma sessão temporária restrita exatamente às permissões RBAC calculadas pelo Paralus para aquela identidade, encerrando e limpando o ambiente assim que a aba ou o timeout de inatividade expira.

## Exemplo
```bash
# Inspecionar a saúde do deployment prompt no namespace paralus-system do cluster gerenciado
kubectl -n paralus-system get deploy,pods -l app.kubernetes.io/name=prompt
```

## Limites e trade-offs
Para equipes que não devem ter permissão de baixar arquivos `kubeconfig` para uso fora do navegador, desabilite a opção *Allow Kubectl Download* na política do usuário/grupo, restringindo o uso apenas ao terminal supervisionado ou à API.

## Como verificar
Abra o terminal web no console do Paralus, execute `kubectl auth whoami` (ou `kubectl auth can-i --list`) e confirme que a identidade efetiva reflete apenas o escopo autorizado.

## Conexões
- [[paralus-kubeconfig-dinamico-just-in-time-serviceaccounts-revogacao]] — Veja também: CNCF Paralus: Provisionamento *Just-in-Time* de ServiceAccounts, `kubeconfig` Auditado e Revogação Instantânea.
- [[paralus-automacao-cli-pctl-gitops-rbac-as-code-ci-cd]] — Veja também: CNCF Paralus: Automação Declarativa (*RBAC-as-Code*) com a CLI `pctl` e API REST em Pipelines GitOps.
- [[paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem]] — Referência cruzada direta com paralus-auditoria-completa-kubectl-api-relay-audit-logs-siem.
- [[paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager]] — Referência cruzada direta com paralus-arquitetura-cncf-zero-trust-kubernetes-access-manager.

## Fontes
- [CNCF Paralus Official GitHub — Zero-Trust Kubernetes Access Manager](https://raw.githubusercontent.com/paralus/paralus/main/README.md) — documentação oficial do Paralus cobrindo RBAC multi-cluster, SSO/OIDC, JIT ServiceAccounts e pctl; consultado em 2026-10-03.
- [Paralus Official Documentation — Zero Trust & Architecture](https://www.paralus.io/docs/) — guia oficial de arquitetura, Relay Agent, Projects, Roles e operação do Paralus; consultado em 2026-10-03.
- [Paralus Documentation — Audit Logs](https://www.paralus.io/docs/usage/audit-logs) — documentação oficial de System Audit Logs e Kubectl/Relay Audit Logs; consultado em 2026-10-03.
