---
id: software.devops.tranche20.001958
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/Infisical/infisical/main/README.md", "https://infisical.com/docs/integrations/platforms/kubernetes/overview", "https://github.com/Infisical/infisical"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Infisical Certificate Management (PKI) e Code Signing: operação de CA Interna/Externa, ACME, EST e assinatura de artefatos

## Em uma frase
O módulo **Certificate Management** do Infisical permite operar uma hierarquia completa de **CA Privada Interna** ou integrar **CAs Externas** (Let's Encrypt, DigiCert, Microsoft AD CS), gerenciando perfis, políticas, protocolos de matrícula (**API**, **ACME** e **EST**), sincronização de certificados (para AWS ACM e Azure Key Vault) e **Code Signing**.

## Por que importa
Manter ferramentas desconectadas para segredos de aplicação, emissão de certificados TLS mTLS e assinatura de pacotes/containers fragmenta a auditoria e as políticas de aprovação.

## Como funciona
No Infisical PKI, você cria *Certificate Profiles* e *Policies* que restringem SANs, algoritmos de chave e TTLs permitidos, expõe endpoints **ACME** ou **EST** para renovação automatizada, monitora vencimentos com alertas configuráveis e utiliza o módulo **Code Signing** para assinar containers e instaladores com aprovação centralizada e trilha completa de auditoria.

## Exemplo
```bash
# Exemplo de uso do Infisical Agent ou CLI para renderizar certificados/segredos em templates:
infisical agent --config /etc/infisical/agent-config.yaml
```

## Limites e trade-offs
Configure *Certificate Syncs* para exportar automaticamente certificados gerenciados pelo Infisical para serviços de borda como AWS Certificate Manager (ACM) ou Azure Key Vault sem upload manual.

## Como verificar
Audite o inventário de certificados ativos, revogados (CRL) e próximos do vencimento na seção PKI do projeto.

## Conexões
- [[infisical-secret-rotation-point-in-time-recovery-honey-tokens]] — Veja também: Infisical Governança de Segredos: `Secret Rotation` automática, `Point-in-Time Recovery` e detecção de intrusão com `Honey Tokens`.
- [[infisical-agent-vault-ai-agents-proxy-injecao-credenciais-kms]] — Veja também: Infisical `Infisical Agent`, `Agent Vault` (para IA) e `KMS`: injeção de segredos sem SDK e proteção contra exfiltração por LLMs.

## Fontes
- [Infisical GitHub — README.md (Open-Source Secret Management, PKI, KMS & PAM Platform, CLI, Leak Prevention, Honey Tokens & Agent Vault)](https://raw.githubusercontent.com/Infisical/infisical/main/README.md) — README oficial do Infisical/infisical detalhando gerenciamento de segredos, Point-in-Time Recovery, Honey Tokens, Agent Vault, PKI, KMS e PAM; consultado em 2026-10-03.
- [Infisical Official Documentation — Kubernetes Operator Overview (v1beta1 InfisicalConnection/InfisicalAuth/InfisicalStaticSecret, Push/Dynamic Secrets & Auto-Reload)](https://infisical.com/docs/integrations/platforms/kubernetes/overview) — Documentação oficial do Infisical Kubernetes Operator cobrindo instalação Cluster-wide vs Namespace-scoped, CRDs v1beta1, auto-reload e métricas Prometheus; consultado em 2026-10-03.
- [Infisical — Official GitHub Repository](https://github.com/Infisical/infisical) — Repositório oficial MIT do Infisical; consultado em 2026-10-03.
