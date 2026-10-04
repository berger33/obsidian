---
id: software.devops.tranche19.001849
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-19.md"
fontes: ["https://developer.hashicorp.com/boundary/docs/what-is-boundary", "https://raw.githubusercontent.com/hashicorp/boundary/main/README.md", "https://github.com/hashicorp/boundary"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# HashiCorp Boundary Session Recording (BSR): gravação e reprodução criptografada de sessões SSH para conformidade

## Em uma frase
Nas edições HCP Boundary Plus e Boundary Enterprise, o recurso **Session Recording & Playback** captura todas as ações interativas de sessões SSH em arquivos **BSR** (*Boundary Session Recording*) assinados e cifrados pelo KMS, armazenando-os em **Storage Buckets** compatíveis com Amazon S3 ou MinIO.

## Por que importa
Auditorias regulatórias (PCI-DSS, SOC2, BACEN) exigem não apenas saber *quem* abriu uma sessão SSH em um servidor de produção, mas poder reproduzir exatamente quais comandos foram digitados e qual saída foi exibida no terminal.

## Como funciona
Quando um `Storage Bucket` é associado ao `Target` SSH com `enable_session_recording = true`, o Worker grava o fluxo da sessão localmente em disco durante a execução e transfere o arquivo `.bsr` assinado criptograficamente para o bucket S3, permitindo reprodução fiel (*playback*) na UI ou Desktop do Boundary.

## Exemplo
```bash
# Listando gravações de sessão registradas no Boundary:
boundary session-recordings list
```

## Limites e trade-offs
Se a política do Storage Bucket exigir gravação obrigatória e o Worker não tiver espaço em disco local ou perder acesso ao bucket S3, o Boundary recusará abrir novas sessões SSH naquele Target (*fail-closed*) para garantir que nenhuma ação ocorra sem auditoria.

## Como verificar
Verifique a lista de gravações com `boundary session-recordings list` após encerrar uma sessão SSH gravada.

## Conexões
- [[boundary-session-controls-max-connections-timeout-cancelamento-auditoria]] — Veja também: HashiCorp Boundary Session Controls: limites de conexões por sessão, `session_max_seconds` e revogação em tempo real.
- [[boundary-automacao-terraform-provider-oidc-managed-groups-gitops]] — Veja também: HashiCorp Boundary como Código: provisionamento declarativo de Scopes, OIDC, Managed Groups e Targets via Terraform Provider.

## Fontes
- [HashiCorp Boundary GitHub — README.md (Identity-Aware Proxy, Controller & Workers, PostgreSQL & KMS Requirements, Dev Mode & CLI)](https://developer.hashicorp.com/boundary/docs/what-is-boundary) — README oficial do hashicorp/boundary detalhando os componentes Controller e Worker, requisitos de banco SQL e KMS, hierarquia de Scopes e boundary connect; consultado em 2026-10-03.
- [HashiCorp Developer — What is Boundary? (Core Workflow, OIDC Authentication, Vault Credential Brokering/Injection, Multi-Hop & Session Recording)](https://raw.githubusercontent.com/hashicorp/boundary/main/README.md) — Documentação oficial do HashiCorp Boundary cobrindo acesso just-in-time sem agente, credenciais dinâmicas via Vault, sessões transparentes e gravação BSR; consultado em 2026-10-03.
- [HashiCorp Boundary — Official GitHub Repository](https://github.com/hashicorp/boundary) — Repositório oficial do HashiCorp Boundary; consultado em 2026-10-03.
